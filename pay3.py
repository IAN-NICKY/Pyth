def computepay(h, r):
    if h <= 40:
        # Regular pay for 40 hours or less
        pay = h*r
    else:
        # Overtime pay: 40 hours at regular rate + extra hours at 1.5 times rate
        exh = h-40
        pay = (40*r) +(1.5*r*exh)
    return pay

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate per hour:")
r = float(rate)

p = computepay(h,r)
    
print("Pay", p)