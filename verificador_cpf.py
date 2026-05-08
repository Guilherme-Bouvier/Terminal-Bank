def validar_cpf(cpf):

    cpf = cpf.strip()

    # 11 dígitos
    if not cpf.isdigit() or len(cpf) != 11:
        return False

    # evita 00000000000
    if cpf == cpf[0] * 11:
        return False

    # primeiro dígito
    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    digito1 = (soma * 10) % 11

    if digito1 == 10:
        digito1 = 0

    if digito1 != int(cpf[9]):
        return False

    # segundo dígito
    soma = 0

    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    digito2 = (soma * 10) % 11

    if digito2 == 10:
        digito2 = 0

    if digito2 != int(cpf[10]):
        return False

    return True