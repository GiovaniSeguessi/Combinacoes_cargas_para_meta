from itertools import combinations_with_replacement

# Função para encontrar combinações que somam um valor específico
def find_combinations(target_sum, possible_values, list_length, max_lists):
    # Gera todas as combinações possíveis com repetição dos valores disponíveis
    combinations = list(combinations_with_replacement(possible_values, list_length))
    # Filtra as combinações válidas que somam o valor alvo
    valid_combinations = [combo for combo in combinations if sum(combo) == target_sum]
    # Ordena as combinações válidas em ordem decrescente
    sorted_combinations = sorted(valid_combinations, reverse=True)
    # Retorna as primeiras combinações (listas) de acordo com o número máximo especificado
    return sorted_combinations[:max_lists]

#Variáveis (target_sum e list_lenght são variáveis dinâmicas)
target_sum = 178
possible_values = [10, 12, 14, 16]
list_length = 14
max_lists = 3

result_lists = find_combinations(target_sum, possible_values, list_length, max_lists)

#Ordena as listas pelo valor em ordem decrescente e imprime as listas
for i, lst in enumerate(result_lists):
    sorted_list = sorted(lst,reverse=True)
    print(f"Cenário {i+1}: {lst}")
