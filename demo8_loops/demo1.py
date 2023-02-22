#print 1 to 10
for a in range(1,10):
    print(a)
colors = ["red", "green", "yellow", "blue", "green"]
print(len(colors))
for i in range(0,5):  ###number of elements in list
    print(colors[i])
###OR####
for i in range(0, len(colors)):
    print(colors[i])

numbers=[45,98,75,65,24,88,74,56,75]
#PRINT ALL ITEM THAT ARE LESS THAN OR EQUAL TO 50
for i in numbers:
    if i <= 50:
        print(i)

####OR###
for i in range(0, len(numbers)):
    if numbers[i]<=50:
     print(numbers[i])
    if numbers[i]==24:
     continue
    print(numbers[i])

     break