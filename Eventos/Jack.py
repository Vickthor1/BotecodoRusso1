from colorama import Fore, init

init()
import sys,time

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)
     
from Boteco_do_Russo_DEMO import*

def __init__(self):
    self.nome = pessoa.nome

class falaJack:
    
    def personagem1_Jack(self):
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
      
      decisam = input(Fore.RESET + '-1 Deixar Jack sózinho e explorar o mapa ou\n -2 bater um papo com Jack')
      if decisam == '1':
         print('')
         sprint(Fore.RESET + 'Jack, vou ter que vazar, vai dar não')
         print('')
         mapa()
         limpar_terminal()
         
      elif decisam == '2':
         print('')
         sprint(Fore.CYAN + f'{self.nome}: Ta bom mano, desce uma cerveja pra esse maluco aqui!')
         print('')
         sprint(Fore.RESET + 'Você olha pro banheiro feminino e tem uma leve impressam de ter visto um rosto conhecido indo pra dentro do banheiro')
         print('')
         sprint(Fore.BLUE + f'Jack: O que é que foi hein {self.nome}, ta de olho em alguma gatinha? ')
         print('')
         pergunta()
         limpar_terminal()
         
      else:
         print(Fore.RESET + '')
         sprint('Números por favor!') 
