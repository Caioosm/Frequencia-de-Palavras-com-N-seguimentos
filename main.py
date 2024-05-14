import threading

# Função para contar a frequência de palavras em um segmento específico
def contar_palavras(segmento, contador):
    for palavra in segmento.split():
        contador[palavra] = contador.get(palavra, 0) + 1

# Função para processar um segmento de texto usando threads
def processar_segmento(segmento, contador, thread_id):
    print(f"Thread {thread_id} iniciada.")
    contar_palavras(segmento, contador)
    print(f"Thread {thread_id} concluída.")

# Função principal
def main(arquivo, num_segmentos):
    # Inicializa um contador de frequência de palavras
    contador = {}

    # Lê o arquivo de texto e divide em N segmentos
    with open(arquivo, 'r') as file:
        texto = file.read()
        tamanho_segmento = len(texto) // num_segmentos
        segmentos = [texto[i:i+tamanho_segmento] for i in range(0, len(texto), tamanho_segmento)]

    # Inicia threads para processar cada segmento
    threads = []
    for i, segmento in enumerate(segmentos):
        thread = threading.Thread(target=processar_segmento, args=(segmento, contador, i))
        threads.append(thread)
        thread.start()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

    # Imprime os resultados consolidados
    print("\nFrequência de palavras consolidada:")
    for palavra, frequencia in contador.items():
        print(f"{palavra}: {frequencia}")

# Chamada da função principal
if __name__ == "__main__":
    arquivo = "arquivo.txt"  # Nome do arquivo de texto
    num_segmentos = 4  # Número de segmentos
    main(arquivo, num_segmentos)
