#importando bibliotecas

import curses
from curses import textpad

#defindo a função principal

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
    sentido = curses.KEY_RIGHT

    for y, x in turtle:
        tela_jogo.addstr(y, x, '@')

#criando loop principal 

    while True:
        
#definindo a array de todas as binds possíveis para movimentação

        key = tela_jogo.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN, curses.KEY_IC, curses.KEY_DC, curses.KEY_PPAGE, curses.KEY_NPAGE]:
            sentido = key

#definindo a "mira" da tartaruga, ou seja, a posição dela

        mira = turtle[0]

#comando para andar para leste

        if sentido == curses.KEY_RIGHT:       
            nova_mira = [mira[0], mira[1]+1]

#comando para andar para oeste

        elif sentido == curses.KEY_LEFT:     
            nova_mira = [mira[0], mira[1]-1]

#comando para andar para norte

        elif sentido == curses.KEY_UP:        
            nova_mira = [mira[0]-1, mira[1]]

#comando para andar para sul

        elif sentido == curses.KEY_DOWN:      
            nova_mira = [mira[0]+1, mira[1]]

#comando para andar para noroeste

        elif sentido == curses.KEY_IC:        
            nova_mira = [mira[0]-1, mira[1]-1]

#comando para andar para sudoeste

        elif sentido == curses.KEY_DC:        
            nova_mira = [mira[0]+1, mira[1]-1]

#comando para andar para nordeste

        elif sentido == curses.KEY_PPAGE:     
            nova_mira = [mira[0]-1, mira[1]+1]

#comando para andar para sudeste

        elif sentido == curses.KEY_NPAGE:     
            nova_mira = [mira[0]+1, mira[1]+1]

        else:
            pass

#deixando os rastros de desenho da tartaruga
        
        turtle.insert(0, nova_mira)
        tela_jogo.addstr(nova_mira[0], nova_mira[1], '@')
        tela_jogo.addstr(turtle[-1][0], turtle[-1][1], '●')
        turtle.pop()

        tela_jogo.refresh()
        
#delimitando área de atuação da tartaruga e exibindo mensagem de game over caso encoste na borda      
        
        if (turtle[0][0] in [posicao[0][0], posicao[1][0]] or
            turtle[0][1] in [posicao[0][1], posicao[1][1]] or
            turtle[0] in turtle[1:]):
            alert = "[ GAME OVER ]"
            tela_jogo.addstr(altura//2, largura//2 - len(alert)//2, alert)

            tela_jogo.nodelay(0)
            tela_jogo.getch()
            break

        tela_jogo.refresh()
