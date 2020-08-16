'''Mary has an n x m piece of paper that she wants to cut into 1 x 1 pieces according to the following rules:

She can only cut one piece of paper at a time, meaning she cannot fold the paper or layer already-cut pieces on top of one another.
Each cut is a straight line from one side of the paper to the other side of the paper. For example, the diagram below depicts the three possible ways to cut a  3 x 2 piece of paper:

Given  n and m, find and print the minimum number of cuts Mary must make to cut the paper into n.m squares that are      1 x 1 unit in size.

Note : you have to write the complete code for taking input and print the result.

Input Format

A single line of two space-separated integers denoting the respective values of  n and m.
'''
n,m=map(int,input().split())
print((n-1)+n*(m-1))
