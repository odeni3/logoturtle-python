#importando bibliotecas e importando funções dos outros arquivos (com apelido), visando a modularização

import curses
from curses import wrapper
from curses.textpad import rectangle
from maincomando import funcao_principal as funcao_principal_comando
from mainkey import main as funcao_principal_key

#menu 1 

menu = ['Iniciar', ' Instruções', 'Sair']      

#menu 2

menu2 = [' Logo Turtle [Fácil]', 'Logo Turtle [Difícil]']   

#função para mostrar o menu

def print_menu(janela_principal, selected_camada_idx):    
    
#centralizando a janela

    janela_principal.clear() 
    h, w = janela_principal.getmaxyx()

#criando e definindo cores

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)     
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)

    verde = curses.color_pair(1)
    vermelho = curses.color_pair(2)
    azul = curses.color_pair(3)

#centralizando o título do jogo e definindo sua cor    

    janela_principal.addstr((h//2) - 4, (w//2) -5, "LOGO TURTLE", curses.A_BOLD | curses.A_UNDERLINE | verde)
    
#obtendo centro da janela e imprimindo o retângulo de contorno do menu 1

    tela_altura, tela_largura = janela_principal.getmaxyx()      

    retangulo_altura = 4
    retangulo_largura = 10

    rect_x = (tela_largura - retangulo_largura) // 2
    rect_y = (tela_altura - retangulo_altura) // 2

    janela_principal.attron(curses.color_pair(1))
    rectangle(janela_principal, rect_y, rect_x - 1, rect_y + retangulo_altura , rect_x + retangulo_largura + 2)
    janela_principal.attroff(curses.color_pair(1))
    
#calculando e definindo as coordenadas de centralização do menu e dispondo as opções na tela, além de exibir as cores   
    
    for idx, camada in enumerate(menu):
        x = w//2 - len(camada)//2 
        y = h//2 - len(menu)//2 + idx
        if idx == selected_camada_idx:
            janela_principal.attron(curses.color_pair(1))
            janela_principal.addstr(y, x, camada)
            janela_principal.attroff(curses.color_pair(1))

#caso a opção não esteja selecionada, volta à cor normal (branca)

        else:
            janela_principal.addstr(y, x, camada)                     

    janela_principal.refresh()

#função para exibir o menu dentro do menu iniciar, exibindo o modo de jogo fácil e o difícil

def print_menu2(janela_principal, selected_camada_idx):
    
#obtendo centro da janela e imprimindo o retângulo de contorno do menu 2   
    
    janela_principal.clear() 
    h, w = janela_principal.getmaxyx()                             
    tela_altura, tela_largura = janela_principal.getmaxyx()  

    retangulo_altura = 4
    retangulo_largura = 10

    rect_x = (tela_largura - retangulo_largura) // 2
    rect_y = (tela_altura - retangulo_altura) // 2

    janela_principal.attron(curses.color_pair(1))
    rectangle(janela_principal, rect_y, rect_x - 6, rect_y + retangulo_altura - 1, rect_x + retangulo_largura + 6)
    janela_principal.attroff(curses.color_pair(1))

#exibindo mensagem para voltar ao menu

    janela_principal.addstr(0,0, "PRESSIONE [HOME] PARA RETORNAR AO MENU")
    janela_principal.addstr(1,0, "PRESSIONE [CTRL + C] PARA FECHAR O JOGO")

#loop que calcula as coordenadas de centralização do menu e exibe as opções na tela   
    
    for idx, camada in enumerate(menu2):
        x = w//2 - len(camada)//2
        y = h//2 - len(menu2)//2 + idx

#faz com que as opções selecionadas mudem a cor

        if idx == selected_camada_idx:          
            janela_principal.attron(curses.color_pair(1))
            janela_principal.addstr(y, x, camada)
            janela_principal.attroff(curses.color_pair(1))

#se a opção não estiver selecionada, volta à cor normal

        else:
            janela_principal.addstr(y, x, camada)           

    janela_principal.refresh()

#função que chama o 2° Menu

def main2(janela_principal):
    curses.curs_set(0)                                                              
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
                
    current_camada_idx = 0

#exibindo o segundo menu e definindo a array inicial na posição [0]     

    print_menu2(janela_principal, current_camada_idx)

    while 1:
        
        key = janela_principal.getch()                                    
        janela_principal.clear()

#elaborando as condicionais de movimentação pelo menu          

        if key == curses.KEY_UP and current_camada_idx > 0:                                             
            current_camada_idx -= 1
        elif key == curses.KEY_DOWN and current_camada_idx < len(menu) - 1:                                 
            current_camada_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 0:
            wrapper(funcao_principal_comando)

#elaborando a condicional que chama o jogo por bind

        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 1:      
            wrapper(funcao_principal_key)

#condição que volta para o primeiro menu (principal)

        elif key == curses.KEY_HOME:                                                      
            curses.wrapper(main)
        print_menu2(janela_principal, current_camada_idx)
        
#atualizando a tela e esperando resposta do usuário

        janela_principal.refresh()
        janela_principal.getch()

#função para executar o menu principal e os seus adjacentes

def main(janela_principal):
   
   curses.curs_set(0)                                                              
   curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
   current_camada_idx = 0
   
#exibe o menu na tela e a camada de seleção

   print_menu(janela_principal, current_camada_idx)    

#loop que aguarda a entrada do usuário   
   
   while 1:
        
        key = janela_principal.getch()          
        janela_principal.clear()
        
#verifica se a tecla up foi pressionada e sobe (caso tenha espaço)

        if key == curses.KEY_UP and current_camada_idx > 0:                                                 
            current_camada_idx -= 1

#verifica se a tecla down foi pressionada e desce (caso tenha espaço)

        elif key == curses.KEY_DOWN and current_camada_idx < len(menu) - 1:                                 
            current_camada_idx += 1

#verifica se Enter foi pressionado e chama a função do segundo menu

        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 0:                        
            curses.wrapper(main2)

#atualizando a tela e esperando resposta do usuário

            janela_principal.refresh()
            janela_principal.getch()

#verifica se Enter foi pressionado e exibe as instruções
                        
        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 1:                        
            
#informações coloridas acerca do modo de jogo Logo Turtle [Fácil]

            janela_principal.attron(curses.color_pair(2))
            janela_principal.addstr(3,0, "Logo Turtle [Fácil]")
            janela_principal.attroff(curses.color_pair(2))
            
            janela_principal.attron(curses.color_pair(1))
            janela_principal.addstr(5,0, "Comandos de Sentido: NORTE, NORDESTE, NOROESTE, LESTE, OESTE, SUL, SUDESTE e SUDOESTE;")
            janela_principal.addstr(6,0, "Comandos de Casas: Quantidade de casas a andar;")
            janela_principal.addstr(7,0, "Comandos Diversos: APAGAR e VOLTAR;")
            janela_principal.addstr(8,0, "[EXEMPLOS]:")
            janela_principal.addstr(9,0, "1- OESTE 10;")
            janela_principal.addstr(10,0, "2- APAGAR 0;")
            janela_principal.addstr(11,0, "3- VOLTAR 0;") 
            janela_principal.attroff(curses.color_pair(1))

            janela_principal.attron(curses.color_pair(4))
            janela_principal.addstr(13,0, "OBS: É necessário digitar o primeiro comando como STRING MAIÚSCULA seguido de um ESPAÇO e um NÚMERO INTEIRO.")
            janela_principal.attroff(curses.color_pair(4))

#divisão das informações entre os modos de jogo

            janela_principal.attron(curses.color_pair(3))
            janela_principal.addstr(15,0, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            janela_principal.attroff(curses.color_pair(3))

#informações coloridas acerca do modo de jogo Logo Turtle [Difícil]

            janela_principal.attron(curses.color_pair(2))
            janela_principal.addstr(17,0, "Logo Turtle [Difícil]")
            janela_principal.attroff(curses.color_pair(2))
            
            janela_principal.attron(curses.color_pair(1))
            janela_principal.addstr(19,0, "Comandos de Sentido [Pontos cardeais]: NORTE, SUL, OESTE e LESTE || [UP/DOWN/LEFT/RIGHT]")
            janela_principal.addstr(20,0, "Comandos de Sentido [Pontos colaterais]: NOROESTE, SUDOESTE, NORDESTE e SUDESTE || [INS/DEL/PGUP/PGDN]")
            janela_principal.attroff(curses.color_pair(1))
            
            janela_principal.attron(curses.color_pair(4))
            janela_principal.addstr(22,0, "OBS: [ GAME OVER ] caso a tartaruga encoste na borda.")
            janela_principal.attroff(curses.color_pair(4))
           
#informações acerca das binds para voltar e para fechar o jogo           
           
            janela_principal.addstr(0,0, "PRESSIONE [HOME] PARA RETORNAR AO MENU")
            janela_principal.addstr(1,0, "PRESSIONE [CTRL + C] PARA FECHAR O JOGO")

#atualizando a tela e esperando resposta do usuário

            janela_principal.refresh()
            janela_principal.getch()

#verifica se Enter (na 3° opção) foi pressionado e sai do jogo    
        
        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 2:                     
            break

        print_menu(janela_principal, current_camada_idx)
        janela_principal.refresh()
            
#chama a função wrapper responsável por iniciar e finalizar as telas definidas nas funções

wrapper(main)
