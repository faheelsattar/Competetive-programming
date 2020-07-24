from queue import Queue
import math
class Node:
    def  __init__(self, value):
        self.value= value
        self.left= None
        self.right= None
       
class BinaryTree:
    def __init__(self):
        self.root = None
        self.tagholder=[]

    def insertNode(self, value):
        q = Queue()
        node = Node(value)
        if self.root == None:
            self.root = node
        else:
            tempnode= self.root
            q.put(tempnode)
            while(q.empty() == False):
                tempnode=q.get()
                if tempnode.left == None:
                    tempnode.left= node
                    break
                else:
                    q.put(tempnode.left) 
                if tempnode.right == None:
                    tempnode.right= node 
                    break 
                else:
                    q.put(tempnode.right)                 
    
            
    def bfs(self):
        q = Queue()
        tree=[]
        if self.root == None:
            return 
        else:
            tempnode= self.root
            q.put(tempnode)
            while (q.empty() == False):
                tempnode=q.get()
                tree.append(tempnode) 
                if(tempnode.left != None):
                   q.put(tempnode.left)
                if (tempnode.right != None): 
                    q.put(tempnode.right)
            return tree

    def show(self):
        tree= self.bfs()
        counter=0
        half= math.floor(len(self.tagholder)/2)
        for node  in tree:
            self.tagholder.append(node.value)
        for i in range(0, half):
            holder=self.tagholder[i][:1] + "/"+self.tagholder[i][1:]
            if holder == self.tagholder[len(self.tagholder)- (i+1)]:
                counter = counter +1
        if counter == half:    
            print("cORRECT")
        print(self.tagholder)
          

b1= BinaryTree()
b1.insertNode("<html>")
b1.insertNode("<h1>")
b1.insertNode("</h1>")
b1.insertNode("<h2>")
b1.insertNode("</h2>")
b1.insertNode("</html>")

print(b1.show())



