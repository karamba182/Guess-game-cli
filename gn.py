import random

def guess_number():
    """ Пишемо умови гри """
    print("Привіт, це CLI гра Угадай число за 7 спроб!")

    """ Генераці випадкогого часла за допомогою радом рандінт """
    number = random.randint(1, 100)
    attempts = 0
    """ максимальна кількість спроб """
    max_attempts = 7
    
    """ ЦЦИКЛ""" 
    while attempts < max_attempts:
        try:
            """ Запитання юзера числа """
            guess = int(input(f"Введіть число від 1 до 100, спроба {attempts + 1} з {max_attempts}: "))
            """ перевірка на правильність """
            attempts += 1
            """ перевірка по діапазону """
            if guess < number:
                print("не-а, мало!")
            elif guess > number:
                print("Ні, Забагато!")
            else:
                print(f"Ну от, вітаю, ти справився за  {attempts} спроб")
                break
        except ValueError:
            print("Введіть вірне число.")

    else:
        print(f"Соррі, ти використав всі {max_attempts} Спроб. У число було  - {number}.")

if __name__ == "__main__":
    guess_number()