marks = float(input("Enter your Marks(0-100): "))
if marks >= 90:
    grade = "A+"
    message = "Outstanding work! You’ve truly excelled!"
elif marks >= 80:
    grade = "A"
    message = "Excellent job! Keep up the great effort!"
elif marks >= 70:
    grade = "B"
    message = "Good work! You’re doing really well!"
elif marks >= 60:
    grade = "C"
    message = "Nice effort! Keep practicing and you’ll improve even more!"
elif marks >= 50:
    grade = "D"
    message = "You passed! A bit more focus and you’ll do even better!"
else:
    grade = "F"
    message = "Don’t be discouraged—learn from this and come back stronger!"

print("Your grade is "+grade)
print(message)