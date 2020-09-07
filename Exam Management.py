#By Charith.K
import pickle
from _CSprojectmodules import project 
ch=1 
while ch!=0:
    print("Hello Student/Parents")
    print("(1) Access StudentFile")
    print("(2) Access ResultFile")
    print("(3) Display StudentReportCard")
    print("(0) Exit ")
    ch=int(input("Enter your choice="))
    if ch==1:
        while ch!=0:
            print(25*"--")
            print("\t","(1) Input Student Details")
            print("\t","(2) Edit Student Details")
            print("\t","(3) Delete Student Record")
            print("\t","(4) Display Student Details")
            print("\t","(0) Exit Menu")
            ch=int(input("\t""Enter your choice="))
            if ch==1:
                project.NewStudent()
            elif ch==2:
                project.editstudent()
            elif ch==3:
                project.deletedetails()
            elif ch==4:
                project.displaydetails()
            elif ch==0:
                print("EXIT")
        ch=1
    elif ch==2:
        while ch!=0:
            print(25*"--")
            print("\t","(1) Input Student's Report")
            print("\t","(2) Edit Student's Report")
            print("\t","(3) Delete Student Record")
            print("\t","(4) Display Student Report")
            print("\t","(0) Exit Menu")
            ch=int(input("\t""Enter your choice="))
            if ch==1:
                project.marks()
            elif ch==2:
                project.editmarks()
            elif ch==3:
                project.deletemarks()
            elif ch==4:
                project.displaymarks()
            elif ch==0:
                print("EXIT")
        ch=2
    elif ch==3:
        while ch!=0:
            print(20*"--")
            print("\t","(1) Display Student ReportCard")
            print("\t","(2) Display StreamWise MeritList")
            print("\t","(0) Exit Menu")
            ch=int(input("\t""Enter your choice="))
            if ch==1:
                project.displayreport()
            if ch==2:
                project.meritlist()
            elif ch==0:
                print("EXIT")
        ch=3
            

#------------------------------------------------------------------------------#-----------------------------------------------------------------------------------            
            
