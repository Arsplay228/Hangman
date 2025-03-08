import os

clear = lambda: os.system("cls")

print("Привет! Я загадал слово, твоя задача - угадать его по буквам.")
input("*Нажми Enter, чтобы продолжить*")
clear()
print("Поехали!")

word = "квокка"

letters = []

isWin = True
hp = 10

while hp > 0:
    isWin = True
    letter = input("Введите букву: ").lower()
    letters.append(letter)
    print(letters)
    for symb in word:
        if symb in letters:
            print(symb, end = " ")
        else:
            print("*", end=" ")
            isWin = False
    print()

    if isWin:
        print("Ты угадал!Молодец!")
        break

    if letter not in word:
        hp -= 1
        print(f"Осталось попыток: {hp}")


