# Aula 03 - Listas Duplas, Pesquisa e Ordenação de Dados

## 1. Listas Encadeadas Duplas
Diferente da lista simples, a lista encadeada dupla possui nodos com **dois ponteiros**: um para o próximo elemento (`proximo`) e outro para o anterior (`anterior`). 

* **Vantagem:** Permite percorrer a lista em ambas as direções (frente e trás). Facilitam a remoção de elementos, pois o nodo sabe quem é o seu antecessor.
* **Aplicações:** Playlists de música (Voltar/Avançar), histórico de navegadores e editores de texto.

```python
class NodoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None # Diferencial da lista dupla
```

## 2. Métodos de Pesquisa em Listas
A eficiência na busca é crucial quando lidamos com o volume de dados do Big Data.

### 2.1 Pesquisa Sequencial
Percorre a lista do início ao fim até encontrar o elemento.
* **Complexidade:** $O(n)$.
* **Uso:** Listas pequenas ou não ordenadas.

### 2.2 Pesquisa Binária
Divide a lista (que deve estar **ordenada**) ao meio repetidamente.
* **Complexidade:** $O(\log n)$.
* **Eficiência:** Em 1 milhão de itens, encontra qualquer valor em no máximo 20 tentativas.

### 2.3 Tabelas Hash (Cálculo de Endereço)
Usa uma função matemática (Hash) para gerar um índice direto para o dado.
* **Complexidade:** $O(1)$ (Acesso quase instantâneo).
* **Conceito:** É a base dos dicionários em Python.

## 3. Ordenação de Dados (Sorting)
Ordenar é fundamental para permitir buscas rápidas e análise de dados.

### 3.1 Métodos Simples
* **Bubble Sort (Bolha):** Flutua o maior elemento para o fim a cada iteração. Ineficiente para grandes volumes.
* **Selection Sort:** Seleciona o menor item e o coloca na primeira posição disponível.
* **Insertion Sort:** Como organizar cartas de baralho; insere cada item na posição correta em relação aos anteriores.

### 3.2 Métodos Eficientes (Dividir para Conquistar)
* **Quicksort:** Escolhe um **pivô** e organiza os dados: menores à esquerda, maiores à direita. É um dos mais rápidos na prática.
* **Mergesort:** Divide a lista em unidades mínimas e as recombina (merge) de forma ordenada. Muito estável e usado em processamento paralelo.

## 4. Implementação Prática: Ordenação e Busca Binária

```python
# Exemplo de Quicksort (Eficiente)
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quicksort(esquerda) + meio + quicksort(direita)

# Exemplo de Busca Binária
def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio # Retorna o índice
        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# Teste
dados = [50, 10, 80, 30, 20]
ordenados = quicksort(dados)
print(f"Dados Ordenados: {ordenados}") # Saída: [10, 20, 30, 50, 80]

pos = busca_binaria(ordenados, 30)
print(f"Elemento 30 encontrado na posição: {pos}") # Saída: 2
```

## 5. Comparativo de Complexidade

| Algoritmo | Melhor Caso | Pior Caso | Recomendação |
| :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | Apenas para fins didáticos. |
| **Quicksort** | $O(n \log n)$ | $O(n^2)$ | Uso geral e alta performance. |
| **Mergesort** | $O(n \log n)$ | $O(n \log n)$ | Quando a estabilidade é crítica. |
| **Busca Binária**| $O(1)$ | $O(\log n)$ | Sempre que os dados estiverem ordenados. |
