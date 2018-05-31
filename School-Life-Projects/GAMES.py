print"(A_N_S_H_)**0.5 software technologies*tm PRESENTS:"
print"_________________________________________________GAME ZONE!!_______________________________________________________"
print"GAME 1... GUESS MY WORD....."
print"it is a fun small miny 10 Question game using some nested loops and other programming methods..."
print "user will see a word with blank spaces and has to complete the blank spaces and answer back"
print"_____________________________________________________________________________________________"
#############function#######

def game(z):
    
    a={'P_ _ _ _ _':'PYTHON','L _ _ _':'LOVE','CHEM_ _ _ _ _\n<the most irritating subject>\n':'CHEMISTRY'}
    #fill the divt
    S=0
    print"IMPORTENT:ANSWER IN CAPITAL LETTERS ONLY..."
    k=1
    for i in a:
        print k,
        print i
        k=k+1
        b=raw_input("ans.:")
        if b==a[i]:
            print "correct answer. YOU GET +50 POINTS.."
            S=S+50
            print
            
        else:
            S=S-20
            print"wrong answer","correct answer is..-->",a[i],"<--, YOU GET -20 POINTS.."
            print
    print "your total=",S
    print
    print
    print
    print"acc. to prograam,you are:"
    print"THE BEST------------------------------------500 PTS."
    print"MASTER--------------------------------------450-499PTS."
    print"JUST THERE----------------------------------400-449PTS."
    print"YET TO GROW HARD ,BABY!---------------------300-399PTS."
    print"ANOTHER PERSON WITH A COMMON IQ-------------200-299PTS."
    print"TU BOHOT BADA IDIOT HAI---------------------100-199PTS."
    print"MORE LIKELY TO GO BACK,CRYING BABY CHILD!---000-99PTS."
    print
    print

    print":. you are:",
    if S>=450 and S<=499:
        print"MASTER"
    elif S==500:
        print "THE BEST,just like me ;p"
    elif S>=400 and S<=449:
        print"JUST THERE"
    elif S>=300 and S<=399:
        print"YET TO GROW HARD ,BABY!"
    elif S>=200 and S<=299:
        print"ANOTHER PERSON WITH A COMMON IQ"
    elif S>=100 and S<=199:
        print"TU BOHOT BADA IDIOT HAI"
    else:
        print"MORE LIKELY TO GO BACK,CRYING BABY CHILD!"
###########function over########



print"press 1 to play the game"
print"press 2 to read instructions"
print"press 3 to exit the game"
z=input("enter your choice:")
if z==2:
    print"you will see a word in front of your screen with blankspaces in between..and a hint in'<>'.\n you just have to think, and answer back the correct and most appropiate answer...\n if your guess is correct you will get +50 pts and if your guess is wrong you will loose -20 pts \n at the end of 10 question game,\n you will get a spetial rank on the bases of your scores"
    print
    y=input("enter 1 to start playing else anything to exit:")
    if y==1:
        game(z)
    else:
        print
elif z==1:
    game(z)
else:
    print









