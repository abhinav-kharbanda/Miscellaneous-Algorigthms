# Solution for the problem https://www.hackerrank.com/contests/101hack19/challenges/two-strings

import string
arr1=[]
arr2=[]
ans=[]
num=int(raw_input())
for i in range(num):
        arr1=raw_input()
        arr2=raw_input()
        flag=0
        for letter in string.ascii_lowercase:
            if letter in arr1 and letter in arr2:    
                ans.append("YES")
                flag=1
                break
        if(not flag):
        	ans.append("NO")


print "\n".join(ans)
                