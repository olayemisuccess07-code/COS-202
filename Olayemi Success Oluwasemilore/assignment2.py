print("   PERSONAL POCKET CGPA CALCULATOR (PPC)   ")
num_courses = int(input("Enter the number of courses taken: "))

total_credit_units = 0
total_quality_points = 0

print("\n--- Enter Course Details ---")
for i in range(1, num_courses + 1):
    print(f"\nCourse {i}:")
    credit_units = int(input("  Enter Credit Units: "))
    score = float(input("  Enter Score Obtained (0 - 100): "))
   
    if score < 0 or score > 100:
        print("  Error: Score must be between 0 and 100. Skipping course.")
        continue


    if score >= 70:
        grade_point = 5.0
        grade = 'A'
    elif score >= 60:
        grade_point = 4.0
        grade = 'B'
    elif score >= 50:
        grade_point = 3.0
        grade = 'C'
    elif score >= 45:
        grade_point = 2.0
        grade = 'D'
    elif score >= 40:
        grade_point = 1.0
        grade = 'E'
    else:
        grade_point = 0.0
        grade = 'F'

    quality_point = credit_units * grade_point
    total_credit_units += credit_units
    total_quality_points += quality_point
   
    print(f"  Grade Earned: {grade} | Quality Points: {quality_point}")


print("               FINAL SUMMARY                 ")

print(f"Total Credit Units Registered: {total_credit_units}")
print(f"Total Quality Points Achieved: {total_quality_points}")

if total_credit_units > 0:
    cgpa = total_quality_points / total_credit_units
    print(f"Your Calculated CGPA is   : {cgpa:.2f}")
   
    if cgpa >= 4.50:
        print("Class: First Class Honours! 🌟")
    elif cgpa >= 3.50:
        print("Class: Second Class Honours (Upper Division)")
    elif cgpa >= 2.40:
        print("Class: Second Class Honours (Lower Division)")
    elif cgpa >= 1.50:
        print("Class: Third Class")
    else:
        print("Class: Pass/Fail status.")
else:
    print("CGPA cannot be computed (0 Credit Units recorded).")
print("=" * 45)