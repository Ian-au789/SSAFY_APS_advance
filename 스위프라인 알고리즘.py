import heapq


def is_intersect(A, B, C, D):
    """선분 (A, B)와 (C, D)가 교차하는지 확인"""
    # 완전 탐색 O(N^2) 비효율적
    def ccw(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    return ccw(A, B, C) * ccw(A, B, D) < 0 and ccw(C, D, A) * ccw(C, D, B) < 0


def sweep_line_intersection(segments):
    """스위프 라인을 사용하여 선분 교차 판별 (힙 활용)"""
    events = []

    # 이벤트 리스트 생성 (시작점, 종료점)
    for i, ((x1, y1), (x2, y2)) in enumerate(segments):
        if x1 > x2:  # x1 < x2가 되도록 정렬
            x1, y1, x2, y2 = x2, y2, x1, y1
        heapq.heappush(events, (x1, 1, i))  # 선분 시작 이벤트
        heapq.heappush(events, (x2, -1, i))  # 선분 끝 이벤트

    active_segments = set()  # 현재 스위프 라인에 있는 선분 저장 (set 사용)

    while events:
        x, event_type, index = heapq.heappop(events)  # 가장 작은 x 값부터 처리

        if event_type == 1:  # 선분 추가
            active_segments.add(index)

            # 현재 존재하는 선분들과 교차 여부 확인
            active_list = sorted(active_segments, key=lambda idx: (segments[idx][0][1], segments[idx][1][1]))  # y 좌표 정렬
            idx = active_list.index(index)

            # 이전 선분과 교차 확인
            if idx > 0 and is_intersect(*segments[active_list[idx - 1]], *segments[index]):
                return True

            # 다음 선분과 교차 확인
            if idx < len(active_list) - 1 and is_intersect(*segments[active_list[idx + 1]], *segments[index]):
                return True

        else:  # 선분 제거
            active_segments.remove(index)

    return False


# 테스트 실행
segments = [((1, 1), (5, 5)), ((2, 3), (6, 1)), ((3, 4), (7, 2))]
print(sweep_line_intersection(segments))  # True (교차 발생)
