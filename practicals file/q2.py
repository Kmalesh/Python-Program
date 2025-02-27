import math

# Input a number from the user
num = float(input("Enter a number: "))

# Square root
print(f"Square root of {num}: {math.sqrt(num)}")

# Ceiling value
print(f"Ceiling of {num}: {math.ceil(num)}")

# Floor value
print(f"Floor of {num}: {math.floor(num)}")

# Factorial (only for integers)
if num.is_integer():
    print(f"Factorial of {int(num)}: {math.factorial(int(num))}")
else:
    print("Factorial is only defined for integers.")

# Power (num^3)
print(f"{num} raised to the power of 3: {math.pow(num, 3)}")

# Logarithm (base 10)
if num > 0:
    print(f"Logarithm (base 10) of {num}: {math.log10(num)}")
else:
    print("Logarithm is not defined for non-positive numbers.")

# Trigonometric functions (sine, cosine, tangent)
angle = float(input("Enter an angle in degrees: "))
angle_rad = math.radians(angle)  # Convert degrees to radians
print(f"Sine of {angle}°: {math.sin(angle_rad)}")
print(f"Cosine of {angle}°: {math.cos(angle_rad)}")
print(f"Tangent of {angle}°: {math.tan(angle_rad)}")

# Constants
print(f"Value of pi: {math.pi}")
print(f"Value of e: {math.e}")