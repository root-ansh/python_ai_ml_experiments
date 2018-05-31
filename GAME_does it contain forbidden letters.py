import time
fl=['d','u','s','t','y','w','i','n','e',' ']
print"you have to enter a 6 different letters word.... i have got some letters...your word should not have those letters..you only have got 6 chances..if u make a word u win!"
for i in range(10000):
    p=raw_input("press enter to play")
    print">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    for i in range (6):
        guess=raw_input("enter your word:")
        if len(guess)<> 6:
            print "enter a valid word"
        else:
            cguess=''
            c=0
            for i in guess:
                if i not in fl:
                    cguess=cguess+i
                elif i in fl:
                    c=c+1
            if cguess==guess:
                print"hurray!! you won the game"
                time.sleep(1)
                break
        
            else:
                print"sorry your word still has",c,"forbidden letters"
    
        if i==5:
            print" sorry,game over..you lose"
    
