# 🧠 Analisador de Pontos Críticos em Redes de Comunicação
##
<p align="center">
  <img src=<img width="1201" height="679" alt="image" src="Rede_de_Comunicação.png"/>
</p>

## 👥 Integrantes
- **ANTÔNIO FELIPE COSTA DE FREITAS**
- **JOÃO VITOR DE ALMEIDA SILVA** 



## 📋 Descrição do Projeto
Este projeto foi desenvolvido para a disciplina **ESTRUTURA DE DADOS AVANÇADA - UNIVERSIDADE ESTADUAL DO MARANHÃO**.  
O objetivo é **analisar redes de comunicação** representadas por grafos não-dirigidos, permitindo verificar conexões entre roteadores e identificar **pontos críticos (vértices de articulação)** cuja falha pode desconectar partes da rede.

O projeto utiliza uma **lista de adjacência** como estrutura de dados principal, oferecendo operações básicas de manipulação de grafos e **visualização gráfica** com a biblioteca `NetworkX`.


## ⚙️ Funcionalidades Implementadas
- Leitura de um grafo a partir de um arquivo `.txt`
- Construção de **lista de adjacência**
- Impressão da estrutura do grafo
- Verificação de **adjacência** entre dois vértices
- Cálculo do **grau de um vértice**
- Listagem de **vizinhos**
- Exibição de **todas as arestas**
- **Plotagem visual** do grafo com `NetworkX` e `Matplotlib`


## 🧩 Estrutura do Projeto
```text
Analisador de Pontos Criticos

─ grafo 1.txt   # Arquivo de entrada do grafo
─ grafo.py      # Implementação principal com lista de adjacência
─ README.md     # Este arquivo
```

## 📄 Exemplo de Arquivo de Entrada (`grafo 1.txt`)
```text
ND
S1 PC0
S1 PC1
S1 PC2
S1 R1
S2 PC3
S2 PC4
S2 PC5
S2 R1
S3 PC6
S3 PC7
S3 PC8
S3 R4

R0 R1
R0 R2
R0 R3
R0 R4
```
A primeira linha indica o **tipo do grafo**:
- ND → Não-dirigido    
- As linhas seguintes representam as **arestas** (conexões entre os vértices).


## ▶️ Como Executar o Projeto

###

## 🖼️ Visualização
O programa gera uma visualização da rede mostrando:
- **Nós**: roteadores, switches e PCs.
- **Arestas**: conexões entre eles.  
- O grafo é desenhado automaticamente em uma janela interativa.



## 📚 Referências
-
