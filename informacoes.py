def maior(e):
    if e >= 18:
        return True
    else:
        return False
idade = int(input('Digite sua idade: '))
if (maior(idade)):
    print('Você já é de maior!')
else:
    print('Você ainda é de menor!')
