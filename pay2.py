hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate per hour:")
r = float(rate)


if h <= 40:
    pay = h*r
else:
    exh = h-40
    pay = (40*r)+(exh*1.5*r) 
print(pay)