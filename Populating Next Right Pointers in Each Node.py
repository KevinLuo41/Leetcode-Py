class Solution:

    def connect(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    # constant space solution
    def connect_2(self, root):
        head = root
        while head:
            current = head
            while current:
                if current.left:
                    current.left.next = current.right
                    if current.next:
                        current.right.next = current.next.left
                current = current.next
            head = head.left
