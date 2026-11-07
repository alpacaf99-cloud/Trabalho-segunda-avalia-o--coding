#  SUDOKU EM PYTHON

Um jogo de Sudoku interativo executado inteiramente no terminal com linhas de comandos; Este projeto foi desenvolvido para um trabalho universitário de Ciéncia da computação do segundo periodo; e foi elaborado em **Python puro**, sem a utilização de funções (`def`) ou bibliotecas externas (`import`). O objetivo arquitetural foi aplicar exclusivamente os fundamentos da programação estruturada, como laços de repetição (`while`, `for`), matrizes bidimensionais e desvios condicionais.

------------------------
------------------------

# Funcionalidades e Modos de Jogo

- Modo Competitivo (4x4): Dois jogadores alternam turnos para resolver um tabuleiro reduzido. Se um jogador tentar uma jogada inválida ou alterar uma casa fixa, ele é penalizado com a perda da vez.
  
- Modo Desafiante (9x9): Jogue o Sudoku clássico contra a máquina! O desafio conta com um temporizador mecânico de **50 ações**. Se você não preencher o quadro antes das tentativas esgotarem, a máquina vence.
  
- Validação Lógica Dinâmica: O sistema impede, em tempo real, a sobreposição de números fixos (do gabarito inicial) e a violação das regras estritas de linha, coluna e subquadrantes (2x2 ou 3x3).
  
- Tratamento Robusto de Erros: As entradas do utilizador são validadas estritamente via texto. Se forem digitadas letras ou símbolos no lugar de coordenadas, o jogo bloqueia a ação e repete o laço sem provocar falhas (dispensando o uso de `try/except`).
  
- Painel de Estatísticas: Um placar global que guarda, na memória da sessão, o total de partidas jogadas, vitórias, pontuação acumulada e a taxa de sucesso.

------------------------
------------------------

# Pré-requisitos

Por ser uma aplicação de arquitetura nativa e independente, o jogo não possui dependências complexas. Você só precisará do interpretador padrão da linguagem.

- Python 3.15 instalado ([Download oficial](https://www.python.org/downloads/)).
  
- Um terminal ou Prompt de Comando (Windows, Linux ou macOS).
  
------------------------
------------------------

# Regras das Partidas
O jogo tem 2 modos o competitivo entre 2 players e um contra a maquina que conta a quantidade de acertos.

Competitivo 4x4 (2 Jogadores)
Cada casa aceita números de 1 a 4.
É proibido repetir números na mesma linha, coluna ou bloco 2x2.
Uma jogada válida concede 10 pontos e passa a vez.
Vence o primeiro jogador que zerar todos os espaços em branco do seu respectivo tabuleiro.

Desafiante 9x9 (Solo)
Cada casa aceita números de 1 a 9.
É proibido repetir números na mesma linha, coluna ou bloco 3x3.
Uma jogada válida concede 20 pontos.
Cuidado: Você possui um limite rígido de 50 ações. Vence quem completar a grade antes do contador chegar a zero.

#Arquitetura do Código
A aplicação repousa num único arquivo fonte, operando sob o paradigma imperativo sequencial (top-down). As engrenagens principais incluem:
Matrizes aninhadas: Declaração manual das grelhas lógicas e dos mapas de casas fixas (Booleanos).
Validação de Subquadrantes: Cálculo matemático em tempo de execução utilizando divisão inteira (//) para definir âncoras locais e varrer matrizes menores (sem necessidade de condicionais if gigantescas).
Laços Infinitos Controlados: Loops aninhados baseados em flags (sinalizadores booleanos como valida_menu = False) que aprisionam a interface até receberem comandos perfeitamente seguros.

# Autores: 
1. João Felipe de Oliveira Silva
2. João Gabriel Teles Gomes Soares
3. Kyvia Wenne Coutinho Bezerra

