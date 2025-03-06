# Class로 단순 연결 리스트를 구현해보자

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None                   # 가장 앞의 노드를 가리키는 표지판

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:                  # 연결 리스트 맨 앞에 삽입하면
            new_node.next = self.head      # 원래 첫 번째 항목을 다음 항목으로 연결
            self.head = new_node           # 현재 항목을 첫 번째 항목으로 업데이트

        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    print("범위를 벗어난 삽입입니다.")
                    return
                current = current.next     # 맨 앞 항목에서부터 다음 항목 하나씩 순서대로 탐색하며 원하는 위치의 선행노드까지 도달
            new_node.next = current.next   # 원래 해당 위치보다 한 칸 앞에 있던 항목을 추가하는 노드의 다음 항목으로 연결
            current.next = new_node        # 선행 노드의 다음 노드와 next로 연결, n-1번째 노드의 next를 자신과 연결 -> n 번째 위치에 삽입

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next     # 하나씩 순서대로 탐색하며 마지막 항목까지 도달
            current.next = new_node        # 마지막 항목 다음에 새로운 노드 연결

    def is_empty(self):
        return self.head is None

    def delete(self, position):
        if self.is_empty():
            print("단순 연결 리스트가 비었습니다")
            return

        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):                    # 삭제하고자 하는 노드의 선행노드까지 도달
                if current is None or current.next is None:
                    print("범위를 벗어났습니다")
                    return
                current = current.next

            deleted_node = current.next                      # 해당 노드의 다음 노드를 삭제
            deleted_data = deleted_node.data
            current.next = current.next.next                 # 삭제한 노드의 다음 노드와 현재 노드를 연결

        return deleted_data

    def search(self, data):
        current = self.head               # 0번째 항목부터 탐색
        position = 0
        while current:
            if current.data == data:      # 찾고자 하는 값과 일치하는 값을 찾을때 까지 탐색
                return position
            current = current.next
            position += 1
        return -1                         # 범위를 벗어날때까지 찾지 못했으면 -1 반환

    # 내가 만든 remove
    def remove(self, data):
        if self.head.data == data:        # 삭제하고자 하는 데이터가 첫 번째 항목에 있으면
            self.head = self.head.next    # head를 다음 항목으로 할당

        current = self.head
        position = 0

        while current:
            if current.next.data == data:          # 삭제하고자 하는 항목 발견시
                current.next = current.next.next   # 그 다음 항목과 그 전 항목 연결 (없다면 자동으로 None으로 설정)
                return
            current = current.next
            position += 1
        print("해당 항목은 존재하지 않습니다.")
        return

    def __str__(self):
        result = []
        current = self.head
        while current:                    # 연결 리스트 내부의 모든 항목 result에 저장
            result.append(current.data)
            current = current.next
        return str(result)                # 문자열 형태로 반환


llist = SinglyLinkedList()

llist.append(1)
llist.append(3)
llist.append(5)

print(str(llist))

llist.insert(2, 1)
llist.insert(4, 3)

print(str(llist))

llist.delete(3)
print(str(llist))
llist.remove(3)
print(str(llist))
llist.remove(5)
print(str(llist))
