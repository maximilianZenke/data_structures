class Node: 
    def __init__(self, data):
        self.data = data
        self.next: Node | None  = None

class Linked_List: 
    def __init__(self): 
        self.head: Node | None =  None 

    def length(self): 
        tmp = self.head 
        count = 0
        while tmp is not None: 
            count += 1 
            tmp = tmp.next 
        print(count)

    def delete(self, data):
        tmp = self.head
        # head
        if(tmp.data == data): 
            newHead = tmp.next 
            self.head = newHead
            return 
        # somewhere inbetween or last 
        while tmp is not None and tmp.next.data != data: 
            tmp = tmp.next 
        if tmp is None: 
            return 
        else: 
            tmp.next = tmp.next.next 

    def prepend(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def append(self,value):
        newNode = Node(value)    
        if (self.head == None): 
            self.head = newNode
        else: 
            tmp = self.head 
            while(tmp.next != None):
                tmp = tmp.next
            tmp.next = newNode
    
    def print_list(self): 
        tmp = self.head
        while tmp is not None: 
            print(tmp.data)
            tmp = tmp.next 


ll = Linked_List()
ll.append(17)
ll.prepend(1)
ll.prepend(0)
ll.print_list()
ll.delete(1)
print(".....")
ll.print_list()
