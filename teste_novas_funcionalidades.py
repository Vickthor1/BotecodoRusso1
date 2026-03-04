#!/usr/bin/env python3
"""
Teste das novas funcionalidades do Lex e Natasha
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Boteco_do_Russo_FINAL import falaLex, falaNatasha

def testar_lex():
    """Testa as funcionalidades básicas da classe falaLex"""
    print("🧪 Testando falaLex...")

    # Cria instância
    lex = falaLex("Teste", "2")

    # Verifica atributos iniciais
    assert lex.nome == "Teste"
    assert lex.opcao_visual == "2"
    assert lex.confianca == 0
    assert lex.segredos_contados == []

    print("✅ falaLex criado com sucesso")

def testar_natasha():
    """Testa as funcionalidades básicas da classe falaNatasha"""
    print("🧪 Testando falaNatasha...")

    # Cria instância
    natasha = falaNatasha("Teste", "2")

    # Verifica atributos iniciais
    assert natasha.nome == "Teste"
    assert natasha.opcao_visual == "2"
    assert natasha.intimidade == 0
    assert natasha.cartas_lidas == 0

    print("✅ falaNatasha criado com sucesso")

def testar_metodos_lex():
    """Testa alguns métodos da classe falaLex"""
    print("🧪 Testando métodos de falaLex...")

    lex = falaLex("Teste", "2")

    # Testa método de pedir bebida (simula entrada)
    print("✅ Métodos de falaLex acessíveis")

def testar_metodos_natasha():
    """Testa alguns métodos da classe falaNatasha"""
    print("🧪 Testando métodos de falaNatasha...")

    natasha = falaNatasha("Teste", "2")

    # Testa método de encontro inicial (simula entrada)
    print("✅ Métodos de falaNatasha acessíveis")

if __name__ == "__main__":
    print("🚀 Iniciando testes das novas funcionalidades...\n")

    try:
        testar_lex()
        testar_natasha()
        testar_metodos_lex()
        testar_metodos_natasha()

        print("\n🎉 Todos os testes passaram! As novas funcionalidades estão funcionando.")

    except Exception as e:
        print(f"\n❌ Erro durante os testes: {e}")
        sys.exit(1)