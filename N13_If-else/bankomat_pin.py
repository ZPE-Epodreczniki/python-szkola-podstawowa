podany_pin = input("Proszę podać PIN: ")

if podany_pin == "1234":
    print("Możesz  wypłacić maksymalnie  100 zł.")
elif podany_pin == "2345":
    print("Możesz  wypłacić maksymalnie 300 zł.")
elif podany_pin == "3374":
    print("Możesz  wypłacić maksymalnie 500 zł.")
elif podany_pin == "1034":
    print("Możesz  wypłacić maksymalnie 700 zł.")
else:
    print("Błędny PIN.")
