import pygame ,sys
import time
import random
pygame.init()

clock=pygame.time.Clock()

# Culori
alb=(255,255,255)
negru=(0,0,0)
rosu=(255,0,0)
gri=(192,192,192)
verde=(0,153,0)
galben=(255,249,186)
albastru=(0,0,204)
gri_deschis=(224,224,224)

nr_blocuri=150

chenar_albastru=(153,255,255)
chenar_verde=(153,255,204)

caracterWidth=50
caracterHeight=50

initialX=60
initialY=60


# Dimensiune display de joc
width=960
height=840
# Dimensiune display total
full_width=1200
full_height=960
Display=pygame.display.set_mode((full_width,full_height))


# Dimensiuni blocuri :
bloc_size=60

# Sunete :
explosion_sound=pygame.mixer.Sound("D:\Practica\Resurse_joc\explozie.wav")
life_sound=pygame.mixer.Sound(r'D:\Practica\Resurse_joc\viata.wav')
attack_sound=pygame.mixer.Sound(r'D:\Practica\Resurse_joc\atac.wav')
bomb_timer=pygame.mixer.Sound(r'D:\Practica\Resurse_joc\timp_bomba.wav')




# Titlu si iconita
pygame.display.set_caption("Bomberman")
icon=pygame.image.load('D:\Practica\Resurse_joc\iconita.png')
pygame.display.set_icon(icon)

# Caractere
imagineCaracter1=pygame.image.load('D:\Practica\Resurse_joc\Bomberman_caracter1.gif')
imagineCaracter2=pygame.image.load('D:\Practica\Resurse_joc\Bomberman_caracter4.gif')



def caracter1(x,y):
    Display.blit(imagineCaracter1,(x,y))


def caracter2(x,y):
    Display.blit(imagineCaracter2,(x,y))

start_ticks=pygame.time.get_ticks()



bonus_dimension=40


vectorX=[]
vectorY=[]

vector_indestructibilX=[]
vector_indestructibilY=[]

vector_sfarsit=[]
vector_sfarsit2=[]
vector_sfarsit3=[]



def generare_blocuri_random():
    
    for i in range(0,nr_blocuri):

        randomBlocX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)
        randomBlocY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)

        while randomBlocX<bloc_size*3 and randomBlocY<bloc_size*3:
            randomBlocX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)
            randomBlocY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)

        while randomBlocX>=width-bloc_size*3 and randomBlocY>=height-bloc_size*3:
            randomBlocX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)
            randomBlocY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)


        if randomBlocX>=width-3*bloc_size:
            if randomBlocY>=height-3*bloc_size:
                randomBlocX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)
                randomBlocY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)

        if randomBlocY>=height-3*bloc_size:
            if randomBlocX>=width-3*bloc_size:
                randomBlocX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)
                randomBlocY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)

        vectorX.append(randomBlocX)
        vectorY.append(randomBlocY)

        if i>0:
            while randomBlocX==vectorX[i] and randomBlocY==vectorY[i]:
                randomBlocX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)
                randomBlocY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)

            


def desenare_limite_laterale():
    
        i=0 
        while i<=900 :
            pygame.draw.rect(Display,chenar_verde,[i,0,bloc_size,bloc_size])
            pygame.draw.rect(Display,chenar_verde,[i,height,bloc_size,bloc_size])
            i+=bloc_size
            pygame.draw.rect(Display,chenar_albastru,[i,0,bloc_size,bloc_size])
            pygame.draw.rect(Display,chenar_albastru,[i,height,bloc_size,bloc_size])
            i+=bloc_size
            

        j=0
        while j<=720:
            pygame.draw.rect(Display,chenar_verde,[0,j,bloc_size,bloc_size])
            pygame.draw.rect(Display,chenar_verde,[width,j,bloc_size,bloc_size])
            j+=bloc_size
            pygame.draw.rect(Display,chenar_albastru,[0,j,bloc_size,bloc_size])
            pygame.draw.rect(Display,chenar_albastru,[width,j,bloc_size,bloc_size])
            j+=bloc_size
        pygame.draw.rect(Display,chenar_verde,[width,height,bloc_size,bloc_size])

# Pauza 
def pauza():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    paused=False

                elif event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        Display.fill(alb)
        mesaj_pe_ecran("Paused",negru,-100,"large")
        mesaj_pe_ecran("Press SPACE to continue or ESC to exit",negru,100,"medium")
        pygame.display.update()
        clock.tick(5)



    ###### Rezolva cu scorul dupa ce adaugi bombele si blocurile !!!!!!!!!!!!!111
# Score
def score(score):
    text.smallfont.render("Score: "+str(score),True,negru)
    Display.blit(text,[full_width-120,60])
    


# Mesaje pe ecran
smallfont=pygame.font.SysFont("comicsansms",20)
mediumfont=pygame.font.SysFont("comicsansms",40)
largefont=pygame.font.SysFont("comicsansms",70)




def start_screen():
    intro =True

    while intro:



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_TAB:
                    intro =False
                    
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key==pygame.K_c:
                    
                    Display.fill(alb)
                    mesaj_pe_ecran("Player1 :",verde,-350,"large")
                    mesaj_pe_ecran("Move left :      left arrow",gri,-250,"medium")
                    mesaj_pe_ecran("Move right :     right arrow",gri,-200,"medium")
                    mesaj_pe_ecran("Move up :        up arrow",gri,-150,"medium")
                    mesaj_pe_ecran("Move down :      down arrow",gri,-100,"medium")
                    mesaj_pe_ecran("Place bomb :      L",rosu,-50,"medium")

                    mesaj_pe_ecran("Player2 :",verde,50,"large")
                    mesaj_pe_ecran("Move left :      a",gri,150,"medium")
                    mesaj_pe_ecran("Move right :     d",gri,200,"medium")
                    mesaj_pe_ecran("Move up :        w",gri,250,"medium")
                    mesaj_pe_ecran("Move down :      s",gri,300,"medium")
                    mesaj_pe_ecran("Place bomb:      E",rosu,350,"medium")

                    mesaj_pe_ecran("Red block = life regeneration                                                           "
                                   ,rosu,500,"small")
                    mesaj_pe_ecran("                                                           Blue block = attack increase",
                                   albastru,500,"small")

                    pygame.display.update()
                    clock.tick(0.2)
                    

        Display.fill(alb)
        mesaj_pe_ecran("    Welcome to Bomberman",
                       verde,
                       -200,
                       "large")
        mesaj_pe_ecran("    The objective of the game is to KILL your opponents",
                       gri,
                       -120,
                       "small")
        mesaj_pe_ecran("    Press TAB to play or ESC to quit",
                       negru,
                       0,
                       "medium")
        mesaj_pe_ecran("    Press C to see the controls",
                       negru,
                       100,
                       "medium")

        desenare_limite_laterale()

        

        pygame.display.update()
        clock.tick(4)


def text_objects(text,culoare,size):
    if size =="small":
        textSurface=smallfont.render(text,True,culoare)
    elif size =="medium":
        textSurface=mediumfont.render(text,True,culoare)
    elif size =="large":
        textSurface=largefont.render(text,True,culoare)
    return textSurface , textSurface.get_rect()

def mesaj_pe_ecran(mesaj,culoare,coordonataY=0,size="small"):
    textSurface , textRectangle = text_objects(mesaj,culoare,size)
    textRectangle.center = (width/2),(height/2)+coordonataY
    Display.blit(textSurface,textRectangle)



def plasare_bomba(caracter1_x,caracter1_y):
     pygame.draw.rect(Display,verde,[caracter1_x,caracter1_y,30,30])
     pygame.display.update()
     clock.tick(0.5)
    
# Main ul jocului

def gameLoop():
    gameExit=False
    gameOverRosu=False
    gameOverAlb=False


    caracter1_x=60
    caracter1_y=60
    caracter1_x_miscare=0
    caracter1_y_miscare=0

    caracter2_x=900
    caracter2_y=780
    caracter2_x_miscare=0
    caracter2_y_miscare=0


    # Bonusuri
    randomViataX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)+10
    randomViataY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)+10

    randomAtacX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)+10
    randomAtacY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)+10


    while not gameExit:
        while gameOverRosu==True:
            Display.fill(alb)

            mesaj_pe_ecran("Game over",
                           rosu,
                           -50,
                           size="large")
            mesaj_pe_ecran("Press ESC to exit.",
                           negru,
                           50,
                           size="medium")
            mesaj_pe_ecran("Red LOST",
                           verde,
                           150,
                           size="medium")
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        gameExit=True
                        gameOverRosu=False

        while gameOverAlb==True:
            Display.fill(alb)

            mesaj_pe_ecran("Game over",
                           rosu,
                           -50,
                           size="large")
            mesaj_pe_ecran("Press ESC to exit.",
                           negru,
                           50,
                           size="medium")
            mesaj_pe_ecran("White LOST",
                           verde,
                           150,
                           size="medium")
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        gameExit=True
                        gameOverAlb=False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True

            # Miscare caractere

            if event.type==pygame.KEYDOWN:

                # Caracter1

                if event.key==pygame.K_LEFT :
                    caracter1_x_miscare-=1
                elif event.key==pygame.K_RIGHT:
                    caracter1_x_miscare+=1
                elif event.key==pygame.K_UP:
                    caracter1_y_miscare-=1
                elif event.key==pygame.K_DOWN:
                    caracter1_y_miscare+=1

                # Caracter2

                if event.key==pygame.K_a:
                    caracter2_x_miscare-=1
                elif event.key==pygame.K_d:
                    caracter2_x_miscare+=1
                elif event.key==pygame.K_w:
                    caracter2_y_miscare-=1
                elif event.key==pygame.K_s:
                    caracter2_y_miscare+=1

                # Pauza
                if event.key==pygame.K_SPACE:
                    pauza()

                # Plasare bomba : 

                if event.key==pygame.K_m:
                    plasare_bomba(caracter1_x,caracter1_y)
                    


            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    caracter1_x_miscare=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    caracter1_y_miscare=0

                if event.key==pygame.K_a or event.key==pygame.K_d:
                    caracter2_x_miscare=0
                if event.key==pygame.K_w or event.key==pygame.K_s:
                    caracter2_y_miscare=0

        # Limite laterale

        if caracter1_x<=bloc_size:
            caracter1_x=bloc_size
        if caracter1_x>=width-caracterWidth:
            caracter1_x=width-caracterWidth
        if caracter1_y<=bloc_size:
            caracter1_y=bloc_size
        if caracter1_y>=height-caracterHeight:
            caracter1_y=height-caracterHeight

        if caracter2_x<=bloc_size:
            caracter2_x=bloc_size
        if caracter2_x>=width-caracterWidth:
            caracter2_x=width-caracterWidth
        if caracter2_y<=bloc_size:
            caracter2_y=bloc_size
        if caracter2_y>=height-caracterHeight:
            caracter2_y=height-caracterHeight


        # Idee pt terminarea jocului
        if caracter2_x<=500:
            gameOverAlb=True


        Display.fill(alb)

        # Bonusuri

        bloc_viata=pygame.Rect(randomViataX,randomViataY,bonus_dimension,bonus_dimension)
        bloc_atac=pygame.Rect(randomAtacX,randomAtacY,bonus_dimension,bonus_dimension)

        pygame.draw.rect(Display,rosu,bloc_viata)
        pygame.draw.rect(Display,albastru,bloc_atac)

        
        # Miscare caractere
        

        caracter1_x+=caracter1_x_miscare
        caracter1_y+=caracter1_y_miscare
        moving_C1=pygame.Rect(caracter1_x,caracter1_y,caracterWidth,caracterHeight)
        pygame.draw.rect(Display,galben,moving_C1)
        caracter1(caracter1_x,caracter1_y)
    
        caracter2_x+=caracter2_x_miscare
        caracter2_y+=caracter2_y_miscare
        moving_C2=pygame.Rect(caracter2_x,caracter2_y,caracterWidth,caracterHeight)
        pygame.draw.rect(Display,galben,moving_C2)
        caracter2(caracter2_x,caracter2_y)

        clock.tick(250)
        
    
        # Limite laterale
        desenare_limite_laterale() 


        

        
            
        # Blocuri indestructibile si destructibile
        collision_tolerance1=10

        #generare_blocuri_random()
        #for i in range(0,nr_blocuri):
         #   bloc_destructibil=pygame.draw.rect(Display,gri,[vectorX[i],vectorY[i],bloc_size,bloc_size])
          #  if moving_C1.colliderect(bloc_destructibil):
           #         if abs(bloc_destructibil.top-moving_C1.bottom) <collision_tolerance1:
            #            caracter1_y_miscare=-0.015
             #       if abs(bloc_destructibil.bottom-moving_C1.top) <collision_tolerance1:
              #          caracter1_y_miscare=+0.015
               #     if abs(bloc_destructibil.right-moving_C1.left) <collision_tolerance1:
                #        caracter1_x_miscare=+0.015
                 #   if abs(bloc_destructibil.left-moving_C1.right) <collision_tolerance1:
                  #      caracter1_x_miscare=-0.015

          #  if moving_C2.colliderect(bloc_destructibil):
           #         if abs(bloc_destructibil.top-moving_C2.bottom) <collision_tolerance1:
            #            caracter2_y_miscare=-0.015
             #       if abs(bloc_destructibil.bottom-moving_C2.top) <collision_tolerance1:
              #          caracter2_y_miscare=+0.015
               #     if abs(bloc_destructibil.right-moving_C2.left) <collision_tolerance1:
                #        caracter2_x_miscare=+0.015
                 #   if abs(bloc_destructibil.left-moving_C2.right) <collision_tolerance1:
                  #      caracter2_x_miscare=-0.015




        collision_tolerance1=10
        
        for i in range(120,width,120):
            for j in range(120,height,120):
                bloc_indestructibil=pygame.draw.rect(Display,negru,[i,j,bloc_size,bloc_size])
                vector_indestructibilX.append(i)
                vector_indestructibilY.append(j)
                

                if randomViataX==i+10 and randomViataY==j+10:
                    randomViataX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)+10
                    randomViataY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)+10

                if randomAtacX==i+10 and randomAtacY==j+10:
                    randomAtacX= (round(random.randrange(bloc_size,width-bloc_size)/60.0)*60.0)+10
                    randomAtacY= (round(random.randrange(bloc_size,height-bloc_size)/60.0)*60.0)+10

                if moving_C1.colliderect(bloc_indestructibil):
                    if abs(bloc_indestructibil.top-moving_C1.bottom) <collision_tolerance1:
                        caracter1_y_miscare=-0.015
                    if abs(bloc_indestructibil.bottom-moving_C1.top) <collision_tolerance1:
                        caracter1_y_miscare=+0.015
                    if abs(bloc_indestructibil.right-moving_C1.left) <collision_tolerance1:
                        caracter1_x_miscare=+0.015
                    if abs(bloc_indestructibil.left-moving_C1.right) <collision_tolerance1:
                        caracter1_x_miscare=-0.015

                if moving_C2.colliderect(bloc_indestructibil):
                    if abs(bloc_indestructibil.top-moving_C2.bottom) <collision_tolerance1:
                        caracter2_y_miscare=-0.015
                    if abs(bloc_indestructibil.bottom-moving_C2.top) <collision_tolerance1:
                        caracter2_y_miscare=+0.015
                    if abs(bloc_indestructibil.right-moving_C2.left) <collision_tolerance1:
                        caracter2_x_miscare=+0.015
                    if abs(bloc_indestructibil.left-moving_C2.right) <collision_tolerance1:
                        caracter2_x_miscare=-0.015


        # Bonusuri generate random
        collision_tolerance2=2

        if moving_C1.colliderect(bloc_viata):
            if abs(bloc_viata.top-moving_C1.bottom)<collision_tolerance2 or abs(bloc_viata.bottom-moving_C1.top)<collision_tolerance2 or abs(bloc_viata.right-moving_C1.left)<collision_tolerance2 or abs(bloc_viata.left-moving_C1.right)<collision_tolerance2:
                randomViataX= 10
                randomViataY= 910
                pygame.mixer.Sound.play(life_sound)

        if moving_C1.colliderect(bloc_atac):
            if abs(bloc_atac.top-moving_C1.bottom)<collision_tolerance2 or abs(bloc_atac.bottom-moving_C1.top)<collision_tolerance2 or abs(bloc_atac.right-moving_C1.left)<collision_tolerance2 or abs(bloc_atac.left-moving_C1.right)<collision_tolerance2:
                 randomAtacX= 70
                 randomAtacY= 910
                 pygame.mixer.Sound.play(attack_sound)

        if moving_C2.colliderect(bloc_viata):
            if abs(bloc_viata.top-moving_C2.bottom)<collision_tolerance2 or abs(bloc_viata.bottom-moving_C2.top)<collision_tolerance2 or abs(bloc_viata.right-moving_C2.left)<collision_tolerance2 or abs(bloc_viata.left-moving_C2.right)<collision_tolerance2:
                 randomViataX= 10
                 randomViataY= 910
                 pygame.mixer.Sound.play(life_sound)

        if moving_C2.colliderect(bloc_atac):
            if abs(bloc_atac.top-moving_C2.bottom)<collision_tolerance2 or abs(bloc_atac.bottom-moving_C2.top)<collision_tolerance2 or abs(bloc_atac.right-moving_C2.left)<collision_tolerance2 or abs(bloc_atac.left-moving_C2.right)<collision_tolerance2:
                 randomAtacX= 70
                 randomAtacY= 910
                 pygame.mixer.Sound.play(attack_sound)

        seconds=(pygame.time.get_ticks()-start_ticks)/1000

        # Umplere arena pentru sfarsitul jocului (dupa un timp anume)

        ### INITIALIZEAZA SI PENTRU caracter2 !!!!!!!!!!!!!!!!!!!

        if seconds>=30:
            # latura stanga
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[initialX,initialY,bloc_size,height-bloc_size])
            vector_sfarsit.append(bloc_indestructibil2)

                
            if caracter1_y>=bloc_size and caracter1_y<=height and caracter1_x<=2*bloc_size-2:
                gameOverRosu=True

            # latura sus
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[2*initialX,initialY,width-2*bloc_size,bloc_size])
            vector_sfarsit.append(bloc_indestructibil2)

            
            if caracter1_x>=bloc_size and caracter1_x<=width and caracter1_y<=2*bloc_size-2:
                gameOverRosu=True

            # latura dreapta
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[width-bloc_size,2*initialY,bloc_size,height-2*bloc_size])
            vector_sfarsit.append(bloc_indestructibil2)

          
            if caracter1_y>=2*bloc_size and caracter1_y<=height and caracter1_x>=width-bloc_size+2:
                gameOverRosu=True
            
            # latura jos
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[2*initialX,height-bloc_size,width-2*bloc_size,bloc_size])
            vector_sfarsit.append(bloc_indestructibil2)

            
            if caracter1_x>=bloc_size and caracter1_x<=width-bloc_size and caracter1_y>=height-bloc_size+2:
                gameOverRosu=True


            for i in range(0,4):
                if moving_C1.colliderect(vector_sfarsit[i]):
                    if abs(vector_sfarsit[i].top-moving_C1.bottom) <collision_tolerance1:
                        caracter1_y_miscare=-0.015
                    if abs(vector_sfarsit[i].bottom-moving_C1.top) <collision_tolerance1:
                        caracter1_y_miscare=+0.015
                    if abs(vector_sfarsit[i].right-moving_C1.left) <collision_tolerance1:
                        caracter1_x_miscare=+0.015
                    if abs(vector_sfarsit[i].left-moving_C1.right) <collision_tolerance1:
                        caracter1_x_miscare=-0.015

        if seconds>=40:
            # latura stanga
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[2*initialX,2*initialY,bloc_size,height-3*bloc_size])
            vector_sfarsit2.append(bloc_indestructibil2)

                
            if caracter1_y>=2*bloc_size and caracter1_y<=height-bloc_size and caracter1_x<=3*bloc_size-2:
                gameOverRosu=True

            # latura sus
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[3*initialX,2*initialY,width-4*bloc_size,bloc_size])
            vector_sfarsit2.append(bloc_indestructibil2)

            
            if caracter1_x>=2*bloc_size and caracter1_x<=width-bloc_size and caracter1_y<=(3*bloc_size)-2:
                gameOverRosu=True

            # latura dreapta
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[width-2*bloc_size,3*initialY,bloc_size,height-4*bloc_size])
            vector_sfarsit2.append(bloc_indestructibil2)

          
            if caracter1_y>=3*bloc_size and caracter1_y<=height-bloc_size and caracter1_x>=width-2*bloc_size-48:
                gameOverRosu=True
            
            # latura jos
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[3*initialX,height-2*bloc_size,width-4*bloc_size,bloc_size])
            vector_sfarsit2.append(bloc_indestructibil2)

            
            if caracter1_x>=2*bloc_size and caracter1_x<=width-bloc_size and caracter1_y>=height-2*bloc_size-48:
                gameOverRosu=True


            for i in range(0,4):
                if moving_C1.colliderect(vector_sfarsit2[i]):
                    if abs(vector_sfarsit2[i].top-moving_C1.bottom) <collision_tolerance1:
                        caracter1_y_miscare=-0.015
                    if abs(vector_sfarsit2[i].bottom-moving_C1.top) <collision_tolerance1:
                        caracter1_y_miscare=+0.015
                    if abs(vector_sfarsit2[i].right-moving_C1.left) <collision_tolerance1:
                        caracter1_x_miscare=+0.015
                    if abs(vector_sfarsit2[i].left-moving_C1.right) <collision_tolerance1:
                        caracter1_x_miscare=-0.015

        if seconds>=50:
            # latura stanga
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[3*initialX,3*initialY,bloc_size,height-5*bloc_size])
            vector_sfarsit3.append(bloc_indestructibil2)

                
            if caracter1_y>=3*bloc_size and caracter1_y<=height-2*bloc_size and caracter1_x<=4*bloc_size-2:
                gameOverRosu=True

            # latura sus
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[4*initialX,3*initialY,width-6*bloc_size,bloc_size])
            vector_sfarsit3.append(bloc_indestructibil2)

            
            if caracter1_x>=3*bloc_size and caracter1_x<=width-2*bloc_size and caracter1_y<=(4*bloc_size)-2:
                gameOverRosu=True

            # latura dreapta
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[width-3*bloc_size,4*initialY,bloc_size,height-6*bloc_size])
            vector_sfarsit3.append(bloc_indestructibil2)

          
            if caracter1_y>=4*bloc_size and caracter1_y<=height-2*bloc_size and caracter1_x>=width-3*bloc_size-48:
                gameOverRosu=True
            
            # latura jos
            bloc_indestructibil2=pygame.draw.rect(Display,gri_deschis,[4*initialX,height-3*bloc_size,width-6*bloc_size,bloc_size])
            vector_sfarsit3.append(bloc_indestructibil2)

            
            if caracter1_x>=3*bloc_size and caracter1_x<=width-2*bloc_size and caracter1_y>=height-3*bloc_size-48:
                gameOverRosu=True



            for i in range(0,4):
                if moving_C1.colliderect(vector_sfarsit3[i]):
                    if abs(vector_sfarsit3[i].top-moving_C1.bottom) <collision_tolerance1:
                        caracter1_y_miscare=-0.015
                    if abs(vector_sfarsit3[i].bottom-moving_C1.top) <collision_tolerance1:
                        caracter1_y_miscare=+0.015
                    if abs(vector_sfarsit3[i].right-moving_C1.left) <collision_tolerance1:
                        caracter1_x_miscare=+0.015
                    if abs(vector_sfarsit3[i].left-moving_C1.right) <collision_tolerance1:
                        caracter1_x_miscare=-0.015

        pygame.display.update()


    
    pygame.quit()
    quit()

start_screen()
gameLoop()

