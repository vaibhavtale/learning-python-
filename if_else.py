is_hot = False
is_cold = False

if is_hot:
    print("it is a good kind of day")
    print("drink plenty of water")
elif is_cold:
    print("it ios cold day")
    print("wear warm clothes")
else:
    print("Enjoy your Day")

# Exercise

good_credit = True
price = 1000000

if good_credit :
    price /= 10
else:
    price /= 5

print(price)

# exrcise 2

name = input("Enter your Name : ")

if len(name) < 3 :
    print("Name must be atleast 3 characters.")
elif len(name) > 50 :
    print("Name can be maximum of 50 characters.")
else :
    print("Here we go..")

# Exercise 3

weight = int(input("Enter your weight : "))
unit = input("Lbs or Kg : ")

if unit.upper() == "Kg":
    converted = weight / 0.45
    print(f"Your weight is {converted} Lbs..")

else:
    converted = weight * 0.45
    print(f"Your weight is {converted} Kg..")
