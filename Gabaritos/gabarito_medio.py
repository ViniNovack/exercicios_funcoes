"""
Gabarito - Nivel Medio (12 exercicios)
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
# Exercicio 13 - Validacao de Dados e Cadastro Continuado
# ============================================================
# def valida_idade(msg):
#     # O laco while so termina quando o usuario digitar um numero
#     # inteiro positivo valido
#     while True:
#         valor = input(msg)
#         if valor.isdigit() and int(valor) > 0:
#             return int(valor)
#         print("Valor invalido! Digite um numero inteiro positivo.")
#
#
# def cadastrar_pessoa():
#     nome = input("Digite o nome: ")
#     # Delega a validacao da idade para a funcao especializada
#     idade = valida_idade("Digite a idade: ")
#     return {'nome': nome, 'idade': idade}
#
#
# cadastrados = []
# while True:
#     pessoa = cadastrar_pessoa()
#     cadastrados.append(pessoa)
#     continuar = input("Deseja continuar? [S/N]: ").strip().upper()
#     if continuar != 'S':
#         break
#
# print("Lista de cadastrados:")
# for c in cadastrados:
#     print(c)


# ============================================================
# Exercicio 14 - Coleta e Estatisticas Numericas
# ============================================================
# def gerar_lista():
#     lista = []
#     # Continua lendo numeros ate o usuario digitar -1 (valor de parada)
#     while True:
#         valor = float(input("Digite um numero (-1 para parar): "))
#         if valor == -1:
#             break
#         lista.append(valor)
#     return lista
#
#
# def analisar_lista(lista):
#     print(f"Maior numero: {max(lista)}")
#     print(f"Menor numero: {min(lista)}")
#     print(f"Soma total: {sum(lista)}")
#     print(f"Media: {sum(lista) / len(lista):.2f}")
#
#
# numeros = gerar_lista()
# if numeros:
#     analisar_lista(numeros)
# else:
#     print("Nenhum numero foi digitado.")


# ============================================================
# Exercicio 15 - Construtor e Exibidor de Matrizes Tabulares
# ============================================================
# def criar_matriz(linhas, colunas):
#     matriz = []
#     for l in range(linhas):
#         linha = []
#         for c in range(colunas):
#             # M[l][c] pede a posicao especifica de cada elemento da matriz
#             valor = float(input(f"Digite o valor de M[{l}][{c}]: "))
#             linha.append(valor)
#         matriz.append(linha)
#     return matriz
#
#
# def exibir_matriz(matriz):
#     # Imprime cada linha com os valores alinhados em colunas de 6
#     # caracteres e 2 casas decimais
#     for linha in matriz:
#         print("  ".join(f"{v:6.2f}" for v in linha))
#
#     # Soma os elementos da terceira coluna (indice 2), se ela existir
#     if len(matriz[0]) >= 3:
#         soma_terceira_coluna = sum(linha[2] for linha in matriz)
#         print(f"Soma da terceira coluna: {soma_terceira_coluna:.2f}")
#
#
# linhas = int(input("Digite o numero de linhas: "))
# colunas = int(input("Digite o numero de colunas: "))
# matriz = criar_matriz(linhas, colunas)
# exibir_matriz(matriz)


# ============================================================
# Exercicio 16 - Carrinho de Compras com Cupons de Desconto
# ============================================================
# def calcular_total(lista_precos):
#     # Soma todos os precos do carrinho
#     return sum(lista_precos)
#
#
# def aplicar_desconto(total, cupom):
#     cupom = cupom.strip().upper()
#     if cupom == 'DEZ':
#         return total * 0.9   # 10% de desconto
#     elif cupom == 'VINTE':
#         return total * 0.8   # 20% de desconto
#     else:
#         # Cupom invalido ou vazio: nao aplica nenhum desconto
#         return total
#
#
# precos = []
# while True:
#     preco_texto = input("Digite o preco de um produto (ou ENTER para finalizar): ")
#     if preco_texto == "":
#         break
#     precos.append(float(preco_texto))
#
# total = calcular_total(precos)
# cupom = input("Digite o cupom de desconto (ou deixe em branco): ")
# total_final = aplicar_desconto(total, cupom)
#
# print(f"Total sem desconto: R$ {total:.2f}")
# print(f"Total a pagar: R$ {total_final:.2f}")


# ============================================================
# Exercicio 17 - Boletim de Notas da Turma
# ============================================================
# def ler_notas():
#     notas = []
#     while True:
#         entrada = input("Digite uma nota (ou ENTER para encerrar): ")
#         if entrada == "":
#             break
#         notas.append(float(entrada))
#     return notas
#
#
# def calcular_estatisticas(lista_notas):
#     # Retorna um dicionario com todas as estatisticas pedidas
#     return {
#         'total': len(lista_notas),
#         'maior': max(lista_notas),
#         'menor': min(lista_notas),
#         'media': sum(lista_notas) / len(lista_notas)
#     }
#
#
# def exibir_boletim(dicionario_estatisticas):
#     print("======= BOLETIM DA TURMA =======")
#     print(f"Total de notas: {dicionario_estatisticas['total']}")
#     print(f"Maior nota: {dicionario_estatisticas['maior']}")
#     print(f"Menor nota: {dicionario_estatisticas['menor']}")
#     print(f"Media da turma: {dicionario_estatisticas['media']:.2f}")
#     print("=================================")
#
#
# notas = ler_notas()
# if notas:
#     stats = calcular_estatisticas(notas)
#     exibir_boletim(stats)
# else:
#     print("Nenhuma nota foi registrada.")


# ============================================================
# Exercicio 18 - Sanitizacao de Texto e Frequencia de Palavras
# ============================================================
# def limpar_texto(texto):
#     # Deixa tudo minusculo e remove pontuacoes simples
#     texto = texto.lower()
#     texto = texto.replace(",", "").replace(".", "")
#     return texto
#
#
# def separar_palavras(texto_limpo):
#     # .split() sem argumento separa a string em palavras usando espacos
#     return texto_limpo.split()
#
#
# def contar_frequencia(lista_palavras):
#     frequencia = {}
#     for palavra in lista_palavras:
#         if palavra in frequencia:
#             frequencia[palavra] += 1
#         else:
#             frequencia[palavra] = 1
#     return frequencia
#
#
# frase = input("Digite uma frase: ")
# texto_limpo = limpar_texto(frase)
# palavras = separar_palavras(texto_limpo)
# frequencia = contar_frequencia(palavras)
# print(frequencia)


# ============================================================
# Exercicio 19 - Fatorial com Visualizacao de Passos e Validacao
# ============================================================
# def leia_int(msg):
#     # Nao aceita entradas vazias nem alfanumericas (isdigit garante
#     # que a string so contem digitos)
#     while True:
#         valor = input(msg)
#         if valor.isdigit() and int(valor) > 0:
#             return int(valor)
#         print("Entrada invalida! Digite um numero inteiro positivo.")
#
#
# def fatorial(n, show=False):
#     resultado = 1
#     passos = []
#     # Percorre de n ate 1 (decrescente) multiplicando o resultado
#     for i in range(n, 0, -1):
#         resultado *= i
#         passos.append(str(i))
#
#     if show:
#         # Monta a string "5 x 4 x 3 x 2 x 1 = 120"
#         equacao = " x ".join(passos)
#         print(f"{equacao} = {resultado}")
#
#     return resultado
#
#
# n = leia_int("Digite um numero inteiro positivo: ")
# mostrar = input("Deseja ver o calculo passo a passo? [S/N]: ").strip().upper() == 'S'
# resultado = fatorial(n, show=mostrar)
# if not mostrar:
#     print(f"O fatorial de {n} e {resultado}.")


# ============================================================
# Exercicio 20 - Simulador de Caixa Eletronico
# ============================================================
# def solicitar_valor_saque():
#     while True:
#         valor = input("Digite o valor a sacar: ")
#         if valor.isdigit() and int(valor) > 0:
#             return int(valor)
#         print("Valor invalido! Digite um numero inteiro positivo.")
#
#
# def calcular_cedulas(valor):
#     # Dicionario que vai guardar quantas cedulas de cada tipo sao necessarias
#     cedulas = {50: 0, 20: 0, 10: 0, 1: 0}
#     restante = valor
#     for nota in cedulas:
#         # Divisao inteira: quantas notas desse valor cabem no restante
#         cedulas[nota] = restante // nota
#         # O resto fica para ser resolvido pelas notas menores
#         restante %= nota
#     return cedulas
#
#
# def exibir_saque(dicionario_cedulas):
#     print("===== Resumo do saque =====")
#     for nota, quantidade in dicionario_cedulas.items():
#         if quantidade > 0:
#             print(f"{quantidade} nota(s) de R$ {nota}")
#     print("============================")
#
#
# valor = solicitar_valor_saque()
# cedulas = calcular_cedulas(valor)
# exibir_saque(cedulas)


# ============================================================
# Exercicio 21 - Jogo de Adivinhacao com Ranking de Tentativas
# ============================================================
# def gerar_numero_secreto(limite):
#     # Gera um numero "pseudo-aleatorio" simples usando apenas contas
#     # matematicas, sem depender da biblioteca random, conforme pedido
#     base = (limite * 7 + 13) % limite
#     return base + 1  # garante um numero entre 1 e limite
#
#
# def jogar_rodada(secreto):
#     tentativas = 0
#     while True:
#         palpite = int(input("Digite seu palpite: "))
#         tentativas += 1
#         if palpite == secreto:
#             print(f"Voce acertou em {tentativas} tentativa(s)!")
#             return tentativas
#         elif palpite < secreto:
#             print("O numero secreto e MAIOR.")
#         else:
#             print("O numero secreto e MENOR.")
#
#
# def salvar_ranking(ranking, nome, tentativas):
#     # Acrescenta o resultado do jogador na lista de classificacao
#     ranking.append({'nome': nome, 'tentativas': tentativas})
#     return ranking
#
#
# ranking = []
# limite = int(input("Digite o limite maximo do numero secreto: "))
# nome = input("Digite seu nome: ")
# secreto = gerar_numero_secreto(limite)
# tentativas = jogar_rodada(secreto)
# ranking = salvar_ranking(ranking, nome, tentativas)
# print(ranking)


# ============================================================
# Exercicio 22 - Conversor de Unidades de Temperatura
# ============================================================
# def celsius_para_fahrenheit(c):
#     return c * 1.8 + 32
#
#
# def fahrenheit_para_celsius(f):
#     return (f - 32) / 1.8
#
#
# def menu_conversor():
#     print("1 - Celsius para Fahrenheit")
#     print("2 - Fahrenheit para Celsius")
#     opcao = input("Escolha uma opcao: ")
#
#     if opcao == '1':
#         valor = float(input("Digite a temperatura em Celsius: "))
#         resultado = celsius_para_fahrenheit(valor)
#         print(f"{valor} C equivalem a {resultado:.2f} F")
#     elif opcao == '2':
#         valor = float(input("Digite a temperatura em Fahrenheit: "))
#         resultado = fahrenheit_para_celsius(valor)
#         print(f"{valor} F equivalem a {resultado:.2f} C")
#     else:
#         print("Opcao invalida!")
#
#
# menu_conversor()


# ============================================================
# Exercicio 23 - Sanitizador e Validador de Nomes Proprios
# ============================================================
# def normalizar_nome(nome):
#     # .split() sem argumento ja ignora espacos extras (inicio, fim e
#     # entre as palavras) automaticamente
#     partes = nome.split()
#     # .capitalize() deixa a primeira letra maiuscula e o resto minusculo
#     nome_normalizado = " ".join(parte.capitalize() for parte in partes)
#     return nome_normalizado
#
#
# def validar_nome_completo(nome_normalizado):
#     partes = nome_normalizado.split()
#     # Um nome completo precisa ter pelo menos 2 partes (nome e sobrenome)
#     return len(partes) >= 2
#
#
# nome_digitado = input("Digite seu nome completo: ")
# nome_normalizado = normalizar_nome(nome_digitado)
# valido = validar_nome_completo(nome_normalizado)
#
# print(f"Nome normalizado: {nome_normalizado}")
# print(f"Nome completo valido? {valido}")


# ============================================================
# Exercicio 24 - Desempenho e Ficha de Jogador de Futebol
# ============================================================
# def cadastrar_jogador():
#     nome = input("Digite o nome do jogador: ")
#     partidas = int(input("Digite a quantidade de partidas disputadas: "))
#     gols_por_partida = []
#     for i in range(partidas):
#         gols = int(input(f"Gols na partida {i + 1}: "))
#         gols_por_partida.append(gols)
#     return {'nome': nome, 'partidas': partidas, 'gols': gols_por_partida}
#
#
# def calcular_media_gols(jogador_dict):
#     total_gols = sum(jogador_dict['gols'])
#     return total_gols / jogador_dict['partidas']
#
#
# def exibir_ficha_jogador(jogador_dict):
#     total_gols = sum(jogador_dict['gols'])
#     media = calcular_media_gols(jogador_dict)
#     print("======= FICHA DO JOGADOR =======")
#     print(f"Nome: {jogador_dict['nome']}")
#     print(f"Partidas disputadas: {jogador_dict['partidas']}")
#     print(f"Total de gols: {total_gols}")
#     print(f"Media de gols por partida: {media:.2f}")
#     print("=================================")
#
#
# jogador = cadastrar_jogador()
# exibir_ficha_jogador(jogador)

