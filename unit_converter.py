while True:
    n = int(input("Enter the number: "))
    units = ["m", "cm", "l", "ml", "km", "kg", "g"]
    unit = input("Enter the unit: ")
    con = input("Convert into: ")
    if(unit == units[0]):
        if(con == units[1]):
            print(f"{n}{unit} convert into {con} = {n * 100}{con}")
        elif (con == units[4]):
            print(f"{n}{unit} convert into {con} = {n / 1000} {con}")
    elif(unit == units[1]):
        if(con == units[0]):
            print(f"{n}{unit} convert into {con} = {n / 100} {con}")
    elif(unit == units[4]):
        if(con == units[0]):
            print(f"{n}{unit} convert into {con} = {n * 1000}{con}")
    elif(unit == units[2]):
        if(con == units[3]):
            print(f"{n}{unit} convert into {con} = {n / 1000} {con}")
    elif(unit == units[3]):
        if(con == units[2]):
            print(f"{n}{unit} convert into {con} = {n / 1000} {con}")
    elif (unit == units[-1]):
        if (con == units[-2]):
            print(f"{n}{unit} convert into {con} = {n / 1000} {con}")
    elif (unit == units[-2]):
        if (con == units[-1]):
            print(f"{n}{unit} convert into {con} = {n * 1000} {con}")
# pipee = "ApplePie"
# countries = ["India", "USA", "UK", "Germany", "Finland", "Micronesia", "Indonesia"]
# print(pipee[-7:-3])
# print(countries[-5:-2])
