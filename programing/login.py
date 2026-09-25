from sys import argv

script,user,password=argv

admin_userid="admin" #admin name
admin_pass=2222

student_user="student" #student name
student_pass=1212

if "admin_userid==admin_pass":
    print("welcome admin: ")
    print("how can i help you:")
    input("what do you want to manage today:")  
    print("admin portal:login succesful")
         
elif "student_user==student_pass:":
    print("welcome student:")
    print("what do you want to manage:")
    std1=input("student details")
    name=input("enter ur name:")

else :
    print("invalid access")   