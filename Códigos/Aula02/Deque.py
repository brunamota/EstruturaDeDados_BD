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