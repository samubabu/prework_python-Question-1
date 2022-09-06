foods=["pizza","tacos","dimsum", "sushi"]

print(foods[1])

#for placeholder in THE LIST WE WANT OT LOOK AT:
    #THIS IS A CODE BLOCK
    #WILL RUN ON EVERY ITEM IN THE LIST FOOD
for food in foods:

    if food=="dimsum":
        continue
    print(f"I like {food} beacause they are yummy")

for index in range(len(foods)):
    print(index)
    print(foods[index])


print(list(enumerate(foods)))

for index, food in enumerate(foods):
    print(f"My No {index+1} food is {food.title()}")

my_tup=1,2
print(type(my_tup))

print(my_tup[1])
for num in my_tup:
    print(num)

my_tup=my_tup+(3,4)
print(my_tup)

#slicing
my_string="Hey Guy let's learn Python"
my_list=("pizza", "taco","dimsum", "sushi")

print(my_string[::-1])

my_list=["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macroni"]

for index in range(len(my_list)):
    if index==6:
        my_string+="chillin' with my homie"
    my_string[index="chicken wing"]
    print(my_string)


    x=5
y=10
i="5"
j="10"
if x==i and x !=y:
    print("Blackbird", end=" ")
else:
    print("singing", end=" ")

print("in the", end=" ")
    print("dead", end=" ")
else:
    print("of night", end=" ")