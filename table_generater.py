while True:
    print("Enter any number you want to convert\nInto a table")
    t = int(input(">> "))
    for i in range(1, 11):
        print(f"{t} x {i} = {t*i}")
    print("Done")
