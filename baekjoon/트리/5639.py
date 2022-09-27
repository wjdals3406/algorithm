# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
graph = [[] for _ in range(n)]
root = data[0]
graph[0].append(root)
stack = [root]
flag = 0
for i in range(1,n):
    
    if data[i] < data[i-1]:
        stack.append(data[i])
    else:
        flag = 1
        if stack[-2] > data[i]: # 24 9
            stack.append(data[i])
        elif stack[-2] < data[i]:
            print(stack.pop())
            stack.append(data[i])
    
    
# def preorder(root):
#     preorder(tree[root][0])  # left
#     preorder(tree[root][1])  # right