import ast
from .nodes import *


def parse(source):
    tree = ast.parse(source).body if isinstance(source, str) else source
    altered_tree = []
    for tree_node in tree:
        n = None
        match tree_node:
            case ast.Assign():
                # TODO: Support multiple targets
                is_declare = isinstance(tree_node.value, ast.Call)
                for target in tree_node.targets:
                    match target:
                        case ast.Name():
                            if is_declare:
                                n = DeclareObject(tree_node.lineno, tree_node.col_offset, target.id,
                                                  tree_node.value.func.id, parse(tree_node.value.args))
                            else:
                                n = Assign(tree_node.lineno, tree_node.col_offset, target.id, parse([tree_node.value]))
                        case ast.Attribute():
                            n = AssignToAttribute(tree_node.lineno, tree_node.col_offset, target.value.id, target.attr,
                                                  parse([tree_node.value]))
            case ast.arguments():
                n = Arguments(parse(tree_node.args), parse(tree_node.defaults),
                              parse(tree_node.kw_defaults), parse([tree_node.kwarg]), parse([tree_node.vararg]),
                              parse(tree_node.kwonlyargs), parse(tree_node.posonlyargs))
            case ast.Attribute():
                n = Attribute(tree_node.lineno, tree_node.col_offset, tree_node.value.id, tree_node.attr)
            case ast.Call():
                match tree_node.func:
                    case ast.Attribute():
                        n = CallObjectFunction(tree_node.lineno, tree_node.col_offset, parse([tree_node.func.value]),
                                               tree_node.func.attr, parse(tree_node.args))
                    case ast.Name():
                        n = Call(tree_node.lineno, tree_node.col_offset, tree_node.func.id, parse(tree_node.args))
            case ast.Constant():
                n = Constant(tree_node.lineno, tree_node.col_offset, tree_node.value)
            case ast.Expr():
                n = Expr(tree_node.lineno, tree_node.col_offset, parse([tree_node.value]))
            case ast.FunctionDef():
                if isinstance(tree_node.body[0], ast.Pass):
                    continue
                n = Function(tree_node.lineno, tree_node.col_offset, tree_node.name, parse([tree_node.args]),
                             parse(tree_node.body), parse(tree_node.decorator_list), tree_node.returns)
            case ast.Import() | ast.ImportFrom():
                n = Include(tree_node.lineno, tree_node.col_offset, tree_node.module,
                            tree_node.names[0].name, tree_node.names[0].asname)
            case ast.Name():
                n = Name(tree_node.lineno, tree_node.col_offset, tree_node.id)
            case ast.While():
                n = While(tree_node.lineno, tree_node.col_offset, parse([tree_node.test]), parse(tree_node.body))

        if n is not None:
            altered_tree.append(n)
    return altered_tree
