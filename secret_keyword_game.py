
import os

kword = input('Digite a palavra chave: ').upper()
comandos = {
    'cls': lambda: os.system('cls'),
}
comando = comandos.get('cls')
comando()

title = 'JOGO DE ADIVINHAÇÃO'
typed = []
chance = (len(kword) // 0.6)  # Quantidade de chances baseado no tamanho da palavra

print(f'{title:*^50}', end='\n\n')

print(f'A palavra possui {len(kword)} letras', end='\n\n')

while True:
    print(f'Você tem {chance:.0f} chances')
    if chance < 1:
        print('Você perdeu!\nInfelizmente acabou as suas chances!')
        break

    letter = input('Digite uma letra: ').upper()

    if len(letter) > 1:
        print('Ahh, aí não vale, só pode digitar uma letra por vez!')
        chance -= 1
        print()
        continue

    if letter in typed:
        print('Essa letra já foi digitada')
        continue

    typed.append(letter)

    if letter in kword:
        print(f'Olha só! Parece que a letra "{letter}" está na palavra secreta!', end='\n')
    else:
        print(f'Opa, parece que "{letter}" não está na palavra secreta!', end='\n')
        chance -= 1
        typed.pop()

    keyword_temp = ''
    for secret_letter in kword:
        if secret_letter in typed:
            keyword_temp += secret_letter
        else:
            keyword_temp += '-'

    if keyword_temp == kword:
        print(f'Parabéns!\nA palavra secreta era {keyword_temp}!')
        break
    else:
        print(f'Mas você ainda não acertou, sua palavra ainda está assim: {keyword_temp}', end='\n\n')