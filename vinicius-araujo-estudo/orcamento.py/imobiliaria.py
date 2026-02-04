print(" ORÇAMENTO DE ALUGUEL ")

print("Seja bem-vindo à Imobiliária R.M")
print("Escolha o tipo de imóvel:")

print("1 - APARTAMENTO  (a partir de R$ 700,00)")
print("2 - CASA         (a partir de R$ 900,00)")
print("3 - ESTÚDIO      (a partir de R$ 1.200,00)")


opcao = int(input("Escolha o tipo de imóvel: "))

while opcao != 1 and opcao != 2 and opcao != 3:
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    opcao = input("Escolha o tipo de imóvel: ")


    if opcao != 1 and opcao != 2 and opcao != 3:
        print("******************************")
        print("Opção Inválida! Você deve escolher (1), (2) ou (3)")
        print("******************************")
            
if opcao == 1:
    tipo = "Apartamento"
    aluguel = 700

elif opcao == 2:
    tipo = "Casa"
    aluguel = 900

elif opcao == 3:
    tipo = "Estúdio"
    aluguel = 1200


# Regras específicas
if tipo == "Apartamento" or tipo == "Casa":

    quartos = 0

    while quartos != 1 and quartos != 2:
        quartos = int(input("Quantidade de quartos (1 ou 2): "))

        if quartos != 1 and quartos != 2:
            print("Quantidade inválida! Digite apenas 1 ou 2.")

    if tipo == "Apartamento" and quartos == 2:
        aluguel += 200

    if tipo == "Casa" and quartos == 2:
        aluguel += 250

garagem = ""

while garagem != "sim" and garagem != "não":
    garagem = input("Deseja vaga de garagem? (sim/não): ")

    if garagem != "sim" and garagem != "não":
        print("******************************")
        print("Resposta inválida! Digite apenas 'sim' ou 'não'")
        print("******************************")

if garagem == "sim":
    aluguel += 300

if tipo == "Estúdio":
    vagas = int(input("Quantidade de vagas de estacionamento: "))

    if vagas >= 2:
        aluguel += 250
        if vagas > 2:
            aluguel += (vagas - 2) * 60

# Desconto para apartamento

if tipo == "Apartamento":
    criancas = ""

    while criancas != "sim" and criancas != "não":
        criancas = input("Possui crianças? (sim/não): ").lower()

        if criancas != "sim" and criancas != "não":
            print("******************************")
            print("Resposta inválida! Digite apenas 'sim' ou 'não'")
            print("******************************")

    if criancas == "não":
        aluguel -= aluguel * 0.05


# Contrato
contrato = 2000
parcelas = 0

while parcelas < 1 or parcelas > 5:
    parcelas = int(input("Deseja parcelar o contrato em até 5 vezes (1 a 5): "))

    if parcelas < 1 or parcelas > 5:
        print("******************************")
        print("Opção inválida! Escolha entre 1 e 5 parcelas.")
        print("******************************")

if parcelas < 1:
    parcelas = 1
elif parcelas > 5:
    parcelas = 5

valor_parcela = contrato / parcelas

# Resultado
print("   RESUMO DO ORÇAMENTO   ")
print("Tipo do imóvel:", tipo)
print("Aluguel mensal: R$", round(aluguel, 2))
print("Contrato: R$", contrato)
print("Parcelamento:", parcelas, "x de R$", round(valor_parcela, 2))

# Gerar CSV
arquivo = open("orcamento_aluguel.csv", "w")
arquivo.write("Parcela,Valor do Aluguel\n")

for i in range(1, 13):
    arquivo.write(str(i) + "," + str(round(aluguel, 2)) + "\n")

arquivo.close()

print("\nObrigado por utilizar a Imobiliária R.M!")
print("Seu orçamento foi gerado com sucesso.")
print("Permanecemos à disposição para qualquer dúvida.")