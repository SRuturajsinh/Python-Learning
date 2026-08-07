
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

i=1
while i<6:
    j=1
    while j<i+1:
        print(j,end="")
        j+=1
    print()
    i+=1
# Output:
# 1
# 12
# 123
# 1234
# 12345

#---------------------------------------------------------

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()

i=5
while i>0:
    j=5
    while j>i-1:
        print(j,end="")
        j-=1
    print()
    i-=1

# Output
# 5
# 54
# 543
# 5432
# 54321
#--------------------------------------------------------
for i in range(6,0,-1):
    for j in range(1,i):
        print(j,end="")
    print()

i=6
while i>0:
    j=1
    while j<i:
        print(j,end="")
        j+=1
    print()
    i-=1

# Output
# 12345
# 1234
# 123
# 12
# 1
#--------------------------------------------------------

for i in range (0,6):
    for j in range(5,i,-1):
        print(j,end="")
    print()

i=0
while i<6:
    j=5
    while j>i:
        print(j,end="")
        j-=1
    print()
    i+=1

# Output
# 54321
# 5432
# 543
# 54
# 5
#--------------------------------------------------------

for i in range(1,6):
    for j in range(0,i):
        print(i,end="")
    print()

i=1
while i<6:
    j=0
    while j<i:
        print(i,end="")
        j+=1
    print()
    i+=1

# Output
# 1
# 22
# 333
# 4444
# 55555