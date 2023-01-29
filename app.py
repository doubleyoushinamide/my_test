name = str(input('Kindly input your name: ').upper())
user = int(input("Kindly input your age: "))

if user < 30:
    print(f"Dear {name} you are qualified to register")
else:
    print(f"Dear {name} you are not qualified. You are too old for this")