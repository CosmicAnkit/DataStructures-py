class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    

    def Insertfirst(self,data):
        '''this function will take an element and insert it in beginning 
        of the list''' 
        node = Node(data,self.head)
        self.head=node

    def ShowList(self):
        '''this function will print elements of linkedlist'''
        if self.head == None:
            print('list is empty.')
        else:
            var = self.head   ## I have created it for itrate through list.
            linkedlist = ''
            while var:
                linkedlist+=str(var.data)+'--->'
                var = var.next
            print(linkedlist)

    def Length(self):
        '''this function will print the length of linkedlist'''
        count = 0
        var = self.head
        while var:
            count+=1
            var = var.next
        print(count)
    
    def IndexInsert(self,index,data):
        ''' this function will take two arguments ,index and element and 
        it will insert the element to given index.'''
        if index<0:
            raise IndexError('Please enter valid Index...!')
        elif index==0:
            self.Insertfirst(data)
        else:
            var = self.head
            count=0
            while var:
                if count == index-1:
                    node = Node(data,var.next)
                    var.next = node
                    break;
                count+=1
                var = var.next

    def popfirst(self):
        '''this function will delete very first element of linkedlist'''
        self.head = self.head.next

    def IndexPop(self,index):
        '''this function will delete element at given index.'''
        if index<0:
            raise IndexError('Please enter valid Index...!')
        elif index==0:
            self.popfirst()
        else:
            count = 0
            var = self.head
            while var:
                if count==index-1:
                    var.next = var.next.next
                    break;
                count+=1
                var = var.next

    def FindIndex(self,value):
        ''' this function will search index of given elemnt if that
        is present in linkedlist.'''
        var = self.head
        count = 0
        while var:
            if var.data is value:
                break;
            count+=1
            var = var.next
        print(count)
    
    def PopByValue(self,value):
        '''this function will take an element as an input and 
        it will delete it from Linked list.'''
        count = 0
        var = self.head
        while var:
            if var.data is value:
                self.IndexPop(count)
                break;
            count+=1
            var = var.next
   


if __name__=='__main__':
   l = LinkedList()
   l.Insertfirst('12')
   l.Insertfirst(14)
   l.Insertfirst('string')
   l.Insertfirst('data')
   l.ShowList()
   l.Length()
   l.IndexInsert(1,241)
#    l.popfirst()
   l.ShowList()
   l.FindIndex(14)
#    l.IndexPop(2)
   l.ShowList()
   l.FindIndex(14)
   l.PopByValue('string')
   l.ShowList()
