print("Welcome! \n To your system \n Create your lock- \n Kindly feed the answer:-")
print("What is your Birthday_Date ?")
birthdate=input("Enter: ")
print("What is your Pet Name ?")
pet_name=input("Enter: ")
print("What is your Favourite Color ?")
fav_color=input("Enter: ")
print(" Now, please feed reset system Question-Answer:- ")
user_question=input("Enter Question: ")
user_answer=input("Enter Answer: ")
print("Welcome to your system \n Unlock the system! \n What is your Birthday_Date ? ")
answer=input("Enter: ")

def system_reset():
    #pass
    print("your system being reset!")
    print(user_question)
    system_reset_ans=input("Enter answer: ")
    if system_reset_ans == user_answer:
        #pass
        print("Your system Reset successfull.")
    else:
        #pass
        print("Incorrect reset answer. \n TRY again:-")

if answer == birthdate:
    print(" correct \n opened successfully ")
else:
    print("wrong \n try again:-")
    print("what is your pet name ? ")
    answer2=input("Enter: ")
    if answer2 == pet_name:
        print(" correct \n opened successfully ")
        system_reset()
    else:
        print("wrong \n try again:-")
        print(" what your favourite color ? ")
        answer3=input("enter:")
        if answer3==fav_color:
            print("correct \n opened successfully ")
        else:
            print(" wrong \n welcome to your reset system! ")
            system_reset()

