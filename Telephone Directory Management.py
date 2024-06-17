def password():
    c=input("Enter Password :")
    if c=="hello":
        print("Access approved")
    else:
        print("Invalid Password")
        password()

def user():
    a=input("Enter User - Admin or Guest, A or G :")
    if a.lower()=="a":
        password()
        menu()
        
    elif a.lower()=="g":
        menu_user()

    else:
      print("Invalid Choice, Try Again")
      user()

def validate(adh):
    global abcd
    c=len(adh)
    if c==12:
      abcd=adh
    else:
      print("Invalid Aadhar, Try Again")
      adh=input("Enter Aadhar Number :")
      validate(adh)
    
    return abcd

def validateno1(no):
    global abcde
    c=len(no)
    if c==10:
      abcde=no
    else:
      print("Invalid Number, Try Again")
      no=input("Enter Number 1 :")
      validateno1(no)

    return abcde

def validatenom(d):
    global abcdefgh
    c=len(d)
    if c==10:
      abcdefgh=d
    else:
      print("Invalid Number, Try Again")
      no=input("Enter New Number :")
      validatenom(d)

    return abcdefgh
def validateno2(no2):
    global abcdef
    c=len(no2)
    if c==10:
      abcdef=no2
    else:
      print("Invalid Number, Try Again")
      no2=input("Enter Number 2 :")
      validateno2(no2)

    return abcdef
       
def validatepin(pn):
    global abcdefg
    c=len(pn)
    if c==6:
      abcdefg=pn
    else:
      print("Invalid Pincode, Try Again")
      pn=input("Enter Pincode:")
      validatepin(pn)

    return abcdefg
def primary(adhc):
    global a3
    a5=int(adhc)
    f10=open("data.txt","r")
    x=f10.readlines()
    a3=adhc
    for i in x:
        a=i.split("\t")
        if a5==int(a[0]):
            print("Aadhar Number Already Exists, Try Again")
            abc=input("Enter Aadhar Number: ")
            adhc=validate(abc)
            ab=primary(adhc)
        else:
            a3=adhc
    return a3
       
def create():
    f=open("data.txt","w")
    f.close()
    print("New File Created")

def add():
    f1= open("data.txt","a+")
    for i in range(1):
        adh=input("Enter Aadhar Number :")
        adhc=validate(adh)
        ab=primary(adhc)
        na=str(input("Enter Name :"))
        no=input("Enter Number 1 :")
        noc=validateno1(no)
        no2=input("Enter Number 2 :")
        no2c=validateno2(no2)
        ad=str(input("Enter Address :"))
        ct=str(input("Enter City :"))
        st=str(input("Enter State :"))
        pn=input("Enter Pincode : ")
        pnc=validatepin(pn)
        f1.write(ab)
        f1.write("\t")
        f1.write(na)
        f1.write("\t")
        f1.write(noc)
        f1.write("\t")
        f1.write(no2c)
        f1.write("\t")
        f1.write(ad)
        f1.write("\t")
        f1.write(ct)
        f1.write("\t")
        f1.write(st)
        f1.write("\t")
        f1.write(pnc)
        f1.write("\n")
        f1.close()
        yn()
def yn():
    b=input("Press Y to add more records and N to exit :")
    c="N"
    d="Y"
    x=b
    if x.lower()==c.lower():
        print("Records Inserted")
    elif x.lower()==d.lower():
        add()
    else:
        print("Invalid Choice, Try Again")
        yn()       
    


def modify():
    f3= open("data.txt","r")
    y=int(input("Aadhar Number Of Record That Has to be modified :"))
    x=f3.readlines()
    index=0
    for i in x:
        a=i.split("\t")
        if int(a[0])==y:
            x.pop(index)
        index=+1
    f3.close()
    f3=open("data.txt","w")
    f3.writelines(x)
    f3.close()
    f1=open("data.txt","a+")
    for i in range(1):
        abcd=str(y)
        adhc=validate(abcd)
        ab=primary(adhc)
        na=str(input("Enter Name :"))
        no=input("Enter Number 1 :")
        noc=validateno1(no)
        no2=input("Enter Number 2 :")
        no2c=validateno2(no2)
        ad=str(input("Enter Address :"))
        ct=str(input("Enter City :"))
        st=str(input("Enter State :"))
        pn=input("Enter Pincode : ")
        pnc=validatepin(pn)
        f1.write(ab)
        f1.write("\t")
        f1.write(na)
        f1.write("\t")
        f1.write(noc)
        f1.write("\t")
        f1.write(no2c)
        f1.write("\t")
        f1.write(ad)
        f1.write("\t")
        f1.write(ct)
        f1.write("\t")
        f1.write(st)
        f1.write("\t")
        f1.write(pnc)
        f1.write("\n")
        f1.close()
    display()

def search_name():
    f2= open("data.txt","r")
    y=input("Name of Person Whose Number is to be searched :")
    x=f2.readlines()
    for i in x:
        a=i.split("\t")
        if y.lower()==(a[1]).lower():
            print("Data found -",a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7], sep="\t")
    f2.close()

def search_no():
    f2= open("data.txt","r")
    y=int(input("Number to be searched :"))
    x=f2.readlines()
    for i in x:
        a=i.split("\t")
        if y==int(a[2]) or y==int(a[3]):
            print("Data found -",a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7], sep="\t")
    f2.close()

def search_adh():
    f2= open("data.txt","r")
    y=int(input("Number to be searched :"))
    x=f2.readlines()
    for i in x:
        a=i.split("\t")
        if y==int(a[0]):
            print("Data found -",a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7], sep="\t")
    f2.close()
    
def search():
    while True:
        print("\n")
        print("Press 1 For Searching Number On The Basis Of Name")
        print("Press 2 For Searching Number On The Basis Of Phone Number")
        print("Press 3 For Searching Number On The Basis Of Aadhar Number")
        print("Press 4 To Exit")
        
        j=int(input("Enter Choice :"))

        if j==1:
            search_name()
        elif j==2:
            search_no()
        elif j==3:
            search_adh()
        elif j==4:
            break
        else:
            print("Wrong Input. Try again")
    

def display():
    f5= open("data.txt","r")
    x=f5.readlines()
    print("Details Are As Follows:")
    for i in x:
        a=i.split("\t")
        print(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],sep="\t",end='\n')
    f5.close()

def delete():
    f3= open("data.txt","r")
    y=int(input("Aadhar Number Of Person Whose Record Has to Be Deleted:"))
    x=f3.readlines()
    index=0
    for i in x:
        a=i.split("\t")
        if int(a[0])==y:
            x.pop(index)
        index=+1
    f3.close()
    f3=open("data.txt","w")
    f3.writelines(x)
    print("Data Modified")
    f3.close()
    display()
def menu():        
    while True:
        print("\n")
        print("Press 1 For Creating a New File")
        print("If File Already Exists-")
        print("Press 2 For Adding Number")
        print("Press 3 For Deleting Number")
        print("Press 4 For Searching Number")
        print("Press 5 For Modifying Number")
        print("Press 6 For Displaying Data")
        print("Press 7 To Change User")
        print("Press 8 To Exit")


        j=int(input("Enter Choice :"))

        if j==1:
            create()
        elif j==2:
            add()
        elif j==3:
            delete()
        elif j==4:
            search()
        elif j==5:
            modify()
        elif j==6:
            display()
        elif j==7:
            user()
        elif j==8:
            break
        else:
            print("Wrong Input. Try again")
def menu_user():
    while True:
        print("\n")
        print("If File Already Exists-")
        print("Press 1 For Searching Number")
        print("Press 2 For Displaying Number")
        print("Press 3 To Change User")
        print("Press 4 To Exit")
        
        j=int(input("Enter Choice :"))

        if j==1:
            search()
        elif j==2:
            display()
        elif j==3:
            user()
        elif j==4:
            break
        else:
            print("Wrong Input. Try again")

user()
