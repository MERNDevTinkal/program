# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # =========================================================
# # 1. PRINT / TRAVERSE
# # =========================================================

# def print_linked_list(head):
#     current = head

#     while current is not None:
#         print(current.data, end=" -> ")
#         current = current.next

#     print("None")


# # =========================================================
# # 2. LENGTH
# # =========================================================

# def get_length(head):
#     count = 0
#     current = head

#     while current is not None:
#         count += 1
#         current = current.next

#     return count


# # =========================================================
# # 3. APPEND
# # Insert at END
# # =========================================================

# def append(head, value):
#     new_node = Node(value)

#     if head is None:
#         return new_node

#     current = head

#     while current.next is not None:
#         current = current.next

#     current.next = new_node

#     return head


# # =========================================================
# # 4. PREPEND
# # Insert at BEGINNING
# # =========================================================

# def prepend(head, value):
#     new_node = Node(value)

#     new_node.next = head

#     return new_node


# # =========================================================
# # 5. INSERT AT POSITION
# # =========================================================

# def insert_at_position(head, position, value):

#     new_node = Node(value)

#     # Position 0 = beginning
#     if position == 0:
#         new_node.next = head
#         return new_node

#     current = head

#     # Move to node before required position
#     for i in range(position - 1):
#         current = current.next

#     new_node.next = current.next
#     current.next = new_node

#     return head


# # =========================================================
# # 6. DELETE FROM BEGINNING
# # =========================================================

# def delete_from_beginning(head):

#     if head is None:
#         return None

#     return head.next


# # =========================================================
# # 7. DELETE FROM END
# # =========================================================

# def delete_from_end(head):

#     if head is None:
#         return None

#     # Only one node
#     if head.next is None:
#         return None

#     current = head

#     # Reach second-last node
#     while current.next.next is not None:
#         current = current.next

#     current.next = None

#     return head


# # =========================================================
# # 8. DELETE AT POSITION
# # =========================================================

# def delete_at_position(head, position):

#     # Delete first node
#     if position == 0:
#         return head.next

#     current = head

#     # Move to node before target
#     for i in range(position - 1):
#         current = current.next

#     # Skip target node
#     current.next = current.next.next

#     return head


# # =========================================================
# # 9. SEARCH
# # =========================================================

# def search(head, value):

#     current = head

#     while current is not None:

#         if current.data == value:
#             return True

#         current = current.next

#     return False


# # =========================================================
# # 10. FIND POSITION
# # =========================================================

# def find_position(head, value):

#     current = head
#     position = 0

#     while current is not None:

#         if current.data == value:
#             return position

#         current = current.next
#         position += 1

#     return -1


# # =========================================================
# # 11. UPDATE AT POSITION
# # =========================================================

# def update_at_position(head, position, value):

#     current = head

#     for i in range(position):
#         current = current.next

#     current.data = value

#     return head


# # =========================================================
# # 12. GET FIRST ELEMENT
# # =========================================================

# def get_first(head):

#     if head is None:
#         return None

#     return head.data


# # =========================================================
# # 13. GET LAST ELEMENT
# # =========================================================

# def get_last(head):

#     if head is None:
#         return None

#     current = head

#     while current.next is not None:
#         current = current.next

#     return current.data


# # =========================================================
# # 14. GET ELEMENT AT POSITION
# # =========================================================

# def get_at_position(head, position):

#     current = head

#     for i in range(position):
#         current = current.next

#     return current.data


# # =========================================================
# # 15. REVERSE LINKED LIST
# # =========================================================

# def reverse(head):

#     previous = None
#     current = head

#     while current is not None:

#         next_node = current.next

#         current.next = previous

#         previous = current
#         current = next_node

#     return previous


# # =========================================================
# # 16. PRINT REVERSE
# # =========================================================

# def print_reverse(head):

#     if head is None:
#         return

#     print_reverse(head.next)

#     print(head.data, end=" ")


# # =========================================================
# # 17. FIND MIDDLE
# # =========================================================

# def find_middle(head):

#     slow = head
#     fast = head

#     while fast is not None and fast.next is not None:

#         slow = slow.next
#         fast = fast.next.next

#     return slow.data


# # =========================================================
# # 18. CHECK EMPTY
# # =========================================================

# def is_empty(head):

#     return head is None


# # =========================================================
# # 19. CLEAR LINKED LIST
# # =========================================================

# def clear():

#     return None


# # =========================================================
# # MAIN PROGRAM
# # =========================================================


# # ---------------------------------------------------------
# # CREATE LINKED LIST
# # ---------------------------------------------------------

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)

# print("1. Original Linked List:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # TRAVERSE
# # ---------------------------------------------------------

# print("\n2. Traversal:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # LENGTH
# # ---------------------------------------------------------

# print("\n3. Length:")
# print(get_length(head))


# # ---------------------------------------------------------
# # APPEND
# # ---------------------------------------------------------

# head = append(head, 50)

# print("\n4. After append 50:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # PREPEND
# # ---------------------------------------------------------

# head = prepend(head, 5)

# print("\n5. After prepend 5:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # INSERT AT POSITION
# # ---------------------------------------------------------

# head = insert_at_position(head, 3, 25)

# print("\n6. After inserting 25 at position 3:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # SEARCH
# # ---------------------------------------------------------

# print("\n7. Search for 30:")
# print(search(head, 30))

# print("Search for 100:")
# print(search(head, 100))


# # ---------------------------------------------------------
# # FIND POSITION
# # ---------------------------------------------------------

# print("\n8. Position of 30:")
# print(find_position(head, 30))


# # ---------------------------------------------------------
# # GET FIRST
# # ---------------------------------------------------------

# print("\n9. First element:")
# print(get_first(head))


# # ---------------------------------------------------------
# # GET LAST
# # ---------------------------------------------------------

# print("\n10. Last element:")
# print(get_last(head))


# # ---------------------------------------------------------
# # GET AT POSITION
# # ---------------------------------------------------------

# print("\n11. Element at position 2:")
# print(get_at_position(head, 2))


# # ---------------------------------------------------------
# # UPDATE
# # ---------------------------------------------------------

# head = update_at_position(head, 2, 99)

# print("\n12. After updating position 2 to 99:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # FIND MIDDLE
# # ---------------------------------------------------------

# print("\n13. Middle element:")
# print(find_middle(head))


# # ---------------------------------------------------------
# # PRINT REVERSE
# # ---------------------------------------------------------

# print("\n14. Print in reverse:")
# print_reverse(head)
# print()


# # ---------------------------------------------------------
# # DELETE FROM BEGINNING
# # ---------------------------------------------------------

# head = delete_from_beginning(head)

# print("\n15. After deleting from beginning:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # DELETE FROM END
# # ---------------------------------------------------------

# head = delete_from_end(head)

# print("\n16. After deleting from end:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # DELETE AT POSITION
# # ---------------------------------------------------------

# head = delete_at_position(head, 2)

# print("\n17. After deleting position 2:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # REVERSE
# # ---------------------------------------------------------

# head = reverse(head)

# print("\n18. After reversing Linked List:")
# print_linked_list(head)


# # ---------------------------------------------------------
# # CHECK EMPTY
# # ---------------------------------------------------------

# print("\n19. Is Linked List empty?")
# print(is_empty(head))


# # ---------------------------------------------------------
# # CLEAR
# # ---------------------------------------------------------

# head = clear()

# print("\n20. After clearing Linked List:")
# print_linked_list(head)

# print("\n21. Is Linked List empty now?")
# print(is_empty(head))

# Linked List
# Linked List is a linear data structure where each element is a separate object, called a node. Each node contains two items: the data and a reference (or link) to the next node in the sequence. This structure allows for efficient insertion and removal of elements from any position in the sequence.

# We use a Linked List when we need frequent insertion and deletion of elements. Unlike an array, we don't need to shift other elements. We can change the links between nodes instead. However, accessing an element is slower because we have to traverse the list from the beginning.

#Traversing a linked list This process of visiting each node one by one is called traversing a Linked List.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Create nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# # Connect nodes
# node1.next = node2
# node2.next = node3


# # Traversing
# current = node1

# while current is not None:
#     print(current.data)
#     current = current.next

# create a void function having head as a parameter, print all the elements of the LL having the same head. 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def print_linked_list(head):
#     current = head

#     while current is not None:
#         print(current.data)
#         current = current.next


# # Create nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# # Connect nodes
# node1.next = node2
# node2.next = node3

# # Head of Linked List
# head = node1

# # Call function
# print_linked_list(head)

# create a function which insert a new node with value 0 at the beginning of a linked list having head in the parameter OF THE function and return the new head.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def insert_at_beginning(head):
#     new_node = Node(0)

#     new_node.next = head

#     return new_node


# def print_linked_list(head):
#     current = head

#     while current is not None:
#         print(current.data)
#         current = current.next


# # Create nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# # Connect nodes
# node1.next = node2
# node2.next = node3

# # Current head
# head = node1

# # Insert 0 at the beginning
# head = insert_at_beginning(head)

# # Print Linked List
# print_linked_list(head)

# Complete a function having head and position as the parameter, you need to insert Node with value 0 at the given position.
# pre assume that linked list have elements more that position

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def insert_at_position(head, position):
#     new_node = Node(0)

#     current = head

#     # Move to the node before the given position
#     for i in range(position - 1):
#         current = current.next

#     # Connect new node to the next node
#     new_node.next = current.next

#     # Connect previous node to new node
#     current.next = new_node

#     return head


# def print_linked_list(head):
#     current = head

#     while current is not None:
#         print(current.data)
#         current = current.next


# # Create nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# # Connect nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4

# # Head
# head = node1

# # Insert 0 at position 2
# head = insert_at_position(head, 2)

# # Print Linked List
# print_linked_list(head)

# Complete a function having head of a ll as one parameter and n as the other parameter, return nth node in the linked list, assuming that n<=length of the LL

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def get_nth_node(head, n):
#     current = head

#     for i in range(n-1):
#         current = current.next

#     return current

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# head = node1
# result_node = get_nth_node(head, 3)
# print(result_node.data) 

# intiAtPosition

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # Add node at the end
#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node

#     # Insert node at a specific position
#     def insert_at_position(self, data, position):
#         new_node = Node(data)

#         # If inserting at position 0
#         if position == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return

#         current = self.head
#         current_position = 0

#         # Reach the node just before the required position
#         while current is not None and current_position < position - 1:
#             current = current.next
#             current_position += 1

#         # Invalid position
#         if current is None:
#             return

#         # Insert new node
#         new_node.next = current.next
#         current.next = new_node

#     # Print linked list
#     def print_list(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" → ")
#             current = current.next

#         print("None")


# # Create linked list
# my_list = LinkedList()

# my_list.append(10)
# my_list.append(20)
# my_list.append(40)

# print("Before insertion:")
# my_list.print_list()

# # Insert 30 at position 2
# my_list.insert_at_position(30, 2)

# print("After insertion:")
# my_list.print_list()

# complete a function which reverse a linked list and return the new head.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def reverse(head):
#     previous = None
#     current = head

#     while current is not None:
#         next_node = current.next

#         current.next = previous

#         previous = current
#         current = next_node

#     return previous


# def print_list(head):
#     current = head

#     while current is not None:
#         print(current.data, end=" → ")
#         current = current.next

#     print("None")


# # Create Linked List
# head = Node(22)

# head.next = Node(33)
# head.next.next = Node(44)
# head.next.next.next = Node(55)


# print("Original:")
# print_list(head)


# # Reverse Linked List
# head = reverse(head)


# print("Reversed:")
# print_list(head)

# complete a function which returns mid of a Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def find_middle(head):
#     slow = head
#     fast = head

#     while fast is not None and fast.next is not None:
#         slow = slow.next
#         fast = fast.next.next

#     return slow


# def print_list(head):
#     current = head

#     while current is not None:
#         print(current.data, end=" → ")
#         current = current.next

#     print("None")


# # Create Linked List
# head = Node(22)
# head.next = Node(33)
# head.next.next = Node(44)
# head.next.next.next = Node(55)
# head.next.next.next.next = Node(66)


# print("Linked List:")
# print_list(head)

# middle = find_middle(head)

# print("Middle:", middle.data)

# Detect if cycle exist in a LL, return True or False.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def has_cycle(head):
#     slow = head
#     fast = head

#     while fast is not None and fast.next is not None:

#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             return True

#     return False


# # Create Linked List
# head = Node(22)
# head.next = Node(33)
# head.next.next = Node(44)
# head.next.next.next = Node(55)

# # Create a cycle:
# # 55 → 44
# head.next.next.next.next = head.next.next


# print(has_cycle(head))

# Merge two sorted LL, return the new head.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node


# def merge_sorted_lists(head1, head2):

#     # Dummy node
#     dummy = Node(0)

#     # Current points to the last node
#     # of the merged list
#     current = dummy

#     while head1 is not None and head2 is not None:

#         if head1.data <= head2.data:
#             current.next = head1
#             head1 = head1.next

#         else:
#             current.next = head2
#             head2 = head2.next

#         current = current.next

#     # If List 1 still has nodes
#     if head1 is not None:
#         current.next = head1

#     # If List 2 still has nodes
#     if head2 is not None:
#         current.next = head2

#     # Return first real node
#     return dummy.next


# def print_list(head):
#     current = head

#     while current is not None:
#         print(current.data, end=" → ")
#         current = current.next

#     print("None")


# # First sorted Linked List
# list1 = LinkedList()

# list1.append(22)
# list1.append(33)
# list1.append(44)
# list1.append(55)


# # Second sorted Linked List
# list2 = LinkedList()

# list2.append(11)
# list2.append(25)
# list2.append(35)
# list2.append(50)


# print("List 1:")
# print_list(list1.head)

# print("List 2:")
# print_list(list2.head)


# # Merge
# new_head = merge_sorted_lists(
#     list1.head,
#     list2.head
# )


# print("Merged List:")
# print_list(new_head)

# Check palindromic linked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node

#     def is_palindrome(self):

#         # Step 1: Find the middle
#         slow = self.head
#         fast = self.head

#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next

#         # Step 2: Reverse the second half
#         previous = None
#         current = slow

#         while current is not None:
#             next_node = current.next
#             current.next = previous
#             previous = current
#             current = next_node

#         # Step 3: Compare both halves
#         left = self.head
#         right = previous

#         while right is not None:

#             if left.data != right.data:
#                 return False

#             left = left.next
#             right = right.next

#         return True


# # Create Linked List
# my_list = LinkedList()

# my_list.append(22)
# my_list.append(33)
# my_list.append(44)
# my_list.append(55)
# my_list.append(44)
# my_list.append(33)
# my_list.append(22)


# print(my_list.is_palindrome())

# Remove nth element from end in a linked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node

#     def remove_nth_from_end(self, n):

#         first = self.head
#         second = self.head

#         # Move first pointer n steps ahead
#         for _ in range(n):
#             if first is None:
#                 return

#             first = first.next

#         # Move both pointers
#         while first is not None and first.next is not None:
#             first = first.next
#             second = second.next

#         # If we have to remove the first node
#         if first is None:
#             self.head = self.head.next
#             return

#         # Remove nth node
#         second.next = second.next.next

#     def print_list(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" → ")
#             current = current.next

#         print("None")


# # Create Linked List
# my_list = LinkedList()

# my_list.append(22)
# my_list.append(33)
# my_list.append(44)
# my_list.append(55)
# my_list.append(66)

# print("Before:")
# my_list.print_list()

# # Remove 2nd node from the end
# my_list.remove_nth_from_end(2)

# print("After:")
# my_list.print_list()

# 1. Create a Doubly Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None


# # Create nodes
# node1 = Node(22)
# node2 = Node(33)
# node3 = Node(44)

# # Connect nodes
# node1.next = node2

# node2.previous = node1
# node2.next = node3

# node3.previous = node2


# # Head
# head = node1

# # Print
# current = head

# while current is not None:
#     print(current.data, end=" ⇄ ")
#     current = current.next

# print("None")

# 2. Append — Add Node at the End

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node
#         new_node.previous = current

#     def print_forward(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" ⇄ ")
#             current = current.next

#         print("None")


# dll = DoublyLinkedList()

# dll.append(22)
# dll.append(33)
# dll.append(44)

# dll.print_forward()

# 3. Prepend — Add Node at the Beginning

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def prepend(self, data):
#         new_node = Node(data)

#         new_node.next = self.head

#         if self.head is not None:
#             self.head.previous = new_node

#         self.head = new_node

#     def print_forward(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" ⇄ ")
#             current = current.next

#         print("None")


# dll = DoublyLinkedList()

# dll.append = None  # Not used here

# dll.prepend(44)
# dll.prepend(33)
# dll.prepend(22)

# dll.print_forward()

# 4. Delete a Node

# Ismein 3 important cases hain:

# Delete head
# Delete middle
# Delete last

# Full program:

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node
#         new_node.previous = current

#     def delete(self, data):
#         current = self.head

#         while current is not None:

#             if current.data == data:

#                 # Delete head
#                 if current.previous is None:
#                     self.head = current.next

#                     if self.head is not None:
#                         self.head.previous = None

#                 # Delete middle or last
#                 else:
#                     current.previous.next = current.next

#                     if current.next is not None:
#                         current.next.previous = current.previous

#                 return

#             current = current.next

#     def print_forward(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" ⇄ ")
#             current = current.next

#         print("None")


# dll = DoublyLinkedList()

# dll.append(22)
# dll.append(33)
# dll.append(44)
# dll.append(55)

# print("Before:")
# dll.print_forward()

# dll.delete(44)

# print("After deleting 44:")
# dll.print_forward()

# 5. Print Forward and Backward

# Doubly Linked List ka advantage ye hai ki hum forward aur backward dono direction mein traverse kar sakte hain.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node
#         new_node.previous = current

#     def print_forward(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" ⇄ ")
#             current = current.next

#         print("None")

#     def print_backward(self):
#         current = self.head

#         if current is None:
#             return

#         # Go to last node
#         while current.next is not None:
#             current = current.next

#         # Move backward
#         while current is not None:
#             print(current.data, end=" ⇄ ")
#             current = current.previous

#         print("None")


# dll = DoublyLinkedList()

# dll.append(22)
# dll.append(33)
# dll.append(44)
# dll.append(55)

# print("Forward:")
# dll.print_forward()

# print("Backward:")
# dll.print_backward()

# 6. Reverse a Doubly Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node
#         new_node.previous = current

#     def reverse(self):
#         current = self.head

#         while current is not None:

#             # Swap previous and next
#             temp = current.previous
#             current.previous = current.next
#             current.next = temp

#             # Current becomes new head
#             if current.previous is None:
#                 self.head = current

#             # Move to next node in original direction
#             current = current.previous

#     def print_forward(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" ⇄ ")
#             current = current.next

#         print("None")


# dll = DoublyLinkedList()

# dll.append(22)
# dll.append(33)
# dll.append(44)
# dll.append(55)

# print("Before reverse:")
# dll.print_forward()

# dll.reverse()

# print("After reverse:")
# dll.print_forward()

# WAP to insert a Node in the beginning for DLL.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node
#         new_node.previous = current

#     def insert_at_beginning(self, data):
#         new_node = Node(data)

#         # New node points to current head
#         new_node.next = self.head

#         # If list is not empty,
#         # current head points back to new node
#         if self.head is not None:
#             self.head.previous = new_node

#         # New node becomes the head
#         self.head = new_node

#     def print_forward(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" ⇄ ")
#             current = current.next

#         print("None")


# # Create DLL
# dll = DoublyLinkedList()

# dll.append(22)
# dll.append(33)
# dll.append(44)

# print("Before:")
# dll.print_forward()

# # Insert 11 at beginning
# dll.insert_at_beginning(11)

# print("After:")
# dll.print_forward()

# WAP to insert a Node in the end for DLL.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         # If list is empty
#         if self.head is None:
#             self.head = new_node
#             return

#         # Go to the last node
#         current = self.head

#         while current.next is not None:
#             current = current.next

#         # Connect last node to new node
#         current.next = new_node

#         # Connect new node back to last node
#         new_node.previous = current

#     def print_forward(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" ⇄ ")
#             current = current.next

#         print("None")


# # Create DLL
# dll = DoublyLinkedList()

# dll.append(22)
# dll.append(33)
# dll.append(44)

# print("Before:")
# dll.print_forward()

# # Insert 55 at the end
# dll.append(55)

# print("After:")
# dll.print_forward()

# Complete a function in which tail node of a DLL is given, print the backward traversal of the DLL.
# Question

# Agar DLL hai:
# None ← 22 ⇄ 33 ⇄ 44 ⇄ 55 → None
#                             ↑
# tail
# Humein tail se start karke backward traversal print karna hai:
# 55 → 44 → 33 → 22 → None

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# def print_backward(tail):

#     current = tail

#     while current is not None:
#         print(current.data, end=" → ")
#         current = current.previous

#     print("None")


# # Create Nodes
# node1 = Node(22)
# node2 = Node(33)
# node3 = Node(44)
# node4 = Node(55)

# # Connect Nodes
# node1.next = node2

# node2.previous = node1
# node2.next = node3

# node3.previous = node2
# node3.next = node4

# node4.previous = node3


# # Tail is the last Node
# tail = node4

# # Backward traversal
# print_backward(tail)

# complete a function to delete a node at Nth position of the doubly LL.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.previous = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next is not None:
#             current = current.next

#         current.next = new_node
#         new_node.previous = current

#     def delete_at_position(self, n):

#         # Empty list
#         if self.head is None:
#             return

#         current = self.head
#         position = 0

#         # Reach the Nth Node
#         while current is not None and position < n:
#             current = current.next
#             position += 1

#         # Invalid position
#         if current is None:
#             return

#         # If deleting the head
#         if current.previous is None:
#             self.head = current.next

#             if self.head is not None:
#                 self.head.previous = None

#         else:
#             # Connect previous Node to next Node
#             current.previous.next = current.next

#             # Connect next Node back to previous Node
#             if current.next is not None:
#                 current.next.previous = current.previous

#     def print_forward(self):
#         current = self.head

#         while current is not None:
#             print(current.data, end=" ⇄ ")
#             current = current.next

#         print("None")


# # Create DLL
# dll = DoublyLinkedList()

# dll.append(22)
# dll.append(33)
# dll.append(44)
# dll.append(55)
# dll.append(66)

# print("Before:")
# dll.print_forward()

# # Delete Node at position 2
# dll.delete_at_position(2)

# print("After:")
# dll.print_forward()

# Stack

# stack is a lifo data structure, which means last in first out. It is a linear data structure that serves as a collection of elements, with two main principal operations: push and pop. The push operation adds an element to the top of the stack, and the pop operation removes the top element from the stack.

# class Stack:
#     def __init__(self):
#         self.stack = []

#     # Add element to the top
#     def push(self, data):
#         self.stack.append(data)

#     # Remove and return top element
#     def pop(self):
#         if self.isEmpty():
#             return None

#         return self.stack.pop()

#     # Check whether stack is empty
#     def isEmpty(self):
#         return len(self.stack) == 0

#     # Return top element without removing it
#     def peek(self):
#         if self.isEmpty():
#             return None

#         return self.stack[-1]

#     # Return number of elements
#     def size(self):
#         return len(self.stack)


# # Create Stack
# s = Stack()

# # Push elements
# s.push(22)
# s.push(33)
# s.push(44)

# print("Stack:", s.stack)

# # Peek
# print("Top element:", s.peek())

# # Size
# print("Size:", s.size())

# # Pop
# print("Removed:", s.pop())

# print("Stack after pop:", s.stack)

# # Check empty
# print("Is empty:", s.isEmpty())

# reverse a string using Stack

# def reverse_string(s):

#     stack = []

#     # Push every character into stack
#     for char in s:
#         stack.append(char)

#     reversed_string = ""

#     # Pop every character from stack
#     while len(stack) > 0:
#         reversed_string += stack.pop()

#     return reversed_string


# # Test
# string = "hello"

# print("Original:", string)
# print("Reversed:", reverse_string(string))

# Valid Parentheses
# TC 1 : "{([])}[]()" -> valid
# TC 2: "{{{}}) []" -> Invalid

# def is_valid(s):

#     stack = []

#     pairs = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }

#     for char in s:

#         # Opening bracket
#         if char in "([{":
#             stack.append(char)

#         # Closing bracket
#         else:

#             # No opening bracket available
#             if len(stack) == 0:
#                 return False

#             # Top opening bracket does not match
#             if stack[-1] != pairs[char]:
#                 return False

#             # Matching bracket found
#             stack.pop()

#     # Stack must be empty at the end
#     return len(stack) == 0


# # Test Case 1
# s1 = "{([])}[]()"
# print("TC 1:", is_valid(s1))


# # Test Case 2
# s2 = "{{{}}) []"
# print("TC 2:", is_valid(s2))  

# Question

# Given a string s containing only L and R, use a Stack to determine whether the string can become empty.

# Rules:

# If the character is L, push it into the Stack.
# If the character is R, pop one L from the Stack.
# If R comes when the Stack is empty, return False.
# After processing the complete string, if the Stack is empty, return True; otherwise return False.

# Given:

# s = "LRRLRLRLR"
# class Stack:

#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if self.isEmpty():
#             return None

#         return self.stack.pop()

#     def isEmpty(self):
#         return len(self.stack) == 0

# def isValidLR(s):
#     stack = Stack()
#     for ele in s:
#         if ele == 'L':
#             stack.push(ele)
#         else:
#             if stack.isEmpty():
#                 return False
#             stack.pop()
#     return stack.isEmpty()
# s = "LRRLRLRLR"
# print(isValidLR(s))

# Find Next greater element of each element present in a list, return the ans list.
# Ex:
# a = [2,1,5,3,4]
# ans = [5,5,-1,4,-1]

# def next_greater_element(a):
#     ans = [-1] * len(a)
#     stack = []
#     for i in range(len(a) - 1, -1, -1):
#         while len(stack) > 0 and stack[-1] <= a[i]:
#             stack.pop()
#         if len(stack) > 0:
#             ans[i] = stack[-1]
#         stack.append(a[i])
#     return ans
# a = [2, 1, 5, 3, 4]
# print(next_greater_element(a))

# Queue is a linear data structure that follows the First In First Out (FIFO) principle. The element that is added first will be removed first. It has two main operations: enqueue (to add an element to the end of the queue) and dequeue (to remove an element from the front of the queue).

# Implement Queue class by using list.

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, data):
#         self.queue.append(data)

#     def dequeue(self):
#         if self.isEmpty():
#             return None

#         return self.queue.pop(0)

#     def front(self):
#         if self.isEmpty():
#             return None

#         return self.queue[0]

#     def isEmpty(self):
#         return len(self.queue) == 0

#     def size(self):
#         return len(self.queue)


# # Testing

# q = Queue()

# q.enqueue(22)
# q.enqueue(33)
# q.enqueue(44)
# q.enqueue(55)

# print(q.queue)

# print(q.front())

# print(q.dequeue())
# print(q.dequeue())

# print(q.queue)

# print(q.size())
# print(q.isEmpty())

#  Queue using List ki complexity

# Yahan interview mein ek important point hai.

# enqueue
# self.queue.append(data)

# Average:

# O(1)
# dequeue
# self.queue.pop(0)

# Ye:

# O(n)

# kyunki first element remove hone ke baad baaki elements shift hote hain.

# Types of Queue : 
# 1. Simple Queue - Follows FIFO principle
# 2. Circular Queue - The last position is connected back to the first position
# 3. Priority Queue - Each element has a priority and is dequeued based on its priority

# Python mein Priority Queue ke liye commonly: heapq use hota hai. --- Python ka built-in module hai jo heap / priority queue implement karne mein help karta hai.

# import heapq

# priorityQueue = []

# heapq.heappush(priorityQueue, 30)
# heapq.heappush(priorityQueue, 10)
# heapq.heappush(priorityQueue, 20)

# print(heapq.heappop(priorityQueue))

# Output:10

# Why 10?

# Python ka default heapq min-heap hota hai.

# Matlab smallest element highest priority par hota hai.
# 30
# 10
# 20
# Heap ke andar logically smallest:

# 10

# isliye:

# heapq.heappop(priorityQueue)

# → 10

# Next pop:

# 20

# Next:

# 30

# heappush() aur heappop()
# Add:
# heapq.heappush(priorityQueue, 30)

# Matlab priority queue mein 30 add karo.

# Remove:
# heapq.heappop(priorityQueue)

# Matlab highest-priority element remove karo.

# Default min-heap mein highest priority = smallest value.

# Reverse a Queue

# Reverse a queue present as a parameter in list format. use deque from collections

# Queue se front se nikala
#         ↓
#       List mein dala
#         ↓
# List se back se nikala
#         ↓
# Queue mein dala

# deque = Double Ended Queue
# q = deque()
# Isme dono ends se efficiently operations kar sakte hain.


# from collections import deque
# def reverseQueue(q):
#     stack = []
#     # Queue se elements nikalo aur stack mein dalo
#     while q:
#         stack.append(q.popleft())
#     # Stack se elements nikalo aur queue mein wapas dalo
#     while stack:
#         q.append(stack.pop())
#     return q
# # Testing
# q = deque([10, 20, 30, 40])
# print("Before:", q)
# reverseQueue(q)
# print("After:", q)

# Next Greater Element — Circular Array

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if self.isEmpty():
#             return None
#         return self.stack.pop()

#     def peek(self):
#         if self.isEmpty():
#             return None
#         return self.stack[-1]

#     def isEmpty(self):
#         return len(self.stack) == 0


# def nextGreaterElementCircular(a):
#     n = len(a)
#     ans = [-1] * n

#     s = Stack()

#     for i in range(2 * n - 1, -1, -1):

#         currentElement = a[i % n]

#         while s.isEmpty() == False and s.peek() <= currentElement:
#             s.pop()

#         if i < n and s.isEmpty() == False:
#             ans[i] = s.peek()

#         s.push(currentElement)

#     return ans


# a = [2, 1, 5, 3, 4]

# print(nextGreaterElementCircular(a))

# insert a data at beginning in a CLL

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class CircularLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, data):
#         new_node = Node(data)

#         # Empty CLL
#         if self.head is None:
#             self.head = new_node
#             new_node.next = self.head
#             return

#         # Find last node
#         current = self.head

#         while current.next != self.head:
#             current = current.next

#         # New node points to old head
#         new_node.next = self.head

#         # Last node points to new node
#         current.next = new_node

#         # New node becomes head
#         self.head = new_node

#     def print_list(self):
#         if self.head is None:
#             print("Empty")
#             return

#         current = self.head

#         while True:
#             print(current.data, end=" → ")
#             current = current.next

#             if current == self.head:
#                 break

#         print("(back to head)")


# cll = CircularLinkedList()

# cll.insert_at_beginning(30)
# cll.insert_at_beginning(20)
# cll.insert_at_beginning(10)
# cll.insert_at_beginning(5)

# cll.print_list()

