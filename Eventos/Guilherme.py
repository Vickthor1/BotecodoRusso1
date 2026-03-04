from colorama import Fore, init
import sys, time

init()

def sprint(texto):
    """Função para imprimir texto com efeito de digitação"""
    for c in texto + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

class falaGuilherme:
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

    def dialogo_guilherme(self):
        """Encontra Guilherme no banheiro"""
        print(Fore.RESET + '')
        sprint('Chegando lá você ouve: To sentindo cheiro de coelinho rosa')
        print('')
        grandam = input('O que você ira fazer? -1 Fugir\n -2 ficar e encarar ou (3) fingir que não ouviu: ')
        
        if grandam == '1':
            print('')
            sprint('Você corre para casa')
            self.limpar_terminal()
            return "ir_casa"
        elif grandam == '2':
            sprint(Fore.LIGHTMAGENTA_EX + 'Desconhecido: Senti sua falta nos treinos')
            print('')
            sprint(Fore.CYAN + f'{self.nome}: Guilherme?')
            print('')
            sprint(Fore.LIGHTMAGENTA_EX + 'Guilherme: Quer fazer um agachamante?')
            print('')
            sprint(Fore.CYAN + f'{self.nome}: Você bebeu vodka?')
            print('')
            sprint(Fore.LIGHTMAGENTA_EX + 'Guilherme: Quer beber comigo?')
            print(Fore.RESET + '')
            self.limpar_terminal()
            return "beber_com_guilherme"
        elif grandam == '3':
            sprint(Fore.RESET + 'Você sente uma mão no ombro')
            sprint('Você vira e é Guilherme seu amigo da academia')
            print('')
            sprint(Fore.CYAN + f'{self.nome}: Qual é Guilherme')
            print('')
            sprint(Fore.LIGHTMAGENTA_EX + 'Guilherme: Ta faltando nos treinos')
            print('')
            sprint(Fore.RESET + 'Guilherme faz um discurso motivacional e depois cai')
            print('')
            sprint('Você chama uma ambulancia e volta pra casa')
            self.limpar_terminal()
            return "ir_casa"
        else:
            sprint(Fore.RESET + 'Números por favor!')
            return self.dialogo_guilherme()

    def beber_com_guilherme(self):
        """Bebendo com Guilherme"""
        beberres = input(Fore.RESET + '-1 Beber com Guilherme ou\n -2 Deixa-lo sóbrio: ')
        
        if beberres == '1':
            print('')
            sprint('Vocês bebem a noite toda')
            print('')
            sprint('Você acorda na cama do Guilherme sem sentir as pernas')
            self.limpar_terminal()
            return "fim_jogo"
        elif beberres == '2':
            print('')
            sprint('Você troca a vodka dele por água')
            print('')
            sprint('Você o deixa em casa dele')
            self.limpar_terminal()
            return "explorar_mapa"
        else:
            sprint('Números apenas!')
            return self.beber_com_guilherme()