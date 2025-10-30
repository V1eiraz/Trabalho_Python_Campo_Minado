# 🐍 Campo Minado em Python (Console)

Um jogo de Campo Minado simples, implementado em Python puro e jogado diretamente no terminal. Este projeto foi criado como um exercício de lógica de programação, manipulação de listas (matrizes) e entrada de dados do usuário.

## 🎮 Funcionalidades

* **Tabuleiro Personalizável:** O usuário pode definir a altura e a largura do tabuleiro (mínimo 3x3, máximo 10x10).
* **Dificuldade Ajustável:** O usuário escolhe o número de bombas a serem colocadas no tabuleiro.
* **Validação de Entrada:** O jogo possui tratamento de erros (`try...except`) para entradas inválidas (ex: digitar "olá" em vez de um número), garantindo que o programa não trave.
* **Interface de Terminal:** Jogo totalmente baseado em texto com comandos simples.
* **Sistema de Jogo Clássico:**
    * **Abrir (`a`):** Revela uma casa. Se for uma bomba, o jogo acaba. Se for vazia, mostra o número de bombas adjacentes.
    * **Marcar (`m`):** Coloca uma bandeira (`M`) em uma casa suspeita.
    * **Sair (`s`):** Encerra o jogo.

## 🚀 Como Executar

Você precisa ter o [Python 3](https://www.python.org/downloads/) instalado em sua máquina.

1.  Clone este repositório ou baixe o arquivo `.py`:
    ```sh
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```
2.  Navegue até a pasta do projeto:
    ```sh
    cd seu-repositorio
    ```
3.  Execute o script:
    ```sh
    python nome_do_arquivo.py
    ```
    (Substitua `nome_do_arquivo.py` pelo nome real do seu arquivo)

## 📖 Como Jogar

1.  Ao iniciar, o jogo pedirá a **Altura**, **Largura** e o **Número de Bombas**.
2.  O tabuleiro será exibido, com todas as casas escondidas (`#`).
3.  Você terá 3 ações por turno:
    * **a**: Para **Abrir** uma casa. O jogo pedirá a linha e a coluna.
    * **m**: Para **Marcar** uma casa com uma bandeira (`M`).
    * **s**: Para **Sair** do jogo.
4.  O objetivo é abrir todas as casas que **não** contêm bombas.
5.  Se você abrir uma casa com uma bomba (`*`), você perde!

## 🔧 Visão Geral do Código

O código é estruturado em funções para modularizar as diferentes partes do jogo.

### Variáveis Globais

* `mapa_real`: Matriz (lista de listas) que contém a posição real das bombas (`*`) e os espaços vazios.
* `mapa_usuario`: Matriz que é exibida ao jogador, mostrando casas escondidas (`#`), marcadas (`M`) ou os números de bombas adjacentes.
* `linha_escolhida` / `coluna_escolhida`: Listas de um elemento usadas para passar a coordenada da jogada atual para as funções (evitando parâmetros).

### Funções Principais

* `colocar_bombas()`: Sorteia posições aleatórias no `mapa_real` e insere o número de bombas definido pelo usuário. Garante que uma bomba não seja colocada em cima de outra.
* `contar_bombas()`: Após o usuário "Abrir" uma casa, esta função verifica as 8 células adjacentes (vizinhança 3x3) e retorna a contagem de bombas (`*`) ao redor.
* `mostrar_quantidade_bombas(quantidade_bombas)`: Atualiza o `mapa_usuario` na posição escolhida. Se a contagem for 0, insere um espaço (` `); caso contrário, insere o número de bombas (como string).
* `printar_mapa()` / `printar_mapa_real()`: Funções auxiliares para formatar e exibir os tabuleiros `mapa_usuario` e `mapa_real` no console.

### Lógica Principal (Loops)

1.  **Loop de Configuração:**
    * O primeiro `while sair == 0:` é responsável por obter as configurações do jogo (tamanho e bombas).
    * Utiliza um bloco `try...except ValueError` para garantir que o usuário digite apenas números inteiros.
    * Valida as regras de negócio (tamanho mínimo/máximo, quantidade de bombas).

2.  **Loop do Jogo:**
    * O segundo `while sair == 0:` é o loop principal do jogo.
    * Ele verifica as condições de vitória a cada turno.
    * Processa a entrada do jogador (`a`, `m` ou `s`) usando `match...case`.
    * Chama as funções apropriadas com base na ação do jogador.
    * Encerra o loop em caso de vitória (campo limpo), derrota (pisar na bomba) ou se o usuário digitar `s`.