def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

def add_student(students):
    while True:
        name = input("Student name: ").strip()
        if name:
            break
        print("Name cannot be blank. Please try again.")

    while True:
        mark_text = input("Mark (0-100): ").strip()

        try:
            mark = int(mark_text)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if 0 <= mark <= 100:
            break

        print("Mark must be between 0 and 100.")

    # A list keeps duplicate names as separate student records.
    students.append({"name": name, "mark": mark})
    print(f"Added {name}.\n")

def show_results(students):
    if not students:
        print("No students have been added yet.\n")
        return

    print("\nStudent Results")
    print("-" * 42)
    print(f"{'Name':<25}{'Mark':>8}{'Grade':>9}")
    print("-" * 42)

    for student in students:
        mark = student["mark"]
        print(f"{student['name']:<25}{mark:>8}{get_grade(mark):>9}")

    marks = [student["mark"] for student in students]
    average = sum(marks) / len(marks)

    print("-" * 42)
    print(f"Average: {average:.1f}")
    print(f"Highest: {max(marks)}")
    print(f"Lowest:  {min(marks)}\n")

def main():
    students = []

    while True:
        print("Student Grade Manager")
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_results(students)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.\n")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram ended.")