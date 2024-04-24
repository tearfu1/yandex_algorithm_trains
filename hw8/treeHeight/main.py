class Node():
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    # def initRoot(self, value):
    #     self.value = value

    def add(self, value):
        if self.value == None:
            self.value = value
            return
        if value < self.value:
            if self.left is None:
                self.left = Node()
                self.left.add(value)
            else:
                self.left.add(value)
            return
        elif value > self.value:
            if self.right is None:
                self.right = Node()
                self.right.add(value)
            else:
                self.right.add(value)
            return

    def maxHeight(self, values):
        height = 0
        for value in values:
            height = max(self.search(value, 1), height)
        return height

    def depths(self, values):
        depths = []
        used = set()
        for value in values:
            if value not in used:
                depths.append(self.search(value, 1))
                used.add(value)
        return depths

    
    def search(self, value, cnt):
        if self.value == value:
            return cnt
        if value < self.value:
            return self.left.search(value, cnt + 1)
        else:
            return self.right.search(value, cnt + 1)

    def inorderTraversal(self):
        if self.value is None:
            return None
        if self.left is not None:
            self.left.inorderTraversal()
        print(self.value, end=" ")
        if self.right is not None:
            self.right.inorderTraversal()


elems = list(map(int, input().split()))
del elems[-1]
root = Node()
root.add(elems[0])
for elem in elems[1:]:
        root.add(elem)
# root.inorderTraversal()
# print()
# print(root.maxHeight(elems))
print(*root.depths(elems))
