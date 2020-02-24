from collections import deque

class MovingAverage:
    
    """
    @param: size: An integer
    """
    def __init__(self, size):
           # do intialization if necessary
           ##self.que = deque([])
           self.que = deque([])
           self.size = size
           self.delta = 0.0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
           if len(self.que) < self.size:
                  self.que.appendleft(val)
           else:
                  self.que.pop()
                  self.que.appendleft(val)
                  self.delta = self.que[0] - self.que[-1]
           return self.delta 
"""
obj = MovingAverage(10)

while True:
    x=input("Please Enter the number：")
    param = round(obj.next(float(x)),2)
    
    print("delta T = ", param)
"""
