"""""""""
Jogo de bar que se chama Bar do Russo - VERSÃO REFATORADA
Todas as funções conectadas de forma clara e organizada
"""""""""

from Eventos import *
from base import *
import os
import pyfiglet
from colorama import Fore, init
from Eventos.barman import falabarman  # Importa a classe do barman
from Eventos.Jack import falaJack      # Importa a classe do Jack
from Eventos.Lulu import falaLulu      # Importa a classe da Lulu
from Eventos.Alice import falaAlice    # Importa a classe da Alice
from Eventos.Guilherme import falaGuilherme  # Importa a classe do Guilherme
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

def jack_bravo_opcoes(jogo):
    """Opções após Jack ficar bravo"""
    nome = jogo["nome"]
    
    resposta = input(Fore.RESET + 'O que você ira fazer? -1 Pedir desculpas\n -2 Descer a porrada ou (3) Deixar falando: ')
    
    if resposta == '1':
        print('')
        sprint(Fore.CYAN + f'{nome}: Desculpa errei, fui muleke')
        print('')
        sprint(Fore.RESET + 'Jack não acredita muito, mas deixa quieto a situação')
        limpar_terminal(jogo["opcao_visual"])
        return jogo
    elif resposta == '2':
        print('')
        sprint(Fore.CYAN + f'{nome}: Cala a boca maluco!!')
        print('')
        sprint(Fore.RESET + 'role os dados para ver se você tem sorte')
        limpar_terminal(jogo["opcao_visual"])
        return jack_porrada(jogo)
    elif resposta == '3':
        limpar_terminal(jogo["opcao_visual"])
        print('')
        sprint(Fore.RESET + 'Você deixa Jack sózinho')
        print('')
        sprint(Fore.RED + 'INFORMAÇÃO GUARDADA!!')
        return explorar_mapa(jogo)
    else:
        sprint(Fore.BLUE + 'Jack: repete paspalho!!')
        return jack_bravo_opcoes(jogo)

def jack_porrada(jogo):
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
    
    limpar_terminal(jogo["opcao_visual"])
    return jogo

def dialogo_barman(jogo):
    """Diálogo com Lex, o barman - USANDO A CLASSE SEPARADA"""
    nome = jogo["nome"]
    opcao_visual = jogo["opcao_visual"]

    # Cria instância da classe barman
    lex = falabarman(nome, opcao_visual)

    # Executa o diálogo e recebe a ação
    acao = lex.dialogo_barman()

    # Baseado na ação retornada, continua o fluxo
    if acao == "explorar_mapa":
        return explorar_mapa(jogo)
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
