# %%

class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.prev = None

# %%
# doubly linked list
a = Node(4)
b = Node(5)
c = Node(6)

a.next = b 
b.prev = a
b.next = c
c.prev = b

# %%
# circluar linked list

i = Node(4)
j = Node(5)
k = Node(6)

i.next = j
j.next = k
k.next = i