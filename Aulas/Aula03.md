# Aula 03 - Listas Duplas, Pesquisa e Ordenação de Dados

## Recapitulação: Listas Encadeadas Simples

Uma Lista Encadeada Simples é uma estrutura onde cada elemento (Nodo) conhece apenas o seu valor e o endereço do próximo elemento.
* **Vantagem:** Inserção e remoção rápidas no início ($O(1)$).
* **Desvantagem:** Para encontrar um item, precisamos de uma Pesquisa Sequencial, pois não há acesso direto por índice como nos vetores.

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

```python
def pesquisa_sequencial(lista_encadeada, alvo):
    """Percorre a lista do início ao fim."""
    atual = lista_encadeada.inicio
    posicao = 0
    
    while atual is not None:
        if atual.conteudo == alvo:
            return f"Sucesso: '{alvo}' encontrado na posição {posicao}"
        atual = atual.proximo
        posicao += 1
        
    return "Erro: Elemento não encontrado"
```

### 2.2 Pesquisa Binária
Divide a lista (que deve estar **ordenada**) ao meio repetidamente.
* **Complexidade:** $O(\log n)$.
* **Eficiência:** Em 1 milhão de itens, encontra qualquer valor em no máximo 20 tentativas.

 ```python
def pesquisa_binaria(dados_ordenados, alvo):
    """Divide a lista ao meio sucessivamente."""
    inicio = 0
    fim = len(dados_ordenados) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if dados_ordenados[meio] == alvo:
            return f"Sucesso: Encontrado no índice {meio}"
        elif dados_ordenados[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return "Erro: Não encontrado"
```

### 2.3 Tabelas Hash (Cálculo de Endereço)
Usa uma função matemática (Hash) para gerar um índice direto para o dado.
* **Complexidade:** $O(1)$ (Acesso quase instantâneo).
* **Conceito:** É a base dos dicionários em Python.

```python
# Simulando uma Tabela Hash de Funcionários
tabela_hash_empresa = {
    "ID-101": "Bruna Mota",
    "ID-102": "Analista de Dados",
    "ID-103": "Engenheiro de ML"
}

def pesquisa_hash(id_busca):
    """Acesso direto ao endereço do dado."""
    # O método .get evita erros se a chave não existir
    return tabela_hash_empresa.get(id_busca, "ID inexistente")

# Teste de Velocidade Instantânea
print(f"Resultado da busca: {pesquisa_hash('ID-101')}")
```

## 3. Ordenação de Dados
Ordenar é fundamental para permitir buscas rápidas e análise de dados.

### 3.1 Métodos Simples
* **Bubble Sort (Bolha):** Flutua o maior elemento para o fim a cada iteração. Ineficiente para grandes volumes.

```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # O último elemento já está no lugar, então não precisamos olhar para ele
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Troca os elementos de lugar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Exemplo: [5, 3, 8, 2] -> [3, 5, 2, 8] -> [3, 2, 5, 8] -> [2, 3, 5, 8]
```

* **Selection Sort:** Seleciona o menor item e o coloca na primeira posição disponível.

```python
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Troca o menor encontrado com o primeiro elemento da parte não ordenada
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista
```

* **Insertion Sort:** Como organizar cartas de baralho; insere cada item na posição correta em relação aos anteriores.

```python
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Move os elementos que são maiores que a chave para uma posição à frente
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista
```

### 3.2 Métodos Eficientes (Dividir para Conquistar)
* **Quicksort:** Escolhe um **pivô** e organiza os dados: menores à esquerda, maiores à direita. É um dos mais rápidos na prática.

```python
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[len(lista) // 2]
        esquerda = [x for x in lista if x < pivo]
        meio = [x for x in lista if x == pivo]
        direita = [x for x in lista if x > pivo]
        return quicksort(esquerda) + meio + quicksort(direita)

# Saída de exemplo para [10, 5, 2, 3]: [2, 3, 5, 10]
```

* **Mergesort:** Divide a lista em unidades mínimas e as recombina (merge) de forma ordenada. Muito estável e usado em processamento paralelo.

```python
def mergesort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esq = lista[:meio]
        dir = lista[meio:]

        mergesort(esq)
        mergesort(dir)

        i = j = k = 0
        # Mesclagem (Merge)
        while i < len(esq) and j < len(dir):
            if esq[i] < dir[j]:
                lista[k] = esq[i]
                i += 1
            else:
                lista[k] = dir[j]
                j += 1
            k += 1
        
        # Garante que nenhum elemento ficou para trás
        while i < len(esq):
            lista[k] = esq[i]
            i += 1
            k += 1
        while j < len(dir):
            lista[k] = dir[j]
            j += 1
            k += 1
    return lista
```

## 4. Comparativo de Complexidade

| Algoritmo | Melhor Caso | Pior Caso | Recomendação |
| :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | Apenas para fins didáticos. |
| **Quicksort** | $O(n \log n)$ | $O(n^2)$ | Uso geral e alta performance. |
| **Mergesort** | $O(n \log n)$ | $O(n \log n)$ | Quando a estabilidade é crítica. |
| **Busca Binária**| $O(1)$ | $O(\log n)$ | Sempre que os dados estiverem ordenados. |
