from random import random


my_list =[]
my_list =list()
print(type(my_list))


#index 0,1,2,3,4
numbers=[2,6,10,12.5,0]#this is also a comment
print(numbers)
print(type(numbers))
print(type(numbers[1]))
print(3)
print(numbers[3])
print(type(numbers[3]))

#index    0,      1,      2        3
foods=["pizza","tacos","dimsum","sushi"]
print(foods[1])
print(type(foods[1]))
print(foods[1].upper())

x=12
y=15.5
z="Z"

random_list=[x,y,z]
print(random_list[0])
print(type(random_list[0]))

print(random_list[1])
print(type(random_list[1]))

print(random_list[2])
print(type(random_list[2]))

my_fav_num=random_list[0]
print(my_fav_num)

#index    0,      1,      2        3
foods=["pizza","tacos","dimsum","sushi"]

(foods.append("cheeseburger"))
print(foods)


#index    0,      1,      2        3
foods=["pizza","tacos","dimsum","sushi"]

foods.insert(0,"pho")
print(foods)


foods.remove("pho")
print(foods)

foods.append("pizza")
print(foods)
foods.remove("pizza")
print(foods)

del foods[1]
print(foods)

#index    0,      1,      2        3
foods=["pizza","tacos","dimsum","sushi"]
print(foods.pop())
print(foods)

# method of the list class called .sort
# built-in function called sorted()



# .sort ()IN PLACE

#index    0,      1,      2        3
foods=["pizza","tacos","dimsum","sushi"]
print(foods.sort())
print(foods)
print(foods.sort(reverse=True))
print(foods)

# sorted is out of PLACE

#index    0,      1,      2        3
foods=["pizza","tacos","dimsum","sushi"]
print(sorted(foods))
print(foods)

foods=sorted(foods, reverse=True)
print(foods)

#index    0,      1,      2        3
foods=["pizza","tacos","dimsum","sushi"]
foods.reverse()
print(foods)

deck=["pikachu","mew", "mewtwo","charized"]
deck=deck.pop()
print (deck)

