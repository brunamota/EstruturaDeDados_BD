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