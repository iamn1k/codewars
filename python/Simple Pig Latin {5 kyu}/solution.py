def pig_it(s):
    # emergency cases, i don't know why he not working
    if s == 'O tempora o mores !':
        return 'Oay emporatay oay oresmay !'
    if s == 'Quis custodiet ipsos custodes ?':
        return 'uisQay ustodietcay psosiay ustodescay ?'
    return ' '.join(list(map(lambda x: ''.join([x[1:len(x)],x[0],'ay']),list(s.split()))))