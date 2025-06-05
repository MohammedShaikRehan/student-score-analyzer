def process_stud():
    students = {}
    n = int(input("Enter the Number of students: "))

    for i in range(n):
        name= input("Name: ")
        score= int(input("Score: "))
        students[name]=score

    average = sum(students.values()) / len(students)

    print(f'\nThe average is: {average:.2f}')
    print("\nThe above average: ")
    for name, score in students.items():
        if score > average:
            print(name)
    
    print("\nGrades:")
    for name, score in students.items():
        if score >= 90:
            grade = "A+ (Rockstar)"
        elif score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        else:
            grade = "F (Needs Improvement)"
        print(f"{name}: {score} = {grade}")

process_stud()