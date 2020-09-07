#Modules
import pickle
import random
from datetime import date
from tabulate import tabulate
def NameValid():
    valid=0
    while valid==0:
        name=input("Enter Your Name=")
        if len(name)>3 and name.isalnum()==False:
            valid=1
        else:
            print("Invalid Name,Please Enter again")
    return name
def FatherName():
    valid=0
    while valid==0:
        name1=input("Enter Your Father's Name=")
        if len(name1)>2 and name1.isalnum()==False:
            valid=1
            return name1
        else:
            print("Invalid Name,Please Enter again")
    
def MotherName():
    valid=0
    while valid==0:
        name2=input("Enter Your Mother's Name=")
        if len(name2)>2 and name2.isalnum()==False:
            valid=1
            return name2
        else:
            print("Invalid Name,Please Enter again")
    
    
def AdmNoGen():
    code=0
    k=random.randint(10000,99999)
    code+=k
    print("Adm.No=",code)
    print("Please Note your Admission number")
    return code
def ClassValid():
    valid=0
    while valid==0:
        Class=int(input("Enter Your Class="))
        if Class=="12":
            valid=1
            return Class
        else:
            print("Invalid,Enter Again")
    
def SecValid():
    valid=0
    while valid==0:
        Sec=input("Enter Your Sec=")
        if Sec.isupper()==True:
            valid=1
            return Sec
        else:
            print("Invalid,Enter Again")
def DOBValid():
   while True:
    try:
        doj=input("Ente Your DOB(DD/MM/YYYY)=")
        d,m,y=[int(x) for x in doj.split('/')]
        doj=date(y,m,d)
        if doj>=date(2001,1,1) and doj<=date(2005,1,1):
            valid=1
            return doj
        else:
            print("Invalid")
    except:
        print("Invalid DOB")
def fPhnchk():
    valid=0
    while valid==0:
        phnno=int(input("Enter Your Phone no.=+965"))
        if phnno>=10000000 and phnno<=99999999:
            valid=1
            return phnno
        else:
            print("Invalid,Enter Again")
def rollchk():
    valid=0
    while valid==0:
        roll=int(input("Enter Your Roll no.="))
        if roll>=1 and roll<=35:
            valid=1
            return roll
        else:
            valid=0
            print("Invalid")
def streamcode():
    print("Enter Your Respective StreamCode")
    print("SC-Science with Computer")
    print("SB-Science with Biology")
    print("SE-Science with Economics")
    print("CM-Commerce with Maths")
    print("HU-Humanities")
    print("CI-Commerce with Informatics Practices")
    valid=0
    while valid==0:
        Str=input("Enter Your StreamCode=")
        if Str=="SC"or Str=="SB"or Str=="SE"or Str=="CM"or Str=="HU"or Str=="CI":
            valid=1
            return Str
        else:
            print("Invalid,Please Enter Your StreamCode")
def GenValid():
    valid=0
    while valid==0:
        Gen=input("Enter Your Gender(M/F)=")
        if Gen=="M" or Gen=="F":
            valid=1
            return Gen
        else:
            print("Invalid,Enter Again")
def NewStudent():
    with open('StudentFile.dat','rb')as student:
        recnew=[]
        try:
            while True:
                rec=pickle.load(student)
                recnew.append(rec)
        except:
            with open('StudentFile.dat','wb')as student:
                n=int(input("Enter the no.of student records="))
                for k in range(n):
                    AdmNo=AdmNoGen()
                    name=NameValid()
                    roll=rollchk()
                    fname=FatherName()
                    mname=MotherName()
                    dob=DOBValid()
                    Gen=GenValid()
                    phnchk=fPhnchk()
                    Class=ClassValid()
                    Sec=SecValid()
                    sc=streamcode()
                    newrec=[AdmNo,roll,name,Class,Sec,Gen,dob,fname,mname,phnchk,sc]
                    pickle.dump(newrec,student)
                for i in recnew:
                    pickle.dump(i,student)
def editstudent():
    with open('StudentFile.dat','rb') as student:
        print("To Cancel,Enter '0'")
        AdmNo=int(input("Enter Your Adm.no="))
        if AdmNo==0:
            return None
        recnew=[]
        try:
            while True:
                rec=pickle.load(student)
                recnew.append(rec)
        except:
            for k in recnew:
                if k[0]==AdmNo:
                    found=1
                    ch=1
                    while ch!=0:
                        print("Enter Your Choice")
                        print("1. Edit your name")
                        print("2. Edit your father's name")
                        print("3. Edit your mother's name")
                        print("4. Edit your  phone no.")
                        print("5. Edit your StreamCode")
                        print("0. EXIT")
                        ch=int(input("Enter your Choice"))
                        if ch==1:
                            rec[2]=input("Enter the corrected name=")
                        elif ch==2:
                            rec[7]=input("Enter the corrected name=")
                        elif ch==3:
                            rec[8]=input("Enter the corrected name=")
                        elif ch==4:
                            rec[9]=int(input("Enter the corrected number="))
                        elif ch==5:
                            rec[10]=input("Enter your Streamcode=")
                with open('StudentFile.dat','wb') as student:
                    pickle.dump(k,student)
                if found==0:
                    print("Invalid Adm.no/Doesn't Exist")
                else:
                    print("Edited Student details successfully")
def displaydetails():
    with open("StudentFile.dat",'rb') as f:
        try:
            list1=[]
            while True:
                rec=pickle.load(f)
                list1.append(rec)
        except:
            print(tabulate(list1,headers=['Adm.No','Roll.no','Name','Class.','Sec.','Gender','DOB','Fathername','Mothername','Phoneno.','StrCode'],tablefmt='psql'))                                   
def deletedetails():
    with open("StudentFile.dat","rb") as recdel:
        found=0
        print("To cancel,Enter '0'")
        AdmNo=int(input("Enter Adm.no of the student to delete the record"))
        recnew=[]
        if AdmNo=='0':
            return None
        try:
            while True:
                rec=pickle.load(recdel)
                if AdmNo!=rec[0]:
                    recnew.append(rec)
                else:
                    found=1
        except:
            with open("StudentFile.dat","wb") as recdel:
                for k in recnew:
                    pickle.dump(k,recdel)
        if found==0:
            print("Invalid Adm.no/Doesn't exist")
        else:
            print("Student record successfully deleted")
            print("Please 'DELETE' student's Result details also.(for avoiding confusion)")

def marks():
    with open ('StudentFile.dat','rb') as student:
        print("To exit,Enter 0")
        AdmNo=int(input("Enter your Adm.No.="))
        if AdmNo==0:
            return None
        try:
            list1=[]
            while True:
                rec=pickle.load(student)
                list1.append(rec)
        except:
            with open("ResultFile.dat","rb") as result:
                 try:
                     recnew=[]
                     while True:
                         rec=pickle.load(result)
                         recnew.append(rec)
                 except:
                     for k in list1:
                         if k[0]==AdmNo and k[10]=="SC":
                             print("Please enter your respective subject marks as instructed")
                             print("SUB1-English(Out of 100)")
                             print("SUB2-Maths(Out of 100)")
                             print("SUB3-Physics(Out of 100)")
                             print("SUB4-Chemistry(Out of 100)")
                             print("SUB5-ComputerScience(Out of 100)")
                             s1=int(input("Enter your marks{SUB1}="))
                             s2=int(input("Enter your marks{SUB2}="))
                             s3=int(input("Enter your marks{SUB3}="))
                             s4=int(input("Enter your marks{SUB4}="))
                             s5=int(input("Enter your marks{SUB5}="))
                             with open("ResultFile.dat","wb") as result:
                                 total_list=[s1,s2,s3,s4,s5]
                                 total=s1+s2+s3+s4+s5
                                 avg=total/5
                                 if s1>=90:
                                    grd1="A1"
                                 elif s1<90 and s1>=80:
                                    grd1="B1"
                                 elif s1<80 and s1>=70:
                                    grd1="B2"
                                 else:
                                    grd1="C1"
                                 if s2>=90:
                                    grd2="A1"
                                 elif s2<90 and s2>=80:
                                    grd2="B1"
                                 elif s2<80 and s2>=70:
                                    grd2="B2"
                                 else:
                                    grd2="C1"
                                 if s3>=90:
                                    grd3="A1"
                                 elif s3<90 and s3>=80:
                                    grd3="B1"
                                 elif s3<80 and s3>=70:
                                    grd3="B2"
                                 else:
                                    grd3="C1"
                                 if s4>=90:
                                    grd4="A1"
                                 elif s4<90 and s4>=80:
                                    grd4="B1"
                                 elif s4<80 and s4>=70:
                                    grd4="B2"
                                 else:
                                    grd4="C1"
                                 if s5>=90:
                                    grd5="A1"
                                 elif s5<90 and s5>=80:
                                    grd5="B1"
                                 elif s5<80 and s5>=70:
                                    grd5="B2"
                                 else:
                                    grd5="C1" 
                                 if s1>=33 and s2>=33 and s3>=33 and s4>=33 and s5>=33 and s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100:
                                     if total>=60:
                                         div='I'
                                         newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SC"]
                                         recnew.append(newrec)
                                         for k in recnew:
                                             pickle.dump(k,result)
                                     elif total>=50 and total<=60:
                                         div='II'
                                         newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SC"]
                                         recnew.append(newrec)
                                         for k in recnew:
                                             pickle.dump(k,result)
                                     elif total<50:
                                            div='III'
                                            newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SC"]
                                            recnew.append(newrec)
                                            for k in recnew:
                                                pickle.dump(k,result)
                                 elif s1<=33 or s2<=33 or s3<=33 or s4<=33 or s5<=33:
                                     c=0
                                     for k in total_list:
                                         if k<=33:
                                             c+=1
                                             if c==1:
                                                 div='CO'
                                                 newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SC"]
                                                 recnew.append(newrec)
                                                 for k in recnew:
                                                     pickle.dump(k,result)
                                             elif c>1:
                                                 div='FA'
                                                 newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SC"]
                                                 recnew.append(newrec)
                                                 for k in recnew:
                                                     pickle.dump(k,result)
                                 else:
                                     print("Invalid Marks,Enter Again")   
                                    

                         if k[0]==AdmNo and k[10]=="SB":
                             print("Please enter your respective subject marks as instructed")
                             print("SUB1-English(Out of 100)")
                             print("SUB2-Maths(Out of 100)")
                             print("SUB3-Physics(Out of 100)")
                             print("SUB4-Chemistry(Out of 100)")
                             print("SUB5-Biology(Out of 100)")
                             s1=int(input("Enter your marks{SUB1}="))
                             s2=int(input("Enter your marks{SUB2}="))
                             s3=int(input("Enter your marks{SUB3}="))
                             s4=int(input("Enter your marks{SUB4}="))
                             s5=int(input("Enter your marks{SUB5}="))
                             with open("ResultFile.dat","wb") as result:
                                 total_list=[s1,s2,s3,s4,s5]
                                 total=s1+s2+s3+s4+s5
                                 avg=total/5
                                 if s1>=90:
                                    grd1="A1"
                                 elif s1<90 and s1>=80:
                                    grd1="B1"
                                 elif s1<80 and s1>=70:
                                    grd1="B2"
                                 else:
                                    grd1="C1"
                                 if s2>=90:
                                    grd2="A1"
                                 elif s2<90 and s2>=80:
                                    grd2="B1"
                                 elif s2<80 and s2>=70:
                                    grd1="B2"
                                 else:
                                    grd2="C1"
                                 if s3>=90:
                                    grd3="A1"
                                 elif s3<90 and s3>=80:
                                    grd3="B1"
                                 elif s3<80 and s3>=70:
                                    grd3="B2"
                                 else:
                                    grd3="C1"
                                 if s4>=90:
                                    grd4="A1"
                                 elif s4<90 and s4>=80:
                                    grd4="B1"
                                 elif s4<80 and s4>=70:
                                    grd4="B2"
                                 else:
                                    grd4="C1"
                                 if s5>=90:
                                    grd5="A1"
                                 elif s5<90 and s5>=80:
                                    grd5="B1"
                                 elif s5<80 and s5>=70:
                                    grd5="B2"
                                 else:
                                    grd5="C1" 
                                 if s1>=33 and s2>=33 and s3>=33 and s4>=33 and s5>=33 and s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100:
                                     if total>=60:
                                         div='I'
                                         newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SB"]
                                         recnew.append(newrec)
                                         for k in recnew:
                                             pickle.dump(k,result)
                                     elif total>=50 and total<=60:
                                         div='II'
                                         newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SB"]
                                         recnew.append(newrec)
                                         for k in recnew:
                                             pickle.dump(k,result)
                                     elif total<50:
                                            div='III'
                                            newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SB"]
                                            recnew.append(newrec)
                                            for k in recnew:
                                                pickle.dump(k,result)
                                 elif s1<=33 or s2<=33 or s3<=33 or s4<=33 or s5<=33:
                                     c=0
                                     for k in total_list:
                                         if k<=33:
                                             c+=1
                                             if c==1:
                                                 div='CO'
                                                 newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SB"]
                                                 recnew.append(newrec)
                                                 for k in recnew:
                                                     pickle.dump(k,result)
                                             elif c>1:
                                                 div='FA'
                                                 newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SB"]
                                                 recnew.append(newrec)
                                                 for k in recnew:
                                                     pickle.dump(k,result)
                                 else:
                                     print("Invalid Marks,Enter Again")   
                                                     
                         if k[0]==AdmNo and k[10]=="SE":
                            print("Please enter your respective subject marks as instructed")
                            print("SUB1-English(Out of 100)")
                            print("SUB2-Maths(Out of 100)")
                            print("SUB3-Physics(Out of 100)")
                            print("SUB4-Chemistry(Out of 100)")
                            print("SUB5-Economics(Out of 100)")
                            s1=int(input("Enter your marks{SUB1}="))
                            s2=int(input("Enter your marks{SUB2}="))
                            s3=int(input("Enter your marks{SUB3}="))
                            s4=int(input("Enter your marks{SUB4}="))
                            s5=int(input("Enter your marks{SUB5}="))
                            with open("ResultFile.dat","wb") as result:
                                total_list=[s1,s2,s3,s4,s5]
                                total=s1+s2+s3+s4+s5
                                avg=total/5
                                if s1>=90:
                                    grd1="A1"
                                elif s1<90 and s1>=80:
                                    grd1="B1"
                                elif s1<80 and s1>=70:
                                    grd1="B2"
                                else:
                                    grd1="C1"
                                if s2>=90:
                                    grd2="A1"
                                elif s2<90 and s2>=80:
                                    grd2="B1"
                                elif s2<80 and s2>=70:
                                    grd1="B2"
                                else:
                                    grd2="C1"
                                if s3>=90:
                                    grd3="A1"
                                elif s3<90 and s3>=80:
                                    grd3="B1"
                                elif s3<80 and s3>=70:
                                    grd3="B2"
                                else:
                                    grd3="C1"
                                if s4>=90:
                                    grd4="A1"
                                elif s4<90 and s4>=80:
                                    grd4="B1"
                                elif s4<80 and s4>=70:
                                    grd4="B2"
                                else:
                                    grd4="C1"
                                if s5>=90:
                                    grd5="A1"
                                elif s5<90 and s5>=80:
                                    grd5="B1"
                                elif s5<80 and s5>=70:
                                    grd5="B2"
                                else:
                                    grd5="C1" 
                                if s1>=33 and s2>=33 and s3>=33 and s4>=33 and s5>=33 and s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100:
                                    if total>=60:
                                        div='I'
                                        newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SE"]
                                        recnew.append(newrec)
                                        for k in recnew:
                                            pickle.dump(k,result)
                                    elif total>=50 and total<=60:
                                        div='II'
                                        newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SE"]
                                        recnew.append(newrec)
                                        for k in recnew:
                                            pickle.dump(k,result)
                                    elif total<50:
                                        div='III'
                                        newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SE"]
                                        recnew.append(newrec)
                                        for k in recnew:
                                                pickle.dump(k,result)
                                elif s1<=33 or s2<=33 or s3<=33 or s4<=33 or s5<=33:
                                    c=0
                                    for k in total_list:
                                        if k<=33:
                                            c+=1
                                            if c==1:
                                                div='CO'
                                                newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SE"]
                                                recnew.append(newrec)
                                                for k in recnew:
                                                    pickle.dump(k,result)
                                            elif c>1:
                                                div='FA'
                                                newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"SE"]
                                                recnew.append(newrec)
                                                for k in recnew:
                                                    pickle.dump(k,result)
                                else:
                                    print("Invalid Marks,Enter Again")   

                         if k[0]==AdmNo and k[10]=="CM":
                             print("Please enter your respective subject marks as instructed")
                             print("SUB1-English(Out of 100)")
                             print("SUB2-Maths(Out of 100)")
                             print("SUB3-Economics(Out of 100)")
                             print("SUB4-Accountancy(Out of 100)")
                             print("SUB5-Business(Out of 100)")
                             s1=int(input("Enter your marks{SUB1}="))
                             s2=int(input("Enter your marks{SUB2}="))
                             s3=int(input("Enter your marks{SUB3}="))
                             s4=int(input("Enter your marks{SUB4}="))
                             s5=int(input("Enter your marks{SUB5}="))
                             with open("ResultFile.dat","wb") as result:
                                 total_list=[s1,s2,s3,s4,s5]
                                 total=s1+s2+s3+s4+s5
                                 avg=total/5
                                 if s1>=90:
                                     grd1="A1"
                                 elif s1<90 and s1>=80:
                                     grd1="B1"
                                 elif s1<80 and s1>=70:
                                     grd1="B2"
                                 else:
                                     grd1="C1"
                                 if s2>=90:
                                     grd2="A1"
                                 elif s2<90 and s2>=80:
                                     grd2="B1"
                                 elif s2<80 and s2>=70:
                                     grd1="B2"
                                 else:
                                     grd2="C1"
                                 if s3>=90:
                                     grd3="A1"
                                 elif s3<90 and s3>=80:
                                     grd3="B1"
                                 elif s3<80 and s3>=70:
                                     grd3="B2"
                                 else:
                                     grd3="C1"
                                 if s4>=90:
                                     grd4="A1"
                                 elif s4<90 and s4>=80:
                                     grd4="B1"
                                 elif s4<80 and s4>=70:
                                     grd4="B2"
                                 else:
                                     grd4="C1"
                                 if s5>=90:
                                     grd5="A1"
                                 elif s5<90 and s5>=80:
                                     grd5="B1"
                                 elif s5<80 and s5>=70:
                                     grd5="B2"
                                 else:
                                    grd5="C1" 
                                 if s1>=33 and s2>=33 and s3>=33 and s4>=33 and s5>=33 and s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100:
                                     if total>=60:
                                         div='I'
                                         newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CM"]
                                         recnew.append(newrec)
                                         for k in recnew:
                                             pickle.dump(k,result)
                                     elif total>=50 and total<=60:
                                         div='II'
                                         newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CM"]
                                         recnew.append(newrec)
                                         for k in recnew:
                                             pickle.dump(k,result)
                                     elif total<50:
                                            div='III'
                                            newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CM"]
                                            recnew.append(newrec)
                                            for k in recnew:
                                                pickle.dump(k,result)
                                 elif s1<=33 or s2<=33 or s3<=33 or s4<=33 or s5<=33:
                                     c=0
                                     for k in total_list:
                                         if k<=33:
                                             c+=1
                                             if c==1:
                                                 div='CO'
                                                 newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CM"]
                                                 recnew.append(newrec)
                                                 for k in recnew:
                                                     pickle.dump(k,result)
                                             elif c>1:
                                                 div='FA'
                                                 newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CM"]
                                                 recnew.append(newrec)
                                                 for k in recnew:
                                                     pickle.dump(k,result)
                                 else:
                                     print("Invalid Marks,Enter Again")   

                         if k[0]==AdmNo and k[10]=="CI":
                             print("Please enter your respective subject marks as instructed")
                             print("SUB1-English(Out of 100)")
                             print("SUB2-Economics(Out of 100)")
                             print("SUB3-Accountancy(Out of 100)")
                             print("SUB4-Business(Out of 100)")
                             print("SUB5-Informatic Practice(Out of 100)")
                             s1=int(input("Enter your marks{SUB1}="))
                             s2=int(input("Enter your marks{SUB2}="))
                             s3=int(input("Enter your marks{SUB3}="))
                             s4=int(input("Enter your marks{SUB4}="))
                             s5=int(input("Enter your marks{SUB5}="))
                             with open("ResultFile.dat","wb") as result:
                                 total_list=[s1,s2,s3,s4,s5]
                                 total=s1+s2+s3+s4+s5
                                 avg=total/5
                                 if s1>=90:
                                     grd1="A1"
                                 elif s1<90 and s1>=80:
                                     grd1="B1"
                                 elif s1<80 and s1>=70:
                                     grd1="B2"
                                 else:
                                     grd1="C1"
                                 if s2>=90:
                                     grd2="A1"
                                 elif s2<90 and s2>=80:
                                     grd2="B1"
                                 elif s2<80 and s2>=70:
                                     grd1="B2"
                                 else:
                                     grd2="C1"
                                 if s3>=90:
                                     grd3="A1"
                                 elif s3<90 and s3>=80:
                                     grd3="B1"
                                 elif s3<80 and s3>=70:
                                     grd3="B2"
                                 else:
                                     grd3="C1"
                                 if s4>=90:
                                     grd4="A1"
                                 elif s4<90 and s4>=80:
                                     grd4="B1"
                                 elif s4<80 and s4>=70:
                                     grd4="B2"
                                 else:
                                     grd4="C1"
                                 if s5>=90:
                                     grd5="A1"
                                 elif s5<90 and s5>=80:
                                     grd5="B1"
                                 elif s5<80 and s5>=70:
                                     grd5="B2"
                                 else:
                                    grd5="C1" 
                                 if s1>=33 and s2>=33 and s3>=33 and s4>=33 and s5>=33 and s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100:
                                     if avg>=60:
                                         div='I'
                                         newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CI"]
                                         recnew.append(newrec)
                                         for k in recnew:
                                             pickle.dump(k,result)
                                     elif avg>=50 and avg<=60:
                                         div='II'
                                         newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CI"]
                                         recnew.append(newrec)
                                         for k in recnew:
                                             pickle.dump(k,result)
                                     elif avg<50:
                                            div='III'
                                            newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CI"]
                                            recnew.append(newrec)
                                            for k in recnew:
                                                pickle.dump(k,result)
                                 elif s1<=33 or s2<=33 or s3<=33 or s4<=33 or s5<=33:
                                     c=0
                                     for k in total_list:
                                         if k<=33:
                                             c+=1
                                             if c==1:
                                                 div='CO'
                                                 print("Better Luck Next time")
                                                 newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CI"]
                                                 recnew.append(newrec)
                                                 for k in recnew:
                                                     pickle.dump(k,result)
                                             elif c>1:
                                                 div='FA'
                                                 newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"CI"]
                                                 recnew.append(newrec)
                                                 for k in recnew:
                                                     pickle.dump(k,result)
                                 else:
                                     print("Invalid Marks, Enter Again")
                         if k[0]==AdmNo and k[10]=="HU":
                            print("Please enter your respective subject marks as instructed")
                            print("SUB1-English(Out of 100)")
                            print("SUB2-History(Out of 100)")
                            print("SUB3-Geography(Out of 100)")
                            print("SUB4-Economics(Out of 100)")
                            print("SUB5-PoliticalScience(Out of 100)")
                            s1=int(input("Enter your marks{SUB1}="))
                            s2=int(input("Enter your marks{SUB2}="))
                            s3=int(input("Enter your marks{SUB3}="))
                            s4=int(input("Enter your marks{SUB4}="))
                            s5=int(input("Enter your marks{SUB5}="))
                            with open("ResultFile.dat","wb") as result:
                                total_list=[s1,s2,s3,s4,s5]
                                total=s1+s2+s3+s4+s5
                                avg=total/5
                                if s1>=90:
                                    grd1="A1"
                                elif s1<90 and s1>=80:
                                    grd1="B1"
                                elif s1<80 and s1>=70:
                                    grd1="B2"
                                else:
                                    grd1="C1"
                                if s2>=90:
                                    grd2="A1"
                                elif s2<90 and s2>=80:
                                    grd2="B1"
                                elif s2<80 and s2>=70:
                                    grd1="B2"
                                else:
                                    grd2="C1"
                                if s3>=90:
                                    grd3="A1"
                                elif s3<90 and s3>=80:
                                    grd3="B1"
                                elif s3<80 and s3>=70:
                                    grd3="B2"
                                else:
                                    grd3="C1"
                                if s4>=90:
                                    grd4="A1"
                                elif s4<90 and s4>=80:
                                    grd4="B1"
                                elif s4<80 and s4>=70:
                                    grd4="B2"
                                else:
                                    grd4="C1"
                                if s5>=90:
                                    grd5="A1"
                                elif s5<90 and s5>=80:
                                    grd5="B1"
                                elif s5<80 and s5>=70:
                                    grd5="B2"
                                else:
                                    grd5="C1"
                                if s1>=33 and s2>=33 and s3>=33 and s4>=33 and s5>=33 and s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100 :
                                    if avg>=60:
                                        div='I'
                                        newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"HU"]
                                        recnew.append(newrec)
                                        for k in recnew:
                                            pickle.dump(k,result)
                                    elif avg>=50 and avg<=60:
                                        div='II'
                                        newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"HU"]
                                        recnew.append(newrec)
                                        for k in recnew:
                                            pickle.dump(k,result)
                                    elif avg<50:
                                        div='III'
                                        newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"HU"]
                                        recnew.append(newrec)
                                        for k in recnew:
                                                pickle.dump(k,result)
                                elif s1<=33 or s2<=33 or s3<=33 or s4<=33 or s5<=33 :
                                    c=0
                                    for k in total_list:
                                        if k<=33:
                                            c+=1
                                            if c==1:
                                                div='CO'
                                                newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"HU"]
                                                recnew.append(newrec)
                                                for k in recnew:
                                                    pickle.dump(k,result)
                                            elif c>1:
                                                div='FA'
                                                newrec=[AdmNo,s1,grd1,s2,grd2,s3,grd3,s4,grd4,s5,grd5,total,avg,div,"HU"]
                                                recnew.append(newrec)
                                                for k in recnew:
                                                    pickle.dump(k,result)
                                else:
                                    print("Invalid Marks,Enter Again")


def displaymarks():
     with open("ResultFile.dat",'rb') as f:
        try:
            list1=[]
            while True:
                rec=pickle.load(f)
                list1.append(rec)
        except:
            print(tabulate(list1,headers=['Adm.No','S1','Gr1','S2','Gr2','S3','Gr3','S4','Gr4','S5','Gr5','Tot.','Avg','Div','Str.'],tablefmt='psql'))                                   
         
def deletemarks():
        with open("ResultFile.dat","rb") as recdel:
            found=0
            print("To cancel,Enter '0'")
            AdmNo=int(input("Enter Adm.no of the student to delete the record="))
            recnew=[]
            if AdmNo=='0':
                return None
            try:
                while True:
                    rec=pickle.load(recdel)
                    if AdmNo!=rec[0]:
                        recnew.append(rec)
                    else:
                        found=1
            except:
                with open("ResultFile.dat","wb") as recdel:
                    for k in recnew:
                        pickle.dump(k,recdel)
            if found==0:
               print("Invalid Adm.no/Doesn't exist")
            else:
               print("Student report successfully deleted")

def editmarks():
    with open('ResultFile.dat','rb') as result:
        print("To Cancel,Enter '0'")
        AdmNo=int(input("Enter your Adm.no="))
        Str=input("Enter your Streamcode=") 
        if AdmNo==0:
            return None
        recnew=[]
        try:
            while True:
                rec=pickle.load(result)
                recnew.append(rec)
        except:
            for k in recnew:
                if k[0]==AdmNo and k[9]==Str:
                    print("Your Previous Avg=",k[7])
                    found=1
                    ch=1
                    while ch!=0:
                        print("Enter Your Choice=")
                        print("1. Edit SUB1")
                        print("2. Edit SUB2")
                        print("3. Edit SUB3")
                        print("4. Edit SUB4")
                        print("5. Edit SUB5")
                        print("0. EXIT")
                        ch=int(input("Enter your Choice="))
                        if ch==1:
                            rec[1]=input("Enter the corrected marks=")
                        elif ch==2:
                            rec[2]=input("Enter the corrected marks=")
                        elif ch==3:
                            rec[3]=input("Enter the corrected marks=")
                        elif ch==4:
                            rec[4]=int(input("Enter the corrected marks="))
                        elif ch==5:
                            rec[5]=input("Enter the corrected marks=")
                with open('ResultFile.dat','wb') as result:
                    pickle.dump(k,result)
                if found==0:
                    print("Invalid Adm.no/Doesn't Exist")
                else:
                    print("Edited Student's Report successfully")

def displayreport():
    AdmNo=int(input("Enter your AdmNo="))
    Str=input("Enter your streamcode=")
    f1=open("StudentFile.dat","rb")
    f2=open("ResultFile.dat","rb")
    try:
        l1,l2=[],[]
        while True:
            rec=pickle.load(f1)
            rec2=pickle.load(f2)
            l1.append(rec)
            l2.append(rec2)
    except: 
        for k in l1:
            if k[0]==AdmNo and k[10]==Str :
                for i in l2:
                    if i[0]==AdmNo:
                        print(5*"--")
                        print(2*"\t","Second Terminal Examination")
                        print("Adm.No=",AdmNo),print("Roll.no=",k[1])
                        print("Name=",k[2]), print("Class=",k[3])
                        print("Stream=",k[10]), print("Sec=",k[4])
                        table_head=["Subject","Max","Marks","Grade"]
                        table_data=[["SUB1","100",i[1],i[2]],["SUB2","100",i[3],i[4]],["SUB3","100",i[5],i[6]],["SUB4","100",i[7],i[8]],["SUB5","100",i[9],i[10]]]
                        print(tabulate(table_data, headers=table_head, tablefmt="psql"))

            else:
                print("Invalid Adm.No/StreamCode,Please Re-enter")
    f1.close()
    f2.close()
def meritlist():
    Str=input("Enter the streamcode=")
    f1=open("StudentFile.dat","rb")
    f2=open("ResultFile.dat","rb")
    try:
        merit=[]
        l1,l2=[],[]
        while True:
            rec=pickle.load(f1)
            rec2=pickle.load(f2)
            l1.append(rec)
            l2.append(rec2)
    except:
        for k in l1:
            if k[10]==Str:
                for i in l2:
                    if i[14]==Str:
                        if i[13]=="I":
                            l3=[k[0],k[2],i[11],i[12],k[3],k[4]]
                            merit.append(l3)
                            print(tabulate(merit,headers=['AdmNo','Name','Total','Avg','Class','Sec'],tablefmt='psql'))
            
            else:
                print("Invalid StreamCode,Please Re-enter")
    f1.close()
    f2.close()            
                        
                            
                    
#i=l2=['Adm.No','S1','Gr1','S2','Gr2','S3','Gr3','S4','Gr4','S5','Gr5','Tot11.','Avg12','Div'13,'Str.14']
#k=l1=[AdmNo,roll,name,Class,Sec,Gen,dob,fname,mname,phnchk,sc]
    
    
