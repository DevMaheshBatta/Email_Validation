email=input("enter your mail")
if len(email)>=6:
    if email[0].isalpha():
        if("@ "in email) and (email.count("@")==1):
            if(email[-4]=="."):
                for i in email:
                    if i==i.space():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i==" " or i == " " or i=="@":
                        if k==1 or j==1:
                            print( "wrong email 5")
                        else:print("wrong email 4")



                        
                    

        else:
            print("wrong email 3")


        
    else:
        print( "wrong email 2")


else:
    print("wrong email")