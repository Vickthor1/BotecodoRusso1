"""""""""
Jogo de bar que se chama Bar do Russo, as escolhas serão feitas com opções numéricas de acordo com o avanço do game. 

"""""""""
from Eventos import*
from base import*
import os
import pyfiglet

from colorama import Fore, init

init()

import sys,time,random

#O jogo era feito em whiles mas vou passar para funções
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1./90)

result = pyfiglet.figlet_format("Boteco do Russo", font = "banner3-D" ) 
sprint(result) 

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)
     
andando = False

def Pessoa():
   nome = input("Qual o nome do seu personagem? ")
   return nome

nome = Pessoa()

while True:
   
   sprint(f"""
      Bem vindo ao "Boteco don Russo",\n
      como todo o lugar infelizmente a falha é algo inevitavel, mas aqui nesse game é evitavel\n
       toda a vez que você falhar, você volta ao vai ter que fazer o game todo de novo, tenha cuidado com quem conversa\n
       (as escolhas seram feitas com atalho rápido, nas escolhas sem numeração responda o que quiser. Sistema de dinheiro, barra de bebida e modo de jogo, não inclusos nem nessa demo e nem na de dia 18 de novembro)\n
           """)
   print('')
   sprint(Fore.RED + ' !!!ATENÇÃO JOGO HUMORISTICO, QUALQUER SEMELHANÇA COM ALGO REAL É MERA CONHECIDENCIA!!! ')
   
   #Aqui o usuario decide se quer limpar ou não o texto ao jogar
   sprint(f"O jogo conta com 2 opções de jogo, uma você conta com a função de apagar mensagens com enter\n a outra sem essa função mas o enter continua os dialogos")
   
   def mensagem():
      opcao = input(f"-1 Apagar mensagens com ENTER\n -2 Não apagar mensagens com ENTER\n Escolha: ")
      if opcao == '1':
      
         return opcao
      elif opcao =='2':
         
         return opcao
      
      else:
         mensagem()
      
   opcao = mensagem()
   
   mendigo = False
   
   def limpar_terminal():
      if opcao =='1':
         input("ENTER para continuar")
         os.system("cls")
      elif opcao == '2':
         input("ENTER para continuar")
      
   #Introdução do jogo
   print(Fore.RESET + '')
   print('')
   sprint(f"""Chegou a sexta feira, dia da semana que o filho chora e a mãe não vê,\n
         {nome} quer curtir a sua grande noite com tudo que ela pode oferecer,\n
         você pega seu telefone e da uma olhada nas suas redes sociais até que...\n         
         """)
   sprint('Você vê que tem um bar novo bem popular na sua cidade')

   def veiculo():
         veiculo_que_sera_usado = input('-1 você prefere ir andando ou\n -2 de moto? ')
         if veiculo_que_sera_usado == '1':
            
            andando = True
            print('')
            sprint('você andou bastante até chegar no bar novo')
            print('')
            sprint(Fore.RED + 'INFORMAÇÂO GUARDADA!')
            print(Fore.RESET + '')
            limpar_terminal()
            return andando
         elif veiculo_que_sera_usado == '2':
            moto = True
            print('')
            sprint('você chegou rapidinho no bar novo')
            print('')
            sprint(Fore.RED + 'INFORMAÇÂO GUARDADA!')
            limpar_terminal()
            return moto
         
         else:
            print(Fore.RESET + '')
            sprint('Não compreendi(digite 1 ou 2)')
            veiculo()

   def comeco():
         print('')
         bar = input(f'-1 Você quer ir a esse bar\n -2 não ir e ficar em casa? ')
         if bar == '1':
            print('')
            sprint('Você decide ir ao bar novo')
            print('')
            limpar_terminal()
            veiculo()
         elif bar == '2':
            print('')
            sprint('Você decide ficar na sua casa assistindo séria e comendo pipoca')
            print('')
            limpar_terminal()
            
         else:
            print('')
            sprint('Não entendi(digite 1 ou 2)')
            comeco()

   comeco()
   
   def personagem1_Jack():
      print(Fore.RESET + '')
      sprint(Fore.CYAN + f'{nome}: Fala ai Jack! ')
      print('')
      sprint(Fore.BLUE + 'Jack: Eae, veio aproveitar a sexta?')
      print('')
      sprint(Fore.CYAN + f'{nome}: Sim, essa semana foi tortura')
      print('')
      sprint(Fore.BLUE + 'Jack: Vou ficar aqui com você na mesa vlw? e me paga uma cerveja ai')
      print('')
      sprint(Fore.CYAN + f'{nome}: Mas Jack sou eu que to em pé')
      print('')
      sprint(Fore.RESET + 'Vocês começam a rir da situação')
      print('')
      sprint(Fore.BLUE + 'Jack: Mas ai namoral, paga uma breja ai?')
      print('')
      decisam = input(Fore.RESET + '-1 Deixar Jack sózinho e explorar o mapa ou\n -2 bater um papo com Jack')
      
      if decisam == '1':
         print('')
         sprint(Fore.RESET + 'Jack, vou ter que vazar, vai dar não')
         print('')
         mapa()
         limpar_terminal()
         
      elif decisam == '2':
         print('')
         sprint(Fore.CYAN + f'{nome}: Ta bom mano, desce uma cerveja pra esse maluco aqui!')
         print('')
         sprint(Fore.RESET + 'Você olha pro banheiro feminino e tem uma leve impressam de ter visto um rosto conhecido indo pra dentro do banheiro')
         print('')
         sprint(Fore.BLUE + f'Jack: O que é que foi hein {nome}, ta de olho em alguma gatinha? ')
         print('')
         pergunta()
         limpar_terminal()
         
      else:
         print(Fore.RESET + '')
         sprint('Números por favor!')
      
   def amigo():
      print('')
      sprint(Fore.RESET + 'Você vê que tem um amigo seu lá')
      print('')
      primeira_fala = input(f'-1 Vai cumprimenta-lo\n -2 não? ')
      if primeira_fala == '1':
         print('')
         sprint('Você decide falar com ele')
         print('')
         limpar_terminal() 
         
                  
      elif primeira_fala == '2':
         print('')
         sprint('Você ignora o Jack e logo vai falar com o barman')
         limpar_terminal() 
         barman()
         
      else:
         print('')
         print('Não compreendi(digite 1 ou 2)')
         amigo()
   
   def barman():
      print(Fore.RESET + '')
      sprint(Fore.CYAN + f'{nome}: Olá boa noite, poderia me servir uma bebida?')
      print('')
      sprint(Fore.LIGHTBLACK_EX + 'Barman: Por que toda essa formalidade amigão, pode ficar à vontade')
      print('')
      sprint(Fore.LIGHTBLACK_EX + 'Barman: Temos, vodka, cachaça, whisky, vinho, skol, heineken, brahma, Itaipava...')
      print('')
      sprint(Fore.RESET + 'Você acaba não prestando muita atenção nas outras coisas que ele diz')
      print('')
      bebida = input(Fore.CYAN + f'{nome}: Eu gostaria de pedir ')
      print('')
      sprint(Fore.RESET + 'Você bate um papo com o Barman e ele te conta a História do Bar e que ele e a filha dele reabriram o bar no Brasil, pelo fato do país deles estarem em guerra e eles não apoiarem isso')
      print('')
      sprint(Fore.LIGHTBLACK_EX + 'Barman: Você é um bom ouvinte meu jovem, meu nome é Alexandre mas pode e chamar de Lex')
      print('')
      sprint(Fore.CYAN + f'{nome}: meu nome é {nome}, prazer em conhecer o senhor')
      print('')
      explorar = input(Fore.RESET + 'Você quer -1 explorar o mapa ou\n -2 quer ir para sua casa? ')
      if explorar == '1':
         mapa()
         limpar_terminal()
         
      elif explorar =='2':
         limpar_terminal()
         
      else:
         sprint(Fore.LIGHTRED_EX + 'Só números')
         barman()
   #fim do dialogo com o barman

   
   def pergunta():
      print(Fore.RESET + '')
      pandora = input('Chegou a hora, qual decisão será feita, você vai falar que -1 sim, vai dizer que\n -2 não ou (3)Ser grosso')
      print('')
      if pandora =='1':
         personagem1_JackSim()
         limpar_terminal()
         
      elif pandora == '2':
         personagem1_JackNao()
         limpar_terminal()
         
      elif pandora == '3':
         personagem1_Jackbravo()
         limpar_terminal()
         
      else:
         print('')
         sprint(Fore.RESET + 'Números por favor!')
         pergunta()
         

   def personagem1_JackNao():
      print('')
      sprint(Fore.CYAN + f'{nome}: Não')
      print('')
      sprint(Fore.RESET + 'Jack não acredita muito em você mas deixa quieto')
      print('')
      limpar_terminal()
      

   def personagem1_JackSim():
      sprint(Fore.CYAN + f'{nome}: Sim')
      print('')
      sprint(Fore.RESET + 'Jack da um sorrisinho malicioso')
      print('')
      sprint(Fore.RESET + 'Jack, louco do jeito que é, zoa falando pra você entrar no banheiro feminino quando ninguém estiver olhando')
      print('')
      resp = input(Fore.RESET + 'O que você vai decidir -1 Dar uma de maluco e entrar\n -2 Não fazer essa maluquice? ')
      if resp == '1':
         print('')
         sprint(Fore.CYAN + f'{nome}: Boa idéia')
         print('')
         sprint(Fore.RESET + 'Você entra no banheiro feminino e avista sua ex e ela liga pra policia')
         print('')
         sprint(Fore.CYAN + f'{nome}: Desculpa, errei fui muleque')
         print('')
         sprint(Fore.RESET + 'Você foi preso')
         limpar_terminal()
         
      
      elif resp == '2':
         print('')
         sprint(Fore.CYAN + f'{nome}Vai se lascar, duente')
         print('')
         sprint(Fore.RESET + 'Jack acha engraçado')
         print('')
         sprint(Fore.RESET + 'você vai pra perto do banheiro feminino e vê sua...')
         sprint(Fore.RESET + 'Você chegou ao limite da demo, para saber o desfecho dessa história apareça no dia 18 de novembro')
         limpar_terminal()
         
      
      else:
         print('')
         sprint(Fore.RESET + 'Não tem essa opção')
         print('')
         

   def personagem1_Jackbravo():
      sprint(Fore.CYAN + f'{nome}:E o quico?')
      print('')
      sprint(Fore.BLUE + 'Jack: É O QUE MENOR!? ')
      print('')
      sprint(Fore.RESET + 'Jack fica com muita raiva e bate na mesa')
      print('')
      sprint(Fore.RESET + 'Todo mundo do bar vira a atenção para vocês')
      print('')
      personagem1_Jackbravo1()
      limpar_terminal()
      

   def personagem1_Jackbravo1():
      resposta = input(sprint(Fore.RESET + 'O que você ira fazer? -1 Pedir desculpas e acalmar Jack\n -2 Descer a porrada no Jack ou (3)Deixar ele falando sozinho'))
      
      if resposta == '1':
         print('')
         sprint(Fore.CYAN + f'{nome}: Desculpa errei, fui muleke')
         Desculpas()
         limpar_terminal()
         
      
      elif resposta == '2':
         print('')
         sprint(Fore.CYAN + f'{nome}: Cala a boca maluco!!')
         print('')
         sprint(Fore.RESET + 'role os dados para ver se você tem sorte')
         limpar_terminal()
         Porrada()
         
      
      elif resposta == '3':
         limpar_terminal()
         Deixar_ele_sozinho()
         
      
      else:
         print('')
         sprint(Fore.BLUE + 'Jack: repete paspalho!!')
         

   def Desculpas():
      print('')
      sprint(Fore.RESET + 'Jack não acredita muito em você, mas deixa quieto a situação')
      limpar_terminal()
      

   def Porrada():
      dado = random.randrange(1,6)
      if dado < 3:
         print('')
         sprint(Fore.LIGHTRED_EX + '+3 Você da tanta porrada na cara do Jack que ele chora')
         print('')
         sprint(Fore.RESET + 'Vocês são expulsos do bar e tem uma divida de 2 mil reais por danos')
         limpar_terminal()
         

      else:
         print('')
         sprint(Fore.LIGHTRED_EX + '-3 Você toma um Jab de esquerda e é nocauteado')
         print('')
         sprint(Fore.RESET + 'Vocês são expulsos do bar e tem uma divida de 2 mil reais por danos')
         limpar_terminal()
         
         
   def Deixar_ele_sozinho():
      print('')
      sprint(Fore.RESET + 'Você deixa Jack sózinho')
      print('')
      sprint(Fore.RED + 'INFORMAÇÃO GUARDADA!!')
      mapa()
      limpar_terminal()
      

   def mapa():
      print(Fore.RESET + '')
      sprint(f'-1 Ir para perto do banheiro Feminino ver se há alguma conhecida\n -2 ir ao banheiro masculino ou (3)ir até o salão principal')
      respos = input('')
      if respos == '1':
         print('')
         Lulu()
         limpar_terminal()
         
      elif respos == '2':
         print('')
         sprint('Você vai até o banheiro masculino')
         Guilherme = True
         limpar_terminal()
         
      elif respos == '3':
         print('')
         sprint('Você vai ao salão principal')
         sprint('Você vê uma jovem cantando no palco e resolve se aproximar, você fica encantado com a voz dela ')
         print('')
         Alice = True
         limpar_terminal()
         
      
      else:
         print('')
         sprint('Só tem esses lugares')
         mapa()
         
   
   def Lulu():
      Lulu_dialogo = input('Você encontra sua ex namorada na frente do banheiro feminino, opção -1 falar com ela só por educação\n -2 ir embora')

      if Lulu_dialogo == '2':
         print('')
         sprint('Você vai pra casa') 
         limpar_terminal()
         

      elif Lulu_dialogo == '1':
         print('')
         sprint('Vocês conversam e ela pergunta se você não quer se sentar à mesa com ela') 
         print('')
         sentarnamesa()
         limpar_terminal()
         

   def sentarnamesa():
      senta = input('-1  Não, eu tô de boa, ir embora ou\n -2 Sim, o que poderia dar errado? ')

      if senta ==  '1':
         print('')
         sprint('Lulu fica meio cabisbaixa, mas deixa você ir embora')
         print('')
         limpar_terminal()
         
      elif senta == '2': 
         print('')
         sprint('Nada demais, afinal você já sabe lidar com ela')
         print('')
         sprint('Vocês se sentam à mesa e ela pede uma bebida')
         print('')
         bebercomLulu()
         limpar_terminal()
         
      
   def bebercomLulu():
      bebidinha = input(Fore.MAGENTA + f'Lulu: Quer uma bebida também {nome}?\n -1 Sim\n -2 Não ')

      if bebidinha == '1':
         print(Fore.RESET + '')
         sprint('Sim, quero me divertir')
         print('')
         sprint('Lulu vai ao banheiro')
         print('')
         sprint(' O garçom anota os pedidos, mas quem leva o pedido até vocês é uma garçonete, que tenta falar com você')
         print('')
         sprint(Fore.LIGHTGREEN_EX + 'Garçonete: Notei que você está sozinho, desculpe incomodar mas vai fazer algo mais tarde?') 
         print('')
         sprint(Fore.RESET + 'Antes mesmo de você responder algo…') 
         print('')
         sprint(Fore.MAGENTA + 'Lulu: QUEM VOCÊ PENSA QUE É, SUA MOCRÉIA ENSEBADA!') 
         print('')
         sprint(Fore.LIGHTGREEN_EX + 'Garçonete: Calma moça você está se alterando')
         print('')
         sprint(Fore.RESET + 'Elas começam a discutir e você acalma a Lulu, e se desculpa com a garçonete') 
         print('')
         sprint('Lulu fica bolada com você, por você dar razão a garçonete, e joga a bebida na sua cara!') 
         print('')
         sprint('A garçonete trás uma toalhinha para você se enxugar e a Lulu vê e fica fazendo birra  e vc vai embora')
         limpar_terminal()
         


      elif bebidinha == '2':
         print('')
         sprint('Não, não to muito afim de beber')
         print('')
         sprint('Lulu começa a virar todas')
         print('')
         sprint(f'{nome}: Hei! Vai com calma')
         print('')
         sprint(Fore.MAGENTA + 'Lulu: Eu zeiuqui eu to fazen…')
         print(Fore.RESET + '')
         sprint('Lulu da uma soluçada, Você vê que Lulu, não está em condições de ir pra casa, pois bebeu muito')
         print('')
         casacomLulu()
         limpar_terminal()
         
      
   def casacomLulu():
      casa = input(f'-1 Levar Lulu para a casa dela\n -2 Convidar Lulu para sua casa? ')

      if casa == '1':
         print('')
         sprint('Após levar Lulu a casa dela, você vê que está tarde, e resolve ir pra sua casa ')
         print('')
         limpar_terminal()
         

      elif casa == '2':
         print('')
         sprint('Você deixa Lulu sóbria') 
         print('')
         sprint('Você e Lulu relembram os velhos tempos, "vendo netflix" na sua casa')
         print('')
         limpar_terminal()
         

      
   def Alice():
      respalice = input('-1  Você_Grita!! ou\n -2  ficar de boa e admirando')
      if respalice == '1':
         sprint('A cantora acha estranho a situação, para de cantar e chama os seguranças')
         print('')
         sprint('Você rapidamente percebe a situação e tenta mentir')
         grita()
         limpar_terminal()
         
      
      elif respalice == '2':
         sprint('Você fica de boa e admira, você quer tentar chamar a atenção dela de algum modo')
         print('')
         deboa()
         limpar_terminal()
         
      
      else:
         print('')
         sprint(Fore.RESET + 'Não tem essa opção')
         print('')
         
   
   def grita():
      print('')
      escolha = input('-1  você fala que e fiscal e estava testando a segurança,\n -2 Você se faz de doido para sair da situação (3) Você diz que é de um show musical e quer falar com a cantora')
      if escolha == '1':
         sprint('Seguranças:Cadê o seu cracha de fiscal?!')
         sprint('Os seguranças te tampam na porrada e te botam para fora do bar')
         limpar_terminal()
         
      
      elif escolha == '2':
         sprint('O segurança liga prara os médicos psiquiatras(manicômio)!')
         print('')
         limpar_terminal()
         
      
      elif escolha == '3':
         sprint('Seguranças:Cadê o seu cracha de fiscal?!')
         sprint('Os seguranças te tampam na porrada e te botam para fora do bar')
         print('')
         limpar_terminal()
         
      
      else:
         print('')
         sprint(Fore.RESET + 'Não tem essa opção')
         print('')
         grita()
         
   
   dado1 = random.randrange(1,6)
   
   def deboa():
      respa = input('-1 Você quer tentar duetar com ela ou\n -2 quer tentar uma troca de olhares?')
      if respa == '1':
         sprint(Fore.LIGHTRED_EX + 'rolagem de dados!!')
         if dado1 <= 3:
            print(Fore.RESET + '')
            sprint(' você canta tão desafinado que ela começa a Rir')
            print('')
            sprint(' A cantora começa a perder o ar de tanto rir e começa a passar mal')
            print('')
            sprint('Os segura acabam vendo a cantora passando mal e ligam para a ambulância')
            print('')
            sprint('Todo mundo fica te olhando e Jack fica bolado com você e te explana para o Barman')
            print('')
            sprint(' Você e expulso do bar e vai ter que pagar o médico da cantora')
            limpar_terminal()
            
         elif dado1 > 3:
            print(Fore.RESET + '')
            sprint('Você canta tão bem que ela se impressiona e te chama para o palco e te entrega um microfone')
            print('')
            sprint('após o termino do show ela vai até você')
            apresentaalice()
            limpar_terminal()
            
         else:
            print('')
            sprint(Fore.RESET + 'Não tem essa opção')
            print('')
            deboa()
            
      elif respa == '2':
         print('')
         sprint('Vocês tem uma intensa troca de olhares')
         print('')
         sprint('Vocês trocam olhares e ela da um sorrisinho de leve para você')
         print('')
         sprint('após o termino do show ela vai até você')
         apresentaalice()
         limpar_terminal()
         
   
   def apresentaalice():
      sprint('Vocês se sentam a mesa e começam a conversar,você conta algumas piadas a ela')
      print('')
      sprint('Vocês conversam bastante, até que ela se apresenta...')
      print('')
      sprint(Fore.YELLOW + 'Alice: Você é muito engraçado alias,meu nome é Alice qual eo seu ?')
      print('')
      sprint(Fore.CYAN + f'{nome}: Meu nome é {nome} adorei você cantando no palco')
      print('')
      sprint(Fore.RESET + 'Você descobre que o dono do bar é o pai da Alice, e que ela ajuda o pai dela a gerar renda extra pro bar cantando')
      print('')
      apresentaalice1 = True
      limpar_terminal()
      
   
   def apresentaalice1():
      sprint('Você vê que vocês dois ja tem uma certa intimidade e o clima ficou bem sereno')
      print('')
      paquera = input('-1 Você quer tentar paquerar a Alice\n -2 Deixar na amizade')
      
      if paquera == '1':
         sprint('Rolagem de dados!!!')
         lulumaluca()
         limpar_terminal()
         
      elif paquera == '2':
         sprint('vocês ficam conversando e bebendo, depois disso você deixa ela em casa e segue seu caminho pra sua')
         limpar_terminal()
         
   dado2 = random.randrange(1,6)
   
   def lulumaluca():
      
      if 3> dado2:
         sprint('Alice fica envergonhada e diz pra você ir com mais calma')
         print('')
         sprint('Lulu a sua ex está de olho no que você estava fazendo')
         print('')
         sprint(Fore.MAGENTA + 'Lulu: Conseguiu arrumar uma mocréia é, seu paspalho!')
         print('')
         sprint(Fore.RESET + 'Lulu tenta acabar com qualquer chance de amizade ou relacionamento de vocês')
         print('')
         sprint(Fore.CYAN + f'{nome}: Para de ser infantiu, eu e você ja era, não vê que está estragando a minha conversa com a  Alice')
         print('')
         sprint(Fore.MAGENTA + 'Lulu: Você sabe bem que nenhuma outra mulher e melhor que euzinha aqui')
         print('')
         sprint(Fore.YELLOW + 'Alice te defende: Não se acha não ele é um cara bacana e merece mais do que uma maluca empacando as conversas dele')
         print('')
         sprint(Fore.RESET + 'Lulu tenta e puxar o cabelo de Alice e Alice da um murro na cara dela elas começam a discutir e brigar')
         print('')
         sprint('Os seguranças aparecem e separam as duas')
         print('')
         sprint(Fore.MAGENTA + 'Lulu: Eu vou te pegar, eu sei onde você mora sua baranga!')
         print('')
         sprint(Fore.CYAN + f'{nome}: Alice me desculpa pela situação eu não queria que...')
         print('')
         sprint(Fore.YELLOW + 'Alice te enterrompe: Nossa, parece que eu vou ter que dormir fora hoje né')
         print('')
         sprint(Fore.RESET + 'Você leva Alice pra sua casa e depois de um tempo vocês se conhecem cada vez mais até que acabam morando juntos')
         print(Fore.RESET +'')
         andando = False
         limpar_terminal()
         return andando
         
      elif 3< dado2:
         sprint('ignorar e acha que foi só impressão sua')
         print('')
         sprint( 'Você sente uma energia meio ruim ali no ambiente, quando você ia avisar a Alice…')
         print('')
         sprint(' A sua ex namorada Lulu aparece e puxa o cabelo de Alice e elas começam a  discutir e brigar')
         print('')
         sprint('Lulu pega uma faca na mesa e ameaça vocês dois, o que você vai fazer? ')
         print('')
         briga()
         limpar_terminal()
         
   
   def briga():
      ameaça = input(f'-1 Tentar reagir a tempo\n -2 Puxar a Alice pela mão para sair dali\n  -3 Tentar chamar a atenção dos seguranças')
 
      if ameaça == '1':
            situacao1()
            limpar_terminal()
            
      
      elif ameaça == '2':
            print('')
            sprint('Você puxa Alice para fora do bar e fala para ela subir na sua moto')
            print('')
            sprint('Vocês dão uma longa volta pela cidade e param em um restaurante')
            print('')
            sprint('Você conta para Alice sobre a Lulu e pede desculpas a ela, Alice fica tocada com a situação')
            print('')
            sprint('Para compensar ela, você leva ela para a casa dela e ela te dá um beijo e se despede de você agradecendo pela noite única e maluca')
            print('')
            andando = False
            limpar_terminal()
            return andando
         
      elif ameaça == '3':
            print('')
            sprint('Os seguranças a levam')
            print('')
            sprint('Alice diz que depois vocês vão rir da situação mas quer distância de você')
            print('')
            andando = False
            limpar_terminal()
            return andando
                  
   dado3 = random.randrange(1,6)
   
   def situacao1():
         if dado3 <= 3:
            print('')
            sprint('Você consegue desarmar Lulu a tempo mas ela começa a gritar o que vai fazer?')
            alicedialogoo()
            limpar_terminal()
            
         else:
            print('')
            sprint('Você não consegue reagir a tempo e ela consegue ferir a Alice') 
            print('')
            sprint('Os seguranças veem a situação ligam para uma ambulância')
            print('')
            sprint('Você vai para o hospital com ela e passa a noite lá')
            print('')
            sprint('Alice diz que depois eles vão rir da situação mas quer distância de você')
            andando = False
            limpar_terminal()
            return andando
            
   
   def alicedialogoo():
         print('')
         lulumaniaca = input('-1 tentar acalmar Lulu,\n -2 Deixar ela gritar enquanto os seguranças estão vindo?')
         
         if lulumaniaca == '1':
            print('')
            sprint('Lulu começa a ir até você chorando, Lulu dá umas pancadas no seu peito te xingando')
            print('')
            sprint('Tudo se resolve de forma pacífica, você ainda apresenta ela a Alice, que fica muito receosa')
            print('')
            sprint(' Sua noite foi toda tomando conta de Lulu, pra não acontecer nenhum acidente, e sim, você volta com a sua ex')
            print('')
            andando = False
            limpar_terminal()
            return andando
            
            
         elif lulumaniaca == '2':
           print('')
           sprint('Os seguranças a levam')
           print('')
           sprint('Alice diz que depois vocês vão rir da situação mas quer distância de você')
           print('')
           andando = False
           limpar_terminal()
           return andando
   
   def Guilherme():
      print(Fore.RESET + '')
      sprint('Chegando lá você ouve uma voz dizendo: To sentindo cheiro de coelinho rosa')
      print('')
      grandam = input('O que você irá fazer??!! -1 Fugir\n -2 ficar e encarar (3)fingir que não ouviu')
      if grandam == '1':
         print('')
         sprint('Você corre pra caramba e vai pra casa')
         limpar_terminal()
         
      
      elif grandam == '2':
         sprint(Fore.LIGHTMAGENTA_EX + 'Desconhecido: Senti sua falta nos treinos')
         print('')
         sprint(Fore.CYAN + f'{nome}: Espera ai, Guilherme?')
         print('')
         sprint(Fore.LIGHTMAGENTA_EX + 'Guilherme: Quer fazer um agachamante não? ')
         print('')
         sprint(Fore.CYAN + f'{nome}: Você bebeu vodka ou agua de coco?')
         print('')
         sprint(Fore.LIGHTMAGENTA_EX + 'Guilherme: Pra mim tanto faz')
         print('')
         sprint(Fore.LIGHTMAGENTA_EX + 'Guilherme: Quer beber comigo? ')
         print(Fore.RESET + '')
         beber()
         andando = False
         limpar_terminal()
         
      
      elif grandam == '3':
         sprint(Fore.RESET + 'Você sente uma mão no seu ombro')
         sprint('você vira pra trás e é Guilherme seu amigo da academia ')
         print('')
         sprint(Fore.CYAN + f'{nome}: Qual é Guilherme ta de vacilação')
         print('')
         sprint(Fore.LIGHTMAGENTA_EX + 'Guilherme: Ta faltando bastante nos treinos hein ')
         print('')
         sprint(Fore.CYAN + f'{nome}: Cara to sem foco na academia')
         print('')
         sprint(Fore.LIGHTMAGENTA_EX + 'Guilherme te faz um discurso motivacional para você se animar pra ir a academia e depois despenca no chão')
         print('')
         sprint(Fore.RESET + 'Você chama uma hambulancia pra ele, depois disso você vê que está tarde e volta pra sua casa')
         andando = False
         limpar_terminal()
         
      
      else:
         print('')
         sprint(Fore.RESET + 'Números por favor!')
         Guilherme()

   def beber():
      beberres = input(Fore.RESET + '-1 Você vai beber com Ghilherme ou\n -2 Vai tentar deixa-lo sóbrio')
      
      if beberres == '1':
         print('')
         print(Fore.RESET + '')
         sprint('Vocês beberam a noite toda e esqueceram do resto, você acordano dia seguinte na cama do guilherme sem sentir suas pernas direito, você olha o grupo da empresa e jack vazou seus videos com o guilherme no bar')
         andando = False
         limpar_terminal()
         return andando
      
      elif beberres == '2':
            print('')
            sprint('Você vai trocando a vodka dele por água e deixand ele sóbrio, após isso deixa ele na casa dele')
            limpar_terminal()
            
      
      else:
         print('')
         sprint('Números apenas!')
         beber()
         
   
   while andando:
      print(Fore.RESET + '')
      sprint('Você foi andando pra casa, durante o caminho um mendingo te aborda com um pedaç de pau na mão')
      print('')
      sprint('Mendigo: Celular e carteira por favor!!')
      print('')
      assalto = input('-1 reagir e tampar ele na porrada,\n -2 Dar a carteira pra ele? ')
      if assalto == '1':
         sprint('ROLAGEM DE DADOS!!!')
         dado4 = random.randrange(1,6)
         mendigo = True
         limpar_terminal()
         break
         
      elif assalto == '2':
         sprint(f'{nome}: Toma pode ficar')
         print('')
         sprint('Você vai pra casa sem a carteira')
         print('')
         limpar_terminal()
         break
         
      else:
         print('')
         sprint('Números apenas!')
         pass
   
   while mendigo:
      if dado4 <= 3:
         sprint('O mendigo da uma paulada na sua cabeça, rouba sua carteira e vai embora')
         print('')
         limpar_terminal()
         
      else:
         sprint('Você da uma voadora no mendingo, tampa ele na porrada, liga pra policia e ele vai preso (por favor não reaja a assaltos, tenha amor a sua vida e familia)')
         print('')
         limpar_terminal()
         
 
   def moto():
      print('')
      sprint(Fore.RED + 'SE BEBER NÃO DIRIJA!!!!')
      print(Fore.RESET + '')
      limpar_terminal()
      
   
   result = pyfiglet.figlet_format("Fim de jogo! Obrigado Por jogar!", font = "digital" ) 
   sprint(Fore.RED + result)
   
   print(Fore.RESET + '')
   sprint('------Créditos Finais----')
   sprint('Programação, roteiro e historia por Victor Hugo Oliveira')
   sprint('História e roteiro por Igor Silva azeredo')
   print('')
   Encerrarmento = True
   
   encerrar = sprint(Fore.RED + 'Digite 1 para sair ') 
   encerrar = input(Fore.YELLOW + 'ou aperte enter para jogar novamente ')
   if encerrar == '':
      print('')
      sprint(Fore.RESET + 'Até logo!')
      print('')
      pass
   else:
      print('')
      sprint(Fore.RESET + 'Tchau!')
      limpar_terminal()
      
