# Projeto: Calculadora Funcional
# Objetivo: Praticar lógica de programação, laços de repetição e tratamento de erros.

while True:
    print("\n--- CALCULADORA PYTHON ---")
    
    try:
        # Usamos try/except para capturar se o usuário digitar letras em vez de números
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        
        operacao = input("Escolha a operação (+, -, *, /): ")

        if operacao == "+":
            print(f"✅ Resultado: {n1} + {n2} = {n1 + n2}")
        elif operacao == "-":
            print(f"✅ Resultado: {n1} - {n2} = {n1 - n2}")
        elif operacao == "*":
            print(f"✅ Resultado: {n1} * {n2} = {n1 * n2}")
        elif operacao == "/":
            if n2 != 0:
                print(f"✅ Resultado: {n1} / {n2} = {n1 / n2}")
            else:
                print("❌ Erro: Não é possível dividir por zero.")
        else:
            print("⚠️ Operação inválida! Tente novamente.")

    except ValueError:
        print("❌ Erro: Por favor, digite apenas números inteiros.")

    # Opção para sair ou continuar
    continuar = input("\nDeseja fazer outro cálculo? (s/n): ").lower()
    if continuar != 's':
        print("Finalizando... Até a próxima!")
        break
