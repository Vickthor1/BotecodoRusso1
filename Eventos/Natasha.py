from colorama import Fore, init
import sys, time, random

init()

def sprint(texto):
    """Função para imprimir texto com efeito de digitação"""
    for c in texto + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

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
        sprint(Fore.MAGENTA + 'Natasha: Bem-vindo aos meus aposentos secretos.')
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
            sprint(Fore.MAGENTA + 'Natasha: Volte quando estiver pronto para conhecer a verdade.')
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