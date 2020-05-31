print"\t\t\t\t\tCRICKET GAMBLER"
print'\t\t###################BE A MAN IF YOU CAN!GET more than10 CRORE$ IN THE GAME#####################'
print'\t\t\t\tbet more everytime you win,dude!'

def match_over():
    print"\n\n\n\n\n\n"
    print"\t|-----------------------------------------------------------------------------------------------|"
    print"\t|=================================GAME...OVER===================================================|"
    print"\t|--------------------------------thanks for playing---------------------------------------------|"
    print"\t|----------------------come next tym and play care fully----------------------------------------|"
    print"\t|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|"
    print"\n\n\n\n\n\n"
###################################
def set(c):
    import os
    p="color %s"%c
    color=p
    os.system(p)
set('ec')
def skoreboard():
    if b==1:
        print" |"
        print"\t|"
        print"\t|",
        print
    elif b==2:
        print" |----"
        print"\t _ _ |"
        print"\t/_ _ _ _",
        print
    elif b==3:
        print" ---|"
        print"\t---|"
        print"\t---|",
        print
    elif b==4:
        print" |   |"
        print"\t|---|"
        print"\t    |",
        print
    elif b==5:
        print" |```"
        print"\t|----|"
        print"\t_ _ _|",
        print
    elif b==6:
        print" |~~~~~"
        print"\t|"
        print"\t|~~~~~~|"
        print"\t|_ _ _ |",
        print
    else:
        print" \        /"
        print"\t \  /\  /"
        print"\t  \/  \/",
        print
################################################################





pl=0
for p in range(100):
    import random
    a=raw_input('press enter:')
    pl=pl+10000
    print"*_* : you have got ",pl,"$ to play wid"
    print"india will play a match of 20 overs"
    n=input("enter how many overs you want to play?(1-10):")
    runs=[1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,6,3,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,'W','W','W','W','W','W','W','W','W','W']
    sk=0
    tw=0
    for i in range(1,n+1,1):
        print"OVER--",i
        r=0
        w=0
        b=0
        print"*_* : ","\t",
        bet_r=input("~~~~~~~~~HOW MUCH WILL INDIA SCORE IN THIS OVER??:")
        bet_ra=input("                                       BET on it:$")
        for j in range(1,7):
            print"BALL",j,
            b=random.choice(runs)
            skoreboard()
            print
            a=raw_input(":"),
            if b=='W':
                runs.remove('W')
                w=w+1
            else:
                r=r+b
                runs.remove(b)
        print"this over:",r,"wickets:",w
        sk=sk+r
        tw=tw+w
   
        print"*_*"
        print"|`BETZONE````````````````````````````````````````````````````````````````````|"
        print"|  *_* :you thought that india will score",bet_r,"runs in this over               |"
        print"|     &you betted:$",bet_ra,"-on it.                                             |"
        print"| RESULT~~~                                                               |"
        if bet_r >=r-4 and bet_r<=r+4:
            print"|*_* :you won!                                                        |"
            print"|   :your guess is in between the min range of actual runs,i.e",r-4,"-",r+4,"|"
            pl=pl+(2*bet_ra)
            print"|   :you get $",(2*bet_ra),"--double than you bet"
            print"|   :amount left wid you:",pl
        else:
            print"|*_* :you lost!                                                       |"
            print"|   :your guess is in NOT IN  the min range of actual runs,i.e",r-4,"-",r+4,"|"
            pl=pl-bet_ra
            print"|   :you get -$",(bet_ra)
        print"|   :amount left wid you:",pl
        print"|____________________________________________________________________________|"
        print
        if pl<-5000:
            print"SORRY,YOU CANNOT PLAY MORE,YOU ARE NOW IN HEAVY DEPT.YOU CAN ONLY HAVE MIN OF -5000$"
            match_over()
            break
        print "\t~total-score:",sk,"/",tw,"~"
    
        print"####################################OVER ENDS################################################"
    
    print"============================================ innings over========================================"
    print "=========================================== innings over==========================="
    print"============================================ innings over========================================"
    print"============================================ inningd over========================================"
    dec=['won','lost']
    z=random.choice(dec)
    print"you know what?INDIA",z,"THE MATCH!!!"
    print"India's SCORE:",sk+150,"/",tw
    print"after 20 overs:"
    if z=='won':
        print "PAKISTANS' SCORE:",sk+72,"/10"
    else:
        print "PAKISTANS' SCORE:",sk+156,"/4"
    print"**********************************************match OVER*****************************************"
    print 
    q=raw_input("enter 1 to play again:")
    if q=='1':
        pass
    
    else:
        match_over()
        
        break
