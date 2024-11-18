#Justin King
#10/6/2024
#P2LAB1
#a circle calculating tool

import math

radius = float(input("What is the radius of the circle? "))
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius**2

print(f"the diameter of the circle is {diameter:.1f}")
print(f"the circumference of the circle is {circumference:.2f}")
print(f"the area of the circle is: {area:.3f}")
