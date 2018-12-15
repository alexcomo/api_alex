# def reverse_list(head):
#     new_head = None  # this is where we build the reversed list (reusing the existing nodes)
#     while head:
#         temp = head  # temp is a reference to a node we're moving from one list to the other
#         head = temp.next  # the first two assignments pop the node off the front of the list
#         temp.next = new_head  # the next two make it the new head of the reversed list
#         new_head = temp
#     return new_head

# class Node:
#     def __init__(self, initdata):
#         self.data = initdata
#         self.next = None
#
#     def data(self):
#         return self.data
#
#     def next(self):
#         return self.next
#
#     def setData(self, newdata):
#         self.data = newdata
#
#     def setNext(self, newnext):
#         self.next = newnext
#
# head = Node(87)
# head.setNext(88)
# head.setNext(89)
# head.setNext(90)
# print(head.getNext())
# print(head.getData())
# #node = temp.head
# # while node:
# #     print(node.value)
# #     node = node.next
#
# # new_head = None  # this is where we build the reversed list (reusing the existing nodes)
# # while head:
# #     temp = head  # temp is a reference to a node we're moving from one list to the other
# #     head = temp.getNext  # the first two assignments pop the node off the front of the list
# #     temp.getNext = new_head  # the next two make it the new head of the reversed list
# #     new_head = temp
# # print(new_head)
#
#
# def reverse_list(head):
#     new_head = None
#     while head:
#         head.next, head, new_head = new_head, head.next, head # look Ma, no temp vars!
#     return new_head
# reverse_list(head)

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

n0 = Node(1,Node(2,Node(3,Node(4,Node(5,)))))

def reverse(head):
    new_head = None
  #  while head:
    temp = head # 1
    head = temp.next # 2
    temp.next = new_head # None
    new_head = temp # 1
    return temp
reverse(n0)
# def reverse(head):
#     temp = head
#     llSize = 0
#     while temp is not None:
#         llSize += 1
#         temp = temp.next
#     for i in range(llSize-1,0,-1):
#         xcount = 0
#         temp = head
#         while (xcount != i):
#             temp.value, temp.next.value = temp.next.value, temp.value
#             temp = temp.next
#             xcount += 1
#     return head

# def reverse(head):
#     new_head = None
#     while head:
#         head.next, head, new_head = new_head, head.next, head
#     return new_head
def printnodes(n):
    b = True
 #   while b == True:
 #       try:
    print(n.value)
      #      n = n.next
 #       except:
 #           b = False

n0 = Node(1,Node(2,Node(3,Node(4,Node(5,)))))
print('Nodes in order...')
#printnodes(n0)
print('---')
print('Nodes reversed...')
n1 = reverse(n0)
printnodes(n1)
#print(n1.value)