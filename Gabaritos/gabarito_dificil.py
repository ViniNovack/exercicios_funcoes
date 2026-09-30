"""
Gabarito - Nivel Dificil (8 exercicios)
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
# Exercicio 25 - Mini-Sistema de Gestao de Alunos
# ============================================================
# def exibir_cabecalho(texto):
#     margem = 4
#     largura = len(texto) + margem
#     moldura = "=" * largura
#     print(moldura)
#     print(texto.center(largura))
#     print(moldura)
#
#
# def cadastrar_aluno():
#     nome = input("Digite o nome do aluno: ")
#     notas = []
#     for i in range(3):
#         nota = float(input(f"Digite a nota {i + 1}: "))
#         notas.append(nota)
#     return {'nome': nome, 'notas': notas}
#
#
# def calcular_media(lista_notas):
#     return sum(lista_notas) / len(lista_notas)
#
#
# def definir_situacao(media):
#     if media >= 7.0:
#         return 'APROVADO'
#     elif media >= 5.0:
#         return 'RECUPERACAO'
#     else:
#         return 'REPROVADO'
#
#
# def exibir_relatorio_turma(lista_alunos):
#     exibir_cabecalho("RELATORIO DA TURMA")
#     soma_medias = 0
#     for aluno in lista_alunos:
#         media = calcular_media(aluno['notas'])
#         situacao = definir_situacao(media)
#         soma_medias += media
#         print(f"{aluno['nome']:15} | Notas: {aluno['notas']} | Media: {media:.2f} | {situacao}")
#     media_geral = soma_medias / len(lista_alunos)
#     print(f"\nMedia geral da turma: {media_geral:.2f}")
#
#
# alunos = []
# while True:
#     aluno = cadastrar_aluno()
#     alunos.append(aluno)
#     continuar = input("Cadastrar outro aluno? [S/N]: ").strip().upper()
#     if continuar != 'S':
#         break
#
# exibir_relatorio_turma(alunos)


# ============================================================
# Exercicio 26 - Controle de Estoque e Inventario de Loja
# ============================================================
# def adicionar_produto(estoque):
#     codigo = input("Digite o codigo do produto: ")
#     nome = input("Digite o nome do produto: ")
#     preco = float(input("Digite o preco unitario: "))
#     quantidade = int(input("Digite a quantidade em estoque: "))
#     estoque.append({'codigo': codigo, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
#     return estoque
#
#
# def atualizar_quantidade(estoque):
#     codigo = input("Digite o codigo do produto a atualizar: ")
#     for produto in estoque:
#         if produto['codigo'] == codigo:
#             nova_quantidade = int(input("Digite a nova quantidade: "))
#             produto['quantidade'] = nova_quantidade
#             print("Quantidade atualizada com sucesso!")
#             return estoque
#     print("Produto nao encontrado.")
#     return estoque
#
#
# def calcular_valor_total_estoque(estoque):
#     # Soma o preco vezes a quantidade de cada produto
#     total = sum(produto['preco'] * produto['quantidade'] for produto in estoque)
#     return total
#
#
# def buscar_mais_caro(estoque):
#     # key=... diz para max() comparar os produtos pelo preco unitario
#     return max(estoque, key=lambda produto: produto['preco'])
#
#
# def exibir_estoque_completo(estoque):
#     print("===== ESTOQUE COMPLETO =====")
#     for produto in estoque:
#         print(f"{produto['codigo']:5} | {produto['nome']:15} | Qtd: {produto['quantidade']:4} | R$ {produto['preco']:.2f}")
#     total = calcular_valor_total_estoque(estoque)
#     print(f"\nPatrimonio total da loja: R$ {total:.2f}")
#
#
# estoque = []
# while True:
#     estoque = adicionar_produto(estoque)
#     continuar = input("Adicionar outro produto? [S/N]: ").strip().upper()
#     if continuar != 'S':
#         break
#
# exibir_estoque_completo(estoque)
# mais_caro = buscar_mais_caro(estoque)
# print(f"Produto mais caro: {mais_caro['nome']} (R$ {mais_caro['preco']:.2f})")


# ============================================================
# Exercicio 27 - Analise de Cadastro de Trabalhador e Aposentadoria
# ============================================================
# def ler_dados_trabalhador():
#     nome = input("Digite o nome: ")
#     ano_nascimento = int(input("Digite o ano de nascimento: "))
#     ctps = int(input("Digite o numero da CTPS (0 se nao possuir): "))
#     dados = {'nome': nome, 'ano_nascimento': ano_nascimento, 'ctps': ctps}
#     # So pergunta ano de contratacao e salario se a pessoa tiver CTPS
#     if ctps != 0:
#         ano_contratacao = int(input("Digite o ano de contratacao: "))
#         salario = float(input("Digite o salario: "))
#         dados['ano_contratacao'] = ano_contratacao
#         dados['salario'] = salario
#     return dados
#
#
# def calcular_idade(ano_nascimento, ano_atual):
#     return ano_atual - ano_nascimento
#
#
# def calcular_tempo_aposentadoria(idade, ano_contratacao, ano_atual):
#     # Regra simplificada: 35 anos de contribuicao a partir da contratacao
#     anos_trabalhados = ano_atual - ano_contratacao
#     anos_faltantes = 35 - anos_trabalhados
#     idade_aposentadoria = idade + anos_faltantes
#     return idade_aposentadoria
#
#
# def formatar_moeda(valor):
#     # Formata como "R$ 2.500,00": primeiro formata no padrao americano
#     # (2,500.00) e depois troca os separadores para o padrao brasileiro
#     texto = f"{valor:,.2f}"
#     texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
#     return f"R$ {texto}"
#
#
# def exibir_ficha_trabalhador(trabalhador_dict):
#     print("===== FICHA DO TRABALHADOR =====")
#     for chave, valor in trabalhador_dict.items():
#         print(f"{chave}: {valor}")
#     print("=================================")
#
#
# ano_atual = 2026
# trabalhador = ler_dados_trabalhador()
# idade = calcular_idade(trabalhador['ano_nascimento'], ano_atual)
# trabalhador['idade'] = idade
#
# if trabalhador['ctps'] != 0:
#     idade_aposentadoria = calcular_tempo_aposentadoria(
#         idade, trabalhador['ano_contratacao'], ano_atual
#     )
#     trabalhador['idade_aposentadoria'] = idade_aposentadoria
#     trabalhador['salario_formatado'] = formatar_moeda(trabalhador['salario'])
#
# exibir_ficha_trabalhador(trabalhador)


# ============================================================
# Exercicio 28 - Gerenciador Financeiro Pessoal
# ============================================================
# def validar_valor_positivo(msg):
#     # try/except captura o erro caso o usuario digite algo que nao seja numero
#     while True:
#         valor = input(msg)
#         try:
#             valor_float = float(valor)
#             if valor_float > 0:
#                 return valor_float
#         except ValueError:
#             pass
#         print("Valor invalido! Digite um numero real maior que zero.")
#
#
# def registrar_receita():
#     fonte = input("Digite a fonte da receita: ")
#     valor = validar_valor_positivo("Digite o valor da receita: ")
#     return {'fonte': fonte, 'valor': valor}
#
#
# def registrar_despesa():
#     categoria = input("Digite a categoria da despesa: ")
#     valor = validar_valor_positivo("Digite o valor da despesa: ")
#     return {'categoria': categoria, 'valor': valor}
#
#
# def calcular_total_categoria(lista_despesas):
#     totais = {}
#     for despesa in lista_despesas:
#         categoria = despesa['categoria']
#         # .get(categoria, 0) retorna 0 se a categoria ainda nao existir no dicionario
#         totais[categoria] = totais.get(categoria, 0) + despesa['valor']
#     for categoria, total in totais.items():
#         print(f"{categoria}: R$ {total:.2f}")
#     return totais
#
#
# def exibir_balanco_geral(lista_receitas, lista_despesas):
#     total_receitas = sum(r['valor'] for r in lista_receitas)
#     total_despesas = sum(d['valor'] for d in lista_despesas)
#     saldo = total_receitas - total_despesas
#
#     print("===== BALANCO GERAL =====")
#     print(f"Total de receitas: R$ {total_receitas:.2f}")
#     print(f"Total de despesas: R$ {total_despesas:.2f}")
#     print(f"Saldo final: R$ {saldo:.2f}")
#     if saldo >= 0:
#         print("Situacao: VERDE")
#     else:
#         print("Situacao: VERMELHO")
#
#
# receitas = []
# despesas = []
#
# while True:
#     tipo = input("Registrar (R)eceita, (D)espesa ou (F)inalizar? ").strip().upper()
#     if tipo == 'R':
#         receitas.append(registrar_receita())
#     elif tipo == 'D':
#         despesas.append(registrar_despesa())
#     elif tipo == 'F':
#         break
#
# calcular_total_categoria(despesas)
# exibir_balanco_geral(receitas, despesas)


# ============================================================
# Exercicio 29 - Processador Numerico e Ordenacao Manual
# ============================================================
# def ler_lista_inteiros():
#     lista = []
#     while True:
#         valor = int(input("Digite um numero (0 para encerrar): "))
#         if valor == 0:
#             break
#         lista.append(valor)
#     return lista
#
#
# def filtrar_pares(lista):
#     return [numero for numero in lista if numero % 2 == 0]
#
#
# def filtrar_impares(lista):
#     return [numero for numero in lista if numero % 2 != 0]
#
#
# def ordenar_lista_manual(lista):
#     # Bubble sort: compara pares vizinhos e troca de posicao quando
#     # estao fora de ordem, repetindo ate a lista ficar toda ordenada
#     lista_ordenada = lista.copy()
#     n = len(lista_ordenada)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if lista_ordenada[j] > lista_ordenada[j + 1]:
#                 lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
#     return lista_ordenada
#
#
# def exibir_resumo_processamento(original, pares, impares, ordenada):
#     print("===== RESUMO DO PROCESSAMENTO =====")
#     print(f"Lista original: {original}")
#     print(f"Numeros pares: {pares}")
#     print(f"Numeros impares: {impares}")
#     print(f"Lista ordenada: {ordenada}")
#
#
# original = ler_lista_inteiros()
# pares = filtrar_pares(original)
# impares = filtrar_impares(original)
# ordenada = ordenar_lista_manual(original)
# exibir_resumo_processamento(original, pares, impares, ordenada)


# ============================================================
# Exercicio 30 - Gerenciador de Tabela de Campeonato
# ============================================================
# def cadastrar_times():
#     times = {}
#     for i in range(4):
#         nome = input(f"Digite o nome do time {i + 1}: ")
#         times[nome] = {'pontos': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0}
#     return times
#
#
# def calcular_pontuacao(vitorias, empates):
#     # Regra do futebol: 3 pontos por vitoria e 1 ponto por empate
#     return vitorias * 3 + empates * 1
#
#
# def registrar_partida(times_dict):
#     nomes = list(times_dict.keys())
#     print("Times disponiveis:", nomes)
#     time_a = input("Digite o nome do primeiro time: ")
#     time_b = input("Digite o nome do segundo time: ")
#     gols_a = int(input(f"Gols de {time_a}: "))
#     gols_b = int(input(f"Gols de {time_b}: "))
#
#     if gols_a > gols_b:
#         times_dict[time_a]['vitorias'] += 1
#         times_dict[time_b]['derrotas'] += 1
#     elif gols_b > gols_a:
#         times_dict[time_b]['vitorias'] += 1
#         times_dict[time_a]['derrotas'] += 1
#     else:
#         times_dict[time_a]['empates'] += 1
#         times_dict[time_b]['empates'] += 1
#
#     # Recalcula os pontos dos dois times envolvidos na partida
#     for time in (time_a, time_b):
#         vitorias = times_dict[time]['vitorias']
#         empates = times_dict[time]['empates']
#         times_dict[time]['pontos'] = calcular_pontuacao(vitorias, empates)
#
#     return times_dict
#
#
# def ordenar_classificacao(times_list):
#     # Ordena do maior para o menor numero de pontos (reverse=True)
#     return sorted(times_list, key=lambda item: item[1]['pontos'], reverse=True)
#
#
# def exibir_tabela_campeonato(times_ordenados):
#     print("===== TABELA DO CAMPEONATO =====")
#     print(f"{'Pos':4}{'Time':15}{'Pts':5}{'V':4}{'E':4}{'D':4}")
#     for posicao, (nome, dados) in enumerate(times_ordenados, start=1):
#         print(f"{posicao:<4}{nome:15}{dados['pontos']:<5}{dados['vitorias']:<4}{dados['empates']:<4}{dados['derrotas']:<4}")
#
#
# times = cadastrar_times()
# while True:
#     times = registrar_partida(times)
#     continuar = input("Registrar outra partida? [S/N]: ").strip().upper()
#     if continuar != 'S':
#         break
#
# classificacao = ordenar_classificacao(list(times.items()))
# exibir_tabela_campeonato(classificacao)


# ============================================================
# Exercicio 31 - Sistema Interativo de Ajuda do Python
# ============================================================
# def exibir_titulo(msg, simbolo='~'):
#     margem = 4
#     largura = len(msg) + margem
#     moldura = simbolo * largura
#     print(moldura)
#     print(msg.center(largura))
#     print(moldura)
#
#
# def validar_comando(comando):
#     # strip() remove espacos; se sobrar algo, o comando nao esta vazio
#     return comando.strip() != ""
#
#
# def obter_ajuda(funcao_ou_biblioteca):
#     # help() e uma funcao nativa do Python que mostra a documentacao
#     try:
#         help(funcao_ou_biblioteca)
#     except Exception:
#         print("Nao foi possivel encontrar ajuda para esse comando.")
#
#
# def exibir_menu_opcoes():
#     print("Digite o nome de uma funcao/biblioteca do Python para ver a ajuda")
#     print("ou digite 'FIM' para encerrar o programa.")
#     return input("Comando: ")
#
#
# def executar_sistema_ajuda():
#     exibir_titulo("SISTEMA DE AJUDA DO PYTHON")
#     while True:
#         comando = exibir_menu_opcoes()
#         if comando.strip().upper() == 'FIM':
#             print("Encerrando o sistema de ajuda...")
#             break
#         if validar_comando(comando):
#             obter_ajuda(comando)
#         else:
#             print("Comando invalido! Digite algo antes de continuar.")
#
#
# executar_sistema_ajuda()


# ============================================================
# Exercicio 32 - Sistema de Urna Eletronica e Apuracao de Votos
# ============================================================
# def inicializar_urna():
#     # Dicionario com os contadores de votos zerados no inicio
#     return {
#         'Candidato 1': 0,
#         'Candidato 2': 0,
#         'Nulos': 0,
#         'Brancos': 0
#     }
#
#
# def registrar_voto(urna, opcao):
#     if opcao in urna:
#         urna[opcao] += 1
#     else:
#         # Qualquer opcao nao reconhecida conta como voto nulo
#         urna['Nulos'] += 1
#     return urna
#
#
# def calcular_percentual(votos_opcao, total_votos):
#     if total_votos == 0:
#         return 0
#     return (votos_opcao / total_votos) * 100
#
#
# def determinar_vencedor(urna):
#     # Remove Nulos e Brancos da disputa, deixando so os candidatos validos
#     candidatos = {chave: valor for chave, valor in urna.items() if chave not in ('Nulos', 'Brancos')}
#     # key=candidatos.get diz para max() comparar pelos valores (votos) do dicionario
#     vencedor = max(candidatos, key=candidatos.get)
#     return vencedor
#
#
# def exibir_boletim_urna(urna):
#     total_votos = sum(urna.values())
#     print("===== BOLETIM DE APURACAO =====")
#     for opcao, votos in urna.items():
#         percentual = calcular_percentual(votos, total_votos)
#         print(f"{opcao:15}: {votos:4} votos ({percentual:.2f}%)")
#
#     vencedor = determinar_vencedor(urna)
#     print(f"\nVencedor da eleicao: {vencedor}")
#
#
# urna = inicializar_urna()
# while True:
#     opcao = input("Digite a opcao de voto (Candidato 1, Candidato 2, Nulos, Brancos) ou 'FIM': ")
#     if opcao.strip().upper() == 'FIM':
#         break
#     urna = registrar_voto(urna, opcao)
#
# exibir_boletim_urna(urna)

