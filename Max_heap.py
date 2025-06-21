#implement maxheap
class Mheap:
    def __init__(self,arr):
        self.arr=arr #list
    def insert(self,val):
        #append in to self.arr(to maintain completeness)and then heapify
        self.arr.append(val)
        self.heapify_up(len(arr)-1)
    def heapify_up(self,ind):
        parent=(ind-1)//2
        if(parent<0):
            return
        if(self.arr[parent]<self.arr[ind]):
            self.arr[parent],self.arr[ind]=self.arr[ind],self.arr[parent]
            self.heapify_up(parent) #all the way up(to root)
    def delete(self):
        #we can delete only the root so replace that with last element to maintain completeness
        self.arr[0]=self.arr[-1]
        self.arr.pop()
        #now heapify down 
        self.heapify_down(0) #index is 0
    def heapify_down(self,ind):
        left,right=2*ind+1,2*ind+2
        if(left>=len(self.arr)):
            return #ind itself a root
        elif(right>=len(self.arr)):
            if(self.arr[ind]<self.arr[left]): #left was last left
                self.arr[ind],self.arr[left]=self.arr[left],self.arr[ind]
                return
        else:
            #both children were there
            if(self.arr[right]>self.arr[left] and self.arr[right]>self.arr[ind]):
                self.arr[ind],self.arr[right]=self.arr[right],self.arr[ind]
                self.heapify_down(right) #pruning the left ssubtree, this makes tc=O(logn)
            elif(self.arr[left]>self.arr[right] and self.arr[left]>self.arr[ind]):
                self.arr[ind],self.arr[left]=self.arr[left],self.arr[ind]
                self.heapify_down(left)
            else:
                return
    def heapify(self):
        #from internal nodes to root node heapify down
        for i in range(len(self.arr)//2-1,-1,-1):
            self.heapify_down(i)
        return self.arr
#how to run this 
arr=[3,8,5,10,15,35,9,18,27]
heap=Mheap(arr)
arr=heap.heapify()
print(arr)
a=[105,37,1]
for i in a:
    heap.insert(i)
print(arr)
#delete operations
heap.delete()
print(arr)
heap.delete()
print(arr)

