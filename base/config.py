from Boteco_do_Russo_DEMO import*

class Configuracao:
    def __init__(self):
        
    
        def sprint(str):
            for c in str + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./90)

            result = pyfiglet.figlet_format("Boteco do Russo", font = "banner3-D" ) 
            return sprint(result)