def soma_tupla(tupla):
    # Calcula a soma de todos os elementos da tupla
    soma = sum(tupla)
    return soma

# Função principal para ler a entrada e exibir a saída
def main():
    # Lê a entrada do usuário e converte para uma tupla de inteiros
    entrada = input()
    tupla_numeros = tuple(map(int, entrada.split()))
    
    # Calcula a soma dos elementos da tupla
    soma = soma_tupla(tupla_numeros)
    
    # Exibe a soma no formato especificado
    print(f"A soma dos elementos da tupla é: {soma}")

# Chama a função principal
if __name__ == "__main__":
    main()
