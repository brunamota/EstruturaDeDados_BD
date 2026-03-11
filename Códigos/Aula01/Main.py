from ContaCorrente import ContaCorrente

conta1 = ContaCorrente(nome = "gabriel", agencia = 123, conta = 45678, saldo_inicial = 1500)

print(conta1.nome)
print(conta1.agencia)
print(conta1.conta)
print(conta1.consultaSaldo())

conta1.depositar(50)
print(f"Saldo da conta R${conta1.consultaSaldo()}")

conta1.saque(200)
print(f"Saldo da conta R${conta1.consultaSaldo()}")


