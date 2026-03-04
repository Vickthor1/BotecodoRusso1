from colorama import Fore, init
import sys, time, random

init()

def sprint(texto):
    """Função para imprimir texto com efeito de digitação"""
    for c in texto + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

class falaJack:
    def __init__(self, nome, opcao_visual):
        self.nome = nome
        self.opcao_visual = opcao_visual

    def limpar_terminal(self):
        """Limpa o terminal baseado na opção do jogador"""
        if self.opcao_visual == '1':
            input("ENTER para continuar")
            print("\033[H\033[J", end="")  # Limpa terminal
        elif self.opcao_visual == '2':
            input("ENTER para continuar")

    def dialogo_jack(self):
        """Diálogo completo com Jack"""
        print(Fore.RESET + '')
        sprint(Fore.CYAN + f'{self.nome}: Fala ai Jack! ')
        print('')
        sprint(Fore.BLUE + 'Jack: Eae, veio aproveitar a sexta?')
        print('')
        sprint(Fore.CYAN + f'{self.nome}: Sim, essa semana foi tortura')
        print('')
        sprint(Fore.BLUE + 'Jack: Vou ficar aqui com você na mesa vlw? e me paga uma cerveja ai')
        print('')
        sprint(Fore.CYAN + f'{self.nome}: Mas Jack sou eu que to em pé')
        print('')
        sprint(Fore.RESET + 'Vocês começam a rir da situação')
        print('')
        sprint(Fore.BLUE + 'Jack: Mas ai namoral, paga uma breja ai?')
        print('')
        decisao = input(Fore.RESET + '-1 Deixar Jack sózinho e explorar o mapa ou\n -2 bater um papo com Jack: ')

        if decisao == '1':
            print('')
            sprint(Fore.RESET + 'Jack, vou ter que vazar, vai dar não')
            print('')
            self.limpar_terminal()
            return "explorar_mapa"
        elif decisao == '2':
            print('')
            sprint(Fore.CYAN + f'{self.nome}: Ta bom mano, desce uma cerveja pra esse maluco aqui!')
            print('')
            sprint(Fore.RESET + 'Você olha pro banheiro feminino e tem uma leve impressão de ter visto um rosto conhecido indo pra dentro do banheiro')
            print('')
            sprint(Fore.BLUE + f'Jack: O que é que foi hein {self.nome}, ta de olho em alguma gatinha? ')
            print('')
            self.limpar_terminal()
            return "pergunta_jack"
        else:
            print(Fore.RESET + '')
            sprint('Números por favor!')
            return self.dialogo_jack()

    def pergunta_jack(self):
        """Jack pergunta sobre interesse em alguém"""
        decisao = input(Fore.RESET + 'Chegou a hora, qual decisão será feita, você vai falar que -1 sim, vai dizer que\n -2 não ou (3) ser grosso: ')

        if decisao == '1':
            return "jack_sim"
        elif decisao == '2':
            return "jack_nao"
        elif decisao == '3':
            return "jack_bravo"
        else:
            sprint(Fore.RESET + 'Números por favor!')
            return self.pergunta_jack()

    def jack_nao(self):
        """Resposta negativa para Jack"""
        print('')
        sprint(Fore.RESET + 'Jack não acredita muito em você mas deixa quieto')
        print('')
        self.limpar_terminal()
        return "continuar_jogo"

    def jack_sim(self):
        """Resposta positiva para Jack - situação complicada"""
        sprint(Fore.CYAN + f'{self.nome}: Sim')
        print('')
        sprint(Fore.RESET + 'Jack da um sorrisinho malicioso')
        print('')
        sprint(Fore.RESET + 'Jack, louco do jeito que é, zoa falando pra você entrar no banheiro feminino quando ninguém estiver olhando')
        print('')
        resp = input(Fore.RESET + 'O que você vai decidir -1 Dar uma de maluco e entrar\n -2 Não fazer essa maluquice? ')

        if resp == '1':
            print('')
            sprint(Fore.CYAN + f'{self.nome}: Boa idéia')
            print('')
            sprint(Fore.RESET + 'Você entra no banheiro feminino e avista sua ex e ela liga pra policia')
            print('')
            sprint(Fore.CYAN + f'{self.nome}: Desculpa, errei fui muleque')
            print('')
            sprint(Fore.RESET + 'Você foi preso')
            self.limpar_terminal()
            return "fim_jogo"
        elif resp == '2':
            print('')
            sprint(Fore.CYAN + f'{self.nome}: Vai se lascar, duente')
            print('')
            sprint(Fore.RESET + 'Jack acha engraçado')
            sprint(Fore.RESET + 'você vai pra perto do banheiro feminino e vê sua...')
            sprint(Fore.RESET + 'Você chegou ao limite da demo, para saber o desfecho dessa história apareça no dia 18 de novembro')
            self.limpar_terminal()
            return "explorar_mapa"
        else:
            sprint(Fore.RESET + 'Não tem essa opção')
            return self.jack_sim()

    def jack_bravo(self):
        """Jack fica bravo - escalação de conflito"""
        sprint(Fore.CYAN + f'{self.nome}: E o quico?')
        print('')
        sprint(Fore.BLUE + 'Jack: É O QUE MENOR!? ')
        print('')
        sprint(Fore.RESET + 'Jack fica com muita raiva e bate na mesa')
        print('')
        sprint(Fore.RESET + 'Todo mundo do bar vira a atenção para vocês')
        print('')
        self.limpar_terminal()
        return "jack_bravo_opcoes"

    def jack_bravo_opcoes(self):
        """Opções após Jack ficar bravo"""
        resposta = input(Fore.RESET + 'O que você ira fazer? -1 Pedir desculpas\n -2 Descer a porrada ou (3) Deixar falando: ')

        if resposta == '1':
            print('')
            sprint(Fore.CYAN + f'{self.nome}: Desculpa errei, fui muleke')
            print('')
            sprint(Fore.RESET + 'Jack não acredita muito, mas deixa quieto a situação')
            self.limpar_terminal()
            return "continuar_jogo"
        elif resposta == '2':
            print('')
            sprint(Fore.CYAN + f'{self.nome}: Cala a boca maluco!!')
            print('')
            sprint(Fore.RESET + 'role os dados para ver se você tem sorte')
            self.limpar_terminal()
            return self.jack_porrada()
        elif resposta == '3':
            self.limpar_terminal()
            print('')
            sprint(Fore.RESET + 'Você deixa Jack sózinho')
            print('')
            sprint(Fore.RED + 'INFORMAÇÃO GUARDADA!!')
            return "explorar_mapa"
        else:
            sprint(Fore.BLUE + 'Jack: repete paspalho!!')
            return self.jack_bravo_opcoes()

    def jack_porrada(self):
        """Combate com Jack - luta"""
        dado = random.randrange(1, 6)

        if dado < 3:
            print('')
            sprint(Fore.LIGHTRED_EX + '+3 Você da tanta porrada na cara do Jack que ele chora')
            print('')
            sprint(Fore.RESET + 'Vocês são expulsos do bar e tem uma divida de 2 mil reais por danos')
        else:
            print('')
            sprint(Fore.LIGHTRED_EX + '-3 Você toma um Jab de esquerda e é nocauteado')
            print('')
            sprint(Fore.RESET + 'Vocês são expulsos do bar e tem uma divida de 2 mil reais por danos')

        self.limpar_terminal()
        return "fim_jogo"
