# Aula 01 - Estruturas de Dados: Tipos Abstratos e Pilhas

Nesta aula, exploraremos como os dados são organizados na computação para garantir eficiência e performance. Veremos a importância dos Tipos Abstratos de Dados (TAD) e como implementar uma das estruturas mais fundamentais: a Pilha.

## 1. O que é Estrutura de Dados?

Na computação, a estrutura de dados consiste no modo de armazenamento e organização de dados em um computador. A correta escolha da categoria de organização impacta diretamente na performance e na velocidade que o computador, ou usuário, levará para encontrá-los.
* **Organização e Relação:** A estrutura não é apenas o local de armazenamento (pastas, bancos de dados), mas a relação entre os dados.
* **Alocação de Memória:**
    * **Estática:** Ocorre na compilação; o espaço é reservado no início e liberado apenas ao fim do programa.
    * **Dinâmica:** Ocorre durante a execução, conforme as operações são realizadas.
* **Lixo de Memória:** É fundamental codificar a liberação de memória para evitar lentidão no sistema operacional, especialmente no Windows

### Dado vs. Informação

* **Dados:** Podem ser números, letras e palavras sem qualquer significado isolado (ex: "08", "07").
* **Informação:** Ocorre quando há algum significado atribuído ao dado (ex: "Idades" ou "Número de pessoas").

## 2. Conceitos Chave de Orientação a Objetos em Python

Antes de criarmos nossas estruturas complexas, precisamos entender como o Python organiza objetos. A Orientação a Objetos permite agrupar dados (atributos) e comportamentos (métodos) em um único bloco chamado **Classe**.

* **Linguagens Não Tipadas:** Como o Python, elas não exigem declaração explícita de tipo. Isso traz velocidade ao programador, mas pode aumentar o consumo de memória e processamento, pois o compilador define o tipo internamente.

| Termo | O que é? | Papel no Python |
| --- | --- | --- |
| **Classe** | O "molde" ou matriz para criar objetos.| Definida pela palavra-chave `class`.|
| **Atributo** | Variáveis que guardam os dados do objeto (o que ele "tem").| Definidos dentro do objeto, geralmente começando com `self`.|
| **Método** | Funções que definem o comportamento (o que ele "faz").| Definidos usando `def` dentro da classe.|
| **`def`** | Palavra-chave para definir uma função ou método.| Em OO, indica que estamos criando uma habilidade para o objeto.|
| **`__init__`** | O método **Construtor** da classe.| Executado automaticamente ao criar o objeto para inicializar seus dados.|
| **`self`** | Referência à própria instância do objeto.| Usado para que o método saiba exatamente qual objeto ele está alterando. |

### Por que usar `self.__atributo`? (Encapsulamento)

Em linguagens como Python, usamos a convenção de dois sublinhados (`__`) antes do nome de um atributo para indicar que ele é **privado**. Isso é fundamental para a criação de TADs, pois impede que o usuário altere dados sensíveis (como o saldo de uma conta ou a base de uma pilha) sem passar pelas regras de segurança que você definiu nos métodos.

## 3. Tipos Abstratos de Dados (TAD)

Os TADs são estruturas capazes de representar tipos de dados que não foram originalmente previstos nas linguagens de programação.
* **Composição:** São divididos em duas camadas: uma de **dados** e outra de **operações**.
* **Encapsulamento:** O usuário nunca tem acesso direto às variáveis, apenas às operações (funções) que as manipulam.
* **Vantagens:** Possibilita a reutilização de código em diferentes programas e facilita a manutenção.

Os TADs podem ser divididos em dois grandes grupos:

* **Genéricos:** Estruturas generalistas que representam qualquer dado (ex: uma lista telefônica).
* **Específicos:** Definidos para um domínio restrito de aplicação (ex: o sistema de `ContaCorrente`).

### Exemplo Prático: TAD Conta Corrente

Imagine que precisamos desenvolver um sistema bancário. Em vez de manipular variáveis soltas pelo código, criamos um **Tipo Abstrato de Dados** que encapsula tudo o que uma conta precisa ter e fazer.

#### 1. Identificação das Variáveis

Nesta camada, definimos os atributos internos que o usuário **não** deve alterar manualmente:

* **Ag:** Número da agência (inteiro).
* **CC:** Número da conta corrente (inteiro).
* **Saldo:** Valor disponível (inteiro/real).

#### 2. Identificação das Operações

Nesta camada, definimos as funções que o programador "cliente" poderá usar para interagir com a conta:

* **InicializaConta:** Recebe os dados iniciais e prepara a conta para uso.
* **Deposito:** Recebe um valor e atualiza o saldo interno.
* **Saque:** Deduz um valor do saldo, garantindo que as regras de negócio sejam seguidas.
* **Saldo:** Retorna o valor atual para visualização, sem permitir alteração direta.

#### 3. Analogia

Explique que um TAD é como um **Controle Remoto**:

* O usuário (cliente) conhece os botões (operações como `Trocar Canal` ou `Aumentar Volume`).
* O usuário **não precisa saber** como os circuitos internos (variáveis) funcionam ou como o sinal é processado.
* Se a fabricante mudar os circuitos internos (manutenção), o controle remoto continua tendo os mesmos botões para o usuário (reutilização e facilidade de manutenção).

## 4. Implementação Prática: TAD em Python

Para materializar o conceito de Tipo Abstrato de Dados, vamos codificar o exemplo da **Conta Corrente**. Note como o usuário do código interage apenas com os métodos, sem precisar manipular o "balanço" interno diretamente.

### Definição da Classe

Uma classe funciona como o "molde" para o nosso TAD. Nela, definimos como os dados serão inicializados e quais operações estão disponíveis.

```python
class ContaCorrente:
    def __init__(self, agencia, conta, saldo_inicial=0):
        """Operação de Inicialização: Define os dados iniciais do TAD."""
        self.agencia = agencia
        self.conta = conta
        self.__saldo = saldo_inicial  # O prefixo '__' indica que o dado é privado (encapsulamento)

    def depositar(self, valor):
        """Operação de Depósito: Atualiza a variável interna saldo."""
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        """Operação de Saque: Atualiza o saldo seguindo uma regra de negócio."""
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            print("Saldo insuficiente ou valor inválido.")
            return False

    def consultar_saldo(self):
        """Operação de Consulta: Retorna o dado ao usuário sem permitir alteração direta."""
        return self.__saldo

```

### Utilizando o TAD

O "cliente" do TAD não precisa saber como a soma ou subtração é feita internamente, apenas como chamar as funções.

```python
# Criando uma instância do nosso TAD
minha_conta = ContaCorrente(agencia=123, conta=45678, saldo_inicial=100)

# Interagindo através das operações definidas
minha_conta.depositar(50)
print(f"Saldo atual: R$ {minha_conta.consultar_saldo()}")

if minha_conta.sacar(30):
    print("Saque efetuado!")

print(f"Saldo final: R$ {minha_conta.consultar_saldo()}")

```
### Pontos Chave

* **Encapsulamento:** O uso de `self.__saldo` protege o dado. Se tentarmos fazer `minha_conta.__saldo = 1000000` fora da classe, o Python criará uma nova variável em vez de alterar o saldo real da conta.
* **Interface vs. Implementação:** O TAD define a **Interface** (os nomes dos métodos e o que eles pedem) enquanto a **Implementação** (o código dentro dos métodos) pode ser alterada sem quebrar quem usa a classe.
* **Vantagem na Manutenção:** Se amanhã a PUC Goiás pedir para cobrar uma taxa de R$ 0,10 por saque, você só altera o método `sacar` dentro do TAD, e todo o resto do sistema continuará funcionando perfeitamente.

## 3. A Estrutura de Dados Pilha (Stack)

As pilhas são estruturas dinâmicas que contêm duas extremidades distintas: o **TOPO** e a **BASE**.

### Regra de Funcionamento: LIFO

A pilha segue o conceito **LIFO** (*last in, first out*), onde tanto a inserção quanto a remoção são feitas pela mesma extremidade: o TOPO. O último elemento que entra é obrigatoriamente o primeiro a sair.

### Aprofundamento e Cuidados

* **Funcionamento Técnico:** Tanto a inserção quanto a remoção ocorrem obrigatoriamente pela mesma extremidade, o **TOPO**.
* **Complexidade de Tempo:**
* * **Listas:** Fornecem tempo $O(n)$ para operações de manipulação.
* **Collections.deque:** Preferível para pilhas maiores, pois fornece complexidade $O(1)$ (mais rápida).
* **Tratamento de Erros:** Tentar realizar um `pop()` em uma pilha vazia causará o erro `IndexError`.

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

### Glossário de Pilhas em Python

| Termo | Definição | Aplicação em Python |
| --- | --- | --- |
| **`append(e)`** | Adiciona um elemento ao final da lista.| Representa o **Empilhamento (Push)** no topo da pilha.|
| **`pop()`** | Remove e retorna o elemento do topo da pilha.| Executa a remoção seguindo a regra **LIFO**.|
| **`peek()`** | Operação em pilhas que permite visualizar o elemento que está no TOPO sem removê-lo.|
| **Topo** | A extremidade onde ocorrem inserções e remoções.| Em listas Python, corresponde ao último índice.|
| **LIFO** | <br>*Last In, First Out*.| O último `append` é o primeiro `pop`.|
| **`deque`** | Classe do módulo `collections`. | Preferível para pilhas grandes pela performance $O(1)$. |

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

## 5. Exercício de Fixação

Com base no conceito de TAD visto hoje, como você estruturaria as **operações** de uma Pilha para garantir que o usuário não manipule a lista base diretamente? Pense em funções como `push(valor)`, `pop()` e `peek()` (que apenas observa o topo).

class PilhaTAD:
    def __init__(self):
        # Encapsulamento: Lista privada para armazenar os itens
        self.__itens = [] 

    def push(self, valor):
        """Adiciona um elemento ao topo."""
        self.__itens.append(valor)

    def pop(self):
        """Remove e retorna o topo (LIFO)."""
        if not self.is_empty():
            return self.__itens.pop()
        return "Pilha Vazia"

    def peek(self):
        """Retorna o valor do topo SEM remover."""
        if not self.is_empty():
            # Retorna o último elemento da lista interna [cite: 313]
            return self.__itens[-1] 
        return None

    def is_empty(self):
        """Verifica se a pilha está vazia[cite: 309]."""
        return len(self.__itens) == 0

# Teste
p = PilhaTAD()
p.push("Página A")
p.push("Página B")
print(f"Espiando o topo: {p.peek()}") # Saída: Página B
print(f"Removendo: {p.pop()}")        # Saída: Página B
print(f"Novo topo: {p.peek()}")       # Saída: Página A
