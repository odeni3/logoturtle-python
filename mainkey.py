import curses
from curses import wrapper
from curses import textpad

def main(tela_jogo):
    
#criando cor
    
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(2)

#cursor invisível
    
    curses.curs_set(0)
    
#colocando as bordas do jogo e colocando a cor
    
    altura, largura = tela_jogo.getmaxyx()
    posicao = [[0,0], [altura-1, largura-2]]
    tela_jogo.attron(GREEN_AND_BLACK)
    textpad.rectangle(tela_jogo, posicao[0][0], posicao[0][1], posicao[1][0], posicao[1][1])

#colocando a tartaruga no centro da tela inicial
    
    turtle = [[altura//2, largura//2]]
    direction = curses.KEY_RIGHT
    for y, x in turtle:
        tela_jogo.addstr(y, x, '@')


#bindando as teclas para movimentação da tartaruga
    
    while True:
        
        key = tela_jogo.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN, curses.KEY_IC, curses.KEY_DC, curses.KEY_PPAGE, curses.KEY_NPAGE]:
            direction = key

        aim = turtle[0]

        if direction == curses.KEY_RIGHT:       #leste
            new_aim = [aim[0], aim[1]+1]
        elif direction == curses.KEY_LEFT:      #oeste
            new_aim = [aim[0], aim[1]-1]
        elif direction == curses.KEY_UP:        #norte
            new_aim = [aim[0]-1, aim[1]]
        elif direction == curses.KEY_DOWN:      #sul
            new_aim = [aim[0]+1, aim[1]]
        elif direction == curses.KEY_IC:        #noroeste
            new_aim = [aim[0]-1, aim[1]-1]
        elif direction == curses.KEY_DC:        #sudoeste
            new_aim = [aim[0]+1, aim[1]-1]
        elif direction == curses.KEY_PPAGE:     #nordeste
            new_aim = [aim[0]-1, aim[1]+1]
        elif direction == curses.KEY_NPAGE:     #sudeste
            new_aim = [aim[0]+1, aim[1]+1]
        else:
            pass

#deixando os rastros de desenho da tartaruga
        
        turtle.insert(0, new_aim)
        tela_jogo.addstr(new_aim[0], new_aim[1], '@')
        tela_jogo.addstr(turtle[-1][0], turtle[-1][1], '●')
        turtle.pop()
        tela_jogo.refresh()
        
#delimitando área de atuação da tartaruga e exibindo mensagem       
        
        if (turtle[0][0] in [posicao[0][0], posicao[1][0]] or
            turtle[0][1] in [posicao[0][1], posicao[1][1]] or
            turtle[0] in turtle[1:]):
            alert = "[ GAME OVER ]"
            tela_jogo.addstr(altura//2, largura//2 - len(alert)//2, alert)
            tela_jogo.nodelay(0)
            tela_jogo.getch()
            break

        tela_jogo.refresh()
