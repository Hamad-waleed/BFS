class Tree :
    ### the class is a simple implementation of a tree,
    # it has nood  has only value and parent
    # the child can be arrived to parent put the parnt can`t be arrived to children
    def __init__(self, value , parent=None):
        self.value = value
        self.parent = parent
    # here to add chiled 
    def add_child(self , value):
        chiled = Tree(value , self )
        return chiled
    # to return the parent of the node
    def getparnt(self):
        return self.parent
# return the path from the node to the root
def path(node):
    path = []
    while node :
        path.append(node.value)
        node = node.parent
    return path