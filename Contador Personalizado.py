def contador(inicio, fim, passo):
    contagem = list()

    # Ordem crescente
    if inicio < fim and passo >= 0:
        if passo == 1 or passo == 0:
            for count in range(inicio, fim + 1):
                contagem.append(count)
        # Passo igual a um ou igual a zero é o mesmo de uma contagem normal de 1 em 1

        else:
            contagem.append(inicio)

            for count in range(inicio, fim + 1, passo):
                if count + passo > fim:
                    break

                contagem.append(count + passo)
        # Se passo for qualquer outro valor ele é uma contagem personalizada

    # Ordem decrescente
    elif inicio > fim or passo <= 0:
        if passo == 1 or passo == 0:
            for count in range(fim, inicio + 1):
                contagem.append(count)

            contagem.sort(reverse=True)
        # Se passo for igual a um ou zero numa ordem reversa, é igual a uma contagem normal porém decrescente

        elif inicio > fim and passo < 0:
            for count in range(fim, inicio + 1, passo * -1):
                if count + passo * -1 > inicio:
                    contagem.sort(reverse=True)
                    contagem.append(fim)
                    break

                contagem.append(count + passo * -1)
        # Se a ordem for invertida tanto pela ordem quanto pelo valor de passo ele realiza a contagem decrescente

        elif passo < 0:
            contagem.append(inicio)

            for count in range(inicio, fim + 1, passo * -1):
                if count + passo * -1 > fim:
                    contagem.sort(reverse=True)
                    break

                contagem.append(count + passo * -1)
        # Se a ordem for invertida apenas pelo passo negativo ele realiza essa contagem decrescente

        else:
            for count in range(fim, inicio + 1, passo):
                if count + passo > inicio:
                    contagem.append(fim)
                    contagem.sort(reverse=True)
                    print('Oi')
                    break

                contagem.append(count + passo)
        # Caso o inicio > fim seja verdadeiro e o passo for positivo ele executa essa contagem decrescente
    return contagem
# Faz a contagem


def mostra_contagem(i, f, p):
    contagem = contador(i, f, p)
    contagem_formatada = ''

    for i, v in enumerate(contagem):
        contagem_formatada += ' ' + str(contagem[i])

    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print(f'{contagem_formatada} FIM!')
# Formata a contagem


print('==' * 30)
print('Personalize sua contagem!')
input_i = int(input('Início: '))
input_f = int(input('Fim: '))
input_p = int(input('Passo: '))
mostra_contagem(input_i, input_f, input_p)
