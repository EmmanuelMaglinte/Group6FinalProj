import random

symbols = ["🍒", "🍋", "🔔", "⭐", "💎"]
chances = [41, 21, 19, 12, 7]
symbols_values = [20, 30, 40, 50, 100]
balance = 500

# Generate random results
def slot_machine():
    reel = ""
    for x in range(3):
        symbol = random.choices(symbols, chances)[0]
        reel += symbol
    return reel

print()
print("\t\tWelcome!! \nSpin cost will be 50 Pesos for every spin\n")
print(f"Your Balance: {balance} ")

while True:
    user = input("Do you want to spin (Yes/No): ").strip().lower()
    if user == "yes":
        if balance < 50:
            print("Insufficient money to spin! \U0001F4B8")
            
            while True:
                money = input("Do you want to deposit (Yes/No): ").strip().lower()
                if money == "yes":
                    deposit = input("How much will you deposit: ")
                    if deposit.isdigit():
                        balance += int(deposit)
                        break
                    else:
                        print("Please enter a valid number. \U0001F4A1")
                elif money == "no":
                    print("Goodbye! Thanks for playing~ \U0001F44B")
                    break  
                else:
                    print("Yes or No ONLY \U0001F6D1")
            if money == "no":
                break
        else:
            balance -= 50
            result = slot_machine() 
            print(f"\n🎰 | {result} | 🎰")
            
           

            if len(set(result)) == 1:
                symbol_index = symbols.index(result[0]) 
                winnings = symbols_values[symbol_index] * 3
                print(f"\n\U0001F48E Congratulations, You hit the JACKPOT!! You won {winnings} pesos! Incredible! \U0001F48E")
            elif len(set(result)) == 2:
                matched_symbol = max(set(result), key=result.count)
                symbol_index = symbols.index(matched_symbol)
                winnings = symbols_values[symbol_index] * 2
                wmsg = [
                f"\U0001F389 Lucky spin! You won {winnings} pesos! \U0001F389",
                f"\n\U00002728 Nice! You won {winnings} pesos! Keep it up! \U00002728",
                f"\n\U0001F31F Great! You won {winnings} pesos! You're on a roll! \U0001F31F",
                f"\n\U0001F48E Amazing! You won {winnings} pesos! Keep it up! \U0001F48E"
            ]
                print(random.choice(wmsg))    
            else:
                winnings = 0
                lmsg = [
                        "\nBetter luck next time! \U0001F91E",
                        "\nToo bad! Spin again! \U0001F61E",
                        "\nOops, so close! Try again! \U0001F62C",
                        "\nNot this time! But don't give up! \U0001F4AA",
                        "\nMaybe next spin will be the lucky one. \U0001F340"
                    ]

                print(random.choice(lmsg))
            balance += winnings 
            print(f"\nBalance: {balance} \U0001F4B0\n")

    elif user == "no":
        print(f"Here is your final balance!: {balance}")
        print("Goodbye! Thanks for playing~ \U0001F44B")
        break

    else:
        print("Yes or No ONLY \U0001F6D1\n")