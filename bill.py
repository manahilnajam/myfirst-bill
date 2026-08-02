print("Please input the prices of the 3 products you obtained:")
product1 = float(input("First Product: "))
product2 = float(input("Second Product: "))
product3 = float(input("Third Product: "))
print("Your total bill is: ", product1 + product2 + product3)
avg = (product1 + product2 + product3) /3
print("Your average bill is: ", avg)
name = input("please enter your name: ")
print("The bill is in the name of: ", name)
print("Is there x in the name?", name.find('x')) # gives only the index position if not exists then the output is nonexistant position
print("Is there m in the name?", name.find('m')) # gives only the index position
print("Is there M in the name?", name.find('M')) # gives only the index position
print("Is there m in the name?",'m' in name)     # TRUE OR FALSE OUTPUT
print("Is there M in the name?", 'M' in name)    # TRUE OR FALSE OUTPUT

