"""
1 - Fibonacci

    -- Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função), 
    e retornar o valor correspondente desse número na sequência Fibonacci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.

    --- Criar uma função recursiva que resolva Fibonacci

    --- Criar uma função linear que resolva Fibonacci
"""

# Loop While para solicitar número para o usuário
def input_numero():
    input_num = 0
    while input_num <= 0:
        try:
            input_num = int(input("Favor inserir um número Inteiro Positovo maior que 0: "))
            if input_num <= 0: # Caso seja menor que 0, solicita o número novamente
                print(f"Número {input_num} é inválido!")
        except ValueError:     # Caso não seja número, cai na exceção
            print(f"Caractere inválido!")
    return input_num

# Solicitando número ao usuário
num = input_numero()  


# Versão Recursiva
def calc_fibonacci_recursivo(num: int):
    if num == 0: # Em ambas funções ele não calcula se é menor que zero pois estou fazendo isso na função input_numero()
        return 0
    elif num == 1:
        return 1
    else:
        return calc_fibonacci_recursivo(num - 1) + calc_fibonacci_recursivo(num - 2)
    
# Validando o Recursivo
print(f"Cálculo Recursivo referente a {num}.: {calc_fibonacci_recursivo(num)}")


# Versão Linear
def calc_fibonacci_linear(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1

    a, b = 0, 1
    for i in range(2, num + 1):
        a, b = b, a + b
    return b

# Validando o Linear
print(f"Cálculo Linear referente a {num}....: {calc_fibonacci_linear(num)}")