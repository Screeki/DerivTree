from DifferTree import DifferTree as tree


def main():
    formula = input('Enter formula')
    differ_tree = tree()
    differ_tree.RootNode = differ_tree.BuildTree(formula)
    differ_tree.PrintTree(differ_tree.RootNode)
    a = differ_tree.NodeToInfixForm(differ_tree.RootNode)
    print(a)


if __name__ == '__main__':
    main()
