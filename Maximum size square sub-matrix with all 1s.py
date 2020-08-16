#Given a binary matrix nxm which contains only 1 and 0, find the largest sub-square matrix which only contains 1s.
class Solution:
    def maxSubMatrix(self, Arr):
        # write your method here
        r=len(Arr)
        c=len(Arr[0])
        aux = [[0 for x in range(c)] for y in range(r)] 
        i=0
        for j in range(c):
            aux[i][j]=Arr[i][j]
        for j in range(r):
            aux[j][i]=Arr[j][i]
        ma=0
        for i in range(1,r):
            for j in range(1,c):
                if Arr[i][j]==0:
                    aux[i][j]=0
                else:
                    aux[i][j]=1+min(Arr[i-1][j],Arr[i][j-1],Arr[i-1][j-1])
                    Arr[i][j]=1+min(Arr[i-1][j],Arr[i][j-1],Arr[i-1][j-1])
                    ma=max(ma,aux[i][j])
        return ma
