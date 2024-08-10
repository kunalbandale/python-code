while True:
    user_input = int(input("Enter a value between 1 to 10: "))
    if 1 <= user_input <= 10:
        print(user_input, "Thanks")
        break
    else:
        print("Invalid Number")
