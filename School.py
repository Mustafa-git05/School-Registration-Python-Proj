import webbrowser as web
import time
import re
price = 20000#Used for calculating the total price that the person eneds to pay
a = 0 #Variable used later for a while function
#Language Selection
Lang = int(input("""Hello and welcome to the Dubai International School Al Garhoud Branch portal!
what language would you like to proceed with?
1. English
2. اللغة العربية
please press 1 or 2 يرجى اختيار الرقم واحد او اثنين
"""))
if Lang == 2:
    print(""" لازلنا نعمل على اضافة اللغة العربية لموقعنا، سنحولكم الى اللغة الانجليزية تلقائيا. نتأسف على التعطيل""")
elif Lang == 1:
    print("This conversation will carry on in English.")
else:
    print("this is not a valid response. The conversation will automaticall carry on in English.")
   
   
#Sign up page-Jamil's part
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #Email format
print("It seems that you dont have an account you will be redirected to our sign up page...")
time.sleep(2)
email=str(input("Whats your email?"))



#Email checker
while True:
    if (re.search(regex,email)): #Checks if the email fits the format
        print("valid email")
        break
    else:
        print("Not valid, please re ente your email")
        time.sleep(2)
        email=str(input("Whats your email?"))
       
       
#Password checker
password=str(input("whats your password"))
confirm=input("confirm your password")
while True:
    if password==confirm and len(password)>=8:
        print("your password matches and its valid")
        break
    else:
        print("Your password either doesent match or is less than 8 characters please re enter it..")
        time.sleep(2)
        password=input("whats your password")
        confirm=input("confirm your password")
       
#Login page
print("you have finished the sign up process please login to your account")
time.sleep(1)
emailLogin=input("Email:")
passwordLogin=input("Password:")
while True:
    if emailLogin==email and passwordLogin==password:
        print("You have logged into your account!")
        break
    elif emailLogin!=email:
        print("the email isnt found in the data base please re enter your email")
        emailLogin=input("Email:")
       
       
    elif passwordLogin!=password:
        print("the password doesent match please re-enter it")
        passwordLogin=input("Password:")
#Selections
time.sleep(3.5)
while True:
    
    Selections = int(input("""How may we help you today?
1. I would like to register my kid into your school.
2. I would like to learn more about your school.
3. I would like to be redirected to your FAQ page.
"""))


   
    #Kassem's part
    if Selections == 2:
        print("Dubai International school was founded on 1 December 1985 in Garhoud, Dubai. A second branch of the school was opened in 1998 in Al Quoz, Dubai. The two branches coordinate by a director general and have the same board of directors. The school gained accreditation from AdvancED in 2012.")
        
    
    #Ayham's part
    elif Selections == 3:
        print("you will be automatically redirected to the FAQ page, please wait...")
        time.sleep(3)
        web.open("http://213.42.28.183:9040/DISGAR/index.php/information")
    
    #Mustafa's part
    elif Selections == 1:
        while a == 0: #start from here
            print("please not that each grades tution fee is 20k AED, and it should be paid at school")
            name=input("What is your childs name?")
            gender=input("What is your childs gender?")
    
    #gender sec
            while True:
                if gender.lower()=="male" or gender.lower()=="female":
                    age=int(input("what is your childs age?"))
                    break
           
                else:
                    print("that is not a valid gender please try again ")
                    gender=input("What is your childs gender?")
    
    #end of gender sec
    
    
    #age sec
            while True:    
                if age>=19:
                    print("Please enter an age less than 19")
                    age=int(input("what is your childs age?"))
       
       
                elif age<19:
                    grade=int(input("""what grade would you like to register your child in?
    please not that kindegarten registrations are not avalible."""))
                break
    #end of age sec
    
    
    #grade sec
            while True:
       
    #grade1 sec
                if grade ==1:
                    print("welcome to grade 1 registration please complete the following steps:")
                    print("There are no electives to choose from for this year please enter your childs emirates ID so he can be registred to this grade.")
                    break
    #end of grade1 sec
       
    #grade2 sec
                elif grade ==2:
                    print("welcome to grade 2 registration please complete the following steps:")
                    print("There are no electives to choose from for this year please enter your childs emirates ID so he can be registred to this grade.")
                    break
    #end of grade2 sec
       
    #grade3 sec
                elif grade ==3:
                    print("welcome to grade 3 registration please complete the following steps:")
                    print("There are no electives to choose from for this year please enter your childs emirates ID so he can be registred to this grade.")
                    break
    #end of grade3 sec
       
    #grade4 sec
                elif grade ==4:
                    print("welcome to grade 4 registration please complete the following steps:")
                    print("There are no electives to choose from for this year please enter your childs emirates ID so he can be registred to this grade.")
                    break
    #end of grade4 sec
    
    #grade5 sec
                elif grade ==5:
                    print("welcome to grade 5 registration please complete the following steps:")
                    print("There are no electives to choose from for this year please enter your childs emirates ID so he can be registred to this grade.")
                    break
     #end of grade5 sec  
       
    #grade6 sec
                elif grade ==6:
                    print("welcome to grade 6 registration please complete the following steps:")
                    print("There are no electives to choose from for this year please enter your childs emirates ID so he can be registred to this grade.")
                    break
    # end of grade6 sec
    
    # grade7 sec
                elif grade ==7:
                    print("welcome to grade 7 registration please complete the following steps:")
                    print("There are no electives to choose from for this year please enter your childs emirates ID so he can be registred to this grade.")
                    break
    # end of grade7 sec
    
    #grade8 sec
                elif grade ==8:
                    print("welcome to grade 8 registration please complete the following steps:")
                    print("There are no electives to choose from for this year please enter your childs emirates ID so he can be registred to this grade.")
                    break
    # end of grade8 sec
    
    # grade9 sec
                elif grade ==9:
                    print("welcome to grade 9 registration please complete the following steps:")
           
            #electives sec
                    print("""please pick one out of the three electives for your""",gender,"""child:
            1) Phsyics
            2)Photopshop
            3)Python""")
                    electives=int(input("Please pick an elective:"))
                    while True:
                        if electives ==1:
                            e="physics"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==2:
                            e="Photoshop"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==3:
                            e="Phython"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        else:
                            print("No such elective exsists")
                            electives=int(input("Please pick an elective:"))
            #end of electives sec
                    break
    # end of grade9 sec
    
       
       
    # grade10 sec
                elif grade ==10:
                    print("welcome to grade 10 registration please complete the following steps:")
             #electives sec
                    print("""please pick one out of the three electives for your""",gender,"""child:
            1) Phsyics
            2)Photopshop
            3)Python""")
                    electives=int(input("Please pick an elective:"))
                    while True:
                        if electives ==1:
                            e="physics"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==2:
                            e="Photoshop"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==3:
                            e="Phython"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        else:
                            print("No such elective exsists")
                            electives=int(input("Please pick an elective:"))
            #end of electives sec
                    break
    # end of grade10 sec
     
       
       
    #grade11 sec
                elif grade ==11:
                    print("welcome to grade 11 registration please complete the following steps:")
            #electives sec
                    print("""please pick one out of the three electives for your""",gender,"""child:
            1) Phsyics
            2)Photopshop
            3)Python""")
                    electives=int(input("Please pick an elective:"))
                    while True:
                        if electives ==1:
                            e="physics"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==2:
                            e="Photoshop"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==3:
                            e="Phython"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        else:
                            print("No such elective exsists")
                            electives=int(input("Please pick an elective:"))
    #end of electives sec
                    break
    # end of grade11 sec
       
       
       
       
                elif grade ==12:
                    print("welcome to grade 12 registration please complete the following steps:")
            #electives sec
                    print("""please pick one out of the three electives for your""",gender,"""child:
            1) Phsyics
            2)Photopshop
            3)Python""")
                    electives=int(input("Please pick an elective:"))
                    while True:
                        if electives ==1:
                            e="physics"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==2:
                            e="Photoshop"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==3:
                            e="Phython"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        else:
                            print("No such elective exsists")
                            electives=int(input("Please pick an elective:"))
            #end of electives sec
                    break
       
                else:
                    print("that grade does not exsit please try again")
                    grade=int(input("""what grade would you like to register your child in?
    please not that kindegarten registrations are not avalible."""))
    
    #end of grade sec
    
    
    #emirates id sec:
            emirates=int(input("please give us all 15 intgers in your childs emirates ID without the dashes:"))
    
            while True:
                strem=str(emirates)
                if len(strem)==15:
                    print("Thank you your childs emirates ID has been put into the system")
                    break
                else:
                    print("that is not a valid emirates ID number!")
                    emirates=int(input("please give us all 15 intgers in your childs emirates ID without the dashes:"))
            print("your",age,"year old",gender,"child,",name,",with emirates id number",emirates,",has succesfuly been registred in grade",grade,".We are excited to welcome him!")
            while True:
                anotherchild=input("Would you like to register another child ")
                if anotherchild.lower()=="yes":
                    print("You will need to refill all the previous forms but for the new child")
                    print("The price you have to pay until now is ",price)
                    price +=20000
                    break
                elif anotherchild.lower()=="no":
                    print("You have finished the process, and the price you will have to pay is",price)
                    a=1
                    break
                else:
                    print("This answer is not valid please answer with yes or no")
