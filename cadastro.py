while True:
    print(' CADASTRO ')
    a_acesso=str(input('E-mal: ')).lower()
    l_acesso = (a_acesso[-10:])
    gmail=['@gmail.com']
    if len(a_acesso) >=15:
        if l_acesso in gmail:
            print('GMAIL válido!')
            a_senha=input('senha: ')
            acesso_libera=[]
            senha_libera=[]
            acesso_libera.append(a_acesso)
            senha_libera.append(a_senha)
            while True:
                print(' LOGUIN ')
                loguin=str(input('faça o loguin: '))
                senha=(input('Digite a senha: '))
                if loguin in acesso_libera:
                    if senha in senha_libera:
                        print('acesso liberado')
                        break
                if loguin not in acesso_libera:
                    print('loguin incorreto')
                if senha not in senha_libera:
                    print('senha incorreta')
                    break
        else:
            print('Apenas Gmail!')
    if len(a_acesso) <14:
        print('Digite um GMAIL válido')
        break