from .parser import *
from .linker import Linker


class Interpreter:
    def __init__(self):
        self._environment = {}
        self._modules = {}
        self._linker = Linker()
        self._configuration_words = []
        self._current_function = None

    def interpret(self, code):
        tree = self._process(code)
        self._handle_objects(tree)
        tree = self._expand(tree)

        return tree, self._linker

    def _expand(self, code):
        tree = []
        for tree_node in code:
            resolved = tree_node.resolve()
            if resolved is not None:
                has_label = tree_node.label is not None
                match resolved:
                    case list():
                        if has_label:
                            resolved[0].label = tree_node.label
                        tree.extend(resolved)
                    case _:
                        if has_label:
                            resolved.label = tree_node.label
                        tree.append(resolved)

        return tree

    def _handle_objects(self, code):
        for tree_node in code:
            match tree_node:
                case DeclareObject():
                    self._linker.link([tree_node])
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
                        for element in processed:
                            element.context = self._linker
                        tree.extend(processed)
                    case _:
                        processed.context = self._linker
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

        if function.has_decorator('config'):
            # Configuration word
            config = function.get_decorator('config')
            self._configuration_words.append(config)

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
