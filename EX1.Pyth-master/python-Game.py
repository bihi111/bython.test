def f():
    i=1
    while i<=3:
        x=eval(input("take a guess :"))
        if x==4:
            print ("great ,you won  1.000.000 $ ")
            break
        if x!=4:
            r=3-i
            if r!=0:
                print ("you have ",r,"chance")
            elif r==0:
                print("game over")
                break
            i+=1
