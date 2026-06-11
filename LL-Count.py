class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
    def append(self, data):
        new_node = Node(data)
        if not self:
            self = new_node
            return
        temp = self
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def display(self):
        temp = self
        while temp:
            print(temp.data, end='->')
            temp = temp.next
        print("None")
    def displaycount(self):
        temp = self
        count = 0
        counte = 0
        while temp:
            if temp.data %2 == 0:
                counte+= 1
            count += 1
            temp = temp.next
        print("Count:", count)
        print("Even Count:", counte)

n=int(input("Enter the number of nodes: "))
for i in range(n):
    data=int(input("Enter the data for node {}: ".format(i+1)))
    if i == 0:
        head = Node(data)
    else:
        head.append(data)
head.display()
head.displaycount()