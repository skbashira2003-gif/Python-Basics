#Create a list containing the squares of numbers from 1 to 10 using list comprehension.
squares = [i * i for i in range(1, 11)]
print(squares)

#Create a new list containing only even numbers using list comprehension.
numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)


#Create a list of numbers divisible by both 3 and 5
numbers = range(1, 101)

divisible = [i for i in numbers if i % 3 == 0 and i % 5 == 0]
print(divisible)

#Generators

# ============================================================
# GENERATORS - 4 TASKS
# ============================================================


# 1. Generate numbers from 1 to 10 using yield

def numbers():
    for i in range(1, 11):
        yield i


for x in numbers():
    print(x)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


print()


# 2. Generate even numbers from 1 to 20

def even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            yield i


for x in even_numbers():
    print(x)

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


print()


# 3. Generate squares of numbers from 1 to 5

def squares():
    for i in range(1, 6):
        yield i * i


for x in squares():
    print(x)

# Output:
# 1
# 4
# 9
# 16
# 25


print()


# 4. Generate numbers divisible by both 3 and 5
# from 1 to 100

def divisible_by_3_and_5():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            yield i


for x in divisible_by_3_and_5():
    print(x)

# Output:
# 15
# 30
# 45
# 60
# 75
# 90
# GENERATOR USING next()
# ============================================================

# 16. Using next() with generator

def my_generator():
    yield 10
    yield 20
    yield 30


gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))

# Output:
# 10
# 20
# 30