from colorama import Fore, init
import sys, time

init()

def sprint(texto):
    """Função para imprimir texto com efeito de digitação"""
    for c in texto + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

class falabarman:
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

    def dialogo_barman(self):
        """Diálogo completo com o barman Lex"""
        print(Fore.RESET + '')
        sprint(Fore.CYAN + f'{self.nome}: Olá boa noite, poderia me servir uma bebida?')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Barman: Por que toda essa formalidade amigão, pode ficar à vontade')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Barman: Temos, vodka, cachaça, whisky, vinho, skol, heineken, brahma, Itaipava...')
        print('')
        sprint(Fore.RESET + 'Você acaba não prestando muita atenção nas outras coisas que ele diz')
        print('')
        bebida = input(Fore.CYAN + f'{self.nome}: Eu gostaria de pedir ')
        print('')
        sprint(Fore.RESET + 'Você bate um papo com o Barman e ele te conta a História do Bar e que ele e a filha dele reabriram o bar no Brasil, pelo fato do país deles estarem em guerra e eles não apoiarem isso')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Barman: Você é um bom ouvinte meu jovem, meu nome é Alexandre mas pode e chamar de Lex')
        print('')
        sprint(Fore.CYAN + f'{self.nome}: meu nome é {self.nome}, prazer em conhecer o senhor')
        print('')
        explorar = input(Fore.RESET + 'Você quer -1 explorar o mapa ou\n -2 quer ir para sua casa? ')

        if explorar == '1':
            self.limpar_terminal()
            return "explorar_mapa"  # Retorna ação para o jogo principal
        elif explorar == '2':
            self.limpar_terminal()
            return "ir_casa"  # Retorna ação para o jogo principal
        else:
            sprint(Fore.LIGHTRED_EX + 'Só números')
            return self.dialogo_barman()  # Tenta novamente
