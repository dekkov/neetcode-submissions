import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Count frequencies
        counts = Counter(tasks)
        

        max_heap = [cnt for cnt in counts.values()]
        heapq.heapify_max(max_heap)
        
        time = 0
        # 3. Queue to store tasks on cooldown: [remaining_count, available_time]
        queue = deque()
        
        while max_heap or queue:
            time += 1
            
            if max_heap:
                # Pop the task with the most remaining instances

                cnt = heapq.heappop_max(max_heap) - 1
                
                if cnt > 0:
                    # Task still needs to run again, put it in the cooldown queue
                    # It will be available again at current `time + n`
                    queue.append([cnt, time + n])
            
            # 4. Check if the task at the front of the queue has finished its cooldown
            if queue and queue[0][1] == time:
                # The task is ready, push its remaining count back into the max-heap
                ready_task_count = queue.popleft()[0]
                heapq.heappush_max(max_heap, ready_task_count)
                
        return time