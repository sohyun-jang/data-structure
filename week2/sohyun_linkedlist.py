class Node: # Node class
    def __init__(self, data):
        self.data = data
        self.link = None
# TIP : None is considered as False in Python

class LinkedList: # Linked list class
    def __init__(self): # Initalize
        self.head = None
        self.tail = None
    
    def append(self, data): # Add new node at the end
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
            # return을 쓰는 이유는 만약 이 조건이 성립할 경우, 밑에 있는 코드를 작성시키지 않고 빠르게 마무리 하기 위하여
            # return을 안적고 if, else로도 같은 시간 복잡도로 같은 결괏값을 만들 수 있음 (하지만 각자의 특징 있음)
            # return: 중간 종료 방식 (코드가 빠르게 빠져나가는 구조로, 불필요한 들여쓰기 줄일 수 있음)
            # if, else: 명확한 분기 (두 경우로 나뉨을 강조할 수 있음, 상황에 따라 가독성이 좋을 수도, 나쁠 수도 있음)
        
        self.tail.link = new_node
        self.tail = new_node
        # 위의 조건문에서 return이 실행되면 밑에는 작동하지 않기 때문에 굳이 else 적지 않아도 괜찮음
    
    def prepend(self, data): # Add new node at the beginning
        new_node = Node(data)
        
        # if self.head is None:
        #     self.head = new_node
        #     self.tail = new_node
        #     return
        # 라고 할 수도 있지만 굳이 조건을 걸지 않아도 됌
        new_node.link = self.head
        self.head = new_node
        # 만약 self.head 값이 None이어도, new_node가 가리키는게 None이어도 상관 없기 때문에 조건을 걸 필요가 없음
        
        if self.tail is None:
            self.tail = new_node
            # 하지만 앞에 추가하는 것이기 때문에 tail은 따로 조건을 걸어주어야함 (빈 노드일 경우)
            
    
    def delete(self, data): # Delete the node with specific value
        prev = None
        curr = self.head
        
        while curr:
        # while curr is not None과 같은 의미 (연결 리스트를 처음부터 끝까지 순회함)
            if data == curr.data:
            # 데이터가 연결 리스트 안에 여러개 있을 수 있지만, 1개만 삭제하고 빠져나오는 코드
                if curr == self.head:
                    self.head = curr.link
                elif curr == self.tail:
                    self.tail = prev
                    self.tail.link = None
                else:
                    prev.link = curr.link
                return
            prev = curr
            curr = curr.link
        return "There is no data in this Linked List"
            
    
    def search(self, data): # Search the node with specific value
        curr = self.head
        while curr:
            if curr.data == data:
            # 이해가 완벽히 되지는 않았지만, curr은 노드 객체 자체를 나타내기 때문에 curr == data가 아닌 curr.data = data 형태로 적어야함
                return True
            curr = curr.link
        return False
    
    def display(self): # Display the linked list
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.link
        print('None')
        
    def reverse(self):
        standard = None
        curr = self.head
        prev = None
        # 길을 잃지 않기 위해서는 3개의 변수 필요함
        
        if curr == None or curr == self.tail:
            return
            # 만약 비어있는 배열이거나, 노드가 한개 뿐이라면 바로 return (뒤에 코드가 실행되지 않음)
        
        while curr:
        # 한 바퀴만에 끝내버림 (= while curr is not None)
            standard = curr.link
            curr.link = prev
            prev = curr
            curr = standard
            # 계속해서 뒤에서부터 바꿀 방법을 고민했는데, 앞에서부터 바꾸면 쉬움
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # 마지막에 무조건 self.head 포인터와 self.tail 포인터 바꿔줘야함
                


linkedList = LinkedList()
linkedList.append(10)
linkedList.append(20)
linkedList.prepend(5)
linkedList.prepend(30)
linkedList.display() # 30 -> 5 -> 10 -> 20 -> None
linkedList.delete(10)
linkedList.display() # 30 -> 5 -> 20 -> None
linkedList.reverse()
linkedList.display() # 20 -> 5 -> 30 -> None
