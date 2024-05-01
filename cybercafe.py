import pickle as p,os
#[loginid,password,name,age,phone_no,time,canplay,gamecharges]

def Bill(name):
    f=open("cus.dat","rb")
    
    try:
        while True:
            q=p.load(f)
            if q[0]==name:
                f.close()
                break

    except:
        f.close()
        print("Record not found.")  
        return
    
    total=q[5]*30
    gamecharges=q[-1]
    Billbeauty(["BILL PAYMENT","------------","NAME: "+q[2],"Phone Number:          "+str(q[4]),"Computer Charges: Rs"+str(total),"Game Charges: Rs"+str(gamecharges),"Total amount to pay = Rs"+str(total+gamecharges)])


    b=input("Type YES to pay your bill: ")

    if b in ["YES","y",'Y',"yes"]:
        print("\n1.Cash\n2.Online payment")
        ca=int(input("Enter your choice:"))
        if ca==1:
            amount=int(input("Payment Amount="+str(total+gamecharges)+":"))
            while amount<(total+gamecharges):
                print("Pay more...")
                amount=int(input("Payment Amount="+str(total+gamecharges)+":"))
    
            if amount>(total+gamecharges):
                print("Amount Returned=",amount-(total+gamecharges))
                
            print("\n",q[2],"has paid the bill successfully.\n ****THANK YOU****") 
        if ca==2:
            print("Pay online.")
            print("\n",q[2],"has paid the bill successfully")
        

def View(name):
    f=open("cus.dat","rb")

    try:
        while True:
            q=p.load(f)
            if q[0]==name:
                f.close()
                break

    except:
        f.close()
        print("\nRecord not found.")  
        return 

    f.close()

    print("\nName:",q[2])
    print("Age:",q[3])
    print("Phone number:",q[4])
    print("Time in cyber cafe",q[-3],"hrs.")
    print("Game charges: Rs",q[-1])

def Delete(loginid):
    f=open("cus.dat","rb")
    g=open("test.dat","wb")
    telsa=True
    try:
        while True:
            q=p.load(f)
            if q[0]==loginid:
                telsa=False
            else:
                p.dump(q,g)
    except:
        f.close()
        g.close()
        os.remove("cus.dat")
        os.rename("test.dat","cus.dat")
        if telsa:
            print("\nRecord not found")

def Modify(loginid,index=None,change=None):
    f=open("cus.dat","rb+")
    telsa=True
    try:
        while True:
            pos=f.tell()
            q=p.load(f)
            if q[0]==loginid:
                telsa=False
                if index==-1:
                    q[-1]+=change
                    f.seek(pos)
                    p.dump(q,f)
                    
                elif index==None:
                    print("\nPREVIOUS DATA-->")
                    View(q[0])
                    print("<--\n")
                    q[2]=input("Enter name of the customer:")
                    q[3]=int(input("Enter age of the customer:"))

                    phone_no=int(input("Enter the phone number:"))
                    while len(str(phone_no))!=10:
                        print("Error type 10 digit phone number...")
                        phone_no=int(input("Enter the phone number:"))   

                    q[4]=phone_no
                    q[5]=int(input("Enter the time in hours needed:"))

                    CanPlay= q[3]>=18
                    q[6]=CanPlay
                    
                    q[7]=int(input("Enter the game charges:"))

                    f.seek(pos)
                    p.dump(q,f)

                
    except:
        f.close()
        if telsa:
            print("\nRecord not found.")

def PlayGames(loginid):
    print()
    q=int(input("\n1.Rock-Paper-Scissor(Rs5 extra charges)\n2.TIC-TAC-TOE(Rs10 extra charges)\n3.Exit\n"))
    if q==1:
        if Modify(loginid,-1,5):
            print("\nRecord not found.")
        else:
            import RPS
    elif q==2:
        if Modify(loginid,-1,10):
            print("\nRecord not found.")
        else:
            import TICTACTOE
    elif q==3:
        return

def chkidpassword(x,y):
    f=open("cus.dat","rb")
    try:
        while True:
            q=p.load(f)
            if q[0]==x and q[1]==y:
                return [True,q[-2]]
    except:
        f.close()
        return [False]

def CusDeta():
    f=open("cus.dat","ab")
    loginid=input("Enter login id of the customer:")

    password=input("Enter password:")
    
    name=input("Enter name of the customer:")

    age=int(input("Enter age of the customer:"))
    if age>=18:
        CanPlay=True
    else:
        CanPlay=False


    delta=True
    firsttme=True
    while delta:
        if firsttme:    
            firsttme=False
        else:
            print("Error type 10 digit phone number...")
        phone_no=int(input("Enter the phone number:"))
        delta=len(str(phone_no))!=10    

    
    time=int(input("Enter the time in hours needed:")) 

    lis=[loginid,password,name,age,phone_no,time,CanPlay,0]

    p.dump(lis,f)

    print("**RECORD ADDED**")
    f.close()

def Billbeauty(b):
    mx=len(b[0])
    for i in range(1,len(b)):
        if mx<len(b[i]):
                mx=len(b[i])

    to="*"*(mx+4)
    print()
    print(to)

    for i in b:
        print("* ",i+" "*(mx-len(i))," *",sep="")
    print(to)
    print()

def Admin():
    while True:
        print("\n1.Modify Customer Details\n2.Delete Customer Details\n3.Customers detail view\n4.Quit\n")
        a=int(input("Enter your choice :"))
        
        if a==4:
            break
        
        LoginId=input("Enter the loginid of the Customer:")
        
        if a==1:
            print()
            Modify(LoginId)
            print("**RECORD MODIFIED**")

        if a==2:
            print()
            Delete(LoginId)
            print("**RECORD DELETED**")

        if a==3:
            View(LoginId)



def User():
    while True:
        print("\n1.Insert user details(if new)\n2.Login\n3.Return to previous menu")
        a=int(input("Enter your choice:"))
        if a==1:
            CusDeta()
        if a==2:
            l=input("Enter user id:")
            p=input("Enter user password:")
            delta1=chkidpassword(l,p)
            if delta1[0]:
                while True:
                    print("\n1.Games\n2.Bill\n3.Return to the previous menu")
                    choice=int(input("Enter your choice:"))
                    if choice==1:
                        if delta1[1]==True:
                            PlayGames(l)
                        else:
                            print("\nAge should be greater than 18 to play.")
                    elif choice==2:
                        Bill(l)
                    else:
                        break
            else:
                print("Invalid")
                  
        if a==3:
            break        


print("       *****SAMARTH CYBER CAFE WELCOMES YOU*****        ")
print()    

while True:
    print("\n1.Admin\n2.User\n3.Exit")
    a=int(input("Enter your choice :"))
    if a==1:
        Admin()
        
    elif a==2:
        User()

    elif a==3:
        print("\n                    THANK YOU VISIT AGAIN               ")
        break

































s
