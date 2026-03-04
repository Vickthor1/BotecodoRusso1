from colorama import Fore, init
import sys, time, random

init()

def sprint(texto):
    """Função para imprimir texto com efeito de digitação"""
    for c in texto + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

class falaAlice:
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

    def encontrar_alice(self):
        """Encontra Alice cantando no palco"""
        respalice = input('-1 Você grita ou\n -2 ficar admirando: ')

        if respalice == '1':
            sprint('A cantora acha estranho, para de cantar e chama os seguranças')
            print('')
            sprint('Você tenta mentir')
            self.limpar_terminal()
            return "alice_reagir_grito"
        elif respalice == '2':
            sprint('Você admira a voz dela')
            print('')
            self.limpar_terminal()
            return "alice_deboa"
        else:
            return self.encontrar_alice()

    def alice_reagir_grito(self):
        """Alice reage ao grito"""
        escolha = input('-1 Você fala que e fiscal testando segurança\n -2 Se faz de doido ou (3) Diz que quer falar com a cantora: ')

        if escolha in ['1', '3']:
            sprint('Seguranças: Cadê o seu cracha?!')
            sprint('Os seguranças te expulsam do bar na porrada')
            self.limpar_terminal()
            return "fim_jogo"
        elif escolha == '2':
            sprint('O segurança liga para médicos psiquiatras (manicômio)!')
            print('')
            self.limpar_terminal()
            return "fim_jogo"
        else:
            sprint(Fore.RESET + 'Não tem essa opção')
            return self.alice_reagir_grito()

    def alice_deboa(self):
        """Alice de boa - tenta sedução"""
        respa = input('-1 Quer tentar dueto com ela ou\n -2 Troca de olhares: ')

        if respa == '1':
            sprint(Fore.LIGHTRED_EX + 'rolagem de dados!!')
            dado1 = random.randrange(1, 6)
            self.limpar_terminal()

            if dado1 <= 3:
                print(Fore.RESET + '')
                sprint('você canta tão desafinado que ela fica mal')
                print('')
                sprint('Os seguranças ligam para ambulância')
                print('')
                sprint('Você é expulso do bar')
                self.limpar_terminal()
                return "fim_jogo"
            else:
                print(Fore.RESET + '')
                sprint('Você canta tão bem que ela te chama para o palco')
                print('')
                sprint('após o termino do show ela vai até você')
                self.limpar_terminal()
                return "alice_apresentacao"
        elif respa == '2':
            print('')
            sprint('Vocês trocam olhares')
            print('')
            sprint('Após o termino do show ela vai até você')
            self.limpar_terminal()
            return "alice_apresentacao"
        else:
            return self.alice_deboa()

    def alice_apresentacao(self):
        """Alice se apresenta"""
        sprint('Vocês se sentam e conversam')
        print('')
        sprint(Fore.YELLOW + 'Alice: Meu nome é Alice qual o seu?')
        print('')
        sprint(Fore.CYAN + f'{self.nome}: Meu nome é {self.nome}')
        print('')
        sprint(Fore.RESET + 'Você descobre que o dono do bar é o pai da Alice')
        print('')
        self.limpar_terminal()
        return "alice_paquera"

    def alice_paquera(self):
        """Decide se quer paquerar Alice"""
        paquera = input('-1 Tentar paquerar a Alice\n -2 Deixar na amizade: ')

        if paquera == '1':
            sprint('Rolagem de dados!!!')
            dado2 = random.randrange(1, 6)
            self.limpar_terminal()
            return self.alice_lulu_acontece(dado2)
        elif paquera == '2':
            sprint('vocês ficam conversando e bebendo')
            self.limpar_terminal()
            return "continuar_jogo"
        else:
            return self.alice_paquera()

    def alice_lulu_acontece(self, dado2):
        """Lulu aparece e complica tudo com Alice"""
        if dado2 < 3:
            sprint('Alice fica envergonhada')
            print('')
            sprint('Lulu aparece e começa a brigar com Alice')
            print('')
            sprint('Elas começam a discutir e briga')
            print('')
            sprint('Os seguranças as separam')
            print('')
            sprint('Lulu ameaça vocês')
            print('')
            sprint(Fore.RESET + 'Você leva Alice pra sua casa')
            print('')
            self.limpar_terminal()
            return "continuar_jogo"
        else:
            sprint('Você sente uma energia ruim')
            print('')
            sprint('Lulu aparece e puxa o cabelo de Alice')
            print('')
            sprint('Lulu pega uma faca e ameaça vocês, o que faz?')
            self.limpar_terminal()
            return "briga_lulu_alice"

    def briga_lulu_alice(self):
        """Briga entre Lulu e Alice com faca"""
        ameaca = input('-1 Tentar reagir\n -2 Puxar Alice para sair\n -3 Chamar seguranças: ')

        if ameaca == '1':
            self.limpar_terminal()
            dado3 = random.randrange(1, 6)

            if dado3 <= 3:
                print('')
                sprint('Você consegue desarmar Lulu a tempo')
                print('')
                sprint('Lulu começa a gritar')
            else:
                print('')
                sprint('Alice é ferida')
                print('')
                sprint('Os seguranças ligam ambulância')
            self.limpar_terminal()
            return "continuar_jogo"
        elif ameaca == '2':
            print('')
            sprint('Você puxa Alice para fora do bar')
            print('')
            sprint('Vocês saem dali')
            self.limpar_terminal()
            return "continuar_jogo"
        elif ameaca == '3':
            print('')
            sprint('Os seguranças levam Lulu')
            print('')
            sprint('Alice quer distância de você')
            self.limpar_terminal()
            return "continuar_jogo"
        else:
            return self.briga_lulu_alice()
