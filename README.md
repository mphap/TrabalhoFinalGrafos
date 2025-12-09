# Modelagem de Grafos de Contato para Mitigação de Surtos

Este repositório contém a implementação e os experimentos computacionais apresentados no artigo **"Modelagem de Grafos de Contato para Mitigação de Surtos: Identificando Comunidades e Pontes Críticas em Saúde Pública"**.

## 📋 Sobre o Projeto
O objetivo deste projeto é simular a propagação de uma doença infecciosa (Modelo SIR) em uma rede social sintética composta por três comunidades: Escola, Fábrica e Asilo. Utilizamos a Teoria dos Grafos para demonstrar que a identificação e o bloqueio de pontes críticas (arestas com alta centralidade de intermediação) são mais eficazes do que cortes aleatórios.

## 🚀 Tecnologias Utilizadas
* **Python 3**
* **NetworkX:** Para modelagem do grafo e algoritmos de centralidade (Girvan-Newman).
* **Matplotlib:** Para visualização da rede e plotagem dos gráficos.
* **Pandas/Numpy:** Para manipulação de dados e tabelas.

## 📊 Experimentos Realizados
O código executa três cenários de simulação:
1.  **Sem Intervenção:** Propagação livre do vírus.
2.  **Corte Aleatório:** Remoção de arestas randômicas.
3.  **Corte Dirigido (Girvan-Newman):** Remoção das arestas de maior *edge betweenness*.

## 📂 Estrutura dos Arquivos
* `Grafo.ipynb`: Notebook principal com todo o código, geração de grafos e simulações.
* `tabela_experimentos.csv`: Resultados numéricos gerados pela simulação.

##  ▶️ Como Executar
Você pode visualizar e executar este código diretamente no Google Colab clicando no arquivo `.ipynb` acima.

---
**Autor:** Marcus Phablo Pereira de Oliveira
**Instituição:** Instituto de Computação (IComp) - UFAM
