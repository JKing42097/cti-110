#Justin King
#11/10/2024
#P4HW2
#payroll calculator program

#variables
total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Loop for multiple employees
while True:
    #employee name or "Done" to terminate
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")
    if employee_name.lower() == "done":
        break
    
    #hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    # Calculate regular hours, overtime hours, regular pay, and overtime pay
    regular_hours = min(40, hours_worked)
    regular_pay = regular_hours * pay_rate
    
    overtime_hours = max(0, hours_worked - 40)
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    
    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay
    
    #employee payroll information
    print("\nEmployee name:", employee_name)
    print(f"{'Hours':9}{'Pay Rate':10}{'OverTime':10}{'OverTime Pay':10}{'Reg Pay':10}{'Gross Pay':10}")
    print(f"{hours_worked:9.1f}{pay_rate:10.2f}{overtime_hours:10.2f}{overtime_pay:10.2f}${regular_pay:10.2f}${gross_pay:10.2f}")
    
    #totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

#final totals
print("\nTotal number of employees entered:", total_employees)
print(f"Total amount paid for overtime:    ${total_overtime_pay:10.2f}")
print(f"Total amount paid for regular hours:${total_regular_pay:10.2f}")
print(f"Total amount paid in gross:        ${total_gross_pay:10.2f}")
