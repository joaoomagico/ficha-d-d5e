from time import sleep
from random import randint
from app import Colors

# Variáveis globais
nome = ""
race = ""
classe = ""
nivel = 0
Atributos = []
dano_recebido = 0
cura = 0
vida = 0
vida_atual = 0
proef = 0
modstr = 0
modcon = 0
moddex = 0
modint = 0
modsab = 0
modchar = 0
arma = ""
ataque = 0
dano = 0

# Função para rolar dados
def rolar_dado(lados):
    return randint(1, lados)

def atualizar_vida_atual():
    global vida_atual
    vida_atual = vida - dano_recebido + cura

def calcular_ataque():
    if classe == 'guerreiro' or classe == 'bárbaro':
        return rolar_dado(20) + modstr + proef
    elif classe == 'ladino':
        return rolar_dado(20) + moddex + proef
    else:
        return 0

def calcular_dano():
    if classe == 'ladino':
        if arma == 'a':
            return rolar_dado(6) + moddex
        elif arma == 'b':
            return rolar_dado(4) + moddex
    elif classe == 'guerreiro' or classe == 'bárbaro':
        if arma == 'a':
            return rolar_dado(8) + modstr
        elif arma == 'b':
            return rolar_dado(12) + modstr
    return 0

def func_showcase_ficha():
    print('Seu nome é: ' + Colors.underline_black + nome + Colors.end)
    print('Sua raça é: ' + Colors.green + race + Colors.end)
    print('Sua classe é: ' + Colors.blue + classe + Colors.end)
    print('Seu nível é: ' + Colors.blue + str(nivel) + Colors.end)
    print('Seus atributos são: ' + Colors.orange + str(Atributos) + Colors.end)
    print('Seu total de vida é: ' + Colors.pink + str(vida) + Colors.end)

def func_Menu_principal():
    while True:
        print('Menu Principal')
        print('1 - Ficha D&d')
        print('2 - Sair')
        print('3 - Criar outro personagem')
        print('4 - Combate')
        op = input('Escolha uma opção: ')
        
        if op == '1':
            func_showcase_ficha()
        elif op == '2':
            print('Até mais!')
            break
        elif op == '3':
            print('Esse processo vai deletar o personagem atual e o substituir, tem certeza que deseja prosseguir?')
            zerar = input('Sim (s) ou Não (n): ')
            if zerar.lower() == 's':
                func_personagem()
            elif zerar.lower() == 'n':
                print('Vamos tentar de novo!')
        elif op == '4':
            func_combate()
        else:
            print('Opção inválida!')

def func_personagem():
    global nome, race, classe, nivel, Atributos, vida, modstr, modcon, moddex, modint, modsab, modchar, proef, arma

    classes = ["guerreiro", "bárbaro", "ladino"]
    raças = ['anão', 'elfo', 'humano', 'orc', 'thiefling']
    
    print('Olá, Me chamo Oru e vou estar o guiando para a criação de seu primeiro personagem!')
    sleep(0.8)
    print('Vamos começar escolhendo sua raça, cada raça tem uma vantagem e uma desvantagem, aqui está um pergaminho contendo os detalhes sobre cada uma: ')
    print(Colors.background_white + '\nAnão: Seres robustos como rochas, de estatura baixa e pesados, fortes e engenhosos. +2 Constituição +1 Força. \n\nElfos: Criaturas faéricas de beleza e inteligência exuberantes. +2 Inteligência +1 Carisma. \n\nHumanos: Seres de grande avareza e desejo por dominação, sua variedade e adaptabilidade os fazem vencer qualquer desafio no fim, apesar de não serem especialistas em nada. +1 em todos os atributos\n \nOrc: Orcs são criaturas inabaláveis, natos guerreiros conhecidos por sua impetuosidade e violência, porém alguns mais controlados vivem entre outras raças em harmonia. +2 em Força +1 em Constituição. \n\nThieflings: Criaturas de uma raça amaldiçoada há muito pelos deuses a ter aspectos infernais. +2 em Carisma e +1 em Destreza' + Colors.end)
    print(Colors.green + str(raças) + Colors.end)

    # Seleção da raça
    while True:
        race = input('E então, qual será sua raça? ')
        if race.lower() not in raças:
            print(Colors.red + 'Escolha uma raça da lista!' + Colors.end)
        else:
            print('Muito bem, sua raça é: ' + Colors.green + race + Colors.end)
            break

    # Seleção da classe
    print('Vamos escolher sua classe, suas escolhas são: ')
    print(Colors.blue + str(classes) + Colors.end)
    while True:
        classe = input('E então, qual será sua classe? ')
        if classe.lower() in classes:
            print('Muito bem, sua classe é: ' + Colors.blue + classe + Colors.end)
            break
        else:
            print(Colors.red + 'Escolha uma classe da lista!' + Colors.end)

    # Seleção do nível
    print('Vamos escolher seu nível, suas escolhas são: ')
    print(Colors.underline_blue + '1-20' + Colors.end)
    while True:
        nivel = int(input('Nível: '))
        if 1 <= nivel <= 20:
            print('Muito bem, seu nível é: ' + Colors.underline_blue + str(nivel) + Colors.end)
            break
        else:
            print(Colors.red + 'Escolha um nível entre 1 e 20!' + Colors.end)

    # Cálculo da proficiência
    if nivel <= 4:
        proef = 2
    elif nivel <= 8:
        proef = 3
    elif nivel <= 12:
        proef = 4
    elif nivel <= 16:
        proef = 5
    elif nivel <= 20:
        proef = 6

    # Atributos
    print('Vamos distribuir seus atributos, os atributos existentes são: ')
    print(Colors.orange + 'STR, CON, DEX, INT, SAB, CHAR')
    print("Distribua 72 pontos entre os seguintes atributos:")

    while True:
        STR = int(input("Força: "))
        CON = int(input("Constituição: "))
        DEX = int(input("Destreza: "))
        INT = int(input("Inteligência: "))
        SAB = int(input("Sabedoria: "))
        CHAR = int(input("Carisma: "))
        Atributos = [STR, CON, DEX, INT, SAB, CHAR]
        Soma_Atributos = sum(Atributos)
        if Soma_Atributos > 72:
            print(Colors.end + f"A soma dos atributos deve ser igual ou inferior a 72, a soma foi: {Soma_Atributos}")
        else:
            print(Colors.orange + f'A soma dos atributos foi: ' + Colors.end + f'{Soma_Atributos}')
            break

    # Adição dos bônus de raça
    if race == 'elfo':
        Atributos[3] += 2
        Atributos[5] += 1
    elif race == 'humano':
        Atributos = [atributo + 1 for atributo in Atributos]
    elif race == 'orc':
        Atributos[0] += 2
        Atributos[1] += 1
    elif race == 'thiefling':
        Atributos[5] += 2
        Atributos[2] += 1
    elif race == 'anão':    
        Atributos[0] += 1
        Atributos[1] += 2

    # Modificadores
    modstr = (Atributos[0] - 10) // 2
    modcon = (Atributos[1] - 10) // 2
    moddex = (Atributos[2] - 10) // 2
    modint = (Atributos[3] - 10) // 2
    modsab = (Atributos[4] - 10) // 2
    modchar = (Atributos[5] - 10) // 2

    # Equipamentos
    dano_arma = 0
    if classe == 'guerreiro' or classe == 'bárbaro':
        print('Para os equipamentos escreva apenas (a) ou (b)')
        while True:
            arma = input("Arma de uma mão e Escudo (a) ou Arma de duas mãos (b): ").lower()
            if arma == 'a':
                print("Então você escolheu a arma de uma mão e o escudo!")
                break
            elif arma == 'b':
                print("Então você escolheu a arma de duas mãos!")
                break
            else:
                print("Escolha entre (a) ou (b)!")

        while True:
            armadura = input("Armadura leve (a) ou Armadura Pesada (b): ").lower()
            if armadura == 'a':
                print("E você escolheu a Armadura leve")
                break
            elif armadura == 'b':
                print("E você escolheu a Armadura Pesada")
                break
            else:
                print("Escolha entre (a) ou (b)")

    elif classe == 'ladino':
        print('Para os equipamentos escreva apenas (a) ou (b)')
        while True:
            arma = input("Arma de uma mão média (a) ou duas armas leves (b): ").lower()
            if arma == 'a':
                print("Então você escolheu a Arma de uma mão média!")
                break
            elif arma == 'b':
                print("Então você escolheu duas armas leves!")
                break
            else:
                print("Escolha entre (a) ou (b)!")

        while True:
            armadura = input("Armadura leve (a) ou Armadura média (b): ").lower()
            if armadura == 'a':
                print("E você escolheu a Armadura leve")
                break
            elif armadura == 'b':
                print("E você escolheu a Armadura média")
                break
            else:
                print("Escolha entre (a) ou (b)")

    # Vida
    if classe == 'guerreiro':
        vida = 10 + (6 * nivel) + (modcon * nivel)
    elif classe == 'bárbaro':
        vida = 12 + (7 * nivel) + (modcon * nivel)
    elif classe == 'ladino':
        vida = 8 + (5 * nivel) + (modcon * nivel)
    else:
        vida = 0  # Default case if class is not recognized

    atualizar_vida_atual()

    print('Seu total de vida é: ' + Colors.pink + str(vida) + Colors.end)
    # Showcase Personagem
    print('Ah, acabei de me lembrar que ainda falta seu nome!')
    nome = input('E qual é seu nome? ')
    print('Então, ' + Colors.underline_black + nome + Colors.end + ', recaptulando...')
    func_showcase_ficha()

def func_combate():
    global dano_recebido, cura, vida_atual
    while True:
        print('1 - Ataque')
        print('2 - vida atual')
        print('3 - curar')
        print('4 - Receber dano')
        print('5 - sair do combate')
        opmenucombate = int(input("Escolha uma opção: "))
        if opmenucombate == 1:
            ataque = calcular_ataque()  # Calcular ataque cada vez que for necessário
            print('Seu ataque é: ' + Colors.red + str(ataque) + Colors.end)
            print('Deseja rolar o dano da arma? ')
            deseja = input('sim (s) ou não (n)')
            if deseja == 's':
                dano = calcular_dano()  # Calcular dano cada vez que for necessário
                print('Seu dano é: ' + Colors.red + str(dano) + Colors.end)
        elif opmenucombate == 2:
            atualizar_vida_atual()  # Atualizar vida atual antes de mostrar
            print('Seu total de vida é: ' + Colors.pink + str(vida_atual) + Colors.end)
        elif opmenucombate == 3:
            valor_da_cura = int(input('Quantidade de vida a ser curada: '))
            if vida_atual + valor_da_cura > vida:
                print('Vida ultrapassada!')
            elif vida_atual + valor_da_cura <= vida:
                cura += valor_da_cura
                atualizar_vida_atual()
        elif opmenucombate == 4:
            dano_recebido += int(input('Quantidade de vida a ser perdida: '))
            atualizar_vida_atual()
        elif opmenucombate == 5:
            break

# Execução do menu principal
func_Menu_principal()
