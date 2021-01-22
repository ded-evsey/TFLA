class Tree:
    def __init__(self, name="", left=None,right=None):
        self.name = name
        self.left = left
        self.right = right
    @classmethod
    def init_tree(cls, expression='', tree=None):
        p_symbol = -1
        is_bracket = False
        for i, s in enumerate(expression):
            if (s == '+' or s == '-') and not is_bracket:
                p_symbol = i
            elif (s == '*' or s == ':') and p_symbol == -1 and not is_bracket:
                p_symbol = i
            elif  s == '(':
                is_bracket = Tree
            elif s == ')':
                is_bracket = False
        if not tree:
            tree = cls()
        if  p_symbol == -1:
            tree.name = expression
        else:

            tree.name += expression[p_symbol]
            tree.left = cls.init_tree(cls.del_brackets(expression[:p_symbol]), tree.left)
            tree.right = cls.init_tree(cls.del_brackets(expression[p_symbol +1:]), tree.right)
        return tree

    @staticmethod
    def del_brackets(expression):
        checked_brackets = 0
        for s in expression:
            if s == '(':
                checked_brackets += 1
            elif s == ')':
                checked_brackets -= 1
            elif checked_brackets:
                continue
            else:
                return expression
        return expression[1:-2]

    def print_tree(self, tree=None, level=0):
        if tree:
            self.print_tree(tree.left, level+1)
            for _ in range(level):
                print('   ',end='',sep='')
            print(tree.name)
            self.print_tree(tree.right, level+1 )

    def calc(self, tree, *args, **kwargs):
        if not tree or not tree.name:
            return 0
        if tree.name == '+':
            return self.calc(tree.left, *args, **kwargs) + self.calc(tree.right, *args, **kwargs)
        elif tree.name == '-':
            return self.calc(tree.left, *args, **kwargs) - self.calc(tree.right, *args, **kwargs)
        elif tree.name == ':':
            return self.calc(tree.left, *args, **kwargs) / self.calc(tree.right, *args, **kwargs)
        elif tree.name == '*':
            return self.calc(tree.left, *args, **kwargs) * self.calc(tree.right, *args, **kwargs)
        elif tree.name in kwargs.keys():
            return kwargs.get(tree.name)
        else:
            return int(tree.name)

if __name__ =='__main__':
    one_tree = Tree()
    exp = "x*(y+z-y1)+w*x2:w3"
    one_tree = Tree.init_tree(exp,one_tree)
    print('Syntax tree')
    one_tree.print_tree(one_tree)
    values = {
        'x': 1,
        'y': 1,
        'z': 1,
        'y1': 1,
        'w': 2,
        'x2': 2,
        'w3': 2
    }
    value_expression = one_tree.calc(one_tree,**values)
    print('value expression:',  value_expression)
