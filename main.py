from random import randint


Turn = 1
Score = 0
defeat = 0

for i in range(5):
    print
    print
    player = input("Rock(r), Paper(p), Scissor(s): ")
    print('  ' + player,'vs ' ,end = '')

    computer = randint(1,3)
    if computer == 1:
        computer = 'r'

    elif computer == 2:
        computer = 'p'

    elif computer == 3:
        computer = 's'

    print(computer)

    if player == computer:
        print("Match draw!!!")

    elif player == 'r' and computer == 'p':
        print("Computer wins!!")
        defeat += 1

    elif player == 'p' and computer == 's':
        print("Computer wins!!")
        defeat += 1

    elif player == 'r' and computer == 's':
        print("  You win!!")
        Score += 1

    elif player == 'p' and computer == 'r':
        print("  You win!!")
        Score += 1

    elif player == 's' and computer == 'r':
        print("  Computer wins!!")
        defeat += 1

    elif player == 's' and computer == 'p':
        print("  You win!!")
        Score += 1
    Turn += 1

print("Total score: " + str(Score))
print("Total defeat: " + str(defeat))
if Score > defeat:
    print("You won the Match!!!")

elif Score < defeat:
    print("Computer won the Match!!!")

else:
    print("Match is Draw!!!")
