str=('google.com')
print ('your sample string is:',str)
count={}
for i in str:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1
print(count)