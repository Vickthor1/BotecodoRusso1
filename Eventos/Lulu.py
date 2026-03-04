from colorama import Fore, init
import sys, time

init()

def sprint(texto):
    """Função para imprimir texto com efeito de digitação"""
    for c in texto + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

class falaLulu:
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

    def encontrar_lulu(self):
        """Encontra Lulu, ex-namorada"""
        dialogo = input('Você encontra sua ex namorada na frente do banheiro feminino, opção -1 falar com ela só por educação\n -2 ir embora: ')

        if dialogo == '2':
            print('')
            sprint('Você vai pra casa')
            self.limpar_terminal()
            return "ir_casa"
        elif dialogo == '1':
            print('')
            sprint('Vocês conversam e ela pergunta se você não quer se sentar à mesa com ela')
            print('')
            self.limpar_terminal()
            return "sentar_mesa_lulu"
        else:
            return self.encontrar_lulu()

    def sentaramesa_lulu(self):
        """Lulu convida para sentar à mesa"""
        senta = input('-1 Não, ir embora ou\n -2 Sim, sentar com ela? ')

        if senta == '1':
            print('')
            sprint('Lulu fica meio cabisbaixa, mas deixa você ir embora')
            print('')
            self.limpar_terminal()
            return "continuar_jogo"
        elif senta == '2':
            print('')
            sprint('Nada demais, afinal você já sabe lidar com ela')
            print('')
            sprint('Vocês se sentam à mesa e ela pede uma bebida')
            print('')
            self.limpar_terminal()
            return "beber_com_lulu"
        else:
            return self.sentaramesa_lulu()

    def bebercom_lulu(self):
        """Bebendo com Lulu"""
        bebidinha = input(Fore.MAGENTA + f'Lulu: Quer uma bebida também {self.nome}?\n -1 Sim\n -2 Não: ')

        if bebidinha == '1':
            print(Fore.RESET + '')
            sprint('Sim, quero me divertir')
            print('')
            sprint('Lulu vai ao banheiro')
            print('')
            sprint('O garçom anota os pedidos, mas quem leva é uma garçonete')
            print('')
            sprint(Fore.LIGHTGREEN_EX + 'Garçonete: Notei que você está sozinho, desculpe incomodar')
            print('')
            sprint(Fore.RESET + 'Antes mesmo de você responder algo…')
            print('')
            sprint(Fore.MAGENTA + 'Lulu: QUEM VOCÊ PENSA QUE É!?')
            print('')
            sprint(Fore.RESET + 'Elas começam a discutir')
            print('')
            sprint('Lulu joga a bebida na sua cara e vai embora')
            self.limpar_terminal()
            return "continuar_jogo"
        elif bebidinha == '2':
            print('')
            sprint('Não, não to muito afim de beber')
            print('')
            sprint('Lulu começa a virar todas')
            print('')
            sprint(f'{self.nome}: Hei! Vai com calma')
            print('')
            sprint(Fore.MAGENTA + 'Lulu: Eu zeiuqui eu to fazen…')
            print(Fore.RESET + '')
            sprint('Lulu está muito bêbada para ir pra casa sozinha')
            print('')
            self.limpar_terminal()
            return "decidir_casa_lulu"
        else:
            return self.bebercom_lulu()

    def decidir_casa_lulu(self):
        """Decidir se leva Lulu para casa"""
        casa = input('-1 Levar Lulu para a casa dela\n -2 Convidar Lulu para sua casa? ')

        if casa == '1':
            print('')
            sprint('Após levar Lulu a casa dela, você vê que está tarde e vai para sua casa')
            print('')
            self.limpar_terminal()
            return "continuar_jogo"
        elif casa == '2':
            print('')
            sprint('Você deixa Lulu ficar em sua casa')
            print('')
            sprint('Vocês relembram os velhos tempos')
            print('')
            self.limpar_terminal()
            return "continuar_jogo"
        else:
            return self.decidir_casa_lulu()
