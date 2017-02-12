# implement queue using stack:
from collections import deque
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        print x
        self.q1.appendleft(x)

            
        
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.appendleft(self.q1.popleft())
        
        res = self.q1.popleft()
        # self.q2.appendleft(res)
        
        while self.q2:
            self.q1.appendleft(self.q2.popleft())
        self.q2 = deque()
        return res
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.q1[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.q1)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
