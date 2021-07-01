#CALCULATOR TO PERFORM ALL ARITHMETIC OPERATIONS

'''USER INPUT'''
print("Welcome To Python Calculator")
a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))

'''ADDITION'''
s = a+b
print( f"The sum of {a} and {b} is {s}")

'''SUBTRACTION'''
m = a-b
print( f"The difference of {a} and {b} is {m}")

'''MULTIPLICATION'''
p = a*b
print( f"The product of {a} and {b} is {p}")

'''DIVISION'''
q = a/b
print( f"The quotient of {a} and {b} is {q}")

'''MODULUS'''
r = a%b
print( f"The remainder of {a} and {b} is {r}")

'''EXPONENT'''
e = a**b
print( f"{a} to the power of {b} is {e}")
