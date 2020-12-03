ounces = float(input("Input your amount of fluid in ounces: "))
servings = float(input("Input the number of people you're serving: "))
actual_amount = ounces / 4
mili = actual_amount * servings * 29.5735
print("You will need " + str(mili) + " ml")