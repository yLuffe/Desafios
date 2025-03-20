"""
2 - Números primos

    -- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input), 
    e retornar todos os números primos até o número N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

    --- Criar uma função recursiva que resolva p

    --- Criar uma função linear que resolva p
"""
    
# Loop While para solicitar número para o usuário
def input_numero():
    input_num = 0
    while input_num <= 1:
        try:
            input_num = int(input("Favor inserir um número Inteiro Positovo maior que 1: "))
            if input_num <= 1: # Caso seja menor que 1, solicita o número novamente
                print(f"Número {input_num} é inválido!")
        except ValueError:     # Caso não seja número, cai na exceção
            print(f"Caractere inválido!")
    return input_num

# Solicitando número ao usuário
num = input_numero()  

# Versão Recursiva
def calc_primo_recusivo(num_input, divisor=2):
    if num_input == 2:
        return True
    if num_input % divisor == 0:
        return False
    if divisor * divisor > num_input:
        return True
    
    return calc_primo_recusivo(num_input, divisor+1)

def lista_primos(num_input, num_atual=2, primos_lista=[]):
    if num_atual > num_input:
        return primos_lista
    if calc_primo_recusivo(num_atual):
        primos_lista.append(num_atual)
    return lista_primos(num_input, num_atual + 1, primos_lista)

print(f"Recursiva: Lista dos números primos até {num}: {lista_primos(num)}")
# Identifiquei que um ponto negativo na recursiva é que consegui fazer
# uma chamada apenas até o número 996, após isso excede o limite de recursividade

# Versão Linear
# Função para cálcular número primo
def calc_primo_linear(num_input: int) -> list:
    lista_primos = []
    for i in range (2, num_input + 1):
        is_primo = True
        for j in range(2, int(i/2) + 1):
            if i % j == 0:
                is_primo = False
                break
        if is_primo:
            lista_primos.append(i)
    return lista_primos
   
print(f"Linear...: Lista dos números primos até {num}: {calc_primo_linear(num)}")


# Nesse contexto utilizei de duas funções para validação do número primo.
# Primeiramente a função de input que já faz a verificação se o número é
# maior ou igual a 2 para que essa responsabilidade não fique com a função
# do cálculo do número primo, assim separando as lógicas e deixando mais legível.