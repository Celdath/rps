import random
keep_going = 'y'
computer_score = 0
your_score = 0

while keep_going == 'y':
    choice = int(input('Type 0 for rock, 1 for paper, and 2 for scissors: '))
    comp_choice = random.randint(0, 2)
    if choice == 0 and comp_choice == 0:
        print('\nYou both chose rock and it is a tie!')
        computer_score += 1
        your_score += 1
    elif choice == 0 and comp_choice == 1:
        print('\nYou chose rock and they chose paper, you lose!')
        computer_score += 1
    elif choice == 0 and comp_choice == 2:
        print('\nYou chose rock and they chose scissors, you win!')
        your_score += 1
    elif choice == 1 and comp_choice == 0:
        print('\nYou chose paper and they chose rock, you win!')
        your_score += 1
    elif choice == 1 and comp_choice == 1:
        print('\nYou both chose paper and it is a tie!')
        computer_score += 1
        your_score += 1
    elif choice == 1 and comp_choice == 2:
        print('\nYou chose paper and they chose scissors, you lose!')
        computer_score += 1
    elif choice == 2 and comp_choice == 0:
        print('\nYou chose scissors and they chose rock, you lose!')
        computer_score += 1
    elif choice == 2 and comp_choice == 1:
        print('\nYou chose scissors and they chose paper, you win!')
        your_score += 1
    elif choice == 2 and comp_choice == 2:
        print('\nYou both chose scissors and it is a tie!')
        computer_score += 1
        your_score += 1
    elif choice >= 3 or choice >= -1:
        print('\nYour choice must be 0 for rock, 1 for paper, and 2 for scissors.')

    print('\nYour score is:', '(', your_score, '-', computer_score, ')')

