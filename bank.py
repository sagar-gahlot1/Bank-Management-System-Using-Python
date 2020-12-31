import sqlite3
conn=sqlite3.connect("bank.db")
cursor=conn.cursor()
cursor.execute("create table if not exists cust(acc_no int primary key,balance int ,name1 char(20) not null)")
class bank:
    def insert_data(self):
        self.acc_no=(input("New Account Number="))
        self.balance=(input("Balance="))
        self.name=input("Customer Name=")
        cursor.execute("insert into cust values(?,?,?)",(self.acc_no,self.balance,self.name))
        conn.commit()
        print("ACCOUNT CREATED SUCCESSFULLY....")
    def display(self):
        cursor.execute("select * from cust")
        l=cursor.fetchall()
        print("ACCOUNT NUMBER||BALANCE ||CUSTOMER NAME")
        for j in range(len(l)):
            for i in range(3):
                print(l[j][i],end="\t\t")
            print("\n")   
    def deposit(self):
        self.x=input("enter the amount to deposit")
        self.y=input("enter the account number to deposit")
        cursor.execute("update cust set balance=balance+? where acc_no=?",(self.x,self.y))
        conn.commit()
        print("BALANCE DEPOSIT SUCCESSFULLY.....")
    def withdrawal(self):
        self.w=input("enter the amount to withdrawal")
        self.x=input("enter acc to withdrawal=")
        print(self.w)
        cursor.execute("update cust set balance=balance-? where acc_no=?",(self.w,self.x))
        conn.commit()
        print("WITHDRAWAL SUCCESSFULLY....")
    def delete(self):
        self.y=input("enter account number to delete=")
        cursor.execute("delete from cust where acc_no=?",(self.y,))
        conn.commit()
        print("DELETE SUCCESSFULLLY....")
    def passbook(self):
        self.p=input("enter the account number to create passbook= ")
        cursor.execute("select * from cust where acc_no= ?",(self.p,))
        pb=cursor.fetchone()
        cursor.execute("select name1 from cust where acc_no= ?",(self.p,))
        x=cursor.fetchone()
        f=open(str(str(x))+"passbook"+'.txt',"w")
        a="Account number= "
        n="Name of custumor= "
        b="Current balance= "
        l=list(pb)
        l.insert(0,a)
        l.insert(2,b)
        l.insert(4,n)
        print(l)
        print("PASSBOOK CREATED SUCCESSFULLY....<=")
        for i in range(len(l)):
            f.write(str(l[i]))
            if i%2!=0:
                f.write("\n")
        f.close()
        
        
b=bank()
while True:
    print("================================BANK OPTIONS=================================\n1. Create an account\n2. Deposit to account\n3. Withdrwal to account\n4. Delete an account\n5. Display all custoumer details\n6. Create passbook\n7. Close\n================================**********==================================\n")
    a=int(input("CHOICE=> "))
    if a==1:
        b.insert_data()
    if a==2:
        b.deposit()
    if a==3:
        b.withdrawal()
    if a==4:
        b.delete()
    if a==5:
        b.display()
    if a==6:
        b.passbook()
    if a==7:
        break
conn.close()
