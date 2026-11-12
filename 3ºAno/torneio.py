menu = ''
menu += '\n1 - Ver equipas\n'
menu += '2 - Ver tabelas de pontos\n'
menu += '3 - Registar pontos\n'
menu += '4 - Ver estado dos robôs\n'
menu += '5 - Inscrever equipa\n'
menu += '0 - Sair\n'

equipas = ['Ciborgues', 'Bits Voadores', 'uauaa', 'robots', 'isse que ta ai']

pontos = {
    'Ciborgues': 0,
    'Bits Voadores': 0,
    'uauaa': 0,
    'robots': 16,
    'isse que ta ai': 20,
    'unecas': 50
}

robos = {
    'robo1': {
        'nome': 'Robo1',
        'equipa': 'Ciborgues',
        'bateria': 100,
    },
    'robo2': {
        'nome': 'Robo2',
        'equipa': 'Bits Voadores',
        'bateria': 80,
    },
    'robo3': {
        'nome': 'Robo3',
        'equipa': 'uauaa',
        'bateria': 60,
    },
    'robo4': {
        'nome': 'Robo4',
        'equipa': 'robots',
        'bateria': 10,
    },
}

for equipa in equipas:
    print(f"Bem-vindos ao torneio {equipa}!")
print("Boa sorte a todas as equipas!")

ativo = True

while ativo:

    print('\n========= Menu =========')
    print(menu)

    opcao = input('Opção: ')

    if opcao == '0':

        sair = input('Deseja sair? S ou N: ').strip().upper()

        if sair == 'S':
            ativo = False
            print('Terminado.')
        else:
            print('Regresso ao menu.')

    
    elif opcao == '1':

        print(equipas)
        print(f"Número de equipas inscritas: {len(equipas)}")

        equipas.append("unecas")
        print(equipas)

        desistiu = equipas.pop(1)
        print(f"A equipa {desistiu} desistiu.")

        equipas.sort()
        print(equipas)

    elif opcao == '2':

        for equipa in pontos:
            print(f"{equipa}: {pontos[equipa]} pontos.")

        print("A equipa com mais pontos é a equipa", max(pontos, key=pontos.get), "com", max(pontos.values()), "pontos.")

        print("A soma de todos os pontos é", sum(pontos.values()), "pontos.")

    elif opcao == '3':

        equipa = input("Digite o nome da equipa: ")
        pontos_equipa = int(input("Digite os pontos ganhos na prova: "))

        if pontos_equipa < 0 or pontos_equipa > 100:
            print("Erro: o número de pontos deve ser um valor entre 0 e 100.")

        elif equipa in pontos:
            pontos[equipa] += pontos_equipa
            print(f"Pontos atualizados para a equipa {equipa}: {pontos[equipa]} pontos.")

        else:
            print(f"A equipa {equipa} não está inscrita.")

    elif opcao == '4':

        for equipa in pontos:

            if pontos[equipa] >= 80:
                print(f"{equipa} - {pontos[equipa]} - Ouro")

            elif pontos[equipa] >= 50:
                print(f"{equipa} - {pontos[equipa]} - Prata")

            elif pontos[equipa] >= 20:
                print(f"{equipa} - {pontos[equipa]} - Bronze")
            else:
                print(f"{equipa} - {pontos[equipa]} - Participação")

        for robo in robos:

            print(f"{robo} - Bateria: {robos[robo]['bateria']}%")

            if robos[robo]['bateria'] <= 20:
                print("ALERTA: carregar antes da próxima prova!")
                print(f"Bateria atual: {robos[robo]['bateria']}%")

    elif opcao == '5':

        nova_equipa = input("Insira o nome da nova equipa: ")

        if nova_equipa not in equipas:
            equipas.append(nova_equipa)
            pontos[nova_equipa] = 0
            robos[nova_equipa] = {'bateria': 100}
            print(f"A equipa {nova_equipa} foi inscrita com sucesso!")
        else:
            print(f"A equipa {nova_equipa} já está inscrita.")
