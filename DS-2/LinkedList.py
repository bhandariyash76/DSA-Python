class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    linked_List = LinkedList()
    linked_List.head = Node(1)
    second = Node(2)
    third = Node(3)

    linked_List.head.next = second
    second.next = third

    while linked_List.head != None:
        print(linked_List.head.item , end=" ")
        linked_List.head = linked_List.head.next
        