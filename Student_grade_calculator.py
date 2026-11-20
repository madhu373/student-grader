def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def main():

    print("================================")
    print(" STUDENT PERFORMANCE CALCULATOR")
    print("================================")

    name = input("Enter Student Name: ")

    subjects = ["Python", "Mathematics", "English", "Science", "Computer Science"]

    marks = []

    for subject in subjects:
        while True:
            mark = float(input("Enter marks for " + subject + ": "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")

    total = calculate_total(marks)

    average = calculate_average(marks)

    percentage = total / len(subjects)

    highest = max(marks)

    lowest = min(marks)

    grade = calculate_grade(percentage)

    print("\n================================")
    print("       STUDENT REPORT")
    print("================================")

    print("Student Name:", name)

    for i in range(len(subjects)):
        print(subjects[i], ":", marks[i])

    print("--------------------------------")
    print("Total Marks:", total, "/ 500")
    print("Average:", round(average, 2))
    print("Percentage:", round(percentage, 2), "%")
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Grade:", grade)

    if min(marks) >= 35:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("================================")


main()
