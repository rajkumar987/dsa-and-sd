# %%
# simple Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # pointer to the next node
        
# create nodes
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
# head is the first node in the list
head = a

# %%
# traverse the list
# current is the current node in the list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next

# %%
# insert a new node at the beginning
new_node = Node(0)
new_node.next = head
head = new_node
print("After inserting a new node at the beginning:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next

# %% 
# insert a new node at the end
new_node = Node(4)
current = head
while current.next:
    current = current.next
current.next = new_node
print("After inserting a new node at the end:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next

# %%
# insert a new node at a specific position
new_node = Node(5)
k = 2
current = head
for i in range(k-1):
    current = current.next
nextNode = current.next 
current.next = new_node
new_node.next = nextNode
print("After inserting a new node at position", k, ":")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next


# %%
#delete the first node
head = head.next
print("After deleting the first node:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next

# %%
#delete the last node
current = head
while current.next.next:
    current = current.next
current.next = None
print("After deleting the last node:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
    
# %%  
# delete the node at kth index
k = 2
current = head
for i in range(k-1):
    current = current.next
current.next = current.next.next

current = head
while current:
    print(current.data,end=" ")
    current = current.next