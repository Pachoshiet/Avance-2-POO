import pygame  
import sys
import time


from pygame import Rect, display
from pygame import mouse
from pygame.constants import MOUSEBUTTONDOWN
from pygame.draw import rect



pygame.init()
Fps=30 
fpsclock = pygame.time.Clock()

size = (1400,788)   
velx = -340
vely = 95
direccion = "derecha"
click =0
lado =1
vx =-360
vy=97
nvl = 0
a =1
b =1
direc ="derecha"
screen = pygame.display.set_mode(size) #crear ventana

letra = pygame.font.SysFont("Arial", 40)
letra1 = pygame.font.SysFont("Arial",20)
r1="1"
r2="2"
r3="0"
s = "100000"
n = "- 30000"
p = "+ 30000"
          

#escanear img
Fondo = pygame.image.load("ima/Fondo12.png").convert() #escanear? imagen pal programa
Pasar = pygame.image.load("ima/Alumnos pasados.png").convert()
pasar2 =pygame.image.load("ima/nextmes2.png").convert()
P1 = pygame.image.load("ima/P1.png").convert()
P1.set_colorkey([0, 0 ,0])#quitar color negro de la imagen
oja = pygame.image.load("ima/oja.png").convert()
oja.set_colorkey([255,255,255])#quitar color blanco
oja2 = pygame.image.load("ima/oja2.png").convert()
oja2.set_colorkey([255,255,255])#quitar color blanco
lista1 = pygame.image.load("ima/Lista1.png").convert()
carnetm = pygame.image.load("ima/carnet mujer.png").convert()
carnetm2 =pygame.image.load("ima/carnet mujer2.png").convert()
carnetG =pygame.image.load("ima/carnetG.png").convert()
fl1 = pygame.image.load("ima/Flecha1.png").convert()
fl1.set_colorkey([255,255,255])
fl2 = pygame.image.load("ima/flecha2.png").convert()
fl2.set_colorkey([255,255,255])
fl3 = pygame.image.load("ima/Flecha3.png").convert()
fl3.set_colorkey([255,255,255])
fl4 = pygame.image.load("ima/flecha4.png").convert()
fl4.set_colorkey([255,255,255])
P2 = pygame.image.load("ima/P2.png").convert()
P2.set_colorkey([0,0,0])
emp = pygame.image.load("ima/Empezar.png").convert()
tut = pygame.image.load("ima/tuto.png").convert()
sal = pygame.image.load("ima/SALIR.png").convert()
sal.set_colorkey([250,250,250])
rosa = pygame.image.load("ima/rosa.png").convert()
rosa.set_colorkey([250,250,250])
tut0 = pygame.image.load("ima/tut0.png").convert()
next = pygame.image.load("ima/NEXT.png").convert()
next.set_colorkey([255,255,255])
tut1 = pygame.image.load("ima/tut1.png").convert()
tut2 = pygame.image.load("ima/tut2.png").convert()
tut3 = pygame.image.load("ima/tut3.png").convert()
x3 = pygame.image.load("ima/x3.png").convert()
globo = pygame.image.load("ima/globo.png").convert()
x3.set_colorkey([255,255,255])
globo.set_colorkey([255,255,255])
#pa los collaiders
Coso = Rect(50,730,170,100)
x = Rect(100,400,100,100)
c=Rect(710,620,100,57)
x2 = Rect(635,410,100,57)
y = Rect(320,630,100,43)
y2 = Rect(450,630,100,43)
#collaiders intro
empe =Rect(550,100,280,85)
tuto = Rect(550,200,280,85)
sali = Rect(550,300,280,85)
ne = Rect(650,610,200,100)
ne1=Rect(30,700,250,100)
ne2=Rect(300,600,250,100)
ne3 = Rect(1250,650,105,90)
while nvl==0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                sys.exit()
    if a==1:
        pygame.draw.rect(screen,(0,0,0),sali,0)
        pygame.draw.rect(screen,(0,0,0),tuto,0)
        pygame.draw.rect(screen,(0,0,0),empe,0)     
        screen.blit(Fondo, [0,0])
        screen.blit(emp,[550,100])
        screen.blit(tut, [550,200])
        screen.blit(sal,[550,300])

    if empe.collidepoint(mouse.get_pos()):
        screen.blit(rosa,[450,110])
        if event.type == MOUSEBUTTONDOWN and event.button==1:
            nvl = 1
    
    if tuto.collidepoint(mouse.get_pos()):
        screen.blit(rosa,[450,215])
        if event.type == MOUSEBUTTONDOWN and event.button==1:
            a=2
    if a==2:
        pygame.draw.rect(screen,(0,0,0),ne1,0)
        pygame.draw.rect(screen,(0,0,0),ne,0)
        pygame.draw.rect(screen,(0,0,0),ne2,0)
        pygame.draw.rect(screen,(0,0,0),ne3,0)
        screen.blit(tut0,[0,0])       
        screen.blit(x3,[1250,650])
               
        if ne1.collidepoint(mouse.get_pos()):
            screen.blit(tut1,[0,0])
        if ne.collidepoint(mouse.get_pos()):
            screen.blit(tut2,[0,0])
        if ne2.collidepoint(mouse.get_pos()):
            screen.blit(tut3,[0,0])      
        if ne3.collidepoint(mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and event.button==1:
            a=1        
    if sali.collidepoint(mouse.get_pos()) and a==1:
        screen.blit(rosa,[450,320])
        if event.type == MOUSEBUTTONDOWN and event.button==1:
            event.type=pygame.QUIT


    pygame.display.flip()
while nvl == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                sys.exit() 
    historia = pygame.image.load("ima/presentacion.png").convert()
    
    empezar = Rect(1000,650,280,85)
    flas = pygame.image.load("ima/rosa1.png").convert()
    pygame.draw.rect(screen,(0,0,0),empezar,0)
    screen.blit(historia,(0,0))
    screen.blit(flas,(1000,650))
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        if empezar.collidepoint(mouse.get_pos()):
            nvl=2
    
    
    pygame.display.flip()
    
while nvl ==2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                sys.exit()
                
    nom = "Nombre:  Cecilia Becerra"
    ed = "Edad:  18"
    nom1 = "Nombre:  Marto Coscu"
    ed1 = "Edad:  32"
    t1 = "Buenas, Soy Marto Coscu, tengo 18"
    t12= "y vengo a la prueba de ICI,asi que"
    t123= "estare unas 3 horas aca."
    t2 = "Buenas, Soy Cecilia Becerra, tengo 18"
    t22= "y vengo a la prueba de ICINF,asi que"
    t223= "estare unas 3 horas aca."
    text1 = letra1.render(t1,1,(0,0,0))
    text12 = letra1.render(t12,1,(0,0,0))
    text123 = letra1.render(t123,1,(0,0,0))
    text2 = letra1.render(t2,1,(0,0,0))
    text22 = letra1.render(t22,1,(0,0,0))
    text223 = letra1.render(t223,1,(0,0,0))
    nombre = letra1.render(nom,1,(0,0,0))
    edad = letra1.render(ed,1,(0,0,0))
    nombre1 = letra1.render(nom1,1,(0,0,0))
    edad1 = letra1.render(ed1,1,(0,0,0))
    
    
    ccara = pygame.image.load("ima/chicacara.png").convert()
    ccara1 = pygame.image.load("ima/carachico.png").convert()
    
    pygame.draw.rect(screen,(0,0,0),y,0)
    pygame.draw.rect(screen,(0,0,0),y2,0)
    pygame.draw.rect(screen,(255,255,255),Coso,0)       
    screen.blit(Fondo, [0,0])  
    screen.blit(P1,[velx,vely])

    if lado == 2:
        screen.blit(P2,[vx,vy])
   
    #para mouse   
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        if Coso.collidepoint(mouse.get_pos()):
            click=1
        if x.collidepoint(mouse.get_pos()):
            click=0
        if c.collidepoint(mouse.get_pos()):
            click=2
        if x2.collidepoint(mouse.get_pos()):
            click=0
    else:
        if click == 1:
            pygame.draw.rect(screen,(0,0,0),x,0)
            screen.blit(lista1,[100,100])
        if Coso.collidepoint(mouse.get_pos()):
            if click==0:
             screen.blit(oja2,[50,650])
        else:
            if click ==0:
             screen.blit(oja,[50,730]) 
        if click ==2:
            pygame.draw.rect(screen,(0,0,0),x2,0)
            screen.blit(carnetG,[620,400])
            if velx==480:
                screen.blit(nombre,[855,540])
                screen.blit(edad,[855,570])
                screen.blit(ccara,[657,485])
            else:
                screen.blit(nombre1,[855,540])
                screen.blit(edad1,[855,570])
                screen.blit(ccara1,[657,485])
        
  #colocando carnet
        if direccion == "stop" and click==0:
            pygame.draw.rect(screen,(0,0,0),c,0)
            screen.blit(carnetm,[710,620])
            if c.collidepoint(mouse.get_pos()):
                screen.blit(carnetm2,[680,620])
            
        
        screen.blit(fl1,[320,630])
        if y.collidepoint(mouse.get_pos()):
            screen.blit(fl2,[320,630])
        screen.blit(fl3,[450,630])
        if y2.collidepoint(mouse.get_pos()):
            screen.blit(fl4,[450,630])
    
    #globo de texto pa 
        if direccion=="stop":
            screen.blit(globo,[820,50])
            if velx == 480:
                screen.blit(text2,(885,60))
                screen.blit(text22,(885,90))
                screen.blit(text223,(885,120))
            if vx == 480:
                screen.blit(text1,(885,60))
                screen.blit(text12,(885,90))
                screen.blit(text123,(885,120))
                
            
    
    
    
    #movimientos, esto no tocar del final que si no se chispotea
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        if y.collidepoint(mouse.get_pos()):
            direccion="izquierda"
        if y2.collidepoint(mouse.get_pos()):
            direccion="derecha"
    
    if direccion == "derecha" and lado==1:
        velx+=1
        if velx == 480:
                direccion = "stop"
    if direccion=="izquierda" and lado == 1:
        velx-=1
    
    if velx == 1420 or velx == -350:
        lado=2
    if vx==-361:
        direccion="derecha"
    
    #direccion de p2
    if direccion =="derecha" and lado==2:
        vx+=1
        if vx == 480:
            direccion = "stop"
    if direccion=="izquierda" and lado==2:
        vx-=1 
        
    if vx == 1420:
            nvl=3 
            direccion="derecha"
        
    if direccion=="izquierda" and vx==-350:
            nvl=3
            direccion = "derecha"
            
    pygame.display.flip()
    
while nvl==3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                sys.exit() 
    lima = pygame.image.load("ima/nextmes.png").convert()
    lima.set_colorkey([255,255,255])                     
    fin =Rect(1100,50,280,85)            
    m1 = letra.render(r1,1,(250,250,250))
    m2 = letra.render(r2,1,(250,250,250))
    m3 = letra.render(r3,1,(250,250,250))
    suel = letra.render(s,1,(250,250,250))
    neg = letra.render(n,1,(250,250,250))
    
    pygame.draw.rect(screen,(0,0,0),fin,0)
    screen.blit(Pasar,[0,0]) 
    screen.blit(lima,[1100,50])
     
    if velx==1420 and vx==1420:
        screen.blit(m1,(1100,250))
        screen.blit(m1,(1100,445))
        screen.blit(suel,(1000,665))
        screen.blit(neg,(1120,665))         
    if velx == 1420 and vx == -350:
        screen.blit(m1,(1100,250))
        screen.blit(m3,(1100,445)) 
        screen.blit(suel,(1000,665))           
    if velx == -350 and vx == 1420:
        screen.blit(m3,(1100,250))
        screen.blit(m1,(1100,445))
        screen.blit(suel,(980,665))
        screen.blit(neg,(1100,665))
        screen.blit(neg,(1220,665))
    if velx == -350 and vx == -350:
        screen.blit(m3,(1100,250))
        screen.blit(m3,(1100,445))
        screen.blit(suel,(980,665))
        screen.blit(neg,(1120,665)) 
        
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        if fin.collidepoint(mouse.get_pos()):   
            velx = -340
            vx =-360
            lado = 1 
            nvl = 4    
    pygame.display.flip()
    
while nvl == 4:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                sys.exit()
                       
    nom = "Nombre:  Barbara Barria"
    ed = "Edad:  18"
    nom1 = "Nombre:  Brayan Koi"
    ed1 = "Edad:  20"
    t1 = "Buenas, Soy Brayan Koi, tengo 20"
    t12= "y vengo a repaso en ICI,asi que"
    t123= "estare una hora aca."
    t2 = "Buenas, Soy Barbara Barria, tengo 18"
    t22= "y vengo a la prueba de ICINF,asi que"
    t223= "estare unas 3 horas aca."
    text1 = letra1.render(t1,1,(0,0,0))
    text12 = letra1.render(t12,1,(0,0,0))
    text123 = letra1.render(t123,1,(0,0,0))
    text2 = letra1.render(t2,1,(0,0,0))
    text22 = letra1.render(t22,1,(0,0,0))
    text223 = letra1.render(t223,1,(0,0,0))
    nombre = letra1.render(nom,1,(0,0,0))
    edad = letra1.render(ed,1,(0,0,0))
    nombre1 = letra1.render(nom1,1,(0,0,0))
    edad1 = letra1.render(ed1,1,(0,0,0))
    
    pd = "NO DEJAR PASAR A PERSONAS" 
    p1 = "DE 20 AÑOS"
    PD = letra1.render(pd,1,(0,0,0))
    PD1 = letra1.render(p1,1,(0,0,0))
    
    ccara = pygame.image.load("ima/chicacara1.png").convert()
    ccara1 = pygame.image.load("ima/carachico1.png").convert()
    Pj4 = pygame.image.load("ima/P4.png").convert()
    Pj4.set_colorkey([255,255,255])
    P3 = pygame.image.load("ima/P3.png").convert()
    P3.set_colorkey([246,246,246]) 
    
    
    pygame.draw.rect(screen,(0,0,0),y,0)
    pygame.draw.rect(screen,(0,0,0),y2,0)
    pygame.draw.rect(screen,(255,255,255),Coso,0)       
    screen.blit(Fondo, [0,0])  
    screen.blit(P3,[velx,vely+72])

    if lado == 2 and nvl==4:
        vy=22
        screen.blit(Pj4,[vx,vy])
   
    #para mouse   
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        if Coso.collidepoint(mouse.get_pos()):
            click=1
        if x.collidepoint(mouse.get_pos()):
            click=0
        if c.collidepoint(mouse.get_pos()):
            click=2
        if x2.collidepoint(mouse.get_pos()):
            click=0
    else:
        if click == 1:
            pygame.draw.rect(screen,(0,0,0),x,0)
            screen.blit(lista1,[100,100])
            screen.blit(PD,(110,300))
            screen.blit(PD1,(110,330))
        if Coso.collidepoint(mouse.get_pos()):
            if click==0:
             screen.blit(oja2,[50,650])
        else:
            if click ==0:
             screen.blit(oja,[50,730]) 
        if click ==2:
            pygame.draw.rect(screen,(0,0,0),x2,0)
            screen.blit(carnetG,[620,400])
            if velx==480:
                screen.blit(nombre,[855,540])
                screen.blit(edad,[855,570])
                screen.blit(ccara,[657,485])
            else:
                screen.blit(nombre1,[855,540])
                screen.blit(edad1,[855,570])
                screen.blit(ccara1,[657,485])
        
  #colocando carnet
        if direccion == "stop" and click==0:
            pygame.draw.rect(screen,(0,0,0),c,0)
            screen.blit(carnetm,[710,620])
            if c.collidepoint(mouse.get_pos()):
                screen.blit(carnetm2,[680,620])
            
        
        screen.blit(fl1,[320,630])
        if y.collidepoint(mouse.get_pos()):
            screen.blit(fl2,[320,630])
        screen.blit(fl3,[450,630])
        if y2.collidepoint(mouse.get_pos()):
            screen.blit(fl4,[450,630])
    
    #globo de texto pa 
        if direccion=="stop":
            screen.blit(globo,[820,50])
            if velx == 480:
                screen.blit(text2,(885,60))
                screen.blit(text22,(885,90))
                screen.blit(text223,(885,120))
            if vx == 480:
                screen.blit(text1,(885,60))
                screen.blit(text12,(885,90))
                screen.blit(text123,(885,120))

    #movimientos, esto no tocar del final que si no se chispotea
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        if y.collidepoint(mouse.get_pos()):
            direccion="izquierda"
            if lado ==1:
                velx-=2
                if velx ==-350:
                    lado=2
        if y2.collidepoint(mouse.get_pos()):
            direccion="derecha"
    
    if direccion == "derecha" and lado==1:
        velx+=2
    if velx == 480:
        direccion = "stop"
    if direccion=="izquierda" and lado==1 :
        velx-=2
    
    if velx == 1400 or velx == -350:
        lado=2
    if vx==-360 and lado==2:
        direccion="derecha"
    
    #direccion de p2
    
    if direccion =="derecha" and lado==2:
        vx+=2
        if vx == 480:
            direccion = "stop"
    if direccion=="izquierda" and lado==2:
        vx-=2 
        
    if vx == 1420:
            nvl=5 
    if direccion=="izquierda" and vx==-350:
            nvl=5
  
    pygame.display.flip()
    
while nvl == 5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                sys.exit() 
    lima = pygame.image.load("ima/nextmes.png").convert()     
    lima.set_colorkey([255,255,255])               
    fin =Rect(1100,50,280,85)            
    m1 = letra.render(r1,1,(250,250,250))
    m2 = letra.render(r2,1,(250,250,250))
    m3 = letra.render(r3,1,(250,250,250))
    suel = letra.render(s,1,(250,250,250))
    neg = letra.render(n,1,(250,250,250))
    
    pygame.draw.rect(screen,(0,0,0),fin,0)
    screen.blit(pasar2,[0,0]) 
    screen.blit(lima,[1100,50])
     
    if velx==1400 and vx==1420:
        screen.blit(m1,(1100,250))
        screen.blit(m1,(1100,445))
        screen.blit(suel,(1000,665))
        screen.blit(neg,(1120,665))         
    if velx == 1400 and vx == -350:
        screen.blit(m1,(1100,250))
        screen.blit(m3,(1100,445)) 
        screen.blit(suel,(1000,665))           
    if velx == -350 and vx == 1420:
        screen.blit(m3,(1100,250))
        screen.blit(m1,(1100,445))
        screen.blit(suel,(980,665))
        screen.blit(neg,(1100,665))
        screen.blit(neg,(1220,665))
    if velx == -350 and vx == -350:
        screen.blit(m3,(1100,250))
        screen.blit(m3,(1100,445))
        screen.blit(suel,(980,665))
        screen.blit(neg,(1120,665))
        
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        if fin.collidepoint(mouse.get_pos()):   
            velx = -340
            vx =-360
            lado = 1 
            nvl = 6    
    pygame.display.flip()
    
while nvl==6:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                sys.exit() 
    finalpa = pygame.image.load("ima/final.png").convert()
    screen.blit(finalpa,(0,0))
    
    pygame.display.flip()