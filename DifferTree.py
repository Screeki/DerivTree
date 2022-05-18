from Node import Node as TreeNode


class DifferTree:
    RootNode = TreeNode
    pos = 0

    def BuildTree(self, s):
        n = TreeNode(s[self.pos])
        if self.IsOperation(n.data):
            self.pos += 1
            n.left = self.BuildTree(s)
            self.pos += 1
            n.right = self.BuildTree(s)
        else:
            n.left = None
            n.right = None
        return n

    def PrintTree(self, node, separator="", side="M"):
        if node is None:
            return
        print(f"{separator} [{side}] {node.data}")
        separator += '\t'
        self.PrintTree(node.left, separator, "L")
        self.PrintTree(node.right, separator, "R")

    def NodeToInfixForm(self, rootNode):
        self.resString = None
        self.arrList = []
        self.NodeToInfix(rootNode)
        return self.arrList[0]

    def NodeToInfix(self, node):
        if node is None:
            return
        self.NodeToInfix(node.right)
        self.NodeToInfix(node.left)
        if '+-/*'.__contains__(node.data):
            a = self.arrList[len(self.arrList) - 1]
            b = self.arrList[len(self.arrList) - 2]
            del self.arrList[-2:]
            self.arrList.append("(" + a + node.data + b + ")")
        else:
            self.arrList.append(node.data)

    def IsOperation(self, symbol):
        return symbol == '/' or symbol == '*' or symbol == '+' or symbol == '-'
