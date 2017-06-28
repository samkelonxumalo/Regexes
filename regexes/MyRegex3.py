import re

filename = "output2.csv"

fout = open("output3.csv",  "w")

regex = re.compile(r"<Object:<Path:/Databases/EGAPostBox/Rented/(P[A-Z]+[0-9]+)(.*)Name:([A-Za-z ]+),HolderType:([A-Za-z]+),ApplicationId:([A-Za-z ]+),StartDate:(\d\d\-\d\d\-\d\d),PaidUntil:(\d\d\-\d\d\-\d\d),LastPaidUntil:(\d\d\-\d\d\-\d\d)")


with open(filename,"r") as f:
    for x in f:
        x = x.strip()
        #if re.match(regex,x):
            #x = regex.sub("",x)
            #fout.write(x + "\r\n")
        now = regex.search(x)
        fout.write(now.group(8))
        #if not x:
            #continue
#always close files
f.close()
fout.close()
