usage = input("Enter usage(domestic/commercial): ")
units = float(input("Enter electricity units: "))

if usage == "domestic":
    if (units >= 0) and (units <= 50):
        bill = 0
        print("Bill generated with ", usage ,"amount :", bill)
    
    elif (units > 50) and (units <= 100):
        bill = units * 5
        print("Bill generated with ", usage ,"amount :", bill)
    
    elif (units > 100) and (units <= 200):
        bill = units * 10
        print("Bill generated with ", usage ,"amount :", bill)
    
    
    elif (units > 200) and (units <= 500):
        bill = units * 15
        print("Bill generated with ", usage ,"amount :", bill)
    
    else:
        bill = units * 25
        print("Bill generated with ", usage ,"amount :", bill)
        
elif usage == "commercial":
    if (units >= 0) and (units <= 200):
        charge_per_unit = 25
        bill = units * charge_per_unit
        print("units: ", units)
        print("Usage: ", usage)
        print(units, "*", charge_per_unit)
        print("Amount", bill)
    elif (units >= 201) and (units <= 500):
        bill = units * 30
        print("Bill generated with", usage, "amount:", bill)
    else:
        bill = units * 40
        print("Bill generated with", usage, "amount:", bill)