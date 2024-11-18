#Justin King
#10/13/2024
#P2HW2
#stores grades and creates a list and calculates different statistics

#create list to put grades in
module_grades = []

#input grades
for i in range(1,7):
    grade=float(input(f"Enter grade for module {i}: "))
    module_grades.append(grade)

#calculate statistics
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

#display results
print("\n----------Results----------")
print(f"Lowest Grade: {lowest_grade:.1f}")
print(f"Highest Grade: {highest_grade:.1f}")
print(f"Sum of Grades: {sum_of_grades:.1f}")
print(f"Average: {average_grade:.2f}")
print("----------------------------")
