# Cálculo de IMC (Índice de Massa Corporal) Em Python

### Este é um script em Python para calcular o Índice de Massa Corporal (IMC), com base na altura e peso informados pelo usuário. O IMC é uma medida usada para avaliar se uma pessoa tem um peso saudável de acordo com a sua altura.

![code](https://github.com/user-attachments/assets/69cf7510-f2ce-447f-95b5-1d21e0a3c43e)


### Funcionalidade
O código faz o seguinte:

Entrada de Dados: O usuário é solicitado a informar sua altura (em metros) e peso (em quilogramas).

Cálculo do IMC: O cálculo do IMC é feito utilizando a fórmula:

𝐼𝑀𝐶 = peso(kg)/ altura(m2)
​
 
### Classificação do IMC: Após calcular o IMC, o programa classifica o valor conforme as faixas estabelecidas pela Organização Mundial da Saúde (OMS):

Abaixo de 18.5: Abaixo do peso
18.5 a 24.9: Peso saudável
25 a 29.9: Sobrepeso
30 a 34.9: Obesidade grau 1
35 a 39.9: Obesidade grau 2
Acima de 40: Obesidade grau 3

### Emojis: Dependendo do resultado do IMC, o programa exibe um emoji correspondente ao estado de saúde da pessoa:

Emoji 😢 para indicar um estado de saúde mais preocupante (abaixo do peso, obesidade)
Emoji 😄 para indicar um estado saudável
Código
python
Copiar
Editar
import emojis

# Entrada de dados do usuário
height = float(input('Informe a Sua Altura: '))
weight = float(input('Informe o seu peso: '))

def imc():
    high = height**2
    calcimc = weight / high

    if calcimc < 18.5:
        print(f'O seu indice de massa corporal e {calcimc:.2f}, você está abaixo do peso', emojis.encode(':cry:'))
    elif calcimc < 24.9:
        print(f'O seu indice de massa corporal e {calcimc:.2f}, você está saudável', emojis.encode(':smile:'))
    elif calcimc < 34.9:
         print(f'O seu indice de massa corporal e {calcimc:.2f}, você está com obesidade de grau 1', emojis.encode(':cry:'))
    elif calcimc < 39.9:
         print(f'O seu indice de massa corporal e {calcimc:.2f}, você está com obesidade de grau 2', emojis.encode(':cry:'))
    elif calcimc > 40:
        print(f'O seu indice de massa corporal e {calcimc:.2f}, você está com obesidade de grau 3', emojis.encode(':cry:'))

### Executa o cálculo do IMC
imc()

Como Usar
Clone ou baixe o repositório.
Abra o script Python no seu ambiente de desenvolvimento.
Execute o script.
Informe a sua altura e peso quando solicitado.
O resultado será mostrado na tela, juntamente com a classificação e o emoji correspondente ao seu IMC.
