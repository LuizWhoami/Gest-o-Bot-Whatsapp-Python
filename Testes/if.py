idade = int(input('idade: '))
nivel = 'avançado'
if idade < 18:
    print('indo')
    if nivel == 'avançado':
        print('pronto')

if idade > 18:
    print('voce é adulto')