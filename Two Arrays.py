# Solution for https://www.hackerrank.com/challenges/two-arrays

n = int(raw_input());
flag=[None] * n;
for i in range(n):
	ninput, sum_final = raw_input().split();
	ninput=int(ninput);
	sum_final=int(sum_final);
	L1=raw_input().split();
	L2=raw_input().split();
	L1.sort(key=int)
	L2.sort(key=int,reverse=True)
	for j in xrange(ninput):
	    if((int(L1[j])+int(L2[j]))>=sum_final):
	        flag[i]='YES';
	    else:
	        flag[i]='NO';
	        break;
print "\n".join(flag);
    