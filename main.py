import emojiswahili

print(emojiswahili.emojize('Mshindi wakwanza anapata :nishani_ya_dhababu:'))
height = float(input('Informe a Sua Altura: '))
weight = float(input('Informe o seu peso: '))

def imc():
    high = height**2
    calcimc = weight / high

    if calcimc < 18.5:
        print(f'O seu indice de massa corporal e {calcimc}, você esta abaixo do peso')
    elif calcimc < 24.9:
        print(f'O seu indice de massa corporal e {calcimc}, você esta saudavel')
    elif calcimc < 34.9:
         print(f'O seu indice de massa corporal e {calcimc}, você esta com obesidade de grau 1')
    elif calcimc < 39.9:
         print(f'O seu indice de massa corporal e {calcimc}, você esta com obesidade de grau 2')
    elif calcimc > 40:
        print(f'O seu indice de massa corporal e {calcimc}, você esta com obesidade de grau 3')

imc()
