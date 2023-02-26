from .parser import *
from .linker import Linker


class Interpreter:
    def __init__(self):
        self._environment = {}
        self._modules = {}
        self._linker = Linker()
        self._current_function = None

    def interpret(self, code):
        tree = self._process(code)

        return tree, self._linker.environment

    def _handle_objects(self, code):
        tree = []
        for tree_node in code:
            match tree_node:
                case DeclareObject():
                    tree.append(tree_node)
                case _:
                    pass


    def _process(self, code):
        tree = []
        for tree_node in code:
            match tree_node:
                case AssignToAttribute():
                    processed = tree_node
                case Expr():
                    processed = tree_node.expression
                case Function():
                    processed = self._function(tree_node)
                case Include():
                    processed = self._include(tree_node.module, tree_node.name, tree_node.alias)
                case While():
                    processed = self._while(tree_node)
                case _:
                    processed = tree_node

            if processed is not None:
                match processed:
                    case list():
                        tree.extend(processed)
                    case _:
                        tree.append(processed)

        return tree

    def _function(self, function):
        self._current_function = function.name

        if function.has_decorator('start'):
            # Entry point
            pass

        if function.has_decorator('interrupt'):
            # Interrupt handler
            pass

        if function.has_decorator('assembly'):
            # Assembly code
            pass

        # TODO: Need to handle function arguments
        # TODO: Need to handle function return values
        # TODO: Need to handle function decorators
        # TODO: Need to handle configuration decorator

        function.body[0].label = function.name
        return self._process(function.body)

    def _include(self, module, name, alias):
        match module:
            case 'time':
                return
            case _:
                if 'picpy.devices' in module:
                    import inspect
                    import os

                    path = os.path.dirname(inspect.getfile(inspect.currentframe()))
                    path = os.path.dirname(path)
                    path = os.path.join(path, f'devices/{module.replace("picpy.devices.", "")}.py')
                    tree = parse(open(path).read())
                    del tree[0]

                    self._linker.link(tree)

                    return []
                if module not in self._modules:
                    self._modules[module] = __import__(module)
                if alias is not None:
                    self._environment[alias] = getattr(self._modules[module], name)
                else:
                    if name == '*':
                        for name in dir(self._modules[module]):
                            self._environment[name] = getattr(self._modules[module], name)
                    self._environment[name] = getattr(self._modules[module], name)

    def _while(self, while_):

        # TODO: Need to handle while loop condition

        tree = self._process(while_.body)
        tree[0].label = f'{self._current_function}_{hash(while_)}'
        tree.append(Goto(f'{self._current_function}_{hash(while_)}'))

        return tree
