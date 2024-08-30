print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
print("\t\t\t*************Tressure Game*************\n\n\n")
print("Instructions :\n")
print("\t*You have to choose from options provided.\n")

task1 = input("There are 2 paths.\nWhich one will you choose\nRight - R\nLeft - L\n")

if task1 == 'r' or task1 == 'R':
    print("You choose the wrong way.\nGame Over!")
    
elif task1 == 'l' or task1=='L':
    task2 = input("Now comes a river. Will you wait or be brave enough to swim?\nWait - W\nSwim - S\n")
    
    if task2 == 's' or task2 == 'S':
        print("There was an alligator in the river which ate you.\nGame over!")
    elif task2 == 'w' or task2 == 'W':
        print("You waited enough a boat man came and you crossed the river.")
        
        task3 = input("There are 3 doors in the palace.\nWhich door will you choose\nRed-R\nGreen-G\nBlack-B\n")
        if task3 == 'R' or task3 == 'r' or task3 == 'g' or task3 == 'G':
            print("Wrong Door!\nGame Over\n")
        elif task3 == 'b' or task3 == 'B':
            print("Congratulations You Won The Game!!!!!")
        else:
            print("Choose the correct option!\nGame over!")    
    else:
        print("Choose the correct option!\nGame over!")
else:
        print("Choose the correct option!\nGame over!")