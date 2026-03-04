from colorama import Fore, init
import sys, time, random

init()

def sprint(texto):
    """Função para imprimir texto com efeito de digitação"""
    for c in texto + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

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
            sprint(Fore.LIGHTBLACK_EX + 'Lex: Se você resolver isso, te dou o drink especial de graça!')
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

        escolha = input(Fore.RESET + '-1 Compartilhar sua própria história\n -2 Dar apoio\n -3 Mudar de assunto: ')

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