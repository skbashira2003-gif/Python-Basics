
# 1. WITHOUT EXCEPTION HANDLING

print('1')
print('2')

# This terminates the program because 4 / 0 causes an error
# a = 4 / 0

print('3')
print('4')

# 2. TRY AND EXCEPT

print('1')
print('2')

try:
    a = 4 / 0

except ZeroDivisionError:
    print("message: Zero Division Error has occurred")

print('3')
print('4')

# 3. SYNTAX ERRORS - EXAMPLES


print('Examples of syntax errors')

# These are examples only. They are commented because
# syntax errors cannot be handled by try-except in the same code.

# a = (1, 2, 3))       # unmatched parenthesis
# s = "rakesh""        # unmatched quotes
# 5 = x                # invalid assignment
# l = [1 2 3]          # missing comma
# if = 21              # using keyword as variable
#     b = 20           # incorrect indentation
# if 10                # missing colon
#     print(True)


# 4. RUNTIME ERRORS - MULTIPLE EXCEPT


print('A')

try:
    import abcdef

except IndexError:
    print(1)

except KeyError as ke:
    print(3, ke)

except (ValueError, TypeError):
    print(4)

except ZeroDivisionError:
    print(5)

except ModuleNotFoundError:
    print(6)

except Exception as e:
    print(7, e)

print('B')
print('C')


# 5. ELSE AND FINALLY - NO ERROR


print('A')

try:
    a = 10 / 4

except IndexError:
    print(1)

except ZeroDivisionError:
    print(2)

else:
    print(3)

finally:
    print(4)

print('B')
print('C')

# 6. ELSE AND FINALLY - ERROR


print("A")

try:
    a = 10 / 0

except IndexError:
    print(1)

except ZeroDivisionError:
    print(2)

else:
    print(3)

finally:
    print(4)

print('B')
print('C')


# 7. FINALLY WITHOUT MATCHING EXCEPT


print('A')

try:
    a = 10 / 0

except IndexError:
    print(1)

except ModuleNotFoundError:
    print(2)

finally:
    print(3)

# NOTE:
# ZeroDivisionError is not handled here.
# Therefore program terminates after finally.

# 8. MULTIPLE EXCEPT + ONE ELSE + ONE FINALLY


print('A')

try:
    a = 10 / 0

except IndexError:
    print(1)

except ModuleNotFoundError:
    print(2)

except ZeroDivisionError:
    print(3)

else:
    print(4)

finally:
    print(5)

print('B')
print('C')


# 9. CHILD ERROR BEFORE PARENT ERROR


print('A')

try:
    a = 10 / 0

except IndexError:
    print(1)

except ModuleNotFoundError:
    print(2)

except ZeroDivisionError:
    print(3)

finally:
    print(4)

print('B')
print('C')


# 11. USER-DEFINED EXCEPTION - SIMPLE


class StudentAlreadyExists(Exception):
    pass


try:
    raise StudentAlreadyExists(
        'Student with rollno 23 already exists'
    )

except StudentAlreadyExists as e:
    print(e)



# 12. PARAMETERIZED USER-DEFINED EXCEPTION

class StudentNotFound(Exception):

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

        super().__init__(
            f'Student rollno: {rollno} with name {name} is not found'
        )


try:
    raise StudentNotFound(1, 'rakesh')

except StudentNotFound as snf:
    print(snf)
    print(snf.rollno)
    print(snf.name)
    
