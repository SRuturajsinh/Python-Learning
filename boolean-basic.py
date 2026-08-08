for i in range(5):
    for j in range(6,i+1,-1):
        print("_",end="")
    for k in range(1,i+2):
        print(k,end="")
    print()

i=1
while i<=5:
    j=5
    while j>=i:
        print("_",end="")
        j-=1
    k=1
    while k<=i:
        print(k,end="")
        k+=1
    print()
    i+=1
# Output
#_____1
#____12
#___123
#__1234
#_12345

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("_",end="")
    for k in range(5,i-1,-1):
        print(k,end="")
    print()

i=5
while i>0:
    j=i
    while j>0:
        print("_",end="")
        j-=1
    k=5
    while k>i-1:
        print(k,end="")
        k-=1
    print()
    i-=1
# Output
#_____5
#____54
#___543
#__5432
#_54321

for i in range(1,6):
    for j in range(i,0,-1):
        print("_",end="")
    for k in range(i,6):
        print(k,end="")
    print()

i=1
while i<6:
    j=i
    while j>0:
        print("_",end="")
        j-=1
    k=i
    while k<6:
        print(k,end="")
        k+=1
    print()
    i+=1

# Output
# _12345
# __2345
# ___345
# ____45
# _____5