weekday =["Sunday", "Monday","Tusday","Wednesday","Thrusday","Friday","Saturday"]
print(weekday[0])
print(weekday[0:3])
print(weekday[-1])
weekday[0] ='DUNDAY'
print(weekday[0])

Numbers = [1,2,3,4,5]
print(Numbers)
#Numbers.append(7)  # adding 7 at the end
#Numbers.insert(0,-1)  # adding -1 in the begining
#Numbers.remove(3)  # remove -3 value from list
#Numbers.clear()  # clear all values form list
print(Numbers)
print(1 in Numbers) # check wether 1 is esit or not in list if exist then true else false will be return
print(len(Numbers)) # find out how many elments in the list
for item in weekday:
    print(item)
for itm in Numbers:
    print(itm)
print("For loop")
i = 0
while i < len(Numbers):
    print(Numbers[i])
    # i += 1
    i = i+1
print("Range")
num1 =range(5) # start 0  and end 4
print(num1)
for j in num1:
    print(j)

num2 =range(5,10) # start 5  and end 10
print(num2)
for k in num2:
    print(k)

num3 =range(5,10,2) # start 5  and end 10 but skip or jump 2 digit
num3 =range(5,10,1) # start 5  and end 10 but skip or jump 1 digit
print(num3)
for l in num3:
    print(l)