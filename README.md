# Boteco do Russo - Versão Final Unificada

## 📋 Descrição
Esta é a versão final unificada do jogo "Boteco do Russo", que combina o código original com as melhorias da refatoração modular. Todo o jogo está contido em um único arquivo Python, facilitando a distribuição e execução.

## 🎮 Sobre o Jogo
"Boteco do Russo" é um jogo de aventura textual humorístico ambientado em um bar. O jogador toma decisões que afetam o desenrolar da história, encontrando diversos personagens e enfrentando situações inesperadas.

### Personagens Principais:
- **Lex (Barman)**: O dono do bar, sempre pronto para uma conversa. Agora com interações expandidas incluindo missões, segredos e apresentação de familiares
- **Natasha**: Irmã misteriosa de Lex, vidente especializada em leitura de cartas do tarô e guardiã dos segredos do bar
- **Jack**: Amigo do jogador, sempre causando confusão
- **Lulu**: Ex-namorada do jogador, cheia de surpresas
- **Alice**: Cantora talentosa, filha do dono do bar
- **Guilherme**: Amigo da academia, com problemas com bebida

## 🚀 Como Jogar
1. Execute o arquivo `Boteco_do_Russo_FINAL.py`
2. Digite o nome do seu personagem
3. Escolha o modo visual (com ou sem limpeza de tela)
4. Tome decisões digitando os números correspondentes
5. Divirta-se explorando todas as possibilidades!

## 📁 Estrutura do Código
O arquivo único contém:
- **Classes dos Personagens**: Cada personagem tem sua própria classe com métodos para interações
- **Funções Auxiliares**: Utilitários como `sprint()` para efeito de digitação
- **Funções de Jogo**: Lógica principal do fluxo do jogo
- **Função Main**: Orquestra todo o jogo

## 🔧 Requisitos
- Python 3.6+
- Bibliotecas: `colorama`, `pyfiglet`

## 📝 Instalação das Dependências
```bash
pip install colorama pyfiglet
```

## 🎯 Melhorias Implementadas
- **Código Modular**: Mesmo em um arquivo único, o código está organizado em classes
- **Manutenibilidade**: Fácil de adicionar novos personagens ou modificar diálogos
- **Reutilização**: Classes podem ser instanciadas conforme necessário
- **Testabilidade**: Cada interação pode ser testada independentemente
- **Novas Funcionalidades do Lex**: Sistema de confiança, missões especiais, apresentação de Natasha, drinks exóticos
- **Personagem Natasha**: Nova personagem com leitura de cartas do tarô, conselhos sobre o futuro, revelação de segredos
- **Sistema de Relacionamentos**: Níveis de confiança e intimidade que afetam as conversas disponíveis
- **Missões Interativas**: Sistema de missões com múltiplos desfechos baseado nas escolhas do jogador

## 👥 Créditos
- **Programação e Roteiro**: Victor Hugo Oliveira
- **História e Roteiro**: Igor Silva Azeredo

## ⚠️ Aviso
Este é um jogo humorístico. Qualquer semelhança com pessoas reais é mera coincidência.

---
*Divirta-se no Boteco do Russo!* 🍻
