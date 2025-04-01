import array
# array 모듈 불러오기

class ArrayList:
    def __init__(self,n):
        self.capacity = n
        array.array('h',[0]*self.capacity)
        # array 모듈에서 그 안에 있는 array 클래스 불러오기
        # 'h'는 타입코드를 의미함 (signed short 정수, 범위: -32,768 ~ 32,767)
        self.size = 0
        

    def add(self,index,item):
        if self.size >= self.capacity:
            return "Array is alreay full."
        # 파이썬에는 return이 실행되면 아래 코드가 실행되지 않기 때문에 굳이 else를 적지 않아도 괜찮음
        elif index<0 or index>self.size:
            # array는 앞에서부터 순서대로 채워지는 구조라 index>self.size로 적어줘야함
            # index > self.capacity - 1로 하면, capacity가 [1, 2, , ]의 array에서 add(3, 1)가 Invalid index 조건에 걸리지 않고 이후 에러 만듦 
            return "Invalid index"
        else:
            for i in range(self.size-1, index-1, -1):
                self.array[i+1] = self.array[i]
                # 전역 array가 아니기 때문에 무조건 self.array로 적어줘야함
                
            # for i in range(self.size, index, -1):
            #     self.array[i] = self.array[i-1]
            
            # 둘 다 가능 (시간 복잡도 둘 다 O(n)), 직관성의 차이
            
            self.array[index] = item
            # item을 추가하는건 else안에 포함되도록 적기(안그럼 에러가 나도 추가해 버리는 불상사 생김)
            self.size += 1
            # self.size의 숫자를 늘리는 작업은 item이 생긴 후 적는게 논리상 더 맞음
            
            
    def remove(self,idx):
        "Student Code"

    def print(self):
        "Student Code"

    def replace(self,idx,item):
        "Student Code"


    def find(self,item):
        "Student Code"


    def is_full(self):
        "Student Code"
        

if __name__=='__main__':
    arr = ArrayList(5)
    arr.add(0,6)
    arr.add(1,1)
    arr.add(2,4)
    arr.add(3,7)
    arr.is_full()

    arr.print()
    

    arr.add(4,1)
    arr.replace(2,5)
    arr.is_full()
    arr.print()
 
    arr.add(1,10)
    arr.print()