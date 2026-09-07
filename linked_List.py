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

