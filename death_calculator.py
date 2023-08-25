age = int(input("Enter your age: "))
mon = int(input("Enter your month: "))
yea = int(input("Enter your year: "))
dat = int(input("Enter your date: "))
agen = int(input("Enter your now age: "))
monn = int(input("Enter your now month: "))
yean = int(input("Enter your now year: "))
datn = int(input("Enter your now date: "))
def see(age, month, year, date):
    return age * date // month + year
print("your death date is:", see(age=age, month=mon, year=yea, date=dat))
