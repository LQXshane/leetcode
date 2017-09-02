# basic version: don't allow reordering of tasks. (hashmap)
# tasks = ['A','A','A','B','B','B'], n = 2
import collections
def basicScheduler(tasks, n):
    '''
    type A: array of tasks
    type n: cool down period
    rtype int: number of intervals the CPU will take to finish all the given tasks
    '''
    # A__A__AB__B__B
    cd = {}; res = ""
    time = 0
    for x in tasks:
        if x in cd and time <= cd[x] + n:
            cd[x] += n + 1
            while time < cd[x]: time += 1; res += "_"
            res += x
        else:
            cd[x] = time
            res += x
        time += 1
        print time, cd
    print res
    return time


res = basicScheduler(['A','B','B','A','B','B'], 3); print res
# AB__BA_B__B

# 621. Task Scheduler
'''
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
'''

from heapq import *
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not n: return len(tasks)
        task_collection = collections.Counter(tasks)
        pq, wait = [], []
        cpu_list = []
        for name, freq in task_collection.items():
            heappush(pq, (- freq, name)) # heapq is minheap

        time = 0
        k = n + 1
        while pq or wait:
            if k == 0:
                while wait: heappush(pq, wait.pop(0))
                k = n + 1
            if pq:
                count, task = heappop(pq)
                count += 1
            else:
                count, task = 0, "idle"
            cpu_list.append(task)
            if count != 0 and count != "idle":
                wait.append((count, task))
            k -= 1
        return len(cpu_list)




# import heapq
# class Solution(object):
#     def leastInterval(self, tasks, n):
#         """
#         :type tasks: List[str]
#         :type n: int
#         :rtype: int
#         """
#         class Task(object):
#             """
#                 Task class to encapsulate notion of task
#             """
#             def __init__(self, name, count):
#                 self.name  = name       # name of task
#                 self.count = -count     # number of instances
#                 self.time  = -1         # time at which it last ran
#
#             def __repr__(self):
#                 return self.name +':' +str(self.count)
#
#             def schedule(self, time):
#                 self.time   = time      # task is scheduled, update time at which it last ran
#                 self.count  += 1        # decrease count
#
#             #def __cmp__(self, other):
#             #    cmp(self.count, other.count)
#
#             def __lt__(self, other):
#                 # if two have same count, use the one with lexicographically smaller
#                 return self.count < other.count or self.count == other.count and self.name < other.name
#
#         if n == 0:
#             # if no cooling period, simply return as many tasks as there're
#             return len(tasks)
#
#
#
#         task_collection = collections.Counter(tasks) # count task occurrences
#         cpu_slots       = []                         # a sequence depicting which task runs when
#         runq            = []                         # a run queue,  a priority queue
#         waitq = collections.deque([])                # a wait queue, a simple queue
#
#         # push all tasks in a run que
#         for name, count in task_collection.items():
#             heapq.heappush(runq, Task(name, count))  # higher the instances, higher the priority
#
#         idle_task = Task("idle", 0) # an idle task
#         time = 0                    # clock
#         while runq or waitq:        # if at least one of the queue has some tasks to run
#
#             if waitq and ( time - waitq[0].time ) > n:  # if wait queue has task whose cooling period has come
#                 heapq.heappush(runq,waitq.popleft())    # put that task in run queue
#
#             if runq:     # schdule highest priority task, if one is ready
#                 task = heapq.heappop(runq)
#                 task.schedule(time)  # consume one instance
#             else:       # no task is ready, so schedule idle task
#                 task = idle_task
#
#             cpu_slots.append(task.name) # task scheduled on CPU
#             if task is not idle_task and task.count != 0:
#                 waitq.append(task)      # if task is not idle task and has at least some instances to run
#             time += 1
#         print cpu_slots
#         return len(cpu_slots)   # cpu slots will also print task schedule
#
# sol = Solution()
# res = sol.leastInterval(['A','A','A', 'B','B','B', 'C'], n = 3)
# print res
