ninput= int(raw_input());
num_array=raw_input().split();
count=0;
pos=0;
i=0;
flag=1;

def check():
	if(all(int(num_array[i]) <= int(num_array[i+1]) for i in xrange(len(num_array)-1))):
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
				temp=num_array[pos];
				num_array[pos]=num_array[pos+1];
				num_array[pos+1]=temp;
				if(check()):
					print "yes";
					print ("swap %s %s" % (pos+1,pos+2));
				else:
					flag=0;
				break;
				
			elif(count>1):
				num_array[pos:pos+count]=num_array[-(len(num_array)-pos+count):-(len(num_array)-pos)];
				if(check()):
					print "yes";
					print("reverse %s %s" % (pos+1,pos+count+1));
				else:
					flag=0;
				break;
			
		i=i+1;
	if(flag==0):
		print "no";

