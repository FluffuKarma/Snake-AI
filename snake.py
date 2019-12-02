import pygame
from sys import exit
import numpy as np

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN import pygame
from sys import exit
import numpy as np
import time

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [400, 300]

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

sizeOfTile=20

posX=int((size[0]/sizeOfTile)/2)
posY=int((size[1]/sizeOfTile)/2)

pos=[[posX,posY]]

direction=[0,1]

counter=0
inverseFps=150

manualMode=True

food=[0,0]

foodEaten=True

#excludes number in random
def foodPosition(pos):
	print(pos)
	print([a[0] for a in pos])
	possible_x=[i for i in range(0, int(size[0]/sizeOfTile)) if i not in [a[0] for a in pos]]
	possible_y=[i for i in range(0, int(size[1]/sizeOfTile)) if i not in [a[1] for a in pos]]
	
	if possible_x!=[]:x=np.random.choice(possible_x)
	if possible_y!=[]:y=np.random.choice(possible_y)

	return [x,y]


while 1:

	dt=clock.tick(inverseFps)

	#print(dt)
	#print(counter)

	##food eating code

	print(pos[0], food)

	if np.array_equal(pos[0],food):
		foodEaten=True
		pos=np.append(pos, [pos[-1]], axis=0)

	if foodEaten==True:
		food=foodPosition(pos)
		foodEaten=False

	##################


	##Draw screen, map, snake and food

	screen.fill(WHITE)


	for j in range(int(size[1]/sizeOfTile)):
		pygame.draw.line(screen, BLACK, [0,int(sizeOfTile*j)], [size[0], int(sizeOfTile*j)])

	for i in range(int(size[0]/sizeOfTile)):
		pygame.draw.line(screen, BLACK, [int(sizeOfTile*i),0], [int(sizeOfTile*i),size[0]])


	for i in range(len(pos)):
		pygame.draw.rect(screen, GREEN, [pos[i][0]*sizeOfTile,pos[i][1]*sizeOfTile,sizeOfTile,sizeOfTile])

	pygame.draw.rect(screen, RED, [food[0]*sizeOfTile, food[1]*sizeOfTile, sizeOfTile, sizeOfTile])

	##################################


	##FPS equalizer

	if counter>=inverseFps/dt:

		pos_placeholder=[[0]]

		for i in range(len(pos)-1):
			pos_placeholder.append(pos[i])
		pos_placeholder[0]=np.add(pos[0],direction)
		#print(pos_placeholder)
		pos=pos_placeholder

		counter=0

	###############

	#print(pos)

	##event manager

	for ev in pygame.event.get():
		if ev.type == pygame.KEYDOWN and manualMode==True:

			if ev.key == pygame.K_w:
				direction=[0,-1]
			if ev.key == pygame.K_a:
				direction=[-1,0]
			if ev.key == pygame.K_d:
				direction=[1,0]
			if ev.key == pygame.K_s:
				direction=[0,1]
			if ev.key == pygame.K_n:
				#print( [[pos[-1][0]-(direction[0]), pos[-1][1]-(direction[1])]])
				pos=np.append(pos, [pos[-1]], axis=0)
				#print(pos)

		if ev.type == pygame.QUIT:
			pygame.quit()
			exit()


	pygame.display.flip()

	counter+=1

pygame.quit()= (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [400, 300]

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

sizeOfTile=20

posX=int((size[0]/sizeOfTile)/2)*sizeOfTile
posY=int((size[1]/sizeOfTile)/2)*sizeOfTile

pos=[[posX,posY]]

direction=[0,sizeOfTile]

updateLenght=1000/2
updateCounter=0


while 1:

	updateCounter+=1

	clock.tick(10000)

	screen.fill(WHITE)


	for j in range(int(size[1]/sizeOfTile)):
		pygame.draw.line(screen, BLACK, [0,int(sizeOfTile*j)], [size[0], int(sizeOfTile*j)])

	for i in range(int(size[0]/sizeOfTile)):
		pygame.draw.line(screen, BLACK, [int(sizeOfTile*i),0], [int(sizeOfTile*i),size[0]])


	for i in range(len(pos)):
		pygame.draw.rect(screen, RED, [pos[i][0],pos[i][1],sizeOfTile,sizeOfTile])

	if updateCounter==updateLenght:
		pos=np.add(pos,direction)
		updateCounter=0

	print(pos)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		direction=[0,-sizeOfTile]
	if keys[pygame.K_a]:
		direction=[-sizeOfTile,0]
	if keys[pygame.K_d]:
		direction=[sizeOfTile,0]
	if keys[pygame.K_s]:
		direction=[0,sizeOfTile]


	pygame.display.flip()

    #if :
    #	break
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

pygame.quit()
