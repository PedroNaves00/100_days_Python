print('Bem vindo a calculadora de gorjeta')
tot = float(input('Qual foi o total da conta? R$'))
pessoas = int(input('Quantas pessoas para dividir a conta?'))
gorjeta = int(input('Qual a porcentagem da gorjeta você gostaria de dar? 10 12 ou 15?'))

conta = (tot + (tot*gorjeta)/100) / pessoas

print(f'Cada pessoa terá que pagar: {conta:.2f}R$')
