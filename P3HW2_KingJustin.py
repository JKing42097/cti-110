# Justin King
# 10/27/2024
# P3HW2
# payroll calculator

#employee info
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#overtime 
if hours > 40:
 overtime_hours = hours - 40
 regular_hours = 40
else:
 overtime_hours = 0
 regular_hours = hours

#pay
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

#results
print("-" * 40)
print(f"Employee name: {name}")
print("-" * 40)
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<12}")
print("-" * 80)
print(f"{hours:<15.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<15.2f}{regular_pay:<15.2f}${gross_pay:<11.2f}")
