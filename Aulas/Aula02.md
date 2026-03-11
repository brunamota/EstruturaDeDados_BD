# Aula 02 - Estruturas de Dados Lineares: Pilhas, Filas, Deques e Listas

Nesta aula, avançaremos no estudo das estruturas lineares. Entenderemos as regras de acesso (LIFO e FIFO), a flexibilidade dos Deques e a importância das Listas Encadeadas para a manipulação eficiente de grandes volumes de dados.

## 1. Pilha (Stack) - Regra LIFO

As pilhas são estruturas dinâmicas que possuem duas extremidades: o **TOPO** e a **BASE**. Elas funcionam sob a regra **LIFO** (*Last In, First Out*), onde o último elemento a entrar é obrigatoriamente o primeiro a sair.

* **Inserção e Remoção:** Ambas ocorrem exclusivamente pela extremidade do TOPO.
* **Aplicações:** Comandos "Desfazer" (Undo) em editores, histórico de navegação (Voltar) e controle de fluxo de funções no sistema operacional.
* **Implementação Básica:**

```python
pilha = []

pilha.append("A") # Empilha (Push)
pilha.append("B") # Empilha (Push)
pilha.append(2) # Empilha (Push)

print(pilha)

print(pilha.pop()) # Desempilha (Pop) -> Saída: "B"

print(pilha)

```

## 2. Fila (Queue) - Regra FIFO

Diferente da pilha, a fila permite a inserção por um lado (retaguarda/fim) e a remoção pelo outro (início). Segue a regra **FIFO** (*First In, First Out*): o primeiro que entra é o primeiro que sai.

* **Funcionamento:** Sempre que adicionamos um elemento, movemos o ponteiro da retaguarda; ao remover, movemos o ponteiro do início.
* **Aplicações:** Filas de impressão, atendimento em call centers e roteamento de pacotes em rede.
* **Implementação Básica:**

```python
fila = []

fila.append(10) # Enfileira
fila.append(20) # Enfileira
fila.append(30) # Enfileira
fila.append(40) # Enfileira

print(fila)

print(fila.pop(0)) # Desenfileira o primeiro elemento -> Saída: 10

print(fila)

```

## 3. Deque (Double-Ended Queue)

O Deque é uma estrutura "híbrida" que generaliza as pilhas e filas, permitindo inserções e remoções em **ambas as extremidades**.
* **Flexibilidade:** Novos itens podem ser adicionados ou removidos tanto no início quanto no fim.
* **Performance:** É altamente recomendado o uso do módulo `collections.deque` em Python, pois ele oferece complexidade **$O(1)$** para operações nas extremidades, enquanto listas comuns podem ser **$O(n)$**.
* **Exemplo com `collections`:**

```python
from collections import deque

# Inicializando o Deque
d = deque([10, 20, 30])
d.append('Fim') # Adiciona à direita
d.appendleft('Início') # Adiciona à esquerda
print(d)

# 1. Remoção pela direita (Final)
ultimo = d.pop()
print(f"Removido da direita: {ultimo}") # Saída: Fim

# 2. Remoção pela esquerda (Início)
primeiro = d.popleft()
print(f"Removido da esquerda: {primeiro}") # Saída: Inicio

print(f"Estado final do Deque: {d}")

```

## 4. Listas Encadeadas Simples

A lista simplesmente encadeada é uma relação de elementos chamados **nodos**, interligados entre si. É o primeiro passo para manipular grandes quantidades de dados sem depender de bibliotecas prontas.

* **Estrutura do Nodo:** Cada elemento contém o dado (conteúdo) e o endereço (elo) para o próximo nodo.
* **Diferencial:** Não exige que os dados estejam em endereços contíguos na memória.

### 4.1. Estrutura Base: Nodo e Lista

Antes das operações, definimos a estrutura do **Nodo** (que guarda o dado e o elo) e da **Lista** (que guarda a referência do início).

```python
class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        # Armazena o conteúdo (pode ser primitivo ou objeto)
        self.conteudo = dado
        # Armazena o endereço/ponteiro para o próximo elemento
        self.proximo = proximo_nodo
class ListaEncadeada:
    def __init__(self):
        # A lista nasce vazia, com o ponteiro de início apontando para None 
        self.inicio = None
```

### 4.2. Operações de Inserção

* **Adicionar no Início:** O novo nodo aponta para o atual `inicio`, e a lista passa a ter esse novo nodo como primeiro elemento.
* **Adicionar no Fim:** Percorremos a lista com um laço `while` até encontrar o último elemento (cujo `proximo` é `None`) e conectamos o novo nodo ali.
* **Adicionar em Posição Específica:** Navegamos até a posição anterior à desejada e ajustamos os ponteiros para "abrir espaço" e inserir o novo elo.

```python
 def adicionar_inicio(self, novo_nodo):
        """O novo nodo aponta para o atual início e assume o posto de primeiro"""
        novo_nodo.proximo = self.inicio
        self.inicio = novo_nodo

    def adicionar_fim(self, novo_nodo):
        """Percorre até o último elemento e conecta o novo nodo ali."""
        if self.esta_vazia():
            self.inicio = novo_nodo
        else:
            aux = self.inicio
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = novo_nodo

    def adicionar_posicao(self, novo_nodo, pos):
        """Navega até a posição anterior e ajusta os elos para inserir o novo."""
        if pos == 0:
            self.adicionar_inicio(novo_nodo)
        else:
            atual = self.inicio
            pos_atual = 0
            while atual is not None and pos_atual < (pos - 1):
                atual = atual.proximo
                pos_atual += 1

            if atual is not None:
                novo_nodo.proximo = atual.proximo
                atual.proximo = novo_nodo

```

### 4.3. Operações de Remoção

* **Remover do Início:** Basta atualizar o ponteiro de `inicio` para que ele aponte para o segundo elemento da lista (`atual.proximo`).
* **Remover do Fim:** Percorremos a lista até o penúltimo nodo e definimos o seu campo `proximo` como `None`, descartando o último elo.
* **Remover por Posição:** Localizamos o nodo anterior ao que será removido e fazemos com que ele aponte diretamente para o sucessor do excluído, "pulando" o elemento indesejado.

```python
    def remover_inicio(self):
        """Atualiza o início para o segundo elemento da lista"""
        if not self.esta_vazia():
            self.inicio = self.inicio.proximo

    def remover_fim(self):
        """Percorre até o penúltimo nodo e remove o elo com o último"""
        if self.esta_vazia():
            return
        if self.inicio.proximo is None:
            self.inicio = None
        else:
            atual = self.inicio
            while atual.proximo.proximo is not None:
                atual = atual.proximo
            atual.proximo = None

    def remover_posicao(self, pos):
        """Localiza o anterior e 'pula' o nodo da posição desejada"""
        if self.esta_vazia():
            return
        if pos == 0:
            self.remover_inicio()
        else:
            atual = self.inicio
            pos_atual = 0
            while atual.proximo is not None and pos_atual < (pos - 1):
                atual = atual.proximo
                pos_atual += 1

            if atual.proximo is not None:
                proximo_nodo = atual.proximo.proximo
                atual.proximo = proximo_nodo

```

### 4.4. Operações de Acesso e Consulta

* **Verificar se está Vazia:** Retorna `True` se o ponteiro de `inicio` for `None`.
* **Tamanho da Lista:** Iniciamos um contador em zero e percorremos todos os nodos incrementando o valor até chegar ao fim.
* **Contar Ocorrências:** Percorre a lista comparando o conteúdo de cada nodo com o valor buscado, somando cada vez que houver uma igualdade.

```python
    def esta_vazia(self):
        """Retorna True se o ponteiro de início for None."""
        return self.inicio is None

    def tamanho(self):
        """Percorre a lista contando os nodos até encontrar None."""
        atual = self.inicio
        cont = 0
        while atual is not None:
            cont += 1
            atual = atual.proximo
        return cont

    def contar_ocorrencias(self, valor):
        """Percorre a lista somando cada vez que o valor é encontrado"""
        atual = self.inicio
        total = 0
        while atual is not None:
            if atual.conteudo == valor:
                total += 1
            atual = atual.proximo
        return total
```

### 4.4. Implementação Completa

```python
class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.conteudo = dado
        self.proximo = proximo_nodo


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    # OPERAÇÕES DE CONSULTA
    def esta_vazia(self):
        """Retorna True se o ponteiro de início for None."""
        return self.inicio is None

    def tamanho(self):
        """Percorre a lista contando os nodos até encontrar None."""
        atual = self.inicio
        cont = 0
        while atual is not None:
            cont += 1
            atual = atual.proximo
        return cont

    def contar_ocorrencias(self, valor):
        """Percorre a lista somando cada vez que o valor é encontrado"""
        atual = self.inicio
        total = 0
        while atual is not None:
            if atual.conteudo == valor:
                total += 1
            atual = atual.proximo
        return total

    # --- OPERAÇÕES DE INSERÇÃO ---
    def adicionar_inicio(self, novo_nodo):
        """O novo nodo aponta para o atual início e assume o posto de primeiro."""
        novo_nodo.proximo = self.inicio
        self.inicio = novo_nodo

    def adicionar_fim(self, novo_nodo):
        """Percorre até o último elemento e conecta o novo nodo ali"""
        if self.esta_vazia():
            self.inicio = novo_nodo
        else:
            aux = self.inicio
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = novo_nodo

    def adicionar_posicao(self, novo_nodo, pos):
        """Navega até a posição anterior e ajusta os elos para inserir o novo."""
        if pos == 0:
            self.adicionar_inicio(novo_nodo)
        else:
            atual = self.inicio
            pos_atual = 0
            while atual is not None and pos_atual < (pos - 1):
                atual = atual.proximo
                pos_atual += 1

            if atual is not None:
                novo_nodo.proximo = atual.proximo
                atual.proximo = novo_nodo

    # --- OPERAÇÕES DE REMOÇÃO ---

    def remover_inicio(self):
        """Atualiza o início para o segundo elemento da lista"""
        if not self.esta_vazia():
            self.inicio = self.inicio.proximo

    def remover_fim(self):
        """Percorre até o penúltimo nodo e remove o elo com o último"""
        if self.esta_vazia():
            return
        if self.inicio.proximo is None:
            self.inicio = None
        else:
            atual = self.inicio
            while atual.proximo.proximo is not None:
                atual = atual.proximo
            atual.proximo = None

    def remover_posicao(self, pos):
        """Localiza o anterior e 'pula' o nodo da posição desejada"""
        if self.esta_vazia():
            return
        if pos == 0:
            self.remover_inicio()
        else:
            atual = self.inicio
            pos_atual = 0
            while atual.proximo is not None and pos_atual < (pos - 1):
                atual = atual.proximo
                pos_atual += 1

            if atual.proximo is not None:
                proximo_nodo = atual.proximo.proximo
                atual.proximo = proximo_nodo

    def imprimir(self):
        atual = self.inicio
        elementos = []
        while atual:
            elementos.append(str(atual.conteudo))
            atual = atual.proximo
        print(" -> ".join(elementos) + " -> None")


# --- TESTE PRÁTICO ---
lista = ListaEncadeada()
lista.adicionar_inicio(Nodo("B"))
lista.adicionar_inicio(Nodo("A"))  # A -> B
lista.adicionar_fim(Nodo("C"))  # A -> B -> C
lista.adicionar_posicao(Nodo("X"), 1)  # A -> X -> B -> C

print(f"Tamanho: {lista.tamanho()}")  # Saída: 4
lista.imprimir()

lista.remover_posicao(1)  # Remove "X"
lista.imprimir()  # Saída: A -> B -> C -> None

```

### Tabela de Comparação: Lista Nativa vs. Lista Encadeada

| Operação | Lista Python (Vetor) | Lista Encadeada |
| --- | --- | --- |
| **Inserção no Início** | Lenta (precisa deslocar todos) | Rápida (ajusta 1 ponteiro) |
| **Acesso por Índice** | Direto e Instantâneo | Precisa percorrer desde o início |
| **Memória** | Contígua (espaço reservado) | Espalhada (ligada por elos) |


## 5. Resumo de Complexidade e Performance

| Estrutura | Regra | Acesso | Performance (Python) |
| --- | --- | --- | --- |
| **Pilha** | LIFO | Unilateral (Topo) | Lista: $O(1)$ para append/pop |
| **Fila** | FIFO | Bilateral (Início/Fim) | Lista: $O(n)$ no pop(0) |
| **Deque** | Híbrida | Bilateral (Início/Fim) | <br>`deque`: $O(1)$ em ambas pontas |
| **Lista Encadeada** | Linear | Sequencial | Inserção rápida, busca $O(n)$ |

### Exercício de Fixação

Com base no conceito de **Fila (FIFO)**, implemente um pequeno sistema em Python que simule o gerenciamento de decolagem em um aeroporto. O sistema deve permitir adicionar aviões à fila de espera e autorizar a decolagem do avião que chegou primeiro.

```python
class ControleDecolagem:
    def __init__(self):
        # Inicializa uma fila vazia utilizando uma lista Python [cite: 1378]
        self.__fila_espera = []

    def adicionar_aviao(self, identificacao):
        """
        Operação Enfileirar: Adiciona um avião ao final da fila (retaguarda).
        """
        self.__fila_espera.append(identificacao) # [cite: 1386]
        print(f"✈️  Avião {identificacao} entrou na fila de espera.")

    def autorizar_decolagem(self):
        """
        Operação Desenfileirar: Remove e retorna o avião do início da fila (regra FIFO).
        """
        if not self.esta_vazia():
            # Remove o elemento no índice 0 (o primeiro que entrou) [cite: 1388]
            aviao = self.__fila_espera.pop(0)
            print(f"✅ Decolagem AUTORIZADA para o avião: {aviao}")
            return aviao
        else:
            print("⚠️  Atenção: Não há aviões na fila de espera!") # [cite: 1388]
            return None

    def listar_espera(self):
        """Retorna a quantidade de aviões aguardando."""
        return len(self.__fila_espera) # [cite: 1384]

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.__fila_espera) == 0 # [cite: 1381]

# --- SIMULAÇÃO PRÁTICA ---

aeroporto = ControleDecolagem()

# Aviões chegando para a pista
aeroporto.adicionar_aviao("PR-ABC")
aeroporto.adicionar_aviao("PT-XYZ")
aeroporto.adicionar_aviao("GOL-123")

print(f"\nAviões aguardando: {aeroporto.listar_espera()}")

# Autorizando decolagens (seguindo a ordem de chegada)
aeroporto.autorizar_decolagem() # Deve autorizar o PR-ABC
aeroporto.autorizar_decolagem() # Deve autorizar o PT-XYZ

print(f"\nAviões restantes na fila: {aeroporto.listar_espera()}")

```

