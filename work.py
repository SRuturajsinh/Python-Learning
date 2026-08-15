list = []
i = 0
while True:
    num = (input("enter number in list: "))
    if num == str("exit"):
        break
    i += 1
    list.append(int(num))
print(list)

target = int(input("enter target: "))

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] + list[j] == target:
            print(f"[{i},{j}] = {list[i]} + {list[j]} = {target}")