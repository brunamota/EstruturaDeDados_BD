# Aula 01 - Estruturas de Dados: Tipos Abstratos e Pilhas

Nesta aula, exploraremos como os dados são organizados na computação para garantir eficiência e performance. Veremos a importância dos Tipos Abstratos de Dados (TAD) e como implementar uma das estruturas mais fundamentais: a Pilha.

## 1. O que é Estrutura de Dados?

Na computação, a estrutura de dados consiste no modo de armazenamento e organização de dados em um computador. A correta escolha da categoria de organização impacta diretamente na performance e na velocidade que o computador, ou usuário, levará para encontrá-los.

### Dado vs. Informação

* **Dados:** Podem ser números, letras e palavras sem qualquer significado isolado (ex: "08", "07").
* **Informação:** Ocorre quando há algum significado atribuído ao dado (ex: "Idades" ou "Número de pessoas").

## 2. Tipos Abstratos de Dados (TAD)

Os TADs são estruturas capazes de representar tipos de dados que não foram originalmente previstos nas linguagens de programação.
* **Composição:** São divididos em duas camadas: uma de **dados** e outra de **operações**.
* **Encapsulamento:** O usuário nunca tem acesso direto às variáveis, apenas às operações (funções) que as manipulam.
* **Vantagens:** Possibilita a reutilização de código em diferentes programas e facilita a manutenção.

## 3. A Estrutura de Dados Pilha (Stack)

As pilhas são estruturas dinâmicas que contêm duas extremidades distintas: o **TOPO** e a **BASE**.

### Regra de Funcionamento: LIFO

A pilha segue o conceito **LIFO** (*last in, first out*), onde tanto a inserção quanto a remoção são feitas pela mesma extremidade: o TOPO. O último elemento que entra é obrigatoriamente o primeiro a sair.

### Aplicações no Cotidiano e na Computação

* **Mundo Real:** Pilha de livros, pratos ou panquecas.
* **Navegação Web:** Comandos de "Ir" e "Voltar" entre páginas.
* **Edição:** Funções de "Desfazer" (Undo) em aplicativos.
* **Algoritmos:** Controle de fluxo de execução de procedimentos e funções (Recursão).

## 4. Implementação em Python

Em Python, a implementação de pilhas é frequentemente realizada utilizando o tipo **Lista**.

### Operações Básicas

1. **Criar Pilha:** `nome_pilha = []`.
2. **Inserir (Push):** `append(elemento)` - Adiciona ao topo.
3. **Remover (Pop):** `pop()` - Remove e retorna o elemento do topo.

### Exemplo Prático

```python
# Criando a pilha (TAD Lista como Pilha)
myStack = []

# Inserindo elementos
myStack.append(1)
myStack.append(2)
myStack.append(3)

print(f"Pilha: {myStack}") # Saída: [1, 2, 3]

# Removendo do topo (LIFO)
removido = myStack.pop()
print(f"Elemento retirado: {removido}") # Saída: 3
print(f"Pilha após remoção: {myStack}") # Saída: [1, 2]

```

> 
> **Dica de Performance:** Para operações de inserção e remoção em larga escala, a classe `deque` do módulo `collections` é preferível, pois oferece complexidade de tempo $O(1)$, enquanto listas comuns podem chegar a $O(n)$.
> 
> 

---

## 5. Exercício de Fixação

Com base no conceito de TAD visto hoje, como você estruturaria as **operações** de uma Pilha para garantir que o usuário não manipule a lista base diretamente? Pense em funções como `push(valor)`, `pop()` e `peek()` (que apenas observa o topo).

