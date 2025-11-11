#The Head of Computing at the University of Poppleton is tasked with dividing a
#group of students into lab groups. A lab group is usually 24 students, but this is
#sometimes varied to create groups of similar size. Write a program that prompts for
#the number of students and group size, and then displays how many groups will be
#needed and how many will be left over in a smaller group.
#How many students? 113
#Required group size? 22
#There will be 5 groups with 3 students left over.
#For bonus credit, see if you can fix the grammar in the output. So if there were 101
#students in groups of 20 the output would be:
#There will be 5 groups with 1 student left over.


print("-------------University of Poppleton-----------")
print()
print("------------Group Allocation-------------------")
print()

student=int(input("Enter the number of students: "))
group_size=int(input("Enter the size of group: "))

no_of_group=student//group_size
left_over_student=student%group_size

if(left_over_student<=1):
   print(f"There will be {no_of_group} groups with {left_over_student} student left over.")

else:
    print(f"There will be {no_of_group} groups with {left_over_student} students left over.")

