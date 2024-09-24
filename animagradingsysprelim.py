import sys

def gradingsystem():
    # Input for attendance
    try:
        attendance_input = input("Enter your number of absences (0 to 4): ")
        attendance = int(attendance_input)

        if attendance < 0 or attendance > 4:
            print("Invalid input! Please enter a number between 0 and 4.")
            sys.exit()

        # Calculate deduction based on absences
        num1 = {0: 1.0, 1: 0.90, 2: 0.80, 3: 0.70}.get(attendance)
        if attendance == 4:
            print("You have failed due to 4 absences.")
            sys.exit()

        print(f"You entered {attendance} absences.")

    except ValueError:
        print("The input you entered is not a valid number.")
        sys.exit()

    try:
        gradeprelim_input = input("Please enter your Prelim Exam grade (0 to 100): ")
        gradeprelim = float(gradeprelim_input)

        if gradeprelim < 0 or gradeprelim > 100:
            print("Please type a grade between 0 and 100 only.")
            sys.exit()

        quizgrade_input = input("Please enter your Quiz Grade (0 to 100): ")
        quizgrade = float(quizgrade_input)

        if quizgrade < 0 or quizgrade > 100:
            print("Please type a grade between 0 and 100 only.")
            sys.exit()

        reqgrade_input = input("Please enter your Requirements Grade (0 to 100): ")
        reqgrade = float(reqgrade_input)

        if reqgrade < 0 or reqgrade > 100:
            print("Please type a grade between 0 and 100 only.")
            sys.exit()

        recigrade_input = input("Please enter your Recitation Grade (0 to 100): ")
        recigrade = float(recigrade_input)

        if recigrade < 0 or recigrade > 100:
            print("Please type a grade between 0 and 100 only.")
            sys.exit()

        print(f"You entered {gradeprelim} in the Prelim Exam Grade.")
        print(f"You entered Quiz Grade: {quizgrade}")
        print(f"You entered Grade for Requirements: {reqgrade}")
        print(f"You entered Recitation Grade: {recigrade}")

        passing_grade = 75
        weight_prelim = 0.20
        weight_midterm = 0.30
        weight_final = 0.50

        # Calculate required prelim grade
        classtand=(quizgrade*0.40)+(reqgrade*0.30)+ (recigrade*0.30)
        print(f"the Class standing is {classtand}")

        prelimoverall = (gradeprelim*0.60)+(num1)+(classtand*0.30)
        print(f"Your Prelim Grade is : {prelimoverall}")

        prelim1 = passing_grade - gradeprelim * weight_prelim / (weight_midterm + weight_final)
        midfin = ((weight_midterm + gradeprelim) - prelim1) - weight_final

        print(f"Overall Grade: {prelim1+midfin}")
        overall_grade=(prelim1+midfin)
        # Calculate required grades for Midterm and Final
        if prelimoverall < 75:
            print("You failed")
            sys.exit()
        else:
            required_midterm = (overall_grade * 0.80) + (prelimoverall * weight_prelim)
            required_final = (overall_grade * weight_final) + (required_midterm* weight_midterm)+(prelimoverall * weight_prelim)
            print(f"Required Midterm Grade for Passing: {required_midterm:.2f}")
            print(f"Required Final Grade for Passing: {required_final:.2f}")

        # Check for Dean's Lister
        if overall_grade >= 90:
            print("You are a Dean’s Lister Scholar!")


    except ValueError:
        print("The grade you entered is not a valid number.")
        sys.exit()

# Run the grading system
gradingsystem()
