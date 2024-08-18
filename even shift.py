"""
The program must accept an integer N as the input. The program must print the even integers that can be
formed by shifting the digits to the right in N.
Note:
- At least 1 even digit is always present in N.
The resulting even integers must be printed without leading zeros.

Boundary Condition(s):
10 <= N <= 10^17

Input Format:
The first line contains N.

Output Format:
The first line contains the even integers that can be formed by shifting the digits to the right in N.

Example Input/Output 1:
Input:
4763

Output:
3476 7634

Explanation:
Here N = 4763 and the integers formed by shifting the digits to the right are given below.
4763
3476
6347
7634
So the even integers formed are 3476 and 7634.
Hence the output is
3476 7634

Example Input/Output 2:
Input:
1020030

Output:
1020030 3010200 301020 30102 2003010"""


n = input()
length = len(n) - 1
n = int(n)


if n%2 ==0 : print(n,end=" ")

for i in range(length):
    n =((n%10) * (10**(length))) + (n//10)
    if n%2==0: print(n,end=" ")