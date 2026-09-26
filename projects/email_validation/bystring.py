print("******EMAIL VALIDATION PROGRAM******")
user_email = input("Enter your email:- ")
#Condition checking
#first condition for checking the minimum length of email --> a@a.pk
if len(user_email) >= 6:
    pass
    if user_email[-3] == "." or user_email[-4] == ".":
        if "@" in user_email and user_email.count("@") == 1:
            if (user_email[0].isalpha() and user_email.islower()) or user_email.isalnum():
                if " " not in user_email and "_" not in user_email:
                    print("Valid email!")
                else:
                    print("space and symbol error!")
            else:
                print("Alphabetical error!Email is not valid!")
        else:
            print("NOT A VALID EMAIL!")
    else:
        print("Email domain is not valid!")
else:
    print("EMAIL IS NOT VALID!")