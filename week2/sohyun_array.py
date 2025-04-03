import array
# array 모듈 불러오기
# array 모듈을 불러와야 하는데 파일 이름이 array이면 내 파일 자체를 불러올 수 있으니 이름은 모듈 이름과 같으면 안됌

class ArrayList:
    def __init__(self,n):
        self.capacity = n
        self.array = array.array('h',[0]*self.capacity)
        # array 모듈에서 그 안에 있는 array 클래스 불러오기
        # 'h'는 타입코드를 의미함 (signed short 정수, 범위: -32,768 ~ 32,767)
        # 배열을 만든 후, self.array에 저장해줘야함!!
        self.size = 0
        

    def add(self,idx,item):
        if self.size >= self.capacity:
            return "Array is alreay full."
        # 파이썬에는 return이 실행되면 아래 코드가 실행되지 않기 때문에 굳이 else를 적지 않아도 괜찮음
        elif idx<0 or idx>self.size:
            # array는 앞에서부터 순서대로 채워지는 구조라 index>self.size로 적어줘야함
            # index > self.capacity - 1로 하면, capacity가 [1, 2, , ]의 array에서 add(3, 1)가 Invalid index 조건에 걸리지 않고 이후 에러 만듦 
            return "Invalid index"
        else:
            for i in range(self.size-1, idx-1, -1):
                self.array[i+1] = self.array[i]
                # 전역 array가 아니기 때문에 무조건 self.array로 적어줘야함
                
            # for i in range(self.size, index, -1):
            #     self.array[i] = self.array[i-1]
            
            # 둘 다 가능 (시간 복잡도 둘 다 O(n)), 직관성의 차이
            
            self.array[idx] = item
            # item을 추가하는건 else안에 포함되도록 적기(안그럼 에러가 나도 추가해 버리는 불상사 생김)
            self.size += 1
            # self.size의 숫자를 늘리는 작업은 item이 생긴 후 적는게 논리상 더 맞음
            
            
    def remove(self,idx):
        if self.size == 0:
            return "Empty Array"
        elif 0 > idx or idx >= self.size:
            return "Invalid index"
        
        # remove라고 그 index칸의 element를 없애는 작업을 할 필요 없음
        # 그냥 뒤의 element들을 한칸씩 당겨서 덮어 씌우면 됌
        for i  in range(idx+1, self.size):
        # self.size까지만 당겨야함
        # self.capacity까지 반복되면 element가 없는 쓰레기 값까지 복사됌
            self.array[i-1] = self.array[i]
        self.array[self.size-1] = 0
        # 원래의 self.size가 self.capacity와 같으면 self.capacity의 값을 0으로 초기화 하는 것이 맞음 
        # 하지만 그게 아니라면 마지막 칸이 항상 마지막 요소의 자리가 아닐 수도 있음
        # 따라서 self.szie - 1의 값을 0으로 초기화 하는 것이 맞음
        self.size -= 1
            

    def print(self):
        # print(self.array)
        # 이렇게 쓰면 배열 전체의 메모리 구조를 출력해내기 때문에 배열 구조가 명확하게 보이지 않음
        # ex) array('h', [10, 20, 30, 0, 0]) 이런식으로 출력됌
        for i in range(0, self.capacity):
        # 반복 범위 self.size: 시간 복잡도 - O(n) / 러닝 타임 - 빠름 / 메모리 사용 - 같음
        # 반복 범위 self.size: 시간 복잡도 - O(N) / 러닝 타임 - 느림 / 메모리 사용 - 같음
        # 시간 복잡도 n과 N의 차이: n = 현재 요소 개수, N = 전체 배열 길이(최대 용량)
            print(self.array[i], end=" ")
        print()
        # 줄바꿈

    def replace(self,idx,item):
        if self.size == 0:
            return "Empty Array"
        elif 0 > idx or idx >= self.size:
            return "Invalid index"
        self.array[idx] = item


    def find(self,item):
        if self.size == 0:
            return "Empty Array"
        for i in range(0, self.size):
        # 반복 범위를 capacity로 잡으면 0으로 초기화된 빈 공간까지 탐색하게 됌
            if self.array[i] == item:
                return i
        return -1
        # 값을 못 찾았을 때의 return도 있어야함
        # return -1이 없으면 암묵적으로 None이 반환되기는 하지만, 명시적인 실패 표현으로 return -1을 해주는 것이 좋음


    def is_full(self):
        print(self.size == self.capacity)
        # 코드 중간 상태 확인용 (배열이 가득 찼는지 여부를 확인하기 위해 필요한 함수)
        # 가득 찼다면 True, 아직 가득 차지 않았다면 False 반환함
        # return self.size == self.capacity로 적으려면 102번쨰 줄에는 print(arr.is_full())로 적어줘야 함
        

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