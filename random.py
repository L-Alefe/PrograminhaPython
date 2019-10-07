from random import randint
q = 0
def cod(e):
    rand = randint(1,3)
    if e == 1:
        n = int(input(print("Digite um número: ")))
        if n > rand:
            print("Quase... Digite um menor.")
        elif n < rand:
            print("Quase... Digite um maior.")
        elif n == rand:
            print("Parabéns, você acertou!!!")
        if n != rand:
            cod(1)
        else:
            q = int(input(print("Quer tentar de novo?")))
            if q == 1:
                cod(1)
            else:
                print("Tial tial")
    elif e == 0:
        print('Tiaal')
if q == 1:
    cod(1)
elif q == 0:
    cod(1)
