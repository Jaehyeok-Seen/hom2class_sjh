class My_stack:
    def __init__(self,size):
        self.size = size
        self.top = -1
        self.stack = [0]*size

    def push(self):
        if self.top == self.size:


















# class Mystack:
#     def __init__(self,size):
#         self.stack = [0]*size
#         self.top = -1
#         self.size = size
#
#     def push(self, item):
#         if self.top == self.size:
#             print("Stack Overflow!")
#             return False
#         self.stack[self.top] = item
#         self.top += 1
#         return True
#
#     def pop(self):
#         if self.top == -1:
#             return -1
#         self.top -= 1
#         return self.stack[self.top]
#
#     def is_empty(self):
#         return self.top == 0
