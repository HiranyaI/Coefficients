import math

#--- Create variables ---
coefficient_1=0 #--->coefficient of x^2
coefficient_2=0 #--->coefficient of x
constant=0 #--->constant value
root_1=0
root_2=0
discriminant=0 

#--- Get coefficient value for x^2 ---
coefficient_1=float(input("Enter the coefficient of x\u00b2:"))

print("\n")

#--- Get coefficient value for x ---
coefficient_2=float(input("Enter the coefficient of x:"))

print("\n")

#--- Get constant value ---
constant=float(input("Enter the constant value of the expression:"))

print("\n")

#--- Calculation for discriminant ---
discriminant=((coefficient_2**2)-(4*coefficient_1*constant))

#---If discriminant value is positive---
if discriminant>0:
    print("The discriminant is greater than zero -> There are two real distinct roots.")
    root_1=((-coefficient_2) - math.sqrt(discriminant)) / (2 * coefficient_1)
    root_2=((-coefficient_2) + math.sqrt(discriminant)) / (2 * coefficient_1)

    print("\n")
    
    if coefficient_2 > 0 and constant >= 0:
        print("The roots of (",(coefficient_1),"x\u00b2 +",(coefficient_2),"X +",(constant),") are",(root_1),"and",(root_2))
    elif coefficient_2 >= 0 and constant < 0:
        print("The roots of (",(coefficient_1),"x\u00b2 +",(coefficient_2),"X",(constant),") are",(root_1),"and",(root_2))
    elif coefficient_2 < 0 and constant >= 0:
        print("The roots of (",(coefficient_1),"x\u00b2",(coefficient_2),"X +",(constant),") are",(root_1),"and",(root_2))
    elif coefficient_2 <= 0 and constant < 0:
        print("The roots of (",(coefficient_1),"x\u00b2",(coefficient_2),"X",(constant),") are",(root_1),"and",(root_2),)

#--- If discriminant value is 0 ---
elif discriminant==0:
    print("The discriminant is zero -> There are two real identical roots.")
    root_1=((-coefficient_2) - math.sqrt(discriminant)) / (2 * coefficient_1)
    root_2=((-coefficient_2) + math.sqrt(discriminant)) / (2 * coefficient_1)

    print("\n")
    
    if coefficient_2 > 0 and constant >= 0:
        print("The roots of (",(coefficient_1),"x\u00b2 +",(coefficient_2),"X +",(constant) ,") are",(root_1),"and",(root_2))
    elif coefficient_2 >= 0 and constant < 0:
        print("The roots of (",(coefficient_1),"x\u00b2 +",(coefficient_2),"X",(constant) ,") are",(root_1),"and",(root_2))
    elif coefficient_2 < 0 and constant >= 0:
        print("The roots of (",(coefficient_1),"x\u00b2",(coefficient_2),"X +",(constant) ,") are",(root_1),"and",(root_2))
    elif coefficient_2 <= 0 and constant < 0:
        print("The roots of (",(coefficient_1),"x\u00b2",(coefficient_2),"X",(constant) ,") are",(root_1),"and",(root_2))

#--- If discriminant value is negetive ---
elif discriminant<0:
    print("The discriminant is less than zero -> There are no real roots.")
