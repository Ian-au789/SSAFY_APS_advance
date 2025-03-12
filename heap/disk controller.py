# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq


def solution(jobs):
    time = 0
    heapq.heapify(jobs)

    while len(jobs) > 0:
        waiting = []

        if jobs[0][0] >= time:
            if time == 0:
                time = jobs[0][0]

            time += jobs[0][1]
            heapq.heappop(jobs)

        else:
            idx = 0
            while jobs[idx][0] <= time and idx < len(jobs):
                request = jobs[idx][0]
                operation = jobs[idx][1]
                heapq.heappush(waiting, [operation, request, idx])

                idx += 1

                if idx == len(jobs):
                    break

            time += waiting[0][0]
            jobs.pop(waiting[0][2])

    return time


print(solution([[0, 3], [1, 9], [3, 5]]))
