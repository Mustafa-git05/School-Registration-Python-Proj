import webbrowser as web
import time
import re
price = 20000 #Used for calculating the total price that the person eneds to pay
a = 0 #Variable used later for a while function
#Language Selection
print("Hello and welcome to the American Public School portal!")
time.sleep(0.5) #to make it flow nicer

#Sign up page
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #Email format
print("It seems that you dont have an account. You will be redirected to our sign up page...")
time.sleep(1)
email=str(input("Please enter your Email: "))

#Email checker
while True:
    if (re.search(regex,email)): #Checks if the email fits the format
        print("Your Email is valid!")
        break
    else:
        print("Email invalid, please re-enter your Email")
        time.sleep(2)
        email=str(input("Please enter your Email: "))
       
       
#Password checker
password=str(input("Please enter your password: "))
confirm=input("Please confirm your password: ")
while True:
    if password==confirm and len(password)>=8:
        print("Your password matches and it is valid!")
        break
    else:
        print("Your password either doesn't match or is less than 8 characters. Please re enter it..")
        time.sleep(2)
        password=input("Please enter your password: ")
        confirm=input("Please confirm your password:")
       
#Login page
print("you have finished the sign up process. Please login to your account")
time.sleep(1)
emailLogin=input("Email: ")
passwordLogin=input("Password: ")
while True:
    if emailLogin==email and passwordLogin==password:
        print("You have logged into your account!")
        break
    elif emailLogin!=email:
        print("This Email is not found in our database. Please re-enter your email")
        emailLogin=input("Email: ")
     
       
    elif passwordLogin!=password:
        print("This password does not match your previous entry. Please re-enter it")
        passwordLogin=input("Password: ")
#Asking the parents how they would like to proceed
time.sleep(3)


b = 1 #used to break the loop later
while b == 1:
    
    Selections = int(input("""How may we help you today?
1. I would like to register my kid into your school.
2. I would like to learn more about your school.
3. I would like to be redirected to your FAQ page.
"""))


   
    #Prints out a brief description about the school
    if Selections == 2:
        time.sleep(1)
        print("Welcome to American Public School, where we are dedicated to providing a nurturing and inclusive educational environment for your child's growth and development. As a government-funded institution, our school prioritizes excellence in education from kindergarten through 12th grade. Our experienced and passionate educators are committed to fostering a love for learning and helping students achieve their fullest potential.")
        time.sleep(4)
        print("At American Public School, we offer a well-rounded curriculum encompassing core subjects such as English, math, science, and social studies, as well as a variety of extracurricular activities to enhance your child's overall experience. Our school is open to all students residing in the designated district, promoting diversity and a sense of community.")
        time.sleep(4)
        print("We pride ourselves on creating a safe and supportive atmosphere where each child is encouraged to explore their interests, develop critical thinking skills, and build lasting friendships. Our commitment extends beyond academics to instill values such as respect, responsibility, and resilience.")
        time.sleep(4)
        print("As partners in your child's education, we value open communication and collaboration with parents. Together, we strive to create an enriching learning journey that prepares students for future academic success and personal growth. Join us at American Public School, where we believe in nurturing not only bright minds but also compassionate hearts.")
        time.sleep(2)
        Mselection = input("Do you require any other services? Please reply with y or n: ") 
        if Mselection == "y":
            print("Splendid! ")
            time.sleep(1)
        elif Mselection == "n":
            print("No problem. Have a wonderful day and we hope to see you in our school one day!")
            break
        else:
            print("Invalid response. The conversation will continue!")
    
    #Redirects the user to an FAQ page (currently dead link will fix soon)
    elif Selections == 3:
        print("You will be automatically redirected to the FAQ page, please wait...")
        time.sleep(2)
        web.open("http://213.42.28.183:9040/DISGAR/index.php/information")
    
    #the registration
    elif Selections == 1:
        while a == 0: #start from here
            print("Please not that each grades' tution fee is 10k Dollars, and it should be paid at school")
            name=input("Please enter your childs name: ")
            gender=input("Please enter your childs gender: ")
    
    #gender sec
            while True:
                if gender.lower()=="male" or gender.lower()=="female":
                    age=int(input("Please enter your childs age: "))
                    break
           
                else:
                    print("That is not a valid gender, please try again")
                    gender=input("Please enter your childs gender: ")
    
    #end of gender sec
    
    
    #age sec
            while True:    
                if age>=19:
                    print("Please enter an age less than 19")
                    age=int(input("Please enter your childs age: "))
       
       
                elif age<19:
                    grade=int(input("what grade would you like to register your child in? (please not that kindegarten registrations are not avalible.)"))
                break


    #end of age sec
    
    
    #grade sec
            while True:
       
    #grade1 sec
                if grade ==1:
                    print("welcome to grade 1 registration! Please complete the following steps:")
                    print("There are no electives to choose from for this year. Please enter your child's ID so he can be registred to this grade.")
                    break
    #end of grade1 sec
       
    #grade2 sec
                elif grade ==2:
                    print("welcome to grade 2 registration! Please complete the following steps:")
                    print("There are no electives to choose from for this year. Please enter your childs ID so he can be registred to this grade.")
                    break
    #end of grade2 sec
       
    #grade3 sec
                elif grade ==3:
                    print("welcome to grade 3 registration! Please complete the following steps:")
                    print("There are no electives to choose from for this year. Please enter your childs ID so he can be registred to this grade.")
                    break
    #end of grade3 sec
       
    #grade4 sec
                elif grade ==4:
                    print("welcome to grade 4 registration! Please complete the following steps:")
                    print("There are no electives to choose from for this year. Please enter your childs ID so he can be registred to this grade.")
                    break
    #end of grade4 sec
    
    #grade5 sec
                elif grade ==5:
                    print("welcome to grade 5 registration! Please complete the following steps:")
                    print("There are no electives to choose from for this year. Please enter your childs ID so he can be registred to this grade.")
                    break
     #end of grade5 sec  
       
    #grade6 sec
                elif grade ==6:
                    print("welcome to grade 6 registration! Please complete the following steps:")
                    print("There are no electives to choose from for this year. Please enter your childs ID so he can be registred to this grade.")
                    break
    # end of grade6 sec
    
    # grade7 sec
                elif grade ==7:
                    print("welcome to grade 7 registration! Please complete the following steps:")
                    print("There are no electives to choose from for this year. Please enter your childs ID so he can be registred to this grade.")
                    break
    # end of grade7 sec
    
    #grade8 sec
                elif grade ==8:
                    print("welcome to grade 8 registration! Please complete the following steps:")
                    print("There are no electives to choose from for this year. Please enter your childs ID so he can be registred to this grade.")
                    break
    # end of grade8 sec
    
    # grade9 sec
                elif grade ==9:
                    print("welcome to grade 9 registration! Please complete the following steps:")
           
            #electives sec
                    electives = int(input("""please pick one out of the three electives for your child:
            1) Nutrition
            2)Art
            3)Marketing
            """))
                    while True:
                        if electives ==1:
                            e="Nutrition"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==2:
                            e="Art"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==3:
                            e="Marketing"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        else:
                            print("No such elective exsists")
                            electives = int(input("""please pick one out of the three electives for your child:
            1)Nutrition
            2)Art
            3)Marketing
            """))
            #end of electives sec
                    break
    # end of grade9 sec
    
       
       
    # grade10 sec
                elif grade ==10:
                    print("welcome to grade 10 registration! Please complete the following steps:")
             #electives sec
                    electives = int(input("""please pick one out of the three electives for your child:
            1) Physics
            2)Photoshop
            3)Python
            """))
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
                            e="Python"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        else:
                            print("No such elective exsists")
                            electives = int(input("""please pick one out of the three electives for your child:
            1)Physics
            2)Photoshop
            3)Python
            """))            
            #end of electives sec
                    break
    # end of grade10 sec
     
       
       
    #grade11 sec
                elif grade ==11:
                    print("welcome to grade 11 registration! Please complete the following steps:")
            #electives sec
                    electives = int(input("""please pick one out of the three electives for your child:
            1)Organic Chemistry
            2)Electrical Physics
            3)Python 2
            """))
                    while True:
                        if electives ==1:
                            e="Organ Chemistry"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==2:
                            e="Electrical Physics"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==3:
                            e="Python 2"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        else:
                            print("No such elective exsists")
                            electives = int(input("""please pick one out of the three electives for your child:
            1)Organic Chemistry
            2)Electrical Physics
            3)Python 2
            """))
    #end of electives sec
                    break
    # end of grade11 sec
       
       
       
       
                elif grade ==12:
                    print("welcome to grade 12 registration please complete the following steps:")
            #electives sec
                    electives = int(input("""please pick one out of the three electives for your child:
            1)Arabian History
            2) Game Design
            3)Advanced Calculus
            """))
                    electives=int(input("Please pick an elective:"))
                    while True:
                        if electives ==1:
                            e="Arabian History"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==2:
                            e="Game Design"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        elif electives==3:
                            e="Advanced Calculus"
                            print("you have succesfully registered your child in",e,"class")
                            break
                        else:
                            print("No such elective exsists")
                            electives = int(input("""please pick one out of the three electives for your child:
            1)Arabian History
            2) Game Design
            3)Advanced Calculus
            """))
            #end of electives sec
                    break
       
                else:
                    print("That grade does not exist. Please try again")
                    grade=int(input("What grade would you like to register your child in? (please not that kindegarten registrations are not avalible.)"))
    
    #end of grade sec
    
    
    #emirates id sec:
            ID=int(input("please give us all 15 integers of your childs ID:"))
    
            while True:
                strem=str(ID)
                if len(strem)==15:
                    print("Thank you! Your childs ID has been put into the system")
                    break
                else:
                    print("that is not a valid emirates ID number!")
                    ID=int(input("please give us all 15 intgers in your childs emirates ID without the dashes:"))
            print("your",age,"year old",gender,"child, "+name+",with emirates id number",ID,"has succesfuly been registred in grade",grade,". We are excited to welcome him!")
            while True:
                anotherchild=input("Would you like to register another child ")
                if anotherchild.lower()=="yes":
                    print("You will need to refill all the previous forms but for the new child")
                    print("The price you have to pay until now is",price)
                    price +=20000
                    break
                elif anotherchild.lower()=="no":
                    print("You have finished the process, and the price you will have to pay is",price,"dollars")
                    print("Thank you for enrolling your child in our school. Have a great day!")
                    a=1
                    b+=1
                    break
                else:
                    print("This answer is not valid please answer with yes or no")
