"""""""""
Jogo de bar que se chama Bar do Russo - VERSÃO FINAL UNIFICADA
Todas as funções conectadas de forma clara e organizada em um único arquivo
"""""""""

import os
import pyfiglet
from colorama import Fore, init
import sys, time, random

init()

# ==================== FUNÇÕES AUXILIARES ====================

def sprint(texto):
    """Função para imprimir texto com efeito de digitação"""
    for c in texto + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

def limpar_terminal(opcao):
    """Limpa o terminal baseado na opção do jogador"""
    if opcao == '1':
        input("ENTER para continuar")
        os.system("cls")
    elif opcao == '2':
        input("ENTER para continuar")

# ==================== CLASSES DOS PERSONAGENS ====================

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
        sprint(Fore.LIGHTBLACK_EX + 'Barman: Temos, vodka, cachaça, whisky, vinho, skol, heineken, brahma, Itaipava..')
        print('')
        sprint(Fore.RESET + 'Você acaba não prestando muita atenção nas outras coisas que ele diz')
        print('')
        pedido = input(Fore.CYAN + f'{self.nome}: Eu gostaria de pedir ')
        print('')
        sprint(Fore.LIGHTBLACK_EX + f'Barman: {pedido}?')
        print('')
        sprint(Fore.RESET + 'Você bate um papo com o Barman e ele te conta a História do Bar e que ele e a filha dele reabriram o bar no Brasil, pelo fato do país deles estarem em guerra e eles não apoiarem isso')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Barman: Você é um bom ouvinte meu jovem, meu nome é Alexandre mas pode e chamar de Lex')
        print('')
        sprint(Fore.CYAN + f'{self.nome}: meu nome é {self.nome}, prazer em conhecer o senhor')
        print('')
        explorar = input(Fore.RESET + 'Você quer -1 explorar o mapa ou\n -2 quer ir para sua casa? ')

        if explorar == '1':
            print('')
            sprint(Fore.RESET + 'Você decide explorar o bar')
            print('')
            self.limpar_terminal()
            return "explorar_mapa"
        elif explorar == '2':
            print('')
            sprint(Fore.RESET + 'Você decide ir para casa')
            print('')
            self.limpar_terminal()
            return "ir_casa"
        else:
            sprint(Fore.RESET + 'Não compreendi')
            return self.dialogo_barman()

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

class falaLex:
    def __init__(self, nome, opcao_visual):
        self.nome = nome
        self.opcao_visual = opcao_visual
        self.confianca = 0  # Nível de confiança com o jogador
        self.segredos_contados = []  # Segredos já revelados

    def limpar_terminal(self):
        """Limpa o terminal baseado na opção do jogador"""
        if self.opcao_visual == '1':
            input("ENTER para continuar")
            print("\033[H\033[J", end="")  # Limpa terminal
        elif self.opcao_visual == '2':
            input("ENTER para continuar")

    def dialogo_inicial(self):
        """Primeiro encontro com Lex no bar"""
        print(Fore.RESET + '')
        sprint(Fore.CYAN + f'{self.nome}: Boa noite! Este lugar parece incrível.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Barman: Bem-vindo ao Boteco do Russo, meu jovem!')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Barman: Eu sou Alexandre, mas pode me chamar de Lex.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Vejo que você é novo por aqui. O que vai querer?')
        print('')

        escolha = input(Fore.RESET + '-1 Pedir uma bebida\n -2 Perguntar sobre o bar\n -3 Conversar sobre a vida: ')

        if escolha == '1':
            return self.pedir_bebida()
        elif escolha == '2':
            return self.historia_bar()
        elif escolha == '3':
            return self.conversar_vida()
        else:
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Como disse? Não entendi...')
            return self.dialogo_inicial()

    def pedir_bebida(self):
        """Lex oferece bebidas especiais"""
        sprint(Fore.CYAN + f'{self.nome}: O que você recomenda?')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Temos várias opções, mas para um novato como você...')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Que tal experimentar nossa especialidade? A "Vodka Russo Original"!')
        print('')

        escolha = input(Fore.RESET + '-1 Aceitar a recomendação\n -2 Pedir algo mais simples\n -3 Perguntar sobre drinks exóticos: ')

        if escolha == '1':
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Excelente escolha! Uma dose da nossa vodka especial.')
            print('')
            sprint(Fore.RESET + '*Você toma um gole e sente um calor reconfortante*')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: E aí, gostou? Esta vodka vem direto da minha terra natal.')
            self.confianca += 1
            self.limpar_terminal()
            return "conversar_mais"
        elif escolha == '2':
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Uma Brahma gelada então! Nada como uma cerveja brasileira.')
            print('')
            sprint(Fore.RESET + '*Você bebe a cerveja e relaxa*')
            self.limpar_terminal()
            return "conversar_mais"
        elif escolha == '3':
            return self.drinks_exoticos()
        else:
            return self.pedir_bebida()

    def drinks_exoticos(self):
        """Lex fala sobre drinks especiais e apresenta um novo personagem"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Ah, você é do tipo aventureiro? Temos drinks bem especiais aqui.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Temos o "Coquetel Russo Secreto", feito com ingredientes que só eu conheço a receita.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Mas antes de te servir, preciso saber se você é confiável...')
        print('')

        escolha = input(Fore.RESET + '-1 Contar um segredo seu\n -2 Oferecer ajuda no bar\n -3 Desistir e pedir algo normal: ')

        if escolha == '1':
            sprint(Fore.CYAN + f'{self.nome}: Bom, eu... [conta um segredo pessoal]')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Interessante... Você parece sincero.')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Está bem, vou te apresentar alguém especial.')
            self.confianca += 2
            self.limpar_terminal()
            return "apresentar_personagem_secreto"
        elif escolha == '2':
            sprint(Fore.CYAN + f'{self.nome}: Posso ajudar em algo?')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Na verdade, temos um problema com uns clientes chatos ultimamente.')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: São três caras no canto ali. Pode conversar com eles e pedir para se comportarem?')
            self.confianca += 1
            self.limpar_terminal()
            return "missao_bar"
        elif escolha == '3':
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Tudo bem, não force. Uma cerveja então!')
            self.limpar_terminal()
            return "conversar_mais"
        else:
            return self.drinks_exoticos()

    def apresentar_personagem_secreto(self):
        """Lex apresenta um novo personagem secreto"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Venha comigo, vou te apresentar alguém que poucos conhecem.')
        print('')
        sprint(Fore.RESET + '*Lex te leva para uma sala nos fundos do bar*')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Esta é Natasha, minha irmã mais nova. Ela não aparece muito por aqui.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Olá... Você deve ser o novo cliente que meu irmão mencionou.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Natasha é especialista em leitura de cartas e prevê o futuro.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Quer que eu leia sua sorte? Posso ver seu futuro amoroso...')
        print('')

        escolha = input(Fore.RESET + '-1 Aceitar leitura de cartas\n -2 Conversar com Natasha\n -3 Voltar ao bar: ')

        if escolha == '1':
            return self.leitura_cartas()
        elif escolha == '2':
            return self.conversar_natasha()
        elif escolha == '3':
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Como quiser. Volte quando mudar de ideia!')
            self.limpar_terminal()
            return "explorar_mapa"
        else:
            return self.apresentar_personagem_secreto()

    def leitura_cartas(self):
        """Natasha lê as cartas para o jogador"""
        sprint(Fore.MAGENTA + 'Natasha: Sente-se e relaxe. Vou embaralhar as cartas...')
        print('')
        sprint(Fore.RESET + '*Natasha embaralha as cartas misteriosamente*')
        print('')
        dado = random.randrange(1, 6)

        if dado <= 2:
            sprint(Fore.MAGENTA + 'Natasha: Vejo... uma ex-namorada ciumenta no seu futuro próximo.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Cuidado com decisões precipitadas no amor.')
        elif dado <= 4:
            sprint(Fore.MAGENTA + 'Natasha: As cartas mostram uma cantora misteriosa...')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Uma conexão musical pode mudar seu destino.')
        else:
            sprint(Fore.MAGENTA + 'Natasha: Interessante... vejo um amigo leal que pode te surpreender.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Às vezes os verdadeiros tesouros estão próximos.')

        print('')
        sprint(Fore.MAGENTA + 'Natasha: Lembre-se, o futuro não é fixo... você pode mudá-lo.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: O que achou? Minha irmã é incrível, não é?')
        self.confianca += 1
        self.limpar_terminal()
        return "explorar_mapa"

    def conversar_natasha(self):
        """Conversa pessoal com Natasha"""
        sprint(Fore.CYAN + f'{self.nome}: Prazer em conhecê-la, Natasha. Você trabalha aqui também?')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Não exatamente... Eu ajudo meu irmão quando preciso.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Este bar tem muitos segredos... alguns deles meus.')
        print('')

        escolha = input(Fore.RESET + '-1 Perguntar sobre os segredos\n -2 Contar sobre você\n -3 Encerrar conversa: ')

        if escolha == '1':
            if 'segredo_natasha' not in self.segredos_contados:
                sprint(Fore.MAGENTA + 'Natasha: Bem... eu vejo coisas que os outros não veem.')
                print('')
                sprint(Fore.MAGENTA + 'Natasha: Por exemplo, vejo que você tem um coração bondoso, mas também impulsivo.')
                print('')
                sprint(Fore.MAGENTA + 'Natasha: Tome cuidado esta noite... nem todos são o que parecem.')
                self.segredos_contados.append('segredo_natasha')
                self.confianca += 1
            else:
                sprint(Fore.MAGENTA + 'Natasha: Já contei segredos demais por hoje...')
        elif escolha == '2':
            sprint(Fore.CYAN + f'{self.nome}: [conta um pouco sobre sua vida]')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Entendo... Você parece alguém que busca significado.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Às vezes o encontramos nos lugares mais inesperados.')
        elif escolha == '3':
            sprint(Fore.MAGENTA + 'Natasha: Foi um prazer conversar. Volte sempre!')
        else:
            return self.conversar_natasha()

        self.limpar_terminal()
        return "explorar_mapa"

    def missao_bar(self):
        """Missão para ajudar no bar"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Ótimo! Temos uns clientes que ficam incomodando as garçonetes.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: São três caras no canto ali. Pode conversar com eles e pedir para se comportarem?')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Se conseguir, te dou o drink especial e talvez alguns conselhos valiosos.')
        print('')

        escolha = input(Fore.RESET + '-1 Aceitar a missão\n -2 Recusar educadamente\n -3 Pedir mais detalhes: ')

        if escolha == '1':
            sprint(Fore.CYAN + f'{self.nome}: Deixa comigo!')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Boa sorte! E cuidado, eles são bem... temperamentais.')
            self.limpar_terminal()
            return "confronto_clientes"
        elif escolha == '2':
            sprint(Fore.CYAN + f'{self.nome}: Desculpe, mas não quero arrumar briga.')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Entendo... nem todos são feitos para heróis.')
            self.limpar_terminal()
            return "conversar_mais"
        elif escolha == '3':
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Eles ficam cantando músicas obscenas e incomodando todo mundo.')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Só peça para eles se acalmarem. Nada de violência desnecessária.')
            return self.missao_bar()
        else:
            return self.missao_bar()

    def confronto_clientes(self):
        """Confronto com os clientes chatos"""
        sprint(Fore.RESET + '*Você se aproxima dos três caras no canto*')
        print('')
        sprint(Fore.CYAN + f'{self.nome}: Ei pessoal, podem baixar o volume aí? Estão incomodando.')
        print('')
        sprint(Fore.RED + 'Cliente 1: Quem você pensa que é, moleque? Cai fora!')
        print('')
        sprint(Fore.CYAN + f'{self.nome}: O barman pediu para eu conversar com vocês.')
        print('')

        escolha = input(Fore.RESET + '-1 Insistir pacificamente\n -2 Usar de humor\n -3 Chamar Lex: ')

        if escolha == '1':
            dado = random.randrange(1, 6)
            if dado <= 3:
                sprint(Fore.RED + 'Cliente 1: Você quer levar porrada? Suma daqui!')
                print('')
                sprint(Fore.RESET + '*Os clientes ficam mais agressivos*')
                self.limpar_terminal()
                return "fracasso_missao"
            else:
                sprint(Fore.RED + 'Cliente 1: Tá bom, tá bom... vamos nos acalmar.')
                print('')
                sprint(Fore.RESET + '*Os clientes baixam o tom*')
                self.confianca += 2
                self.limpar_terminal()
                return "sucesso_missao"
        elif escolha == '2':
            sprint(Fore.CYAN + f'{self.nome}: Ei, eu também gosto de uma música alta, mas vamos respeitar os outros?')
            print('')
            sprint(Fore.RED + 'Cliente 2: Hahaha, o cara tem razão. Vamos beber em paz.')
            print('')
            sprint(Fore.RESET + '*Os clientes riem e acalmam*')
            self.confianca += 1
            self.limpar_terminal()
            return "sucesso_missao"
        elif escolha == '3':
            sprint(Fore.CYAN + f'{self.nome}: LEX! Preciso de ajuda aqui!')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Já estou indo!')
            print('')
            sprint(Fore.RESET + '*Lex aparece e resolve a situação rapidamente*')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Obrigado pela tentativa, amigo.')
            self.limpar_terminal()
            return "missao_meia_sucesso"
        else:
            return self.confronto_clientes()

    def sucesso_missao(self):
        """Sucesso na missão"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Impressionante! Você conseguiu sem violência.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Como prometido, aqui está seu drink especial!')
        print('')
        sprint(Fore.RESET + '*Lex prepara um drink colorido e misterioso*')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Prove! É feito com vodka, mel silvestre e um toque secreto.')
        print('')
        sprint(Fore.RESET + '*O drink tem um sabor incrível, você se sente revigorado*')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Agora você é um amigo do bar. Volte sempre!')
        self.confianca += 3
        self.limpar_terminal()
        return "explorar_mapa"

    def fracasso_missao(self):
        """Fracasso na missão"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Tudo bem, nem sempre dá certo. Obrigado por tentar.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Aqui, uma bebida por conta da casa para compensar.')
        print('')
        sprint(Fore.RESET + '*Você recebe uma bebida grátis*')
        self.confianca += 1
        self.limpar_terminal()
        return "explorar_mapa"

    def missao_meia_sucesso(self):
        """Meio sucesso na missão"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Pelo menos tentou. Aqui está um drink normal, mas com desconto.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Da próxima vez, chame logo!')
        self.confianca += 1
        self.limpar_terminal()
        return "explorar_mapa"

    def historia_bar(self):
        """Lex conta a história do bar"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Ah, a história do Boteco do Russo... É uma história interessante.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Eu vim da Rússia há muitos anos, fugindo da guerra.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Minha filha Alice nasceu aqui no Brasil. Ela herdou meu amor pela música.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Este bar era um lugar abandonado. Eu o reformei com minhas próprias mãos.')
        print('')

        if self.confianca >= 2:
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Já que você provou ser confiável, vou te contar um segredo...')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Este bar tem uma adega secreta nos fundos, com vinhos raros.')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Só pessoas especiais têm acesso.')
            self.segredos_contados.append('adega_secreta')

        self.limpar_terminal()
        return "conversar_mais"

    def conversar_vida(self):
        """Conversa pessoal sobre a vida"""
        sprint(Fore.CYAN + f'{self.nome}: Como você veio parar aqui? Qual sua história?')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Minha história... É longa, meu amigo.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Deixei tudo para trás: família, amigos, minha terra natal.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Mas aqui encontrei paz... e uma nova família.')
        print('')

        escolha = input(Fore.RESET + '-1 Compartilhar sua própria história\n -2 Dar apoio\n -3 Mudar assunto: ')

        if escolha == '1':
            sprint(Fore.CYAN + f'{self.nome}: [conta um pouco da sua história]')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Entendo... Todos temos nossas batalhas.')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Lembre-se: o passado molda, mas não define o futuro.')
            self.confianca += 1
        elif escolha == '2':
            sprint(Fore.CYAN + f'{self.nome}: Você construiu algo incrível aqui. Deve se orgulhar.')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Obrigado, meu amigo. Significa muito ouvir isso.')
            self.confianca += 1
        elif escolha == '3':
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Como quiser. Sempre estou aqui para conversar.')

        self.limpar_terminal()
        return "conversar_mais"

    def conversar_mais(self):
        """Continuar conversa com Lex"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Mais alguma coisa? Ou quer explorar o bar?')
        print('')

        escolha = input(Fore.RESET + '-1 Pedir mais uma bebida\n -2 Perguntar sobre outros clientes\n -3 Ir explorar o bar\n -4 Conversar sobre Alice: ')

        if escolha == '1':
            return self.pedir_bebida()
        elif escolha == '2':
            return self.falar_clientes()
        elif escolha == '3':
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Divirta-se! E cuidado com as confusões.')
            self.limpar_terminal()
            return "explorar_mapa"
        elif escolha == '4':
            return self.falar_alice()
        else:
            return self.conversar_mais()

    def falar_clientes(self):
        """Lex fala sobre outros clientes"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Bem, temos vários tipos por aqui...')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Jack é um bom rapaz, mas impulsivo demais.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Lulu... ah, Lulu. Uma mulher complicada, mas com bom coração.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: E tem o Guilherme, que aparece de vez em quando.')
        print('')

        if self.confianca >= 3:
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Já que confio em você, fique de olho no Jack hoje.')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Ele anda estranho ultimamente...')

        self.limpar_terminal()
        return "conversar_mais"

    def falar_alice(self):
        """Lex fala sobre sua filha Alice"""
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Minha Alice... Ela é tudo para mim.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Veio ao mundo cantando, literalmente!')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Ela herdou minha voz... e minha teimosia.')
        print('')
        sprint(Fore.LIGHTBLACK_EX + 'Lex: Mas é talentosa. Um dia vai ser famosa.')
        print('')

        escolha = input(Fore.RESET + '-1 Dizer que concorda\n -2 Perguntar se ela canta hoje\n -3 Mudar assunto: ')

        if escolha == '1':
            sprint(Fore.CYAN + f'{self.nome}: Ela realmente tem talento incrível!')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Obrigado! Você entende de música?')
            self.confianca += 1
        elif escolha == '2':
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Ela canta todas as sextas. Hoje é sexta... mas ela não está.')
            print('')
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Deve estar ensaiando algo novo.')
        elif escolha == '3':
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Como quiser.')

        self.limpar_terminal()
        return "conversar_mais"

class falaNatasha:
    def __init__(self, nome, opcao_visual):
        self.nome = nome
        self.opcao_visual = opcao_visual
        self.intimidade = 0  # Nível de intimidade com o jogador
        self.cartas_lidas = 0  # Número de leituras de cartas feitas

    def limpar_terminal(self):
        """Limpa o terminal baseado na opção do jogador"""
        if self.opcao_visual == '1':
            input("ENTER para continuar")
            print("\033[H\033[J", end="")  # Limpa terminal
        elif self.opcao_visual == '2':
            input("ENTER para continuar")

    def encontro_inicial(self):
        """Primeiro encontro com Natasha nos fundos do bar"""
        print(Fore.RESET + '')
        sprint(Fore.MAGENTA + 'Natasha: Bem-vinda aos meus aposentos secretos.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Poucos têm o privilégio de vir aqui.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Meu irmão confia em você... isso já diz muito.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Sou Natasha, vidente e guardiã dos segredos deste bar.')
        print('')

        escolha = input(Fore.RESET + '-1 Pedir uma leitura de cartas\n -2 Conversar sobre o futuro\n -3 Perguntar sobre os segredos do bar\n -4 Sair educadamente: ')

        if escolha == '1':
            return self.leitura_cartas_completa()
        elif escolha == '2':
            return self.falar_futuro()
        elif escolha == '3':
            return self.segredos_bar()
        elif escolha == '4':
            sprint(Fore.MAGENTA + 'Natasha: Volte quando estiver pronta para conhecer a verdade.')
            self.limpar_terminal()
            return "voltar_lex"
        else:
            return self.encontro_inicial()

    def leitura_cartas_completa(self):
        """Leitura completa das cartas com mais detalhes"""
        if self.cartas_lidas >= 3:
            sprint(Fore.MAGENTA + 'Natasha: Já li suas cartas muitas vezes hoje...')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: O futuro precisa de tempo para se revelar.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Volte amanhã para uma nova leitura.')
            self.limpar_terminal()
            return "explorar_mapa"
        else:
            sprint(Fore.MAGENTA + 'Natasha: Sente-se confortavelmente. Vou preparar as cartas.')
            print('')
            sprint(Fore.RESET + '*Natasha acende velas aromáticas e embaralha o baralho*')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Pense em uma pergunta específica ou deixe o universo guiar.')
            print('')

            # Leitura de 3 cartas
            cartas = []
            for i in range(3):
                carta = random.choice([
                    "O Louco", "A Sacerdotisa", "A Imperatriz", "O Imperador",
                    "O Hierofante", "Os Amantes", "A Carruagem", "A Justiça",
                    "O Eremita", "A Roda da Fortuna", "A Força", "O Enforcado",
                    "A Morte", "A Temperança", "O Diabo", "A Torre",
                    "A Estrela", "A Lua", "O Sol", "O Julgamento", "O Mundo"
                ])
                cartas.append(carta)

            sprint(Fore.MAGENTA + f'Natasha: A primeira carta representa seu passado: {cartas[0]}')
            self.interpretar_carta(cartas[0], "passado")

            sprint(Fore.MAGENTA + f'Natasha: A segunda carta mostra seu presente: {cartas[1]}')
            self.interpretar_carta(cartas[1], "presente")

            sprint(Fore.MAGENTA + f'Natasha: A terceira carta revela seu futuro: {cartas[2]}')
            self.interpretar_carta(cartas[2], "futuro")

            print('')
            sprint(Fore.MAGENTA + 'Natasha: Lembre-se: as cartas mostram possibilidades, não certezas.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Você tem o poder de mudar seu destino.')

            self.cartas_lidas += 1
            self.intimidade += 1
            self.limpar_terminal()
            return "conversar_natasha"

    def interpretar_carta(self, carta, contexto):
        """Interpreta uma carta do tarô baseada no contexto"""
        interpretacoes = {
            "O Louco": {
                "passado": "Você sempre foi aventureiro, tomando decisões impulsivas.",
                "presente": "Está em um momento de mudança e novos começos.",
                "futuro": "Uma jornada inesperada está chegando."
            },
            "A Sacerdotisa": {
                "passado": "Teve intuições fortes que o guiaram.",
                "presente": "Confie em sua voz interior.",
                "futuro": "Segredos serão revelados."
            },
            "Os Amantes": {
                "passado": "Relações importantes moldaram sua vida.",
                "presente": "Uma escolha amorosa se aproxima.",
                "futuro": "Encontrará harmonia em relacionamentos."
            },
            "A Torre": {
                "passado": "Mudanças bruscas aconteceram.",
                "presente": "Prepare-se para transformações.",
                "futuro": "Estruturas antigas ruirão."
            },
            "A Estrela": {
                "passado": "Sempre teve esperança.",
                "presente": "A esperança renasce em você.",
                "futuro": "Seus desejos se realizarão."
            }
        }

        if carta in interpretacoes:
            sprint(Fore.CYAN + interpretacoes[carta][contexto])
        else:
            sprint(Fore.CYAN + f'A carta {carta} traz mensagens positivas para seu {contexto}.')

        print('')

    def falar_futuro(self):
        """Conversa sobre conceitos do futuro"""
        sprint(Fore.MAGENTA + 'Natasha: O futuro não é linear como muitos pensam.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: É como um rio com muitos afluentes possíveis.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Suas escolhas de hoje criam os caminhos de amanhã.')
        print('')

        escolha = input(Fore.RESET + '-1 Perguntar sobre seu futuro pessoal\n -2 Falar sobre livre arbítrio\n -3 Compartilhar medos sobre o futuro\n -4 Mudar assunto: ')

        if escolha == '1':
            sprint(Fore.CYAN + f'{self.nome}: O que você vê no meu futuro?')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Vejo potencial... mas também vejo dúvidas.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Você tem o dom de conectar pessoas, mas ainda não percebe.')
            self.intimidade += 1
        elif escolha == '2':
            sprint(Fore.MAGENTA + 'Natasha: O livre arbítrio existe, mas é limitado.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Podemos escolher nossos caminhos, mas não controlar todas as consequências.')
        elif escolha == '3':
            sprint(Fore.CYAN + f'{self.nome}: [compartilha medos sobre o futuro]')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: O medo do desconhecido é natural...')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Mas lembre-se: você já sobreviveu a muitos "desconhecidos" antes.')
            self.intimidade += 1
        elif escolha == '4':
            return self.encontro_inicial()

        self.limpar_terminal()
        return "conversar_natasha"

    def segredos_bar(self):
        """Natasha revela segredos do bar"""
        if self.intimidade < 2:
            sprint(Fore.MAGENTA + 'Natasha: Ainda não confio o suficiente para compartilhar nossos segredos.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Prove sua lealdade primeiro.')
            self.limpar_terminal()
            return "conversar_natasha"
        else:
            sprint(Fore.MAGENTA + 'Natasha: Muito bem... você provou ser digno.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Este bar foi construído sobre uma antiga adega russa.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Meu pai trouxe vinhos raros da nossa terra natal.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: E há... outras coisas escondidas aqui.')
            print('')

            escolha = input(Fore.RESET + '-1 Perguntar sobre as "outras coisas"\n -2 Pedir para ver a adega\n -3 Guardar segredo: ')

            if escolha == '1':
                sprint(Fore.MAGENTA + 'Natasha: Coisas do passado... artefatos, documentos, memórias.')
                print('')
                sprint(Fore.MAGENTA + 'Natasha: Alguns dizem que há até um tesouro escondido.')
                print('')
                sprint(Fore.MAGENTA + 'Natasha: Mas o verdadeiro tesouro são as histórias que guardamos.')
            elif escolha == '2':
                sprint(Fore.MAGENTA + 'Natasha: A adega é sagrada. Só meu pai tem a chave completa.')
                print('')
                sprint(Fore.MAGENTA + 'Natasha: Talvez um dia você prove ser digno o suficiente.')
            elif escolha == '3':
                sprint(Fore.MAGENTA + 'Natasha: Sábia decisão. Alguns segredos são perigosos demais.')

            self.intimidade += 1
            self.limpar_terminal()
            return "conversar_natasha"

    def conversar_natasha(self):
        """Continuar conversa com Natasha"""
        sprint(Fore.MAGENTA + 'Natasha: O que mais gostaria de saber?')
        print('')

        escolha = input(Fore.RESET + '-1 Perguntar sobre sua vida\n -2 Pedir conselhos\n -3 Falar sobre o bar\n -4 Sair: ')

        if escolha == '1':
            return self.historia_natasha()
        elif escolha == '2':
            return self.conselhos_natasha()
        elif escolha == '3':
            return self.falar_bar_natasha()
        elif escolha == '4':
            sprint(Fore.MAGENTA + 'Natasha: Até a próxima. Que o universo guie seus passos.')
            self.limpar_terminal()
            return "voltar_lex"
        else:
            return self.conversar_natasha()

    def historia_natasha(self):
        """Natasha conta sua história"""
        sprint(Fore.MAGENTA + 'Natasha: Minha história... é entrelaçada com a deste bar.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Nasci na Rússia, mas cresci entre dois mundos.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Meu dom de ver o futuro se manifestou cedo.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Meu pai me ensinou a usar este dom com responsabilidade.')
        print('')

        if self.intimidade >= 3:
            sprint(Fore.MAGENTA + 'Natasha: Mas há um segredo que poucos sabem...')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Eu vejo não só o futuro, mas também vidas passadas.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: E a sua... tem muitas camadas interessantes.')

        self.intimidade += 1
        self.limpar_terminal()
        return "conversar_natasha"

    def conselhos_natasha(self):
        """Natasha dá conselhos"""
        sprint(Fore.MAGENTA + 'Natasha: Que tipo de conselho procura?')
        print('')

        escolha = input(Fore.RESET + '-1 Sobre amor\n -2 Sobre carreira\n -3 Sobre amizades\n -4 Sobre vida em geral: ')

        conselhos = {
            '1': 'No amor, seja verdadeiro consigo mesmo. As máscaras caem com o tempo.',
            '2': 'Sua carreira florescerá quando você seguir sua paixão, não suas obrigações.',
            '3': 'Amigos verdadeiros são raros. Cuide daqueles que ficam nas noites difíceis.',
            '4': 'A vida é como um rio: às vezes calma, às vezes turbulenta. Aprenda a navegar ambas.'
        }

        if escolha in conselhos:
            sprint(Fore.CYAN + conselhos[escolha])
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Reflita sobre estas palavras. Elas podem ajudar mais do que imagina.')

        self.intimidade += 1
        self.limpar_terminal()
        return "conversar_natasha"

    def falar_bar_natasha(self):
        """Natasha fala sobre o bar de sua perspectiva"""
        sprint(Fore.MAGENTA + 'Natasha: Este bar é mais do que parece.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: É um ponto de encontro entre mundos.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: Cada cliente traz sua própria energia.')
        print('')
        sprint(Fore.MAGENTA + 'Natasha: E você... trouxe uma energia interessante.')
        print('')

        escolha = input(Fore.RESET + '-1 Perguntar sobre outros clientes\n -2 Perguntar sobre você\n -3 Concordar e continuar: ')

        if escolha == '1':
            sprint(Fore.MAGENTA + 'Natasha: Cada um tem seu papel nesta história.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Alguns buscam redenção, outros aventura.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Observe atentamente... você pode aprender muito.')
        elif escolha == '2':
            sprint(Fore.MAGENTA + 'Natasha: Minha energia? É de proteção e sabedoria.')
            print('')
            sprint(Fore.MAGENTA + 'Natasha: Eu vejo os fios que conectam as pessoas.')
        elif escolha == '3':
            sprint(Fore.MAGENTA + 'Natasha: Fico feliz que perceba. Poucos notam.')

        self.limpar_terminal()
        return "conversar_natasha"

# ==================== FUNÇÕES DE INICIALIZAÇÃO ====================

def mostrar_titulo():
    """Exibe o título do jogo"""
    result = pyfiglet.figlet_format("Boteco do Russo", font="banner3-D") 
    sprint(result)

def criar_jogador():
    """Cria e retorna dicionário com dados iniciais do jogador"""
    nome = input("Qual o nome do seu personagem? ")
    return {
        "nome": nome,
        "opcao_visual": None,
        "veiculo": None,
        "no_bar": False
    }

def exibir_introducao(jogo):
    """Exibe a introdução do jogo"""
    sprint(f"""
      Bem vindo ao "Boteco don Russo",
      como todo o lugar infelizmente a falha é algo inevitavel, mas aqui nesse game é evitavel
      toda a vez que você falhar, você volta ao vai ter que fazer o game todo de novo, tenha cuidado com quem conversa
      (as escolhas seram feitas com atalho rápido, nas escolhas sem numeração responda o que quiser. 
      Sistema de dinheiro, barra de bebida e modo de jogo, não inclusos nem nessa demo e nem na de dia 18 de novembro)
           """)
    print('')
    sprint(Fore.RED + ' !!!ATENÇÃO JOGO HUMORISTICO, QUALQUER SEMELHANÇA COM ALGO REAL É MERA CONHECIDENCIA!!! ')

def escolher_modo_visual(jogo):
    """Permite ao jogador escolher como quer jogar"""
    sprint("O jogo conta com 2 opções de jogo, uma você conta com a função de apagar mensagens com enter\n a outra sem essa função mas o enter continua os dialogos")
    
    while True:
        opcao = input("-1 Apagar mensagens com ENTER\n -2 Não apagar mensagens com ENTER\n Escolha: ")
        if opcao in ['1', '2']:
            jogo["opcao_visual"] = opcao
            sprint(Fore.RED + 'INFORMAÇÂO GUARDADA!')
            print(Fore.RESET + '')
            limpar_terminal(opcao)
            return jogo
        else:
            sprint('Não compreendi(digite 1 ou 2)')

def introducao_historia(jogo):
    """Inicia a história do jogo"""
    nome = jogo["nome"]
    print(Fore.RESET + '')
    print('')
    sprint(f"""Chegou a sexta feira, dia da semana que o filho chora e a mãe não vê,
         {nome} quer curtir a sua grande noite com tudo que ela pode oferecer,
         você pega seu telefone e da uma olhada nas suas redes sociais até que...""")
    sprint('Você vê que tem um bar novo bem popular na sua cidade')
    return jogo

# ==================== FUNÇÕES DE ESCOLHAS PRINCIPAIS ====================

def escolher_ir_bar(jogo):
    """Jogador decide se vai ao bar ou fica em casa"""
    print('')
    opcao = input('-1 Você quer ir a esse bar\n -2 não ir e ficar em casa? ')
    
    if opcao == '1':
        print('')
        sprint('Você decide ir ao bar novo')
        print('')
        limpar_terminal(jogo["opcao_visual"])
        jogo = escolher_veiculo(jogo)
        jogo["no_bar"] = True
        return jogo
    elif opcao == '2':
        print('')
        sprint('Você decide ficar na sua casa assistindo séria e comendo pipoca')
        print('')
        limpar_terminal(jogo["opcao_visual"])
        return jogo
    else:
        sprint('Não entendi(digite 1 ou 2)')
        return escolher_ir_bar(jogo)

def escolher_veiculo(jogo):
    """Jogador escolhe como chegar ao bar"""
    while True:
        veiculo = input('-1 você prefere ir andando ou\n -2 de moto? ')
        
        if veiculo == '1':
            jogo["veiculo"] = "andando"
            print('')
            sprint('você andou bastante até chegar no bar novo')
            print('')
            sprint(Fore.RED + 'INFORMAÇÂO GUARDADA!')
            print(Fore.RESET + '')
            limpar_terminal(jogo["opcao_visual"])
            return jogo
        elif veiculo == '2':
            jogo["veiculo"] = "moto"
            print('')
            sprint('você chegou rapidinho no bar novo')
            print('')
            sprint(Fore.RED + 'INFORMAÇÂO GUARDADA!')
            print(Fore.RESET + '')
            limpar_terminal(jogo["opcao_visual"])
            return jogo
        else:
            sprint('Não compreendi(digite 1 ou 2)')

def encontrar_amigo(jogo):
    """Jogador encontra Jack no bar - primeira pessoa que vê"""
    print('')
    sprint(Fore.RESET + 'Você vê que tem um amigo seu lá')
    print('')
    primeira_fala = input('-1 Vai cumprimenta-lo\n -2 não? ')
    
    if primeira_fala == '1':
        print('')
        sprint('Você decide falar com ele')
        print('')
        limpar_terminal(jogo["opcao_visual"])
        return dialogo_jack(jogo)
    elif primeira_fala == '2':
        print('')
        sprint('Você ignora o Jack e logo vai falar com o barman')
        limpar_terminal(jogo["opcao_visual"])
        return dialogo_barman(jogo)
    else:
        sprint('Não compreendi(digite 1 ou 2)')
        return encontrar_amigo(jogo)

def dialogo_jack(jogo):
    """Diálogo com Jack - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Jack
    jack = falaJack(nome, opcao_visual)
    
    # Executa o diálogo e recebe a ação
    acao = jack.dialogo_jack()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "explorar_mapa":
        return explorar_mapa(jogo)
    elif acao == "pergunta_jack":
        return pergunta_jack(jogo)
    else:
        return dialogo_jack(jogo)

def pergunta_jack(jogo):
    """Jack pergunta se viu alguém interessante - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Jack
    jack = falaJack(nome, opcao_visual)
    
    # Executa a pergunta e recebe a ação
    acao = jack.pergunta_jack()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "jack_sim":
        return jack_sim(jogo)
    elif acao == "jack_nao":
        return jack_nao(jogo)
    elif acao == "jack_bravo":
        return jack_bravo(jogo)
    else:
        return pergunta_jack(jogo)

def jack_nao(jogo):
    """Resposta negativa para Jack - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Jack
    jack = falaJack(nome, opcao_visual)
    
    # Executa a resposta negativa
    jack.jack_nao()
    return jogo

def jack_sim(jogo):
    """Resposta positiva para Jack - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Jack
    jack = falaJack(nome, opcao_visual)
    
    # Executa a resposta positiva e recebe a ação
    acao = jack.jack_sim()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "explorar_mapa":
        return explorar_mapa(jogo)
    elif acao == "fim_jogo":
        return jogo  # Fim do jogo
    else:
        return jogo

def jack_bravo(jogo):
    """Jack fica bravo - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Jack
    jack = falaJack(nome, opcao_visual)
    
    # Executa a resposta brava e recebe a ação
    acao = jack.jack_bravo()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "jack_bravo_opcoes":
        return jack_bravo_opcoes(jogo)
    else:
        return jogo

def jack_bravo_opcoes(jogo):
    """Opções após Jack ficar bravo - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Jack
    jack = falaJack(nome, opcao_visual)
    
    # Executa as opções e recebe a ação
    acao = jack.jack_bravo_opcoes()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "continuar_jogo":
        return jogo
    elif acao == "explorar_mapa":
        return explorar_mapa(jogo)
    else:
        # Para jack_porrada ou outros casos
        return jogo

def dialogo_barman(jogo):
    """Diálogo com Lex, o barman - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa o diálogo e recebe a ação
    acao = lex.dialogo_inicial()

    # Baseado na ação retornada, continua o fluxo
    if acao == "explorar_mapa":
        return explorar_mapa(jogo)
    elif acao == "conversar_mais":
        return conversar_lex(jogo)
    elif acao == "apresentar_personagem_secreto":
        return apresentar_natasha(jogo)
    elif acao == "missao_bar":
        return missao_lex(jogo)
    elif acao == "ir_casa":
        return jogo
    else:
        # Se retornou uma nova ação, processa recursivamente
        return dialogo_barman(jogo)

def explorar_mapa(jogo):
    """Jogador escolhe para onde ir no bar"""
    print(Fore.RESET + '')
    sprint('-1 Ir para perto do banheiro Feminino\n -2 ir ao banheiro masculino ou (3) ir até o salão principal')
    respos = input('')
    
    if respos == '1':
        print('')
        limpar_terminal(jogo["opcao_visual"])
        return encontrar_lulu(jogo)
    elif respos == '2':
        print('')
        sprint('Você vai até o banheiro masculino')
        limpar_terminal(jogo["opcao_visual"])
        return dialogo_guilherme(jogo)
    elif respos == '3':
        print('')
        sprint('Você vai ao salão principal')
        sprint('Você vê uma jovem cantando no palco e resolve se aproximar, você fica encantado com a voz dela ')
        print('')
        limpar_terminal(jogo["opcao_visual"])
        return encontrar_alice(jogo)
    else:
        sprint('Só tem esses lugares')
        return explorar_mapa(jogo)

def conversar_lex(jogo):
    """Continuar conversa com Lex - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa a conversa e recebe a ação
    acao = lex.conversar_mais()

    # Baseado na ação retornada, continua o fluxo
    if acao == "explorar_mapa":
        return explorar_mapa(jogo)
    elif acao == "conversar_mais":
        return conversar_lex(jogo)
    else:
        return dialogo_barman(jogo)

def apresentar_natasha(jogo):
    """Lex apresenta Natasha - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa a apresentação e recebe a ação
    acao = lex.apresentar_personagem_secreto()

    # Baseado na ação retornada, continua o fluxo
    if acao == "leitura_cartas":
        return leitura_cartas_lex(jogo)
    elif acao == "conversar_natasha":
        return dialogo_natasha(jogo)
    elif acao == "explorar_mapa":
        return explorar_mapa(jogo)
    else:
        return dialogo_barman(jogo)

def leitura_cartas_lex(jogo):
    """Natasha lê as cartas através de Lex - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa a leitura e recebe a ação
    lex.leitura_cartas()

    # Sempre volta para explorar o mapa
    return explorar_mapa(jogo)

def dialogo_natasha(jogo):
    """Conversa com Natasha através de Lex - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa a conversa e recebe a ação
    lex.conversar_natasha()

    # Sempre volta para explorar o mapa
    return explorar_mapa(jogo)

def missao_lex(jogo):
    """Missão para ajudar Lex - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa a missão e recebe a ação
    acao = lex.missao_bar()

    # Baseado na ação retornada, continua o fluxo
    if acao == "confronto_clientes":
        return confronto_clientes(jogo)
    elif acao == "conversar_mais":
        return conversar_lex(jogo)
    else:
        return dialogo_barman(jogo)

def confronto_clientes(jogo):
    """Confronto com os clientes chatos - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa o confronto e recebe a ação
    acao = lex.confronto_clientes()

    # Baseado na ação retornada, continua o fluxo
    if acao == "fracasso_missao":
        return fracasso_missao(jogo)
    elif acao == "sucesso_missao":
        return sucesso_missao(jogo)
    elif acao == "missao_meia_sucesso":
        return missao_meia_sucesso(jogo)
    else:
        return confronto_clientes(jogo)

def sucesso_missao(jogo):
    """Sucesso na missão - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa o sucesso da missão
    lex.sucesso_missao()

    # Volta para explorar o mapa
    return explorar_mapa(jogo)

def fracasso_missao(jogo):
    """Fracasso na missão - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa o fracasso da missão
    lex.fracasso_missao()

    # Volta para explorar o mapa
    return explorar_mapa(jogo)

def missao_meia_sucesso(jogo):
    """Meio sucesso na missão - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaLex
    lex = falaLex(nome, opcao_visual)

    # Executa o meio sucesso da missão
    lex.missao_meia_sucesso()

    # Volta para explorar o mapa
    return explorar_mapa(jogo)

def dialogo_natasha_direto(jogo):
    """Diálogo direto com Natasha - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaNatasha
    natasha = falaNatasha(nome, opcao_visual)

    # Executa o encontro e recebe a ação
    acao = natasha.encontro_inicial()

    # Baseado na ação retornada, continua o fluxo
    if acao == "leitura_cartas_completa":
        return leitura_cartas_natasha(jogo)
    elif acao == "falar_futuro":
        return falar_futuro_natasha(jogo)
    elif acao == "segredos_bar":
        return segredos_bar_natasha(jogo)
    elif acao == "conversar_natasha":
        return conversar_natasha_direto(jogo)
    elif acao == "voltar_lex":
        return dialogo_barman(jogo)
    else:
        return dialogo_natasha_direto(jogo)

def leitura_cartas_natasha(jogo):
    """Leitura completa das cartas por Natasha - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaNatasha
    natasha = falaNatasha(nome, opcao_visual)

    # Executa a leitura e recebe a ação
    acao = natasha.leitura_cartas_completa()

    # Baseado na ação retornada, continua o fluxo
    if acao == "conversar_natasha":
        return conversar_natasha_direto(jogo)
    elif acao == "explorar_mapa":
        return explorar_mapa(jogo)
    else:
        return dialogo_natasha_direto(jogo)

def falar_futuro_natasha(jogo):
    """Natasha fala sobre o futuro - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaNatasha
    natasha = falaNatasha(nome, opcao_visual)

    # Executa a conversa e recebe a ação
    natasha.falar_futuro()

    # Volta para o diálogo com Natasha
    return dialogo_natasha_direto(jogo)

def segredos_bar_natasha(jogo):
    """Natasha revela segredos do bar - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaNatasha
    natasha = falaNatasha(nome, opcao_visual)

    # Executa a revelação e recebe a ação
    acao = natasha.segredos_bar()

    # Baseado na ação retornada, continua o fluxo
    if acao == "conversar_natasha":
        return conversar_natasha_direto(jogo)
    else:
        return dialogo_natasha_direto(jogo)

def conversar_natasha_direto(jogo):
    """Continuar conversa direta com Natasha - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaNatasha
    natasha = falaNatasha(nome, opcao_visual)

    # Executa a conversa e recebe a ação
    acao = natasha.conversar_natasha()

    # Baseado na ação retornada, continua o fluxo
    if acao == "historia_natasha":
        return historia_natasha(jogo)
    elif acao == "conselhos_natasha":
        return conselhos_natasha(jogo)
    elif acao == "falar_bar_natasha":
        return falar_bar_natasha(jogo)
    elif acao == "voltar_lex":
        return dialogo_barman(jogo)
    else:
        return conversar_natasha_direto(jogo)

def historia_natasha(jogo):
    """Natasha conta sua história - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaNatasha
    natasha = falaNatasha(nome, opcao_visual)

    # Executa a história
    natasha.historia_natasha()

    # Volta para o diálogo com Natasha
    return dialogo_natasha_direto(jogo)

def conselhos_natasha(jogo):
    """Natasha dá conselhos - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaNatasha
    natasha = falaNatasha(nome, opcao_visual)

    # Executa os conselhos
    natasha.conselhos_natasha()

    # Volta para o diálogo com Natasha
    return dialogo_natasha_direto(jogo)

def falar_bar_natasha(jogo):
    """Natasha fala sobre o bar - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe falaNatasha
    natasha = falaNatasha(nome, opcao_visual)

    # Executa a conversa
    natasha.falar_bar_natasha()

    # Volta para o diálogo com Natasha
    return dialogo_natasha_direto(jogo)

# ==================== PERSONAGENS - LULU ====================

def encontrar_lulu(jogo):
    """Encontra Lulu, ex-namorada - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Lulu
    lulu = falaLulu(nome, opcao_visual)
    
    # Executa o encontro e recebe a ação
    acao = lulu.encontrar_lulu()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "ir_casa":
        return jogo
    elif acao == "sentar_mesa_lulu":
        return sentaramesa_lulu(jogo)
    else:
        return encontrar_lulu(jogo)

def sentaramesa_lulu(jogo):
    """Lulu convida para sentar à mesa - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Lulu
    lulu = falaLulu(nome, opcao_visual)
    
    # Executa a decisão de sentar e recebe a ação
    acao = lulu.sentaramesa_lulu()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "continuar_jogo":
        return jogo
    elif acao == "beber_com_lulu":
        return beber_com_lulu(jogo)
    else:
        return sentaramesa_lulu(jogo)

def beber_com_lulu(jogo):
    """Bebendo com Lulu - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Lulu
    lulu = falaLulu(nome, opcao_visual)
    
    # Executa a decisão de beber e recebe a ação
    acao = lulu.bebercom_lulu()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "continuar_jogo":
        return jogo
    elif acao == "decidir_casa_lulu":
        return decidir_casa_lulu(jogo)
    else:
        return beber_com_lulu(jogo)

def decidir_casa_lulu(jogo):
    """Decidir se leva Lulu para casa - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Lulu
    lulu = falaLulu(nome, opcao_visual)
    
    # Executa a decisão sobre a casa e recebe a ação
    acao = lulu.decidir_casa_lulu()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "continuar_jogo":
        return jogo
    else:
        return decidir_casa_lulu(jogo)

# ==================== PERSONAGENS - ALICE ====================

def encontrar_alice(jogo):
    """Encontra Alice cantando no palco - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Alice
    alice = falaAlice(nome, opcao_visual)
    
    # Executa o encontro e recebe a ação
    acao = alice.encontrar_alice()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "alice_reagir_grito":
        return alice_reagir_grito(jogo)
    elif acao == "alice_deboa":
        return alice_deboa(jogo)
    else:
        return encontrar_alice(jogo)

def alice_reagir_grito(jogo):
    """Alice reage ao grito - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Alice
    alice = falaAlice(nome, opcao_visual)
    
    # Executa a reação ao grito e recebe a ação
    acao = alice.alice_reagir_grito()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "fim_jogo":
        return jogo
    else:
        return alice_reagir_grito(jogo)

def alice_deboa(jogo):
    """Alice de boa - tenta sedução - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Alice
    alice = falaAlice(nome, opcao_visual)
    
    # Executa a interação positiva e recebe a ação
    acao = alice.alice_deboa()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "fim_jogo":
        return jogo
    elif acao == "alice_apresentacao":
        return alice_apresentacao(jogo)
    else:
        return alice_deboa(jogo)

def alice_apresentacao(jogo):
    """Alice se apresenta - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Alice
    alice = falaAlice(nome, opcao_visual)
    
    # Executa a apresentação e recebe a ação
    acao = alice.alice_apresentacao()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "alice_paquera":
        return alice_paquera(jogo)
    else:
        return jogo

def alice_paquera(jogo):
    """Decide se quer paquerar Alice - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Alice
    alice = falaAlice(nome, opcao_visual)
    
    # Executa a decisão de paquera e recebe a ação
    acao = alice.alice_paquera()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "continuar_jogo":
        return jogo
    else:
        # Para o caso de alice_lulu_acontece, a classe já lida com isso internamente
        return alice_paquera(jogo)

def briga_lulu_alice(jogo):
    """Briga entre Lulu e Alice com faca - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Alice
    alice = falaAlice(nome, opcao_visual)
    
    # Executa a briga e recebe a ação
    acao = alice.briga_lulu_alice()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "continuar_jogo":
        return jogo
    else:
        return briga_lulu_alice(jogo)

# ==================== PERSONAGENS - GUILHERME ====================

def dialogo_guilherme(jogo):
    """Encontra Guilherme no banheiro - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Guilherme
    guilherme = falaGuilherme(nome, opcao_visual)
    
    # Executa o diálogo e recebe a ação
    acao = guilherme.dialogo_guilherme()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "ir_casa":
        return jogo
    elif acao == "beber_com_guilherme":
        return beber_com_guilherme(jogo)
    else:
        return dialogo_guilherme(jogo)

def beber_com_guilherme(jogo):
    """Bebendo com Guilherme - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]
    
    # Cria instância da classe Guilherme
    guilherme = falaGuilherme(nome, opcao_visual)
    
    # Executa a decisão de beber e recebe a ação
    acao = guilherme.beber_com_guilherme()
    
    # Baseado na ação retornada, continua o fluxo
    if acao == "fim_jogo":
        return jogo
    elif acao == "explorar_mapa":
        return explorar_mapa(jogo)
    else:
        return beber_com_guilherme(jogo)

# ==================== FINAL DO JOGO ====================

def assalto_na_rua(jogo):
    """Assalto quando vai andando para casa"""
    if jogo["veiculo"] == "andando":
        print(Fore.RESET + '')
        sprint('Você foi andando pra casa, um mendigo te aborda')
        print('')
        sprint('Mendigo: Celular e carteira por favor!!')
        print('')
        assalto = input('-1 reagir na porrada ou\n -2 Dar a carteira: ')
        
        if assalto == '1':
            sprint('ROLAGEM DE DADOS!!!')
            dado4 = random.randrange(1, 6)
            limpar_terminal(jogo["opcao_visual"])
            
            if dado4 <= 3:
                sprint('O mendigo te bate e rouba sua carteira')
            else:
                sprint('Você o bate, liga pra policia e ele vai preso')
            limpar_terminal(jogo["opcao_visual"])
        elif assalto == '2':
            nome = jogo["nome"]
            sprint(f'{nome}: Toma pode ficar')
            print('')
            sprint('Você vai pra casa sem carteira')
            limpar_terminal(jogo["opcao_visual"])
        else:
            sprint('Números apenas!')
            return assalto_na_rua(jogo)
    
    return jogo

def exibir_fim(jogo):
    """Exibe tela final do jogo"""
    print(Fore.RESET + '')
    result = pyfiglet.figlet_format("Fim de jogo!", font="digital") 
    sprint(Fore.RED + result)
    
    print(Fore.RESET + '')
    sprint('------Créditos Finais----')
    sprint('Programação, roteiro e historia por Victor Hugo Oliveira')
    sprint('História e roteiro por Igor Silva azeredo')
    print('')

# ==================== FUNÇÃO PRINCIPAL ====================

def main():
    """Função principal que orquestra todo o fluxo do jogo - CONECTANDO TUDO!"""
    mostrar_titulo()
    
    while True:
        # INICIALIZAÇÃO - Cria jogador e escolhas iniciais
        jogo = criar_jogador()
        exibir_introducao(jogo)
        jogo = escolher_modo_visual(jogo)
        jogo = introducao_historia(jogo)
        
        # DECISÃO PRINCIPAL - Ir ao bar ou não
        jogo = escolher_ir_bar(jogo)
        
        # SE FOI AO BAR - Toda interação acontece aqui
        if jogo["no_bar"]:
            jogo = encontrar_amigo(jogo)  # Encontra Jack
            jogo = assalto_na_rua(jogo)   # Possível assalto voltando
        
        # FIM DO JOGO
        exibir_fim(jogo)
        
        # PERGUNTA PARA JOGAR NOVAMENTE
        encerrar = input(Fore.RED + 'Digite 1 para sair ' + Fore.YELLOW + 'ou aperte enter para jogar novamente: ')
        if encerrar == '1':
            print('')
            sprint(Fore.RESET + 'Tchau!')
            break
        else:
            print('')
            sprint(Fore.RESET + 'Até logo!')
            print('')

if __name__ == "__main__":
    main()