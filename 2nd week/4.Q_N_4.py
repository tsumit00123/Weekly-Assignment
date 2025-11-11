#A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
#frst count the sweets and then divide them according to how many pupils attend
#that day. Write a program that will tell the teacher how many sweets to give to each
#pupil, and how many she will have left over.

print("----Sweet distribution between students-----")

no_of_sweet=int(input("Enter total count of sweet: "))
no_of_student_attend=int(input("Enter the number of student attend: "))


sweets_given_to_each_student=no_of_sweet//no_of_student_attend
leftover_sweet=no_of_sweet%no_of_student_attend

print(f"Total number of sweet given to each student: {sweets_given_to_each_student}")
print(f"Total number of leftover sweet: {leftover_sweet}")