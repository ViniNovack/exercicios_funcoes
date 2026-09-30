"""
Gabarito - Nivel Facil (12 exercicios)
Raciocinio Algoritmico - PUCPR

Cada exercicio abaixo esta 100% comentado (nao executa nada por
padrao). O codigo de cada exercicio e exatamente o que seria escrito
normalmente -- com a(s) funcao(oes) exigida(s) pelo enunciado e o
programa principal chamando essas funcoes -- apenas com "#" na frente
de cada linha.

Como usar:
1. Encontre o exercicio que deseja testar (procure pelo cabecalho
   "Exercicio NN - Titulo").
2. Selecione todas as linhas comentadas desse exercicio.
3. Use o atalho de comentar/descomentar do seu editor
   (Ctrl + / no VS Code e em varios outros editores) para remover o
   "#" de todas as linhas selecionadas de uma vez.
4. Rode o arquivo normalmente (python nome_do_arquivo.py).
5. Quando terminar, comente o bloco novamente antes de testar outro
   exercicio, para eles nao se misturarem.
"""


# ============================================================
# Exercicio 01 - Mensagem Personalizada com Moldura
# ============================================================
# def titulo(texto):
#     # Define uma margem fixa de espaco extra ao redor do texto
#     margem = 4
#     # O tamanho da moldura acompanha automaticamente o texto + a margem
#     largura = len(texto) + margem
#     moldura = "~" * largura
#     print(moldura)
#     # center() centraliza o texto dentro da largura calculada, usando
#     # espacos para preencher os dois lados
#     print(texto.center(largura))
#     print(moldura)
#
#
# # Testando a funcao com o exemplo do enunciado
# titulo('CURSO DE PYTHON')


# ============================================================
# Exercicio 02 - Calculador de Area de Terreno
# ============================================================
# def area(largura, comprimento):
#     # Multiplica as duas dimensoes para obter a area em metros quadrados
#     resultado = largura * comprimento
#     # :.2f formata o numero com exatamente 2 casas decimais
#     print(f"A area do terreno e de {resultado:.2f} m2")
#
#
# largura = float(input("Digite a largura do terreno (m): "))
# comprimento = float(input("Digite o comprimento do terreno (m): "))
# area(largura, comprimento)


# ============================================================
# Exercicio 03 - Verificador de Par ou Impar
# ============================================================
# def par_ou_impar(numero):
#     # O resto da divisao por 2 igual a 0 indica que o numero e par
#     if numero % 2 == 0:
#         return 'PAR'
#     else:
#         return 'IMPAR'
#
#
# numero = int(input("Digite um numero inteiro: "))
# # A funcao apenas retorna o resultado; quem imprime e o programa principal
# resultado = par_ou_impar(numero)
# print(f"O numero {numero} e {resultado}")


# ============================================================
# Exercicio 04 - Contador com Passo Personalizado
# ============================================================
# def contador_passo(inicio, fim, passo):
#     # Se o passo for 0, assume passo = 1 para evitar um laco infinito
#     if passo == 0:
#         passo = 1
#     # Usamos o valor absoluto do passo, pois a direcao (crescente ou
#     # decrescente) sera decidida com base em inicio e fim
#     passo = abs(passo)
#
#     if inicio <= fim:
#         # Contagem crescente: soma o passo a cada repeticao
#         for numero in range(inicio, fim + 1, passo):
#             print(numero)
#     else:
#         # Contagem decrescente: subtrai o passo a cada repeticao
#         for numero in range(inicio, fim - 1, -passo):
#             print(numero)
#
#
# inicio = int(input("Digite o valor inicial: "))
# fim = int(input("Digite o valor final: "))
# passo = int(input("Digite o passo: "))
# contador_passo(inicio, fim, passo)


# ============================================================
# Exercicio 05 - Fatorial de um Numero
# ============================================================
# def fatorial(numero):
#     resultado = 1
#     # Multiplica o resultado por cada numero de 1 ate "numero"
#     for i in range(1, numero + 1):
#         resultado *= i
#     return resultado
#
#
# numero = int(input("Digite um numero inteiro: "))
# resultado = fatorial(numero)
# print(f"O fatorial de {numero} e {resultado}.")


# ============================================================
# Exercicio 06 - Analisador Numerico Sem Bibliotecas
# ============================================================
# def analisa_numero(n):
#     dobro = n * 2
#     triplo = n * 3
#     # Calcula a raiz quadrada usando o operador de potencia (** 0.5),
#     # sem precisar importar o modulo math
#     raiz = n ** 0.5
#     print(f"Dobro: {dobro}")
#     print(f"Triplo: {triplo}")
#     print(f"Raiz quadrada: {raiz:.2f}")
#
#
# n = float(input("Digite um numero real: "))
# analisa_numero(n)


# ============================================================
# Exercicio 07 - Validador de Situacao Eleitoral
# ============================================================
# def voto(ano_nascimento):
#     # Ano corrente fixado no codigo, conforme pedido no enunciado
#     ano_atual = 2026
#     idade = ano_atual - ano_nascimento
#
#     if idade < 16:
#         return 'VOTO NEGADO'
#     elif idade in (16, 17) or idade >= 70:
#         return 'VOTO OPCIONAL'
#     else:
#         return 'VOTO OBRIGATORIO'
#
#
# ano_nascimento = int(input("Digite o ano de nascimento: "))
# situacao = voto(ano_nascimento)
# print(situacao)


# ============================================================
# Exercicio 08 - Gerador de Tabuada Formatada
# ============================================================
# def tabuada(num):
#     print(f"===== Tabuada do {num} =====")
#     # Percorre de 1 a 10 (o range(1, 11) para no 10, pois o limite
#     # superior nunca e incluido)
#     for i in range(1, 11):
#         # {i:2} alinha o numero em 2 posicoes, deixando a tabela mais organizada
#         print(f"{num} x {i:2} = {num * i}")
#     print("=============================")
#
#
# num = int(input("Digite um numero para ver a tabuada: "))
# tabuada(num)


# ============================================================
# Exercicio 09 - Descobrindo o Maior Valor com Empacotamento
# ============================================================
# def maior(*numeros):
#     # "*numeros" empacota todos os argumentos recebidos em uma tupla
#     print(f"Numeros recebidos: {numeros}")
#     print(f"Quantidade de numeros: {len(numeros)}")
#     print(f"O maior valor e: {max(numeros)}")
#
#
# # Testando com o exemplo do enunciado
# maior(2, 9, 4, 5, 7, 1)


# ============================================================
# Exercicio 10 - Ficha de Jogador com Parametros Opcionais
# ============================================================
# def ficha(nome='<desconhecido>', gols=0):
#     # Se nome ou gols nao forem informados na chamada, os valores
#     # padrao definidos na assinatura da funcao sao usados automaticamente
#     print(f"Jogador: {nome}")
#     print(f"Gols marcados: {gols}")
#
#
# nome = input("Digite o nome do jogador (ou deixe em branco): ")
# gols_texto = input("Digite a quantidade de gols (ou deixe em branco): ")
#
# # Verifica o que foi digitado para decidir quais parametros passar
# if nome and gols_texto:
#     ficha(nome, int(gols_texto))
# elif nome:
#     ficha(nome=nome)
# elif gols_texto:
#     ficha(gols=int(gols_texto))
# else:
#     ficha()


# ============================================================
# Exercicio 11 - Media Aritmetica e Dicionario de Situacao
# ============================================================
# def calcula_media(nota1, nota2):
#     media = (nota1 + nota2) / 2
#     # Situacao depende se a media atinge o valor minimo de aprovacao (7.0)
#     situacao = 'Aprovado' if media >= 7.0 else 'Reprovado'
#     # Retorna um dicionario com as duas informacoes organizadas
#     return {'Media': media, 'Situacao': situacao}
#
#
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# resultado = calcula_media(nota1, nota2)
# print(resultado)


# ============================================================
# Exercicio 12 - Contador de Vogais em Frases
# ============================================================
# def conta_vogais(texto):
#     # Converte tudo para minusculas para nao precisar testar
#     # maiusculas e minusculas separadamente
#     texto = texto.lower()
#     vogais = "aeiou"
#     contador = 0
#     # Percorre a frase caractere por caractere
#     for letra in texto:
#         if letra in vogais:
#             contador += 1
#     return contador
#
#
# frase = input("Digite uma frase: ")
# total = conta_vogais(frase)
# print(f"A frase possui {total} vogais.")

