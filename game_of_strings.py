'''You are given an initial string s and a final string t. A game played with strings that lasts for k seconds has the following rules:

1)For each i from 1 to k (both inclusive), any index from string s is selected and character at that index is shifted i units to the right. The shift is circular, that is, if z is shifted by 1 unit, it becomes a.
2)Any  index i can be picked at most once.

  Write a program to identify if string t can be achieved from string s by following the rules,
Input format:-

The first line contains N, the number of test cases. Each test case contains
A string s
A string t
An integer k

Output format:-

Print Yes if string t can be achieved from string s using the given rules. Otherwise, print No.

Constraints:

1 <= len(s), len(t) <= 106
1 <= N <= 100

Example Input
4
edyst
geyst
3
input
ouput
9
abc
bcd
55
abc
bcd
10

Example output
Yes
Yes
Yes
No'''

def diff(f,s):
    c=ord(f)-ord(s)
    if c>0:
        c=(122-ord(f))+((ord(s)+1)-97)
    return abs(c)
for _ in range(int(input())):
    s=input()
    t=input()
    k=int(input())
    a=[]
    flag=1
    for i in range(len(s)):
        v=diff(s[i],t[i])
        if v!=0:
            if v not in a and 1<=v<=k:
                a.append(v)
            else:
                l=k//26
                for j in range(1,l+1):
                    h=(v+(j*26))
                    if 1<=h<=k and h not in a:
                        a.append(h)
                        break
                else:
                    flag=0
                    break
    if(flag):
        print('Yes')
    else:
        print('No')
