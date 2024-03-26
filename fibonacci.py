def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Teste a função
n_terms = 10
print("Sequência de Fibonacci com", n_terms, "termos:")
for i in range(n_terms):
    print(fibonacci(i), end=", ")