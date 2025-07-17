class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        if self.head:
            temp = self.head
            print("None <---> ", end = "")
            while temp is not None:
                print(temp.value,end = " <---> ")
                temp = temp.next
            print("None")
        else:
            return None
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            return True
        
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp     # for remove we dont need temp.value, we need temp  
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
        return True
    
    def popFirst(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp   # for remove we dont need temp.value, we need temp  
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return "invalid index"
        elif index < (self.length//2):
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp     # for insert and remove we dont need temp.value, we need temp
    
    def insert(self, index, value):
        if index < 0 or index > self.length:    # index out of bounds
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index-1)
            after = before.next

            new_node.next = after
            new_node.prev = before
            before.next = new_node
            after.prev = new_node
            self.length += 1
            return True
    
    def remove(self, index, value):
        if index < 0 or index > self.length:
            return "invalid index"
        elif index == 0:
            return self.prepend()
        elif index == self.length:
            return self.pop()
        else:
            temp = self.get(index)

            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp.value
