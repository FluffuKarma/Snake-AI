import pygame
from sys import exit
import numpy as np

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