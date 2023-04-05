def convert_score(grade):
    if grade == "A+":
        gpa = 4.5
    elif grade == "A":
        gpa = 4
    elif grade == "B+":
        gpa = 3.5
    elif grade == "B":
        gpa = 3
    elif grade == "C+":
        gpa = 2.5
    elif grade == "C":
        gpa = 2
    elif grade == "D+":
        gpa = 1.5
    elif grade == "D":
        gpa = 1
    elif grade == "F":
        gpa = 0

    return gpa


archive_credit, submit_credit = 0, 0
archive_gpa, submit_gpa = 0, 0


while True:
    print("작업을 선택하세요.\n")
    print("1. 입력\n")
    print("2. 계산\n")
    user_value = input()
    value = int(user_value)
    if value == 1:
        user_value = input("학점을 입력하세요: ")
        credit = int(user_value)
        user_value = input("평점을 입력하세요: ")
        gpa = convert_score(user_value)
        if gpa > 0:
            submit_credit += credit
            submit_gpa += credit * gpa
        archive_credit += credit
        archive_gpa += credit * gpa
    else:
        submit_gpa /= submit_credit
        archive_gpa /= archive_credit

        print("제출용: " + str(submit_credit)+ "학점 (GPA: " + str(submit_gpa) + ")")
        print("열람용: " + str(archive_credit)+ "학점 (GPA: " + str(archive_gpa) + ")")
        break