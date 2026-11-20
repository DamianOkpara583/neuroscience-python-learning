 # input type

# stri, float, int, bool

# everry data type has its form of methond

name = input("What is your name? ")
print(f"Hello, {name}!")

# method
name.upper()

#fxn
# print ()

print (f"Hello, {name.upper()}!")

print (f"Hello, {name.lower()}!")

lastname = input("What is your last name? ")
firstname = input("What is your first name? ")
print(f"Hello, {firstname.title} {lastname.lower}!")



firstvalue = int(input("Enter first number: "))
secondvalue = int(input("Enter second number: "))

result = firstvalue / secondvalue


print(f"The result of dividing {firstvalue} by {secondvalue} is {result}.")

# conparism operators

# ==equal to
# != not equal to
# > greater than
# < less than

year_of_birth = int(input("What year were you born? "))
this_year = int(input("What year is it now? "))

print (this_year > year_of_birth)
result = this_year - year_of_birth
print (f"You are {result} years old.")

