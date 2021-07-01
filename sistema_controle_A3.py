iniciar = input('Deseja iniciar? S para Sim e N para Não ')

if iniciar == 'S' or iniciar == 's':
    renda = float(input('Digite sua renda: '))

    gastos = float(input('Digite o valor da soma total de gastos: '))

    investimentos = input('Houve investimentos? S para Sim e N para Não ')

    if investimentos == 'S' or investimentos == 's' :
        investimentoValor = float(input('Digite o valor total investimentos: '))
    elif investimentos == 'N' or investimentos == 'n' :
        investimentoValor = 0
    else :
        print('Caractere não identificado')

    somaTotal = gastos + investimentoValor

    if somaTotal > renda:
         print('Gastos mais altos que rendas')
    elif somaTotal < renda:
        print('Gastos mais baixos que rendas')
        
    porcentagemGastos = (gastos * 100) / renda
    print('Porcentagem de gastos foi de: '+ str(round(porcentagemGastos,2)))

    porcentagemInvestimentos = (investimentoValor * 100) / renda
    print ('Porcentagem de investimentos foi de: ' + str(round(porcentagemInvestimentos,2)))
else :
    print ('Muito obrigado por iniciar' )
