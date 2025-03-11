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
            while jobs[idx][0] >= time and idx < len(jobs):
                idx += 1
                request = jobs[idx][0]
                operation = jobs[idx][1]
                heapq.heappush(waiting, [operation, request, idx])

                if idx == len(jobs):
                    break

            time += waiting[0][0]
            jobs.pop(idx)

    return time
