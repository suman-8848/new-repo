class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    def insert_beginning(self, data):
        node = Node(data,self.head)
        self.head = node
    def print_list(self):
        itr = self.head
        listr = ''
        if self.head is not None:
            while itr:
                listr+= str(itr.data) +'-->'
                
                itr = itr.next
            
        print(listr)
    def insert_at_mid(self,data,pos):
        
        beg = self.head
        getpos =0
        while beg:
            if getpos == pos-1:
                node = Node(data,beg.next)
                beg.next = node
                break
            
            beg = beg.next
            getpos+=1
        




            



if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_beginning(6)
    l1.insert_beginning(3)
    l1.insert_beginning(0)
    l1.insert_beginning(1)
    l1.insert_at_mid(8,4)
    l1.print_list()
    


