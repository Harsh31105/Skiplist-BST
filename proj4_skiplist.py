from random import random

class SkipList:
    #Skip-List.

    class Element:
        #Skip-List element.

        def __init__(self, value, height):
            #Generating a skip-list element.
            self.value = value
            self.quantity = 1
            self.next = [None]*height
        

    def __init__(self):
        #Generating an empty SkipList
        self.head = self.Element(float("-inf"), height = 0)
        self.tail = self.Element(float("inf"),  height = 0)
        self.numElements = 0
        self.head.next.append(self.tail)


    @staticmethod
    def randomHeight():
        """
        Generates a random height with using a coin-toss geometric distribution.
        """
        height = 1
        #50-50 coin toss. As long as coin-toss has one-result, height is incremented by 1. 
        while random() < 0.5:
            height += 1
        return height


    def searchPath(self, value):
        """
        Let path be the path returned by this method,
        then path[h] stores the last element visited
        at height h during the search of value through
        the skip-list.
        a.k.a. We are storing wherever we should turn. 
        """
        element = self.head
        path = [None]*len(self.head.next)
        #Looping through the levels. 
        for h in range(len(self.head.next)-1, -1, -1):
            #Going in a level until the node is greater than the value we're looking for. 
            while element.next[h].value < value:
                #Every time we meet an element that does not contradict, we mark that we're crossing it. 
                element = element.next[h]
            #After we make the turn, we mark where we made the turn. 
            path[h] = element
        return path


    def trackPath(self, value):
        element = self.head
        path = []
        #Looping through the levels. 
        for h in range(len(self.head.next)-1, -1, -1):
            #Going in a level until the node is greater than the value we're looking for. 
            while element.next[h].value < value:
                #Every time we meet an element that does not contradict, we mark that we're crossing it. 
                path.append(element.next[h].value)
                element = element.next[h]
            #After we make the turn, we mark where we made the turn.
            if h > 0:
                path.append(element.value)
            else:
                path.append(element.next[h].value)
        
        predecessor = self.searchPath(value)
        target = predecessor[0].next[0]
        #Either the element we're looking for is next to the predecessor, or it doesn't exist in the skiplist. 
        if target.value == value:
            for i in range(0,len(path)):
                print(path[i],end="\n")
        else:
            print("Doesn't Exist!")


    def insert(self, value):
        #Inserts a value into the skip-list.
        predecessor = self.searchPath(value)
        target = predecessor[0].next[0]
        self.numElements += 1

        #Counts the number of times of inputs that have been repeated. 
        if target.value == value:
            target.quantity += 1
            return

        #Setting a height. 
        heightChoice = int(input("Press 0 for random height, else enter the height."))
        if heightChoice == 0:
            height = self.randomHeight()
        else:
            height = heightChoice
            
        newElement = self.Element(value, height)

        #This loop connects the new node back to the preceding nodes at each level for its given height.
        for h in range(len(predecessor), height):
            self.head.next.append(self.tail)
            predecessor.append(self.head)

        #For each level, it makes the connections for the predeccesor and the successor nodes. 
        for h in range(height):
            newElement.next[h] = predecessor[h].next[h]
            predecessor[h].next[h] = newElement


    def delete(self, value):
        #Deletes one entry of value in the skip-list.
        predecessor = self.searchPath(value)
        target = predecessor[0].next[0]

        #If the element doesn't actually exist, you can't delete it!
        if target.value != value:
            return

        #Well, now we know we're deleting some element. 
        self.numElements -= 1

        #If repeated insertion has happened before, just deacreasing quantity of it. 
        if target.quantity > 1:
            target.quantity -= 1
            return

        #For all height-levels,        
        for h in range(len(target.next)):
            predecessor[h].next[h] = target.next[h]
            #When we reach the precise predecessor & successor node,
            if predecessor[h] is self.head and predecessor[h].next[h] is self.tail:
                #We delete the entire item/stack and then exit the loop.
                del self.head.next[max(1, h):]
                break

    def __iter__(self):
        """
        Iterator over the element in the skip-list.
        """
        element = self.head.next[0]
        while len(element.next) > 0:
            yield element
            element = element.next[0]


    def __len__(self):
        """
        Returns the number of unique elements in
        the skip-list.
        """
        return self.numElements
    


    def _repr_level(self, l):
        """
        Represents the l-th level in the skip-list.
        """
        return" ".join(["-inf"]
                      +["-"*len(str(x.value)) if l > len(x.next)-1 else str(x.value) for x in self]
                      +["+inf"]) 


    def __repr__(self):
        """
        Represents the skip-list.
        """
        return "\n".join(self._repr_level(l) for l in range(len(self.head.next)-1, -1, -1))

def main():

    skip = SkipList()
    
    while True:
        op = input("Type 'insert' , 'delete' or 'search' for operations.")

        if op == "insert":
            num = int(input("Integer:"))
            skip.insert(num)
            print(skip)
        elif op == "search":
            num = int(input("Integer:"))
            skip.trackPath(num)
        elif op == "delete":
            num = int(input("Integer:"))
            skip.delete(num)
            print(skip)

main()
        
