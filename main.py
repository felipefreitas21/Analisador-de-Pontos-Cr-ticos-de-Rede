import grafo as gr

arquivo = "grafo 1.txt"

tipo, arestas = gr.ler_arquivo(arquivo)
if tipo != "D":
    grafo = gr.construir_grafo(arestas) 

    i = 1

    while i >= 1 and i <= 4: 
        i = int(input("1. Funções Básicas \n2. Vizualizar Lista Adjacência \n3. Vizualizar Grafo\n4. Indentificar Pontos Críticos \n"))
        if i == 1: 
            j = int(input("1. Listas Arestas \n2. Listar Vizinhos \n3. Calcular Grau \n4. Verificar Adjacências\n "))
            if j == 1:
                gr.listar_arestas(arestas)

            if j == 2: 
                vertice = input("Informe o vértice que você deseja visualizar os vizinhos: ").upper()
                gr.listar_vizinhos(grafo, vertice)

            if j == 3:
                vertice = input("Informe o vértice: ").upper()
                gr.calcular_grau(grafo, vertice)

            if j == 4:
                vertice1 = input("Informe o primeiro vértice: ").upper()
                vertice2 = input("Informe o segundo vértice: ").upper()
                if vertice1 in grafo.keys() and vertice2 in grafo.keys():
                    if gr.ver_adj(grafo, vertice1, vertice2) == True:
                        print("São adjacentes")
                    else:
                        print("Não são adjacentes")
                else:
                    print("Informe vértices que existam no grafo.")

        if i == 2: 
            gr.imprimir_listadj(grafo)
        if i == 3: 
            gr.plotar_grafo(grafo)
        if i == 4:
            criticos = gr.identificar_criticos(grafo)
            print(f"Os pontos críticos são: {criticos}")
            gr.plotar_grafo_criticos(grafo, criticos)

            decisao = input("Deseja visualizar o grafo após a remoção de algum ponto crítico?[S/N]\n").upper()
            if decisao == "S" or decisao == "SIM":
                remocao = input(f"Esolha o ponto crítico que deseja remover {criticos}:\n").upper()
                if remocao in criticos:
                    if gr.remover_criticos(grafo, remocao)!=False: 
                        copia = gr.remover_criticos(grafo, remocao)
                        print("Após a remoção:")
                        gr.imprimir_listadj(copia)
                        gr.plotar_grafo(copia)
                else:
                    print("Informe um ponto criítico!")
else:
    print("Este grafo não representa uma rede de comunicação, pois ele é dirigido!")
        


        
    

