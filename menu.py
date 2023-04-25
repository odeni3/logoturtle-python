import curses
from curses import wrapper
from maincomando import funcao_principal as funcao_principal_comando
from mainkey import main as funcao_principal_key

menu = ['Iniciar', '   Instruções', 'Sair  ']                  #Menu 1    
menu2 = [' Logo Turtle [Fácil]', 'Logo Turtle [Difícil]']   #Menu2
def print_menu(stdscr, selected_camada_idx):    
    
    stdscr.clear() 
    h, w = stdscr.getmaxyx()                    #Obtém o centro da janela

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
    
    verde = curses.color_pair(1)
    vermelho = curses.color_pair(2)
    azul = curses.color_pair(3)
        
    for idx, camada in enumerate(menu):
        x = w//2 - len(camada)//2               #Calcula as coordenadas para centralizar o menu e dispor as opções na tela
        y = h//2 - len(menu)//2 + idx
        if idx == selected_camada_idx:          #Faz com que cada seleção fique colorida
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, camada)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, camada)          #Se não estiver selecionado, volta a cor normal

    stdscr.refresh()

def print_menu2(stdscr, selected_camada_idx):
    
    stdscr.clear() 
    h, w = stdscr.getmaxyx()                    #Obtém o centro da janela
        
    for idx, camada in enumerate(menu2):
        x = w//2 - len(camada)//2               #Calcula as coordenadas para centralizar o menu e dispor as opções na tela
        y = h//2 - len(menu2)//2 + idx
        if idx == selected_camada_idx:          #Faz com que cada seleção fique colorida
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, camada)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, camada)          #Se não estiver selecionado, volta a cor normal

    stdscr.refresh()

def main2(stdscr): 
    curses.curs_set(0)                                                              
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
                
    current_camada_idx = 0
                
    print_menu2(stdscr, current_camada_idx)     

    while 1:
        key = stdscr.getch()                    
                        
        stdscr.clear()
                        
        if key == curses.KEY_UP and current_camada_idx > 0:                                                 
            current_camada_idx -= 1
        elif key == curses.KEY_DOWN and current_camada_idx < len(menu) - 1:                                 
            current_camada_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 0:
            wrapper(funcao_principal_comando)

        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 1:
            wrapper(funcao_principal_key)
            
        print_menu2(stdscr, current_camada_idx)
        stdscr.refresh()
        stdscr.getch()

def main(stdscr):
   curses.curs_set(0)                                                              
   curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
   
   current_camada_idx = 0
   
   print_menu(stdscr, current_camada_idx)     #Exibe o menu na tela e a camada de seleção

   while 1:
        key = stdscr.getch()                    #Aguarda a entrada do usuário
        
        stdscr.clear()
        
        if key == curses.KEY_UP and current_camada_idx > 0:                                                 #Verifica se a tecla up foi pressionada e sobe (caso tenha espaço)
            current_camada_idx -= 1
        elif key == curses.KEY_DOWN and current_camada_idx < len(menu) - 1:                                 #Verifica se a tecla down foi pressionada e desce (caso tenha espaço)
            current_camada_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 0:                        #Verifica se Enter foi pressionado e mostra na tela o string escolhido
            curses.wrapper(main2)
            stdscr.refresh()
            stdscr.getch()
        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 1:                        #Verifica se Enter foi pressionado e mostra na tela o string escolhido
            
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(1,0, "Logo Turtle [Fácil]")
            stdscr.attroff(curses.color_pair(2))
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(3,0, "Comandos de Sentido: NORTE, NORDESTE, NOROESTE, LESTE, OESTE, SUL, SUDESTE e SUDOESTE;")
            stdscr.addstr(4,0, "Comandos de Casas: Quantidade de casas a andar;")
            stdscr.addstr(5,0, "Comandos Diversos: APAGAR e VOLTAR;")
            stdscr.addstr(7,0, "[EXEMPLOS]:")
            stdscr.addstr(8,0, "1- OESTE 10;")
            stdscr.addstr(9,0, "2- APAGAR 0;")
            stdscr.addstr(10,0, "3- VOLTAR 0;")
            stdscr.attroff(curses.color_pair(1))
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(12,0, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            stdscr.attroff(curses.color_pair(3))
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(14,0, "Logo Turtle [Difícil]")
            stdscr.attroff(curses.color_pair(2))
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(16,0, "Comandos de Sentido [Pontos cardeais]: NORTE, SUL, OESTE e LESTE || [UP/DOWN/LEFT/RIGHT]")
            stdscr.addstr(17,0, "Comandos de Sentido [Pontos colaterais]: NOROESTE, SUDOESTE, NORDESTE e SUDESTE || [INS/DEL/PGUP/PGDN]")
            stdscr.attroff(curses.color_pair(1))
            stdscr.attron(curses.color_pair(4))
            stdscr.addstr(19,0, "OBS: [ GAME OVER ] caso a tartaruga encoste na borda.")
            stdscr.attroff(curses.color_pair(4))
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(38,0, "PRESSIONE [BACKSPACE] PARA RETORNAR AO MENU")
            
            stdscr.refresh()
            stdscr.getch()
        elif key == curses.KEY_ENTER or key in [10, 13] and current_camada_idx == 2:                        #Verifica se Enter foi pressionado e mostra na tela o string escolhido
            break
        
        print_menu(stdscr, current_camada_idx)
        stdscr.refresh()

curses.wrapper(main)