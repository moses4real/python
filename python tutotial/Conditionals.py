"""
age = input("Enter your age:")
new_age = float (age) + 50
print(new_age)

def age_foo(age):
    new_age = float(age) + 50
    return new_age

age = input("Enter your age:")
print(age_foo(age))

a = 5

if a < 5:
    print("less than 5")
elif a == 5:
    print("equal to 5")
else:
    print("equal or greater than 5")


def age_foo(age):
    new_age = age + 50
    return new_age

age = float(input("Enter your age:"))

if age < 150:
    print(age_foo(age))
else:
    print("How is that possible?")
"""