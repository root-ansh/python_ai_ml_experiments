pa=10000                                                                
ca=10000                                                               
#deck shuffling_________________________________________________________________________________________________________
print "11=j,12=q,13=k,14=A"
import random
cards=[2,3,4,5,6,7,8,9,10,11,12,13,14, 2,3,4,5,6,7,8,9,10,11,12,13,14, 2,3,4,5,6,7,8,9,10,11,12,13,14, 2,3,4,5,6,7,8,9,10,11,12,13,14,]
random.shuffle(cards)
pc=[]                                                               
for i in range(1,6,2):
    pc.append(cards[i])
print"                                                    YOUR CARDS:[],[],[]"
print"....."
cc=[]                                                               
for i in range(31,38,3):
    cc.append(cards[i])

print"                                                   computer CARDS:[],[],[]"
print"....................."

#betting loop
print"hey, gambler! you have $",pa," t0 play with"
print"myself computer! i have $",ca," t0 play with"
print"_______________________________________________________________________________"
pa=10000                                                                
ca=10000                                                                
boot=0
for i in range(10000):
    print"HAND ",i+1
    k=input("enter some amount to bet;or enter 0 to stop betting and show cards:$")
    if k>0:
        if pa-k<0 or ca-k<0:
            print" you or computer don't have sufficient amount to play that hand..opening card without adding last bet"
            break
        print"(- you betted:",k,"\n,value left with you:",pa,'-',k,'=',pa-k,")\n"
        print"(- computer betted:",k,"\n,value left with pc:",ca,'-',k,'=',ca-k,")\n\n"
        print
        print"-bot value=initial bot+ your BET + P.C. BET=",boot,"+",k,"+",k,"=",boot+(2*k)
        print"______________________________________________________________________/`"
        print
        print
        pa=pa-k
        ca=ca-k
        boot= boot+(2*k)
        
    else:
        break
print"*************************************************"


print "total boot=",boot
print"your amount left=",pa
print"computer amount left=",ca
print"***************"
print
#betting loop over
print"                                                         your cards:",pc
print"                                                     computer cards:",cc
print
print
print"******************************************************"
#checking conditions acc to priority
for i in range(1):
    if pc[0]==pc[1] and pc[1]==pc[2] and cc[0]==cc[1] and cc[1]==cc[2]:
        print"palyer has a trail"
        print "computer has a trail"
        if pc[0]>cc[0]:
            print"CONGRATS!! YOU HAVE WON YOUR NEW AMOUNT=amount left+boot:",pa,"+",boot,"=",pa+boot
            pan=pa+boot    
            pa=pan          #putting players new amount in old variable for loop transversal
            can=ca          #computers new amount
            ca=can          #putting computers new amount i old variable for loop transversal
            break
        else:
            print"Computer HAVE WON. computer's NEW AMOUNT=amount left+boot:",ca,"+",boot,"=",ca+boot
            pan=pa          #players new amount
            pa=pan          #putting players new amount in old variable for loop transversal
            can=ca+boot     #computers new amount
            ca=can          #putting computers new amount i old variable for loop transversal
            break
    elif pc[0]==pc[1] and pc[1]==pc[2]:
        
        print"palyer has a trail"
        print":. by trail rule,CONGRATS!! YOU HAVE WON YOUR NEW AMOUNT=amount left+boot:",pa,"+",boot,"=",pa+boot,"$"
        pan=pa+boot     
        pa=pan         
        can=ca          
        ca=can         
        break
    elif cc[0]==cc[1] and cc[1]==cc[2]:
        print"computer has a trail"
        print":. by trail rule,Computer HAVE WON. computer's NEW AMOUNT=amount left+boot:",ca,"+",boot,"=",ca+boot
        pan=pa          
        pa=pan          
        can=ca+boot     
        ca=can          
        break
    elif (pc[0]+pc[1]+pc[2])>(cc[0]+cc[1]+cc[2]):
        print"palyer has a higher sum total"
        print":. by sum rule,CONGRATS!! YOU HAVE WON YOUR NEW AMOUNT=amount left+boot:",pa,"+",boot,"=",pa+boot
        pan=pa+boot     
        pa=pan         
        can=ca          
        ca=can
        break
        
        
    elif (pc[0]+pc[1]+pc[2])<(cc[0]+cc[1]+cc[2]):
        print"palyer has a higher sum total"
        print":. by sum rule,COMputer  HAVE WON. computer's NEW AMOUNT=amount left+boot:",ca,"+",boot,"=",ca+boot
        pan=pa+boot     
        pa=pan         
        can=ca          
        ca=can
        break
        
    elif (pc[0]+pc[1]+pc[2])==(cc[0]+cc[1]+cc[2]):
        print" both player and computer have the same sum total. :.boot will be distributed half- half"
        print"your new amount:amount left+boot=",pa,"+",boot/2,"=",pa+(boot/2)
        print"computers' new amount:amount left+boot=",ca,"+",boot/2,"=",ca+(boot/2)
        pan=pa+(boot/2)
        pa=pan
        can=ca+(boot/2)
        ca=can
        break

print"             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"


#####################
        
        
