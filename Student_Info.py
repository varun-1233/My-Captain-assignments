import csv


def write_to_csv(student_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_Number", "Email_ID"])

        writer.writerow(student_list)

if __name__ == '__main__':
    condition = True
    student_num=1
    while condition == True:

        student = input("Enter student info for student #{} in the following format (Name Age Contact_Number Email_ID) ".format(student_num))

        info_list = student.split(' ')

        print("\nEntered information is-\n Name: {}\n Age: {}\n Contact_Number: {}\n Email_ID: {}".format(info_list[0], info_list[1], info_list[2], info_list[3]))

        checker=input("Is the entered information correct? (yes/no) ")
        if checker == "yes":
            write_to_csv(info_list)

            check = input("Enter yes/no to enter more student details ")
            if check == "yes":
                condition = True
                student_num=student_num+1
            elif check == "no":
                condition = False
        elif checker == "no":
            print("\nPlease re-eneter the values!")