account={}
accpwd={}
bal=0
import random
from datetime import datetime
print('welcome to XYZ banking services')
while True:
    print('**************************************************************')
    print('Please select your option:','\n','1.Already a user(sign in)','\n','2.new user(sign up)','\n','3.EXIT' )
    n=int(input())
    if(n==2):
            account_no='83840000'+str(random.randint(1000,9999))
            if account_no not in account:
                account_no=account_no
            else:
                account_no='83840000'+str(random.randint(1000,9999))
            name=input('enter your name')
            m_no=int(input('enter mobile number'))
            if(len(str(m_no))==10):
               m_no=m_no
            else:
                print('number not accepted')
                break
            gno=int(input('pls enter your gender: 1.Male,2:.Female,3:Other'))
            if(gno==1):
                gen='Male'
            elif(gno==2):
                gen='Female'
            elif(gno==3):
                gen='Other'
            else:
                print('invalid input')
                break
            dob=str(input('enter your date of birth'))
            pwd=input('enter your password')
            pwd2=input('confirm your password')
            if(pwd==pwd2):
                print('your account',account_no,'has been successfully created')
                account[account_no]={'NAME':name,'Mobile':m_no,'Gender':gen,'DOB':dob,'Balance':bal}
                accpwd[account_no]=pwd
            else:
                print('passwords dont match')
                break
    elif(n==1):
                a=input('enter your account number')
                b=input('enter your password')
                if(a in accpwd):
                    if(accpwd[a]==b):
                        print('you have succseessfully logged in')
                        print('Available services:')
                        print('1.check acoount details and balance','\n','2.deposit amount','/n/','3.withraw amount','\n','4.Transfer amount')
                        s=int(input('select your service'))
                        if(s==1):
                            print('Account No:',a)
                            print('Name:',account[a]['NAME'])
                            print('MOBILE NO:',account[a]['Mobile'])
                            print('Gender:',account[a]['Gender'])
                            print('DOB:',account[a]['DOB'])
                            print('BALANCE:',account[a]['Balance'])
                        elif(s==2):
                            amt=int(input('enter amount to be deposited'))
                            account[a]['Balance']=account[a]['Balance']+amt
                            print('amount Rs.',amt,'is successfully deposited')
                        elif(s==3):
                            amt=int(input('enter amount to be withdrawn'))
                            if(amt<account[a]['Balance']):
                              account[a]['Balance']=account[a]['Balance']-amt
                              print('amount Rs.',amt,'is successfully withdrwan')
                            else:
                                print('insufficient funds')
                                break
                        elif(s==4):
                            amt=int(input('ammount to be transfered'))
                            if(amt<account[a]['Balance']):
                              c=input('account to be transfered')
                              if c in account:
                                    account[a]['Balance']=account[a]['Balance']-amt
                                    account[c]['Balance']=account[c]['Balance']+amt
                                    print('amount Rs.',amt,'is successfully transfered')
                              else:
                                  print('invalid account to be transfered')
                                  break
                            else:
                                print('insufficient funds')
                                break
                        else:
                            print('service not available')
                            break
                else:
                    print('invalid account number')
                    
    elif(n==3):
               print('Thank you for chossing us')
               break 
    else:
            print('sorry input not accepted')
