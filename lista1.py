import math

# Lista de Exercícios - 1 

# 1 --------------------------------------
print("\n1 - Faça um programa que escreva o seu nome completo em python")
print("Everthon Igor de Souza")

# 2 --------------------------------------
print("\n2 - Qual é o tipo de dado (int ou float) do resultado de cada uma das operações matemáticas abaixo? ")

# 3 --------------------------------------
print("\n3 - E qual é o resultado das expressões do exercício 2 quando executadas no Python?")

print("8 ÷ 4 + 2 x 3")
resultado = (8 / 4) + (2 * 3)
print(resultado)
print(type(resultado)) # 8 -> int

print("15 - 4 x 2 + 10") 
resultado = 15 - (4 * 2) + 10
print(resultado)
print(type(resultado)) # 17 -> int

print("(10 - 3) x (5 + 2)")
resultado = (10 - 3) * (5 + 2)
print(resultado)
print(type(resultado)) # 49 -> int

print("100 ÷ (5 + 5)")
resultado = 100 / (5 + 5)
print(resultado)
print(type(resultado)) # 10 -> int

print("23 + 4") 
resultado = 23 + 4
print(resultado)
print(type(resultado)) # 27 -> int

print("7 + 3 x (10 ÷ 2)") 
resultado = 7 + 3 * (10 / 2)
print(resultado)
print(type(resultado)) # 22 -> int

print("(8 + 2) x 3 - 5")
resultado = (8 + 2) * 3 - 5
print(resultado)
print(type(resultado)) # 25 -> int

print("50 ÷ 5 + √16") 
resultado = (50 / 5) + math.sqrt(16)
print(resultado)
print(type(resultado)) # 14 -> int

print("5 + √25 x 2 - 3")
resultado = 5 + math.sqrt(25) * 2 - 3
print(resultado)
print(type(resultado)) # 12 -> int

print("20 - 4 x (√9 + 1)") 
resultado = 20 - 4 * (math.sqrt(9) + 1)
print(resultado)
print(type(resultado)) # 4 -> int

# 4 --------------------------------------
print("\n4 - Crie três variáveis para armazenar as seguintes informações: seu nome, sua idade e seu hobby favorito.") 
print("Use f-strings para criar uma mensagem que inclua as três variáveis e imprima a mensagem no console.")
nome = "Everthon"
idade = 32
hobby = "estudar musica"
print(f"Meu nome é {nome}, tenho {idade} anos e adoro {hobby}")

# 5 --------------------------------------
questao = "\n5 - Você está trabalhando em um sistema para calcular o salário de um funcionário baseado em algumas variáveis, como o salário base, o bônus e os descontos. O código foi feito por outra pessoa e está apresentando um erro. Execute o código, identifique o erro e corrija-o. Justifique a sua correção com um comentário # acima do que foi corrigido. "
print(questao)
salario_base = 3500.00
bonus = 500.00
descontos = 300.00
salario_liquido = salario_base + bonus - descontos
print(f"O salario liquido é {salario_liquido}")
print("O erro estava na declaração no uso da variavel 'desconto', na declaração estava com 'd' maiusculo e no uso com o 'd' minusculo")

# 6 --------------------------------------
questao = "\n6 - Suponha que uma empresa tem um código de produto no formato PROD-XXXX, onde XXXX são dígitos de 0 a 9, e ela deseja verificar se os códigos segue o formato correto. Por exemplo, PROD-1234 é válido, mas prod-1234 e PROD1234 não são." 
questao += "\nFaça um programa que retorne se o código prod0000 é válido ou não, justificando sua resposta."
print(questao)

def valida_codigo(codigo):
    print(f"\nCodigo informado: {codigo}")
    if not "-" in codigo: #contains
        print("Código não é valido, não possui o caracter '-'")
    else:
        print("O código possui o separador '-'")

    inicio_codigo = codigo[0:4] #substring
    if inicio_codigo != "PROD":
        print(f"Código não é valido, o inicio deve ser 'PROD' e o informado foi '{inicio_codigo}'")
    else:
        print("O inicio do código informado é válido")

    final_codigo = codigo[-4:] #indice negativo, pega os 4 ultimos caracteres da string
    try:
        valor_inteiro = int(final_codigo)
        print(f"O final do código informado '{final_codigo}' é valido")
    except Exception as ex:
        print(f"O final do código informado '{final_codigo}' não é valido")

valida_codigo("prod0000")
valida_codigo("prod-0000")
valida_codigo("PROD-XXXX")
valida_codigo("PROD-0000")

# 7 --------------------------------------
questao = "\n7 - Você trabalha para o Detran/SP e recebeu uma tarefa de separar as partes (letras e números) de uma determinada placa de veículo no modelo antigo. Faça um código que automatize essa separação. Use a placa ABC-1234 como exemplo."
print(questao)
placa = "ABC-1234"

if not "-" in placa:
    print("Não existe o caracter '-' na placa informada")

resultado = placa.split('-')
print(f"Inicio da placa: {resultado[0]}")
print(f"Final da placa: {resultado[1]}")