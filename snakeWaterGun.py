import random
choice=['snake','water','gun']

player1=random.choice(choice)
player2=input("enter your choice\n")


if(player2!='snake' and player2!='water' and player2!='gun'):
    print('You gave invalid input')

elif(player1==player2):
    print("choice of computer was:",player1)
    print("draw")
else:
    if(player1=='snake'):
        if(player2=='gun'):
            print("choice of computer was:",player1)
            print("you win")
        else:  
            print("choice of computer was:",player1)  
            print("you lose")
    elif(player1=="water"):
        if(player2=='snake'):
            print("choice of computer was:",player1)
            print("you win")
        else:
            print("choice of computer was:",player1)    
            print("you lose")
    else:
        if(player2=='water'):
            print("choice of computer was:",player1)
            print("you win")
        else:    
            print("choice of computer was:",player1)
            print("you lose")               
