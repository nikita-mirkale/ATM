data={1:"English",2:"Hindi",3:"Marathi",4:"Other"}
banktype={1:"Deposit",2:"Fast Cash",3:"MINI Statement",4:"Cash Withdrawl",5:"PIN Change",6:"Transfer" }
database={1:{'Account No': 12341234123, 'Mobile No': 8788336068, 'PIN': 2811,'Balance':20000},2:{'Account No': 90909049395, 'Mobile No': 8887336068, 'PIN': 2435,'Balance':20000},4:{'Account No': 89898087863, 'Mobile No': 9032541221, 'PIN': 8974,'Balance':20000},5:{'Account No': 44444444443, 'Mobile No': 8485838281, 'PIN': 8008,'Balance':20000}}
newpin=[]
lang=[]
type=[]
acc=0
mob=None
pin=None
bank_balance=0
print("*"*89)
print(f"{" "*40} WELCOME TO ATM !")
print("*"*89)
while True:
    print(" Customer insert their Card. Please don't remove your card.")
    
    language=input("""  
                        PLEASE SELECT THE LANGUAGE
                
                   
                    1. English           2.Hindi
                    3. Marathi          4. Other""")
    i=input(" Enter your language: ")
    if language not in i:
        print("Invalid language selection. Please try again.")
        continue
    lang.append(i) 
    # print(" Please Register Yourself... ")
    # acc=int(input(" Enter Your Account Number: "))
    # # if acc==len(int(12)):
    # #      print(" ")
    # # else:
    # #      print("Invalid..!")
    # bank_balance=int(input(" Enter Your Bank Balance: "))

    # mob=int(input("Enter Your Mobile Number : "))
    # # if mob==len(int(10)):
    # #      print(" ")
    # # else:
    # #      print(" Invalid..!")
    # generate_pin=int(input("Generate Your PIN: "))
    # # if generate_pin==len(int(4)):
    # #      print(" ")
    # # else:
    # #      print("Error")
    # # database[acc]={"Account No":acc,"Mobile No":mob,"PIN":generate_pin}
    # # print(database)

    
    
    banking_type=input("""
                                Select Your Transaction.
                        1.Deposit                2.Fast Cash
                        3.MINI Statement         4.Cash Withdrawl
                        5.PIN Change             6.Transfer
                        7.Registration      """)
    bt=int(input(" Enter the number of type:(1/2/3/4/5/6) "))
    type.append(bt)
    account_type=input(" Click the account type (if savings : 1, or current: 2 : ): ")
    if account_type not in account_type:
        print("Invalid account type selected. Please try again.")
        continue
    if account_type=='yes':
        continue
    pin=eval(input(" Please Enter Your PIN : "))
    
   
    if bt==1:# deposite
         print(" Acceptable Denomination($100,$200,$500,$2000)")
         amount1=int(input(" Enter the amount: "))
         [bank_balance]=bank_balance+amount1
         d=input(" Continue or cancel")
         if d=="countinue":
              print(" Your Transaction is being processed, please wait.")
              d = input("Continue or cancel: ").lower()
              print("Your current balance is ",bank_balance)
         else: 
              print("Transaction Cancel ! ")
                          
              break
         
    elif bt==2:#Fast cash
        amount2=int(input(" Please Select Amount: "))
        bank_balance=bank_balance-amount2
        print(" Your current bank balance is ",bank_balance)
        print(" Your Transaction is being processed, please wait.")
        break

    elif bt==3:#mini statement
         print(" Wel-come to ATM")
         print(" State Bank Of India")
         print("Account Number : ",acc)
         print("Your Mobile number: ",mob)
         print("IFCE code- 0004333")
         print(" Your Bank Balance",bank_balance)
         print(" Your Transaction is being processed, please wait.")
         break
    
    elif bt==4:# cash withdrawl
         ammount4=int(input(" Please enter amount: "))
         op=(input("""                   
                                        Press if Yes
                                        press if No"""))
         if bank_balance>ammount4: # type: ignore
                        print(" Your Transaction is being processed, please wait...")
                        bank_balance=bank_balance-ammount4 # type: ignore
                        print("Your bank balance is ",bank_balance)
         else:
                print("You don't have Efficient Bank Balance..!")
           
         break
                      
    elif bt==5:#pin change
         mob=int(input(" Enter Your 10 Digits Mobile Number: "))
         newpin=input("Enter the PIN")
         database[acc]["PIN"]=newpin
         print(" confirm !")
        #  old_pin=int(input(" Enter Your Old PIN: "))
        #  new_pin=int(input(" Enter Your New PIN: "))
         print(" Your Transaction is being processed, please wait.")
         break
    elif bt==6:# transfer
         pass
    elif bt==7:
         print(" Please Register Yourself... ")
         acc=int(input(" Enter Your Account Number: "))
            # if acc==len(int(12)):
            #      print(" ")
            # else:
            #      print("Invalid..!")
         bank_balance=int(input(" Enter Your Bank Balance: "))
         mob=int(input("Enter Your Mobile Number : "))
            # if mob==len(int(10)):
            #      print(" ")
            # else:
            #      print(" Invalid..!")
         generate_pin=int(input("Generate Your PIN: "))
            # if generate_pin==len(int(4)):
            #      print(" ")
            # else:
            #      print("Error")
        #  database[acc]={"acc":acc,"pin":pin,"mob":mob,"balance":bank_balance}
    else:
        print(" Invalid Banking Type selected!! ")
    choice=input(" Do You Want to Continue(yes/no): ")
    if choice.lower()=='no':
         
        print(" Remove Your card!\n Thank You!")
    break

   
     

    

