import mysql.connector as sql
import sys
import time
from click import option
import numpy.random as npr
import os
class Coperative:

    def __init__(self):
        npr.RandomState(0)
        self.owner= []
        self.bank = "wisdom coperative"
        self.location ="ogbomoso"
        self.amount="0"
        self.user_input=""
        self.customer={}
        self.sponsor={}
        self.paid={}
        self.shareInt={}
       
        # self.mycursor.execute("create database coperative")
        # self.mycursor.execute("show databases")
        self.cm()
        
        # self.details()

    def cm(self):
        myCon=sql.connect(host="127.0.0.1", user= 'root', passwd='', database='coperative')
        mycursor=myCon.cursor()
        # mycursor.execute("create table customer (customer_id int(4), fullName varchar(50),address varchar(50), email varchar(50), phone varchar(11), password varchar(20)) ")
        # mycursor.execute("alter table customer change customer_id customer_id int(4) primary key auto_increment")
        # mycursor.execute("alter table customer add unique(phone)")
        myQuery="insert into customer (fullName, address, email, phone, password) values(%s, %s, %s, %s, %s)"
        self.acc_name = input("Enter your prefered account name >> ")
        self.add=input('Fill in your address>> ')
        self.email=input('Enter your email address>> ')
        self.phone = input("Enter your phone number >> ")
        self.pin = input("Enter your prefered password >> ")
        val=(self.acc_name, self.add, self.email, self.phone, self.pin)
        myquery= "insert into customer (fullName, address, email, phone, password) values(%s, %s, %s, %s, %s)"
        mycursor.execute(myQuery, val)
        myCon.commit()
        print(mycursor.rowcount, "records insert successfully")
        # myCon.close()

    def details(self):
        print("welcome to "+ self.bank)
        time.sleep(2)
        self.mainMenu()

    def mainMenu(self):
        print(""" choose operation, Enter:
        1. To open account
        2. To transact
        3. To quit""")
        option=input(">>> ")
        if option=="1":
            self.openAcount()
        elif option=="2":
            self.login()
        elif option =="3":
            self.quit()
        else:
            print("invalid selection")
            time.sleep(2)
            self.mainMenu()

    def openAcount(self):
        self.acc_name = input("Enter your prefered account name >>")
        self.phone = input("Enter your phone number >>")
        while len(self.phone) != 11:
            print("Invalid phone number. Phone lenght must be 11")
            self.phone = input("Enter your phone number >>")
        self.pin = input("Enter your prefered password >> ")
        while len(self.pin) !=4 and type(self.pin) != int:
            print("Invalid pin, pin must be integer value")
            self.pin = input("Enter your prefered password >> ")
        # self.acc_type= input("Enter 1 for savings, 2 for share account >>")
        self.acc_number = npr.randint(1000000000)
        self.balance = 0
        self.loan=0
        self.payLoan=0
        self.shareAccount=0
        self.paidInt=0
        self.shareInterest=0
        self.customers_details=[self.acc_name, self.pin, self.phone, self.acc_number, self.balance, self.loan, self.shareAccount, self.payLoan, self.paidInt, self.shareInterest]
        self.customer[self.acc_number] = self.customers_details
        print(self.customer)
        print(self.acc_name + " welcome to " + self.bank)
        time.sleep(2)
        self.mainMenu()


    def login(self):
        user_acct = int(input("please enter your account number to login > "))
        user_pin = input("please enter your password to login > ")
        self.user_detail = self.customer.get(user_acct)
        if self.user_detail != None and user_pin == self.user_detail[1]:
            print("welcome "+ self.customer[user_acct][0]+ " with the account number "+ str(self.acc_number))
            self.operation()
        else:
            print("invalid password")
            time.sleep(2)
            self.login()
            
    def account_type(self):
        print("""please choose account type:
        1. savings
        2. Loan account
        3. share account""")
        option= input(">>> ")
        if option==self.customer[self.acc_number][3]:
            self.operation()
        else:
            print("invalid selection")
            self.account_type()


    def operation(self):
        print("""please enter your operation:
            1. withdraw
            2. check balance
            3. deposit
            4. Apply for loan
            5. pay for loan
            6. transfer fund 
            7. buy share
            8. close account
            8. Menu""")
        option= input(">>> ")
        # time.sleep(2)
        if option =="1":
            self.withdraw()
        elif option== "2":
            self.checkBalance()
        elif option== "3":
            self.deposit()
        elif option== "4":
            self.applyForLoan()
        elif option== "5":
            self.payForLoan()
        elif option== "6":
            self.transferFund()
        elif option== "7":
            self.buyShare()
        elif option== "8":
            self.closeAccount()
        elif option== "9":
            self.mainMenu()
        else:
            print("invalid selection")
            time.sleep(2)
            self.operation()    

    def withdraw(self):
        amount ={1:1000, 2:2000, 3:5000, 4:10000, 5:15000, 6:20000}
        print("""please choose amount:
        1. 1000
        2. 2000
        3. 5000
        4. 10000
        5. 15000
        6. 20000
        7. other""")
        option= int(input(">>> "))
        if option > 0 and option < 7:
            if self.user_detail[5] >= amount[option]:
                print("hold on while your transaction is processing.......")
                self.user_detail[5] -= amount[option]
                time.sleep(3)
                print("please take your cash")
                time.sleep(2) 
                self.another() 
            else:
                 print("insufficient balance")
                 time.sleep(2)
                 self.another()
        elif option == 7:
            self.amount=int(input("please enter amount"))
            if self.user_detail[5] >= self.amount:
                print("hold on while your transaction is processing.......")
                time.sleep(3)
                print("please take your cash")
                self.user_detail[5] -= self.amount 
                time.sleep(2)
                self.another()
            else:
                print("insufficient balance")
                time.sleep(2)
            self.another()
        else:
            print("Invalid selection")
            time.sleep(2)
            self.withdraw()

    def another(self):
        self.command= input("press 1 to perform another transaction, press 2 to quit>> ")
        if self.command =="1":
            self.mainMenu()
        elif self.command=="2":
            time.sleep(2)
            self.quit()
        else:
            print("inavlid selection")
            time.sleep(2)
            self.another()

    def checkBalance(self):
        print("""choose account to view balance:
        1. main balance
        2. loan balance
        3. share interest balance
        4. cancel""")
        option=input(">>> ")
        if option=="1":
            print("your balance is ", self.user_detail[5])
            time.sleep(2)
            self.another()
        elif option=="2":
            print("your balance is ", self.user_detail[8])
            time.sleep(2)
            self.another()
        elif option=="3":
            print("your balance is ", self.user_detail[9])
            time.sleep(2)
            self.another()
        elif option=="4":
            self.another()
        else:
            print("invalid selection")
            time.sleep(2)
            self.another()

    def deposit(self):
        print("""choose account to deposit in:
        1. main account
        2. savings account
        3. pay back loan
        4. cancel""")
        option=input(">>> ")
        if option=="1":
            dep=int(input("input amount > "))
            self.user_detail[5] += dep
            time.sleep(2)
            print("your account has been successfully credited with", dep)
            time.sleep(2)
            self.another()
        elif option=="2":
            dep=int(input("input amount > "))
            self.user_detail[6] += dep
            time.sleep(2)
            print("your account has been successfully credited with", dep)
            time.sleep(2)
            self.another()
        elif option=="3":
            dep=int(input("input amount > "))
            self.payForLoan()
        elif option=="4":
            time.sleep(2)
            self.another()

    def applyForLoan(self):
        if self.user_detail[5] >= 50000:
            print("please fill your sponsposor's details")
            self.collact=input("Enter your sponsor's name>> ")
            self.collactNum=int(input("Enter your sponsor,s phone number>> "))
            while len(self.phone) != 11:
                print("Invalid phone number. Phone lenght must be 11")
                self.collactNum = int(input("Enter your sponsor,s phone number>> "))
            self.collactAdd=input("Enter your sponsor's address>> ")
            self.collactEmail=input("Enter your sponsor's email address>> ")
            self.coll=[self.collact, self.collactNum, self.collactAdd, self.collactEmail ]
            self.sponsor=self.coll
            print(self.sponsor)
            if self.user_detail[8]==0:
                self.applyAmount=int(input("Enter Loan amount>> "))
                self.payDate=input("Enter the pay date , (e.g 25th dec. 2023) >> ")
                print("hold on while we process your request.......")
                time.sleep(3)
                if self.user_detail[5]>=50000 and self.user_detail[5]< 100000 and self.applyAmount<=100000:
                    print("you're eligible to borrow maximum of 100,000")
                    self.user_detail[5]+=self.applyAmount
                    self.user_detail[8]+=self.applyAmount
                    print("you have receive a loan of ", self.applyAmount, " to be paid on ", self. payDate )
                    time.sleep(2)
                    self.another()
                elif self.user_detail[5]>=100000 and self.user_detail[5]<150000 and self.applyAmount<=150000:
                    print("you're eligible to borrow maximum of 150,000")
                    self.user_detail[5]+=self.applyAmount
                    self.user_detail[8]+=self.applyAmount
                    print("you have receive a loan of ", self.applyAmount, " to be paid on ", self. payDate )
                    time.sleep(2)
                    self.another()
                elif self.user_detail[5]>=150000 and self.user_detail[5]<500000 and self.applyAmount<=500000:
                    print("you're eligible to borrow maximum of 500,000")
                    self.user_detail[5]+=self.applyAmount
                    self.user_detail[8]+=self.applyAmount
                    print("you have receive a loan of ", self.applyAmount, " to be paid on ", self. payDate )
                    time.sleep(2)
                    self.another()
                elif self.user_detail[5]>=500000 and self.user_detail[5]<2000000 and self.applyAmount<=2000000:
                    print("you're eligible to borrow maximum of 2,000,000")
                    self.user_detail[5]+=self.applyAmount
                    self.user_detail[8]+=self.applyAmount
                    print("you have receive a loan of ", self.applyAmount, " to be paid on ", self. payDate )
                    time.sleep(2)
                    self.another()
                elif self.user_detail[5]>=2000000 and self.user_detail[5]<5000000 and self.applyAmount<=5000000:
                    print("you're eligible to borrow maximum of 5,000,000")
                    self.user_detail[5]+=self.applyAmount
                    self.user_detail[8]+=self.applyAmount
                    print("you have receive a loan of ", self.applyAmount, " to be paid on ", self. payDate )
                    time.sleep(2)
                    self.another()
                elif self.user_detail[5]>=5000000 and self.user_detail[5]<10000000 and self.applyAmount<=10000000:
                    print("you're eligible to borrow maximum of 10,000,000")
                    self.user_detail[5]+=self.applyAmount
                    self.user_detail[8]+=self.applyAmount
                    print("you have receive a loan of ", self.applyAmount, " to be paid on ", self. payDate )
                    time.sleep(2)
                    self.another()
                else:
                    print("you're not eligible for this loan")
                    time.sleep(2)
                    self.another()
            else:
                print("you still have an outstanding debt, please clear your debt to be eligible    for loan!!!")
                time.sleep(2)
                self.another()
        else:
            print("you must have at least 50000 in your main account to perform this operation")
            time.sleep(2)
            self.another()

    def payForLoan(self):
        if self.user_detail[8] !=0:
            self.pay= float(input("Enter amount you wish to pay >>"))
            percentage= self.user_detail[8] / 100 / 1
            self.inter =self.pay - percentage
            self.paidin=[self.paidInt]
            self.paid=self.paidin
            if self.user_detail[5] >=self.pay:
                self.user_detail[5]-=self.pay
                self.user_detail[8]-=self.inter
                self.paidInt+=percentage
                time.sleep(2)
                print("transaction successful")
                time.sleep(2)
                print("you still have an outstanding debt of ", self.user_detail[8], " and  interest of 1% to pay")
                time.sleep(2)
                self.another()
            else:
                print("insufficient fund, please check your interest")
                time.sleep(2)
                self.another()
        else:
            print("you don't have an outstanding loan to pay for")
            time.sleep(2)
            self.another()
        
    def transferFund(self):
        print("""Enter account you wish to transfer to:
        1. Transfer from main account to savings account
        2. Transfer from main account to share account
        3. transfer to other account
        4. go back to operation
        5. go back to main menu""")
        option=input(">>> ")
        if option =="1":
            self.tfmain_savings()
        elif option =="2":
            self.tfMain_share()
        elif option=="3":
            self.tfOther()
        elif option =="4":
            self.operation()
        elif option=="5":
            self.mainMenu()
        else:
            print("invalid selection")
            self.transferFund()

    def tfmain_savings(self):
        savings=int(input("Enter amount>> "))
        if self.user_detail[5]>=savings:
            self.user_detail[6]+=savings
            time.sleep(2)
            print("transaction successful")
            time.sleep(2)
            self.another()
        else:
            print("insufficient Fund")
            time.sleep(2)
            self.another()

    def tfMain_share(self):
        share=int(input("Enter amount>> "))
        if self.user_detail[5]>=share:
            self.user_detail[5]-=share
            self.user_detail[7]+=share
            time.sleep(2)
            print("transaction successful")
            time.sleep(2)
            self.another()
        else:
            print("insufficient Fund")
            time.sleep(2)
            self.another()

    def tfOther(self):
        acc_num=input("Enter distination account number")
        other=int(input("Enter amount>> "))
        if self.user_detail[5]>=other:
            self.user_detail[5]-=other
            time.sleep(2)
            print("transaction successful")
            time.sleep(2)
            self.another()
        else:
            print("insufficient fund")
            time.sleep(2)
            self.another()
        

    def buyShare(self):
        self.share=int(input("Enter share amount>> "))
        percentage= self.user_detail[7] / 100 / 2.5
        self.user_detail[5] -=self.share
        self.user_detail[7]+=self.share
        self.shareInterest+=percentage
        self.shareArr=[self.shareInterest]
        self.shareInt=self.shareArr
        time.sleep(2)
        print("transaction successful")
        time.sleep(2)
        self.another()

    def closeAccount(self):
        print("""please choose the account you wish to close:
        1. savings account
        2. share account
        3. All your account
        4. cancel""")
        option=input(">>> ")
        if option=="1":
            ans=input("enter 1 to confirm this action or 2 to go back >> ")
            if ans =="1" and self.user_detail[6] !=0:
                self.user_detail[6]-=self.user_detail[6]
                print("please take your total cash of ", self.user_detail[6])
                time.sleep(2)
                self.another()
            elif ans=="2":
                self.closeAccount()
            else:
                print("no fund in this account")
                time.sleep(2)
                self.another()
        elif option=="2":
            ans=input("enter 1 to confirm this action or 2 to go back >> ")
            if ans =="1" and self.user_detail[7] !=0:
                self.sClose=self.user_detail[7] + self.user_detail[9]
                self.user_detail[7]-=self.sClose
                print("please take your total cash of ", self.sClose)
                time.sleep(2)
                self.another()
            elif ans=="2":
                self.closeAccount()
            else:
                print("no fund in this account")
                time.sleep(2)
                self.another()
        elif option=="3":
            ans=input("enter 1 to confirm this action or 2 to go back >> ")
            self.all=self.user_detail[5]+ self.user_detail[6]+ self.user_detail[7]+ self.user_detail[9]
            if ans =="1" and self.all !=0:
                self.user_detail[5]-=self.user_detail[5]
                self.user_detail[6]-=self.user_detail[6]
                self.user_detail[7]-=self.user_detail[7]
                self.user_detail[9]-=self.user_detail[9]
                print("please take your total cash of ", self.all)
                time.sleep(2)
                self.quit()
            elif ans=="2":
                self.closeAccount()
            else:
                print("no fund in this account")
                time.sleep(2)
                self.another()
        elif option=="4":
            self.another()


    def quit(self):
        print("thank you for banking with us")
        time.sleep(2)
        sys.exit()

    def d_b(self):
        myCon=sql.connect(host="127.0.0.1", user= 'root', passwd='', database="coperative_db")
        mycursor=myCon.cursor()
        mycursor.execute("create database coperative_db")

atm = Coperative()

# myCon=sql.connect(host="127.0.0.1", user= 'root', passwd='', database="coperative_db")
# mycursor=myCon.cursor()

#  mycursor.execute("create database coperative_db")
# mycursor.execute("show databases")
# for db in mycursor:
#     print(db)

# mycursor.execute("create table customer (customer_id int(4), fullName varchar(50),address varchar(50), email varchar(50), phone varchar(11), password varchar(20)) ")

# mycursor.execute("show tables")
# for table in mycursor:
    # print(table)