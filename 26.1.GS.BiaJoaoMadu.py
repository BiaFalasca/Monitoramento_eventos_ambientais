'''
Global Solution 01.2026
Integrantes:
- Beatriz Falasca Lopes da Silva (RM570086)
- João Ricardo Travaglin Abi Saber (RM573129)
- Maria Eduarda Rodrigues da Silva (RM572951)
'''

# Listas para armazenamento de dados
tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

#Cores
VERMELHO = "\033[91m"
ROSA = "\033[38;5;206m"
ROXO = "\033[38;5;93m"
VERDE = "\033[38;5;34m"
FUNDO_VERDE_ESCURO = "\033[48;5;28m"
BRANCO = "\033[97m"
RESET = "\033[0m"

# Solicitação ao usuário para dar início ao cadastro

while True:
    try:
        quantidade_eventos = int(input("\nDigite a quantidade de eventos registrados: "))

        if quantidade_eventos <= 0:
            print(f"\n{ROSA}Ótima notícia! Nenhum desastre ambiental foi registrado no período analisado.{RESET}")
            exit()
        else:
            break

    except ValueError:
        print(f"{VERMELHO}Erro: digite apenas números inteiros.{RESET}")

i= 0
for i in range(quantidade_eventos):
    print(f"\n{FUNDO_VERDE_ESCURO}{BRANCO}=== Cadastro do Evento {i + 1} ==={RESET}")
    print(f"\nPreencha as informações solicitadas a seguir:")
    tipo = input("Tipo de evento (Exemplo: desmatamento, queimada, variação climática ...): ").lower()
    pais = input("País: ").lower()
    regiao = input("Região: ").lower()
    cidade = input("Cidade: ").lower()

    # Solicitando e validando a área
    while True:
        try:
            area = float(input("Área afetada (km²): "))

            if area <= 0:
                print(f"{VERMELHO}Erro: a área deve ser maior que zero.{RESET}")
            else:
                break
        except ValueError:
            print(f"{VERMELHO}Erro: digite apenas números.{RESET}")

    # Solicitando e validando a intensidade
    while True:
        try:
            intensidade = int(input("Intensidade (1 a 10): "))

            if intensidade < 1 or intensidade > 10:
                print(f"{VERMELHO}Erro: a intensidade deve estar entre 1 e 10.{RESET}")
            else:
                break
        except ValueError:
            print(f"{VERMELHO}Erro: digite apenas números inteiros.{RESET}")

    # Solicitando e validando a ocorrência
    while True:
        try:
            ocorrencia = int(input("Número de ocorrências: "))

            if ocorrencia < 0:
                print(f"{VERMELHO}Erro: o número de ocorrências não pode ser negativo.{RESET}")
            else:
                break
        except ValueError:
            print(f"{VERMELHO}Erro: digite apenas números inteiros.{RESET}")

    # Armazenamento nas listas
    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(ocorrencia)

# ANÁLISE DOS DADOS
# Total de eventos
total_eventos = len(tipos_eventos)

# Soma das áreas afetadas
total_areas = sum(areas_afetadas)

# Média das intensidades
media_intensidade = sum(intensidades) / total_eventos

# Evento com maior área afetada
maior_area = areas_afetadas.index(max(areas_afetadas))

# Região com maior número de ocorrências
maior_ocorrencia = ocorrencias.index(max(ocorrencias))

# Densidade média (ocorrências / área)
soma_densidades = 0

for i in range(total_eventos):
    densidade = ocorrencias[i] / areas_afetadas[i]
    soma_densidades += densidade

densidade_media = soma_densidades / total_eventos

# Quantidade de eventos acima da média de intensidade
eventos_acima_media = 0

for intensidade in intensidades:
    if intensidade > media_intensidade:
        eventos_acima_media += 1

# Evento mais crítico
# Critério: intensidade + área
indice_critico = 0
maior_pontuacao = 0

for i in range(total_eventos):
    pontuacao = intensidades[i] * areas_afetadas[i]

    if pontuacao > maior_pontuacao:
        maior_pontuacao = pontuacao
        indice_critico = i

# RELATÓRIO FINAL

print(f"\n{VERDE}======================================")
print(f"RELATÓRIO DE EVENTOS AMBIENTAIS")
print(f"======================================{RESET}")

print(f"\n{VERDE}Total de eventos registrados: {total_eventos}{RESET}")

print(f"\n{FUNDO_VERDE_ESCURO}{BRANCO}Área total afetada: {total_areas:.2f} km²{RESET}")

print(f"{FUNDO_VERDE_ESCURO}{BRANCO}Média das intensidades: {media_intensidade:.2f}{RESET}")

print(f"\nRegião com mais ocorrências: {regioes[maior_ocorrencia]}")

print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media}")

print(f"Densidade média: {densidade_media:.2f} ocorrências/km²")

print(f"\n{VERMELHO}======================================")
print(f"Evento Mais Crítico{RESET}")
print(f"Tipo: {tipos_eventos[indice_critico]}")
print(f"Intensidade: {intensidades[indice_critico]}")
print(f"Área afetada: {areas_afetadas[indice_critico]:.2f} km²")
print(f"{VERMELHO}======================================{RESET}")

print(f"\n{ROXO}======================================")
print(f"Local completo do evento mais crítico:{RESET}")
print(f"{cidades[indice_critico]} - {regioes[indice_critico]} - {paises[indice_critico]}")
print(f"{ROXO}======================================{RESET}")