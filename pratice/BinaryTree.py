

class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return self.__str__()


class BinaryTree:
    def __init__(self):
        self.root = None
        self.flat_str = ''
        self.flat_l = []
        self.max_l = 0

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.__insert(self.root, val)

    def __insert(self, tn: TreeNode, val):
        if tn.val >= val:
            if tn.left is None:
                tn.left = TreeNode(val)
                print(f'insert [{val}] into left of [{tn}]')
            else:
                self.__insert(tn.left, val)
        else:
            if tn.right is None:
                tn.right = TreeNode(val)
                print(f'insert [{val}] into right of [{tn}]')
            else:
                self.__insert(tn.right, val)

    def __print_tree(self, tn: TreeNode, max_l):
        if tn is None:
            return
        # print(f'{tn.val=}')
        self.flat_str += f'{tn.val}, '
        self.flat_l.append(tn.val)
        if tn.left is not None:
            self.max_l = max_l +  1
            self.__print_tree(tn.left, self.max_l)
        if tn.right is not None:
            self.max_l = max_l +  1
            self.__print_tree(tn.right, self.max_l)

    def get_node(self, val):
        return self.__get_node_by_val(self.root, val)

    def __get_node_by_val(self,tn: TreeNode, val: int = None):
        print(f'{tn=}, {val=}')
        if val is None:
            return None
        if tn is None:
            return None
        if tn.val == val:
            return tn
        else:
            if val > tn.val:
                return self.__get_node_by_val(tn.right, val)
            else:
                return self.__get_node_by_val(tn.left, val)

    def __str__(self):
        self.__print_tree(self.root, self.max_l)
        return self.flat_str


if __name__ == "__main__":
    # n = [11,24,5,1,0,42,-1,42,-2,34,5,2,2,6,4,5,20,44,56,78,220]
    n = range(0, 100)
    bt = BinaryTree()
    for i in n:
        bt.insert(i)
    print(bt.__str__())
    print(bt.flat_l)
    t = bt.get_node(100)
    print(f'{t=}')
    t = bt.get_node(220)
    print(f'{t=}')
    print(f'{bt.max_l=}')