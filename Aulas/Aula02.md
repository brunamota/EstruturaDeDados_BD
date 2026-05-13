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

Antes das operações, definimos a estrutura do **Nodo** (que guarda o dado e o elo) e da **Lista** (que guarda a referência do início). Nesta implementação otimizada, usamos dataclasses para simplificar o Nodo e métodos para que a lista se comporte como uma lista nativa do Python.

```python
from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class Nodo:
    conteudo: Any
    proximo: Optional['Nodo'] = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self._tamanho = 0  # Controle de tamanho O(1)
```

- @dataclass: Em Python, o método __init__ costuma ser repetitivo. A @dataclass gera automaticamente o construtor, o __repr__ (exibição para debug) e comparadores. Isso reduz o código visual e foca no que importa: os dados.

- typing (Any, Optional): Python é uma linguagem dinamicamente tipada, o que pode causar confusão em estruturas de ponteiros. Usar Any indica que o nodo aceita qualquer dado, e Optional['Nodo'] deixa explícito que o campo proximo pode ser um objeto ou None. Isso ajuda ferramentas de autocompletar e evita erros de "ponteiro nulo".

### 4.2. Operações de Inserção

* **Adicionar no Início:** O novo nodo aponta para o atual `inicio`, e a lista passa a ter esse novo nodo como primeiro elemento.
* **Adicionar no Fim:** Percorremos a lista com um laço `while` até encontrar o último elemento (cujo `proximo` é `None`) e conectamos o novo nodo ali.
* **Adicionar em Posição Específica:** Navegamos até a posição anterior à desejada e ajustamos os ponteiros para "abrir espaço" e inserir o novo elo.
* A grande diferença aqui é o Encapsulamento. O usuário da lista não precisa saber que a classe Nodo existe; ele apenas envia o valor, e a lista gerencia a criação dos elos internamente.

```python
def adicionar_inicio(self, valor):
        # Cria o novo nodo apontando para o antigo início
        self.inicio = Nodo(valor, self.inicio)
        self._tamanho += 1

    def adicionar_fim(self, valor):
        if self.esta_vazia():
            self.adicionar_inicio(valor)
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = Nodo(valor)
            self._tamanho += 1

    def adicionar_posicao(self, valor, pos):
        if pos <= 0:
            self.adicionar_inicio(valor)
        elif pos >= self._tamanho:
            self.adicionar_fim(valor)
        else:
            atual = self.inicio
            for _ in range(pos - 1):
                atual = atual.proximo
            # Insere o novo nodo entre 'atual' e 'atual.proximo'
            atual.proximo = Nodo(valor, atual.proximo)
            self._tamanho += 1

```

### 4.3. Operações de Remoção

* **Remover do Início:** Basta atualizar o ponteiro de `inicio` para que ele aponte para o segundo elemento da lista (`atual.proximo`).
* **Remover do Fim:** Percorremos a lista até o penúltimo nodo e definimos o seu campo `proximo` como `None`, descartando o último elo.
* **Remover por Posição:** Localizamos o nodo anterior ao que será removido e fazemos com que ele aponte diretamente para o sucessor do excluído, "pulando" o elemento indesejado.

```python
    def remover_inicio(self):
        if not self.esta_vazia():
            self.inicio = self.inicio.proximo
            self._tamanho -= 1

    def remover_posicao(self, pos):
        if self.esta_vazia(): return
        if pos == 0:
            self.remover_inicio()
        else:
            atual = self.inicio
            for _ in range(pos - 1):
                if atual.proximo is None: break
                atual = atual.proximo
            
            if atual.proximo:
                atual.proximo = atual.proximo.proximo
                self._tamanho -= 1

```

### 4.4. Operações de Acesso e Consulta

* **Verificar se está Vazia:** Retorna `True` se o ponteiro de `inicio` for `None`.
* **Tamanho da Lista:** Iniciamos um contador em zero e percorremos todos os nodos incrementando o valor até chegar ao fim.
* **Contar Ocorrências:** Percorre a lista comparando o conteúdo de cada nodo com o valor buscado, somando cada vez que houver uma igualdade.
* Em vez de criar métodos como lista.contar_elementos(), usamos os Protocolos do Python. Isso faz com que nossa lista encadeada se comporte como uma lista nativa da linguagem.Por que usar Métodos "Mágicos"?Eles permitem que funções nativas do Python (como len(), print() e in) entendam como interagir com a sua estrutura personalizada.
    * __len__: Faz com que len(lista) funcione instantaneamente. Como mantemos o atributo _tamanho, não precisamos percorrer a lista toda para contar (otimização de $O(n)$ para $O(1)$).
    * __iter__: Transforma a lista em um Iterável. Ao usar yield, permitimos que qualquer loop for percorra a lista sem expor os ponteiros internos.
    * __str__: Define como a lista aparece ao ser impressa.

```python
   def esta_vazia(self):
        return self.inicio is None

    def __len__(self):
        """Retorna o tamanho da lista usando len(lista)"""
        return self._tamanho

    def __iter__(self):
        """Permite percorrer a lista com 'for item in lista'"""
        atual = self.inicio
        while atual:
            yield atual.conteudo
            atual = atual.proximo

    def contar_ocorrencias(self, valor):
        """Usa a iteração nativa para contar"""
        return sum(1 for item in self if item == valor)

    def __str__(self):
        """Representação visual automática com print(lista)"""
        return " -> ".join(map(str, self)) + " -> None"
```

### 4.4. Teste Prático

Ao usar esses padrões, seu código se torna "Pythonico": ele é limpo, eficiente e segue as convenções que desenvolvedores experientes utilizam em projetos reais, indo além do básico acadêmico.

```python
# Instanciação
lista = ListaEncadeada()

# Inserção direta de valores (sem precisar instanciar Nodo manualmente)
lista.adicionar_inicio("B")
lista.adicionar_inicio("A")     # A -> B
lista.adicionar_fim("C")        # A -> B -> C
lista.adicionar_posicao("X", 1) # A -> X -> B -> C

# Consulta e Impressão
print(f"Tamanho: {len(lista)}") # Usa o método __len__
print(lista)                    # Usa o método __str__ (Saída: A -> X -> B -> C -> None)

# Busca nativa (funciona por causa do __iter__)
print(f"Existe 'B'? {'B' in lista}") 

# Remoção
lista.remover_posicao(1)        # Remove "X"
print(lista)                    # Saída: A -> B -> C -> None

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
📝 Explicação dos Conceitos Aplicados:
* FIFO (First In, First Out): O avião "PR-ABC" foi o primeiro adicionado, logo, foi o primeiro a ter a decolagem autorizada através do pop(0).
* Encapsulamento: A lista __fila_espera é privada para impedir que alguém "fure a fila" alterando posições intermediárias manualmente.
* Performance: Para sistemas com um volume massivo de dados (Big Data), recomenda-se o uso de collections.deque para que a remoção do início (popleft) tenha complexidade $O(1)$ em vez de $O(n)$ das listas comuns.
