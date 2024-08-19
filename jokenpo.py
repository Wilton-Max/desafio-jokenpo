import random

def player_choice():
    choice = input("Escolha: pedra, papel ou tesoura ").lower()
    while choice not in ["pedra", "papel", "tesoura"]:
        choice = input("Invalid choice. pedra, papel, ou tesoura: ").lower()
    return choice

def computer_choice():
    options = ["pedra", "papel", "tesourapa"]
    return random.choice(options)

def winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "pedra" and computer == "tesoura") or (player == "papel" and computer == "pedra") or (player == "tesoura" and computer == "papel"):
        return "player"
    else:
        return "computer"

def play():
    wins = 0
    losses = 0
    ties = 0

    while True:
        player = player_choice()
        computer = computer_choice()

        print(f"Você escolheu: {player}")
        print(f"O computador escolheu: {computer}")

        result = winner(player, computer)

        if result == "tie":
            ties += 1
            print("Empate!")
        elif result == "player":
            wins += 1
            print("Jogador venceu!")
        else:
            losses += 1
            print("computador venceu!")

        play_again = input("Jogar novamente? (y/n): ").lower()
        if play_again == 'n':
            break
    
    print("\nGame Statistics:")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ties: {ties}")

play()