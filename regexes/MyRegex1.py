import re

filename = "ass.csv"
fout = open("output.csv", "w")


with open(filename,'r') as f:
    next(f)
    for x in f:
        x = x.rstrip()
        if re.match('<Object:<Path:/Databases/EGAPostBox/Rented/P[A-Z]+[0-9]+>', x ):
            fout.write(x+'\n')
        if not x:
           continue

# always close your files otherwise nothing closes and you end up with nothing
f.close()
fout.close()
