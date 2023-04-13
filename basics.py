import random

# c = random.randint(1,10);
# cFloat = random.random() #prints float between 0 and 1 ,but not 1
# print(c)

# # Lists
# list1 = ["a","b",1,0.3,True] # can hold any type of value


#Loops
# fruits = ["Apple","Orange","Banana"]

# for item in fruits:
#     print(item)

# Average height
# student_heights = [180, 124, 165, 173, 189, 169, 146]

# total = 0
# count = 0
# max = 0
# for item in student_heights:
#     if item > max:
#         max = item
#     count += 1
#     total += item

# print(round(total/count))

################################## for loop Range ###############################

# for number in range(1,5): # 1 to 4
#     print(number)

# for number in range(1,11,2): # 1 to 10, every two interval
#     print(number)

# for number in range(2,101,2): # 1 to 10, every two interval
#     print(number)

for number in range(1,101):
    if(number % 3 and number % 5):
        print("FizzBuzz")
    elif (number % 3):
        print("Fizz")
    elif(number % 5):
        print("Buzz")







    