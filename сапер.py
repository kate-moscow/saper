import random
import pygame
from pygame import color
pygame.init ()

empty=0
otkrito=1
bomb=2
close=3
flag=4
xz=5
k=1
size= (600,600)
kontur = 9
block=20
W=20
pygame.display.set_caption("Saper")
okno= pygame.display.set_mode(size)
time= pygame.time.Clock()
black=(0,0,0)
green=(0,34,0)
grey=(82,82,82)
white=(255,255,255)
pole= []
bomb_count=30
flag_count=14
#создание массива под поле#
for i in range (W):
    a=[0]*W
    pole.append(a)
field=pole
#создание бомб и областей помечающих, что бомба рядом#
def set_bomb (bomb_count):
    for x in range (bomb_count):
        q=random.randint(0,W-1)
        p=random.randint(0,W-1)
        pole[q][p] = bomb
        for i in range (3):
            for j in range(3):
                l=q-i+1
                n=p-j+1
                if  l>=0 and n>=0 and l<20 and n<20:
                    if  pole[l][n]!=bomb:
                        pole[l][n]=close
    return(pole)

#проверка на то, какую ячейку открыл игрок#
def check(row,col):
    if pole[row][col] == 0:
        field[row][col]=9
        T=True
        while  T :
            for i in range (W):
                for j in range (W):
                    if field[i][j]==9:
                        x=i
                        y=j
                        if (x-1>=0 and x-1<20) and pole[x-1][y]!=bomb:
                            field [x-1][y]= 9
                            field [x][y]= 0
                            pole [x][y] = 1
                        if (x+1>=0 and x+1<20) and pole[x+1][y]!=bomb:
                            field [x+1][y]= 9
                            field [x][y]= 0
                            pole [x][y] = 1
                        if (y+1>=0 and y+1<20) and pole[x][y+1]!=bomb:
                            field [x][y+1]= 9
                            field [x][y]= 0
                            pole [x][y] = 1
                        if (y-1>=0 and y-1<20) and pole[x][y-1]!=bomb:
                            field [x][y-1]= 9
                            field [x][y]= 0
                            pole [x][y] = 1 
    return(pole,field)

set_bomb(bomb_count)
#основной цикл#
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #реагирование поля на нажатие мышки#
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse //(kontur+W)
            row= y_mouse//(kontur+W)
            check(row,col)
    #Отрисовка поляи проверка каждой клетки#
    for row in range (W):
        for col in range (W):
            if pole[row][col]==otkrito:
                color=green
            elif pole[row][col]==empty: # or pole[row][col]==bomb:
                color=grey
            elif pole[row][col]==bomb:
                color=black
            elif pole[row][col]==close:
               color=white
            x = col * W +(col)*kontur +15
            y = row * W +(row)*kontur +15
            pygame.draw.rect(okno,color,(x,y,block,block),) 
    pygame.display.flip()
    time.tick(60)
