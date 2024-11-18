#Justin King
#11/10/2024
#P4HW1
#grades list and calculator

valid_scores = []
# Enter number of scores
num_scores = int(input("How many scores do you want to enter? "))
# Enter the scores
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{len(valid_scores) + 1}: "))
        if 0 <= score <= 100:
            valid_scores.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")

print("\n------------- Results -------------")
# Show lowest score
lowest_score = min(valid_scores)
print(f"Lowest Score : {lowest_score}")
# List without the lowest score
modified_scores = [score for score in valid_scores if score != lowest_score]
print(f"Modified List : {modified_scores}")
# Average of the new list
average_score = sum(modified_scores) / len(modified_scores)
print(f"Scores Average: {average_score:.2f}")
# Letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print(f"Grade : {letter_grade}")
