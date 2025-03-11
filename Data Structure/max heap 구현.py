# class로 최대 힙을 구현해보자
# 완전 이진트리는 부모 노드를 자식 노드의 인덱스의 정수 나눗셈 2에 저장된다.

class MaxHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._siftup(len(self.heap) - 1)         # 노드 새로 삽입하고 순서 검사

    def _siftup(self, idx):
        parent = (idx - 1) // 2

        while idx > 0 and self.heap[idx] > self.heap[parent]:    # 힙의 범위를 벗어나지 않고 자식 노드가 부모 노드보다 클 경우
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]    # 서로 자리 바꾸기
            idx = parent
            parent = (idx - 1) // 2

    def heappop(self):           # 힙은 오직 루트 노드만 삭제
        if len(self.heap) == 0:
            raise IndexError("힙이 비었습니다.")

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()    # 제일 마지막 리프 노드를 루트 노드에 저장
        self._siftdown(0)                 # 아래로 내려가며 위치 조정
        return root

    def heapify(self, array):             # 받은 리스트를 힙으로 변환
        self.heap = array[:]
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):      # 리스트의 중앙에서 시작해 모든 노드에 sift-down 실행
            self._siftdown(i)                    # 리스트 중앙 위치가 힙에서는 마지막 리프 노드를 자식으로 가지는 노드

    def _siftdown(self, idx):
        n = len(self.heap)
        largest = idx
        left = 2 * idx + 1         # 왼쪽 오른쪽 자식 노드
        right = 2 * idx + 2

        if left < n and self.heap[left] > self.heap[largest]:     # 왼쪽 자식보다 크기가 작으면 최댓값 갱신
            largest = left

        if right < n and self.heap[right] > self.heap[largest]:   # 오른쪽 자식보다 크기가 작으면 최댓값 갱신
            largest = right

        if largest != idx:                                        # 부모 노드가 최댓값이 아니라면 최댓값과 자리 바꾸기
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self._siftdown(largest)                               # 원하는 위치에 도달할 때 까지 반복

