# Solution for the problem https://www.hackerrank.com/challenges/almost-sorted
ninput= int(raw_input());
num_array=raw_input().split();
num_array=map(int,num_array)
count=0;
pos=0;
i=0;
flag=1;

def check():
	return (num_array==sorted(num_array,key=int))
def swap(a,b):
    temp=num_array[a];
    num_array[a]=num_array[b];
    num_array[b]=temp
    if(check()):
        print "yes";
        print ("swap %s %s" % (a+1,b+1));
        return True;
    else:
        return False;
    
    
if(check()):
	print "yes";
else:
	while(i<len(num_array)-1):
		if(num_array[i]>num_array[i+1]):
			j=i;
			pos=i;
			count=0;
			while(j<len(num_array)-1 and num_array[j]>num_array[j+1] ):
				count=count+1;
				j=j+1;
			if(count==1):
                            temp_l=sorted(num_array)
                            if(swap(i,num_array.index(temp_l[i]))):
                                break
                            else:
                                flag=0
                                break
			elif(count>1):
                                num_array[pos:pos+count+1]=num_array[pos+count:pos-1:-1] 
				if(check()):
					print "yes";
					print("reverse %s %s" % (pos+1,pos+count+1));
					break;
				else:
					flag=0;
					break;                    

		i=i+1;
	if(flag==0):
		print "no";
