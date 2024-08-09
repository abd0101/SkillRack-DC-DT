'''
The program must take two strings s1 and s2 as input. 
For every ch in s1, the program must print the nearest character present in s2.
If two nearest characters are present the program must print the smallest character in s2
Ex. if 'c' has both nearest characters 'a' and 'e' , the program must print 'a' as output. 

Sample Input 1 :verified correct
Sample Output 1 :vt ee r ie fe ie ee dc

'''
s1, s2 = input().split()
s2 = set(s2)
    
for i in s1:
    print(i,end="")
    ch = ord(i)
    for j in range(14):
        neighbor_1 = chr(ch - j)
        neighbor_2 = chr(ch + j)
        if neighbor_1 in s2:
            print(neighbor_1,end=" ")
            break
        elif neighbor_2 in s2:
            print(neighbor_2,end=" ")    
            break
        