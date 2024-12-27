from pulp import* 

def ler_input():
  num_brinquedos, num_pacotes, max_producao = map(int, input().split())
  brinquedos = []
  pacotes = []
  restricoes = [[]]
  for _ in range(num_brinquedos):
    lucro, capacidade = map(int, input().split())
    brinquedos.append((lucro, capacidade))
    restricoes.append([])
  for _ in range(num_pacotes):
    primeiro, segundo, terceiro, lucro_pacote = map(int, input().split())
    pacotes.append(((primeiro, segundo, terceiro), lucro_pacote))
    restricoes[primeiro].append(_)
    restricoes[segundo].append(_)
    restricoes[terceiro].append(_)
  return num_brinquedos, num_pacotes, max_producao, brinquedos, pacotes, restricoes

def resolver_problema(num_brinquedos, num_pactoes, max_producao, brinquedos, pacotes, restricoes):
  problema = LpProblem("Otimizacao_de_Lucro", LpMaximize)
  x = [LpVariable(f"brinquedo_{i}", lowBound=0, upBound=brinquedos[i][1], cat="Integer") for i in range(num_brinquedos)]
  y = [LpVariable(f"pacote_{i}", lowBound=0, cat="Integer") for i in range(num_pactoes)]
  
  for i in range(num_brinquedos):
    problema += x[i] + lpSum(y[j] for j in restricoes[i+1]) <= brinquedos[i][1]
  problema += lpSum(pacotes[i][1] * y[i] for i in range(num_pactoes)) + lpSum(brinquedos[i][0] * x[i] for i in range(num_brinquedos))
  problema += lpSum(x[i] for i in range(num_brinquedos)) + lpSum(3*y[i] for i in range(num_pacotes))  <= max_producao 
  
  problema.solve(GLPK(msg=0))
  print(value(problema.objective))
  
num_brinquedos, num_pacotes, max_producao, brinquedos, pacotes, restricoes = ler_input()
resolver_problema(num_brinquedos, num_pacotes, max_producao, brinquedos, pacotes, restricoes)
