import re
f=open("phone.txt","r")
fp=open("copy.txt","w")
match=re.findall("[+91|91|0]?[9876]{1}\d{9}",f.read())
for m in match:
    fp.write(m+"\n")
fp.close()