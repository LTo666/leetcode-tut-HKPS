class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.data)
  
  def print_list(self):
    print(self.data)
    if self.next is not None:
      self.next.print_list()

  def revert_print_list(self):
    print(self.data)
    if self.prev is not None:
      self.prev.revert_print_list()


class LinkedList:
  def __init__(self, data=None):
    if data is not None:
      self.head = Node(data)
      self.tail = self.head
    else:
      self.head = None
      self.tail = None


  def append(self, data):
    if self.head is None:
      self.head = Node(data)
      self.tail = self.head
    else:
      node = Node(data)
      node.prev = self.tail
      self.tail.next = node
      self.tail = node

  def print_list(self):
    if self.head is not None:
      self.head.print_list()

  def revert_print_list(self):
    if self.tail is not None:
      self.tail.revert_print_list()


# initiate the linkedlist
llist = LinkedList()

# For loop to add nodes
for i in range(1, 11):
  llist.append("Node" + str(i))

# print the linkedlist
print("The linkedlist is: ")
llist.print_list()

# print the linkedlist in reverse
print("The linkedlist in reverse is: ")
llist.revert_print_list()