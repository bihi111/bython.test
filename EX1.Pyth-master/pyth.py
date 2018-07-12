import webbrowser
import time
print ("********************************************************************************")
print ("********************************************************************************")
r=3
while r!=1 and r!=2:
    r=eval(input("to continue in english  : press (1) ** ** to continue in french : press (2)\n "))
    if r==1:
        m=str(input("what's your name : \n"))

        a=str(input("how old are you : \n"))

        n=str(input("are you male or female: \n"))

        c=(input( "where are you from \n(Casablanca, Rabat,Marrakech):"))
        print("wait ...")
        if c=="Rabat" or c=="Casablanca" or c=="Marrakech "or c=="rabat" or c=="casablanca" or c=="marrakech":
            time.sleep(5)
            print("*******************************************************************************")
            print("*******************************************************************************")
            print ("             to use docfinder you must follow these steps:")
            print("wait ...")
            time.sleep(4)
            print("first step : ")
            print("     choose your city.")
            time.sleep(4)
            print("second step :")
            print("     choose the nearest clinic.")
            time.sleep(4)
            print("third step :")
            print("     check that the doctor is present.")
            time.sleep(4)
            print("fourth step :")
            print("     chick the number of patients with doctor.")
            time.sleep(4)
            print ("to go directly to DOCFINDER click Entre :")
            webbrowser.open('https://www.google.com')   
        else:
            print("sorry ,docfinder does not support this city :  ",c)
            r!=2
    elif r==2: 
        m=(input(" : quel est votre nom :  \n"))
        a=eval(input("quel âge avez vous : \n"))
        n=(input(":vous êtes un homme ou une femme? \n"))
        c=(input( "où vivez-vous: \n(Casablanca, Rabat,Marrakech):"))
        print("wait ...")    
        c=(input( "où vivez-vous: \n(Casablanca, Rabat,Marrakech):"))
        if c=="Rabat" or c=="Casablanca" or c=="Marrakech" or c=="rabat" or c=="casablanca" or c=="marrakech":
            time.sleep(5)
            print("*******************************************************************************")
            print("*******************************************************************************")
            print ("            Pour utiliser docfinder suivez ces etapes:")
            print("Wait ...")
            time.sleep(4)
            print("la première étape : ")
            print("     choisissez votre ville: .")
            time.sleep(4)
            print("la deuxième étape: ")
            print("    choisissez la clinique la plus proche: .")
            time.sleep(4)
            print("la troisième étape: ")
            print("     vérifier si le docteur est présent. ")
            time.sleep(4)
            print("la quatrième étape: ")
            print("     vérifiez le nombre de patients avec le medecin.")
            time.sleep(4)
            print("pour aller directement à DOCFINDER cliquez  Entre  : ")
            webbrowser.open('https://www.google.com')
        else :
            print ("docfinder n'inclut pas cette ville :  ",c)
            r!=1
    
            
