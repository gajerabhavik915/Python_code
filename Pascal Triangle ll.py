
list = [1]

index = 1


for i in range(index): #0
    new_list = []
    list1 = [0] + list + [0]          #[0,1,1,0]
    for j in range(len(list1)-1):     #0
        new_list.append(list1[j]+list1[j+1])
    list = new_list

print(list)
