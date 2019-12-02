import pygame
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

allTiles=[]
for i in range(int(size[0]/sizeOfTile)):
	for j in range(int(size[1]/sizeOfTile)):
		allTiles.append([i,j])


print(allTiles)

justAte=False

#excludes number in random
def foodPosition(pos):
	print(pos)

	allTiles_placeholder=allTiles.copy()

	print(pos)
	for i in range(len(pos)-2):
		print(allTiles_placeholder)
		print(allTiles)
		print(pos[i], i)
		try: allTiles_placeholder.remove([pos[i][0],pos[i][1]])
		except: return

	return allTiles_placeholder[np.random.randint(len(allTiles_placeholder))]


while 1:

	dt=clock.tick(inverseFps)


	##Game Logic

	print(justAte, pos)

	##checks for snake-snake contact
	if justAte==False and True in [pos[0][1]==i[1] and pos[0][0]==i[0] for i in pos[1:]] : 
		pygame.quit()
		exit()

	##################################################################

	##food eating code

	print(pos[0], food)

	if np.array_equal(pos[0],food):
		foodEaten=True
		pos=np.append(pos, [pos[-1]], axis=0)
		justAte=True

	if foodEaten==True:
		food=foodPosition(pos)
		foodEaten=False

	##################


	##FPS equalizer and movement

	if counter>=inverseFps/dt:

		pos_placeholder=[[0]]

		for i in range(len(pos)-1):
			pos_placeholder.append(pos[i])
		pos_placeholder[0]=np.add(pos[0],direction)
		#print(pos_placeholder)
		pos=pos_placeholder

		counter=0


		##justAte makes it so the game doesn't end if you get to 2 lenght, 
		##because rect 1 and 2 intercept on first growth
		if justAte==True: justAte=False

	###############



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
				justAte=True
				#print(pos)

		if ev.type == pygame.QUIT:
			pygame.quit()
			exit()


	pygame.display.flip()

	counter+=1

pygame.quit()
