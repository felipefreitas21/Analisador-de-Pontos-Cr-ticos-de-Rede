import grafo as gr

arquivo = "grafo 1.txt"

tipo, arestas = gr.ler_arquivo(arquivo)
if tipo == "D":
    dirigido = True
else:
    dirigido = False

grafo = gr.construir_grafo(arestas, dirigido)  #construção do grafo

i = 1

while i >= 1 and i <= 3: 
    i = int(input("1. Funções Básicas \n2. Vizualizar Lista Adjacência \n3. Vizualizar Grafo\n4. Indentificar Pontos Críticos \n5. Vizualizar Remoção de ponto crítico\n"))
    if i == 1: 
        j = int(input("1. Listas Arestas \n2. Listar Vizinhos \n3. Calcula1r Grau \n4. Verificar Adjacências\n "))
        if j == 1:
            gr.listar_arestas(arestas) #listar arestas

        if j == 2: #listar vizinhos
            vertice = input("Informe o vértice que você deseja visualizar os vizinhos: ").upper()
            gr.listar_vizinhos(grafo, vertice)

        if j == 3: #calcular grau
            vertice = input("Informe o vértice: ").upper()
            gr.calcular_grau(grafo, vertice)

        if j == 4: #Verificar adjacências
            vertice1 = input("Informe o primeiro vértice: ").upper()
            vertice2 = input("Informe o segundo vértice: ").upper()
            if vertice1 in grafo.keys() and vertice2 in grafo.keys():
                if gr.ver_adj(grafo, vertice1, vertice2) == True:
                    print("São adjacentes")
                else:
                    print("Não são adjacentes")
            else:
                print("Informe vértices que existam no grafo.")

    if i == 2: #imprimir lista de adjacência
        gr.imprimir_listadj(grafo)
    if i == 3: #plotar grafo real
        gr.plotar_grafo(grafo, dirigido)
    if i == 4: #indentificar pontos crítico
        criticos = gr.indentificar_criticos(grafo)
        print(f"Os pontos críticos são: {criticos}")
        gr.plotar_grafo_criticos(grafo, criticos)

    if i == 5:
        vertice = (input("Escolha os pontos críticos : S1, S2, S3, S4, S5, S6, S7, S8, R0, R1, R2, R3, R4\n")).upper()
        if gr.remover_criticos(grafo, vertice) != False:
            copia = gr.remover_criticos(grafo, vertice)
            gr.imprimir_listadj(copia)
            gr.plotar_grafo(copia, dirigido)
        else:
            print("Tente novamente. Informe um ponto crítico")
    

