student_info = []
total_students = int(input("How many students are in the class? "))

response = 0
while response != total_students:
    new_student = {}
    name = input("Enter student's name: ")
    grade = float(input("Enter student's grade: "))
    new_student["Name"] = name
    new_student["Grade"] = grade
    student_info.append(new_student)
    response += 1
    
    show = input("Do you want to show uploaded student info? (yes/no): ")
    if show.lower() == "yes":
        for info in student_info:
            print(info)
    
    option = input("Would you like to add more students? (yes/no): ")
    if option.lower() == "no":
        print("Student information has been uploaded to the portal.")
        break
