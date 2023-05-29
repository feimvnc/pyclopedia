class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None 
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node 
        
    def printList(self):
        temp = self.head 
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next 
        print("\n")
            
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = prev 
            prev = current 
            current = temp 
        self.head = prev 


def main():
    lst = LinkedList()
    lst.push(1)
    lst.push(2)
    lst.push(3)
    lst.push(4)
    lst.push(5)
    lst.printList()

    lst.reverse()
    lst.printList()
    
if __name__ == "__main__":
    main()

