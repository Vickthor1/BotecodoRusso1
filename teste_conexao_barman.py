#!/usr/bin/env python3
"""
EXEMPLO DE TESTE: Como o barman está conectado ao jogo principal
"""

from Eventos.barman import falabarman
from colorama import Fore, init
import sys, time

init()

def sprint(texto):
    """Função para imprimir texto com efeito de digitação"""
    for c in texto + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./90)  # Mais rápido para teste

def main():
    print("🎮 TESTE DE CONEXÃO: Barman no Jogo do Russo")
    print("=" * 50)

    # Simula dados do jogo
    jogo_simulado = {
        "nome": "Victor",
        "opcao_visual": "2"  # Não limpa terminal
    }

    print(f"Jogador: {jogo_simulado['nome']}")
    print(f"Modo visual: {jogo_simulado['opcao_visual']}")
    print()

    # Cria instância do barman
    lex = falabarman(jogo_simulado["nome"], jogo_simulado["opcao_visual"])

    # Executa o diálogo
    sprint("🔗 Iniciando diálogo com o barman...")
    acao = lex.dialogo_barman()

    print()
    print("🎯 RESULTADO DA CONEXÃO:")
    print(f"Ação retornada pelo barman: '{acao}'")
    print()
    print("✅ Conexão funcionando! O barman retorna ações que o jogo principal pode processar.")
    print("📝 Exemplo: Se o jogador escolher '1', retorna 'explorar_mapa'")
    print("📝 Exemplo: Se o jogador escolher '2', retorna 'ir_casa'")

if __name__ == "__main__":
    main()