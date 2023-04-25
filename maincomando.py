import curses
import time
from curses import wrapper, newwin, textpad

def funcao_principal(telaprincipal):

#criando e estabelecendo cores
    
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    
    verde = curses.color_pair(1)
    troca = curses.color_pair(2)
    vermelho = curses.color_pair(3)
    azul = curses.color_pair(4)

#configurando a tela inicial e o cursor
    
    curses.curs_set(1)
    curses.echo()
    curses.nocbreak()

#criando os parâmetros de altura e largura (coordenadas) da janela principal e da tartaruga

    altura, largura = telaprincipal.getmaxyx()  
    tartarugay, tartarugax = altura // 2, largura // 2

#criando a janela de início antes do jogo começar
  
    inicio = newwin(1, tartarugax, tartarugay, 45)
    inicio.clear()
    inicio.addstr("PRESSIONE [ENTER] PARA COMEÇAR", verde)
    curses.curs_set(0)
    inicio.getch()
    inicio.clear()
    inicio.refresh()

#criando a janela de jogo

    window = newwin(altura-3, largura)
    window.attron(verde)
    window.border()

#criando loop principal
    
    while True:

#criando janela da caixa de digitação

        curses.curs_set(1)
        texto = newwin(1, largura - 20, altura-1, 0)
        texto.clear()
        texto.addstr("DIGITE AS MOVIMENTAÇÕES:", verde)
        texto.refresh()
        digitado = texto.getstr(0, len("DIGITE AS MOVIMENTAÇÕES:"), largura - 20).decode("utf-8")

#condicionais para receber o sentido e a quantidade de casas para andar        
        
        sentido = str(digitado.split(" ")[0])
        casa_final = int(digitado.split(" ")[1])
        casa_atual = 0
        
#comando para não existir movimentação negativa

        if casa_final < 0:
            window.addstr(1, 1, "[ NÃO HÁ MOVIMENTAÇÃO NEGATIVA | PRESSIONE [ENTER] PARA RESETAR ]", troca)
            window.getch()
            window.clear()
            window.border()
            window.addstr(tartarugay,tartarugax, ' ', verde)
            tartarugay, tartarugax = altura // 2, largura // 2
            window.addstr(tartarugay,tartarugax, '@', verde)

#comando para apagar

        elif sentido == "APAGAR":
            window.clear()
            window.border()
            window.addstr(tartarugay,tartarugax, '@', verde)

#comando para voltar
        
        elif sentido == "VOLTAR":
            window.addstr(tartarugay,tartarugax, ' ', verde)
            tartarugay, tartarugax = altura // 2, largura // 2
            window.addstr(tartarugay,tartarugax, '@', verde)
        
#comando para andar para oeste
    
        elif sentido == "OESTE":
            if tartarugax - casa_final >= 1:
                while casa_atual < casa_final:
                    window.addstr(tartarugay, tartarugax - casa_atual, "●", verde)
                    casa_atual += 1
                tartarugax -= casa_final
                window.addstr(tartarugay,tartarugax, '@', verde)

#comando para andar para leste
        
        elif sentido == "LESTE":
            if tartarugax + casa_final < largura - 1:
                while casa_atual < casa_final:
                    window.addstr(tartarugay, tartarugax + casa_atual, "●", verde)
                    casa_atual += 1
                tartarugax += casa_final
                window.addstr(tartarugay,tartarugax, '@', verde)

#comando para andar para norte
        
        elif sentido == "NORTE":
            if tartarugay - casa_final >= 1:
                while casa_atual < casa_final:
                    window.addstr(tartarugay - casa_atual, tartarugax, "●", verde)
                    casa_atual += 1
                tartarugay -= casa_final
                window.addstr(tartarugay,tartarugax, '@', verde)

#comando para andar para sul
        
        elif sentido == "SUL":
            if tartarugay + casa_final < altura - 4:
                while casa_atual < casa_final:
                    window.addstr(tartarugay + casa_atual, tartarugax, "●", verde)
                    casa_atual += 1
                tartarugay += casa_final
                window.addstr(tartarugay,tartarugax, '@', verde)

#comando para andar para nordeste
        
        elif sentido == "NORDESTE":
            if tartarugay - casa_final >= 1 and tartarugax + casa_final < largura - 2:
                while casa_atual < casa_final:
                    window.addstr(tartarugay - casa_atual , tartarugax + casa_atual, "●", verde)
                    casa_atual += 1
                tartarugay -= casa_final
                tartarugax += casa_final
                window.addstr(tartarugay,tartarugax, '@', verde)

#comando para andar para noroeste
        
        elif sentido == "NOROESTE":
            if tartarugay - casa_final >= 1 and tartarugax - casa_final >= 1:
                while casa_atual < casa_final:
                    window.addstr(tartarugay - casa_atual , tartarugax - casa_atual, "●", verde)
                    casa_atual += 1
                tartarugay -= casa_final
                tartarugax -= casa_final
                window.addstr(tartarugay,tartarugax, '@', verde)

#comando para andar para sudeste
        
        elif sentido == "SUDESTE":
            if tartarugay + casa_final < altura - 3 and tartarugax + casa_final < largura - 2:
                while casa_atual < casa_final:
                    window.addstr(tartarugay + casa_atual, tartarugax + casa_atual, "●", verde)
                    casa_atual += 1
                tartarugay += casa_final
                tartarugax += casa_final
                window.addstr(tartarugay,tartarugax, '@', verde)

#comando para andar para sudoeste
        
        elif sentido == "SUDOESTE":
            if tartarugay + casa_final < altura - 3 and tartarugax - casa_final >= 1:
                while casa_atual < casa_final:
                    window.addstr(tartarugay + casa_atual, tartarugax - casa_atual , "●", verde)
                    casa_atual += 1
                tartarugay += casa_final
                tartarugax -= casa_final
                window.addstr(tartarugay,tartarugax, '@', verde)

#comando para não existir movimentação fora da rosa dos ventos
        
        else:
            window.addstr(1, 1, "[ ESSA DIREÇÃO NÃO EXISTE | PRESSIONE [ENTER] PARA RESETAR ]", troca)
            window.getch()
            window.clear()
            window.border()
            window.addstr(tartarugay,tartarugax, ' ', verde)
            tartarugay, tartarugax = altura // 2, largura // 2
            window.addstr(tartarugay,tartarugax, '@', verde)
        window.refresh()