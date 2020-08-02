import pygame
import random
import sys
from sys import maxsize

class Node(object):
    def __init__(self, i_depth, i_playerNum, i_sticksRemaining, i_value = 0):
        self.i_depth = i_depth
        self.i_playerNum = i_playerNum
        self.i_sticksRemaining = i_sticksRemaining
        self.i_value = i_value
        self.children = []
        self.CreateChildren()

    def CreateChildren(self):
        if self.i_depth >= 0:
            for i in range(1, 3):
                v = self.i_sticksRemaining - i
                self.children.append( Node( self.i_depth - 1,-self.i_playerNum, v, self.RealVal(v)))
    
            
    def RealVal(self, value):
        if (value == 0):
            return maxsize * self.i_playerNum
        elif (value < 0):
            return maxsize * -self.i_playerNum
        return 0

def MinMax(node, i_depth, i_playerNum):
    if(i_depth == 0) or (abs(node.i_value) == maxsize):
        return node.i_value
    i_bestValue = maxsize * -i_playerNum

    for i in range(len(node.children)):
        child = node.children[i]
        i_val = MinMax(child, i_depth -1, -i_playerNum)
        if (abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)):
            i_bestValue = i_val
    return i_bestValue

def WinCheck(i_sticks, i_playerNum):
    if i_sticks <= 0:
        print("*"*30)
        if i_playerNum > 0:
            if i_sticks == 0:
                endscreen(0)
        else:
            if i_sticks == 0:
                endscreen(1)
        print("*"*30)
        return 0
    return 1

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def linspace(a, b, n=100):
    if n < 2:
        return b
    diff = (float(b) - a)/(n - 1)
    return [diff * i + a  for i in range(n)]

def intro():
	lbx = 200
	width = 150
	height = 75
	rbx = scw - lbx - width
	bby = sch - height - 20
	run = True
	while run:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if (lbx + width) > mouse[0] > lbx and (bby + height) > mouse[1] > bby:
					if event.button == 1:
						run = False
				elif (rbx + width) > mouse[0] > rbx and (bby + height) > mouse[1] > bby:
					sys.exit()

			win.blit(startscreen, (0, 0))
			mouse = pygame.mouse.get_pos()

			if (lbx + width) > mouse[0] > lbx and (bby + height) > mouse[1] > bby:
				pygame.draw.rect(win, (LIGHT_GREEN), (lbx, bby, width, height))
			else:
				pygame.draw.rect(win, (GREEN), (lbx, bby, width, height))

			if (rbx + width) > mouse[0] > rbx and (bby + height) > mouse[1] > bby:
				pygame.draw.rect(win, (LIGHT_RED), (rbx, bby, width, height))
			else:
				pygame.draw.rect(win, (RED), (rbx, bby, width, height))

			smallText = pygame.font.Font("freesansbold.ttf",35)
			textSurf, textRect = text_objects("Играть!", smallText)
			textRect.center = (lbx + width/2, bby + height/2)
			win.blit(textSurf, textRect)

			smallText = pygame.font.Font("freesansbold.ttf",35)
			textSurf, textRect = text_objects("Выйти", smallText)
			textRect.center = (rbx + width/2, bby + height/2)
			win.blit(textSurf, textRect)
			pygame.display.update()

def endscreen(w):
	lbx = 200
	width = 150
	height = 75
	rbx = scw - lbx - width
	bby = sch - height - 20
	run = True
	win.blit(fade, (0,0))
	while run:
		clock.tick(30)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if (lbx + width) > mouse[0] > lbx and (bby + height) > mouse[1] > bby:
					if event.button == 1:
						game()
				elif (rbx + width) > mouse[0] > rbx and (bby + height) > mouse[1] > bby:
					sys.exit()
			
			mouse = pygame.mouse.get_pos()

			if (lbx + width) > mouse[0] > lbx and (bby + height) > mouse[1] > bby:
				pygame.draw.rect(win, (LIGHT_GREEN), (lbx, bby, width, height))
			else:
				pygame.draw.rect(win, (GREEN), (lbx, bby, width, height))

			if (rbx + width) > mouse[0] > rbx and (bby + height) > mouse[1] > bby:
				pygame.draw.rect(win, (LIGHT_RED), (rbx, bby, width, height))
			else:
				pygame.draw.rect(win, (RED), (rbx, bby, width, height))

			if w == 0:
				win.blit(humanwon, (307, 50))
				smallText = pygame.font.Font("freesansbold.ttf",30)
				textSurf, textRect = text_objects("Eще раз!", smallText)
				textRect.center = (lbx + width/2, bby + height/2)
				win.blit(textSurf, textRect)
			else:
				win.blit(compwon, (307, 50))
				smallText = pygame.font.Font("freesansbold.ttf",35)
				textSurf, textRect = text_objects("Реванш!", smallText)
				textRect.center = (lbx + width/2, bby + height/2)
				win.blit(textSurf, textRect)

			smallText = pygame.font.Font("freesansbold.ttf",35)
			textSurf, textRect = text_objects("Выйти", smallText)
			textRect.center = (rbx + width/2, bby + height/2)
			win.blit(textSurf, textRect)
			pygame.display.update()

def game():
	i_stickTotal = 16
	i_depth = 10
	i_curPlayer = 1
	width = 63
	height = 215
	sbh = 70
	sbw = 140
	sbx = scw/2-sbw/2
	sby = sch-sbh*11/10
	sc = 0
	x = linspace(width/2, scw - width*3/2, i_stickTotal)
	y = []
	p = []
	for i in range(i_stickTotal):
		y.append(150)
		p.append(1)

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				for i in range(len(x)):
					if (x[i] + width) > event.pos[0] > x[i] and (y[i] + height) > event.pos[1] > y[i]:
						if event.button == 1:
							if sc < 2:
								if p[i] == 1:
									y[i] += 50 * p[i]
									p[i] *= -1
									sc += 1
								else:
									y[i] += 50 * p[i]
									p[i] *= -1
									sc -= 1
								
							else:
								if p[i] == -1:
									y[i] += 50 * p[i]
									p[i] *= -1
									sc-=1

			if event.type == pygame.MOUSEBUTTONDOWN and sc != 0:
				if (sbx + sbw) > event.pos[0] > sbx and (sby + sbh) > event.pos[1] > sby:
					if event.button == 1:
						for k in range(len(p)):
							if p[k] == -1:
								speed = 4
								while y[k] < 600:
									clock.tick(60)
									win.blit(bg, (0, 0))
									for i in range(len(x)):
										win.blit(stick, (x[i], y[i], width, height))
									y[k] += speed
									speed *=12/10
									pygame.display.update()
						i_stickTotal -= sc
						WinCheck(i_stickTotal, i_curPlayer)
						sc = 0
						am = []
						for i in range(len(x)):
							if y[i] == 150:
								am.append(i)
						i_curPlayer *= -1
						node = Node(i_depth, i_curPlayer, i_stickTotal)
						bestChoice = -100
						i_bestValue = -i_curPlayer * maxsize
						for i in range(len(node.children)):
							n_child = node.children[i]
							i_val = MinMax(n_child, i_depth, -i_curPlayer)
							if (abs(i_curPlayer * maxsize - i_bestValue)):
								i_bestValue = i_val
								bestChoice = i
						bestChoice += 1
						c_choice = bestChoice
						while c_choice > 0:
							cc = random.choice(am)
							speed = 4
							while y[cc] > -100 - height:
								clock.tick(60)
								win.blit(bg, (0, 0))
								for i in range(len(x)):
									win.blit(stick, (x[i], y[i], width, height))
								y[cc] -= speed
								speed *=12/10
								pygame.display.update()
							c_choice -= 1
							am.remove(cc)
						i_stickTotal -= bestChoice
						WinCheck(i_stickTotal, i_curPlayer)
						i_curPlayer *= -1

			mouse = pygame.mouse.get_pos()
			win.blit(bg, (0, 0))
			for i in range(len(x)):
				if (x[i] + width) > mouse[0] > x[i] and (y[i] + height) > mouse[1] > y[i]:
					if sc < 2:
						win.blit(stick, (x[i]-5, y[i]-5, width+75, height+75))
					else:
						if y[i] == 200:
							win.blit(stick, (x[i]-5, y[i]-5, width+75, height+75))
						else:
							win.blit(stick, (x[i], y[i], width, height))
				else:
					win.blit(stick, (x[i], y[i], width, height))

			if (sbx + sbw) > mouse[0] > sbx and (sby + sbh) > mouse[1] > sby:
				pygame.draw.rect(win, (LIGHT_GREEN), (sbx, sby, sbw, sbh))
			else:
				pygame.draw.rect(win, (GREEN), (sbx, sby, sbw, sbh))

			smallText = pygame.font.Font("freesansbold.ttf",30)
			textSurf, textRect = text_objects("Палочек осталось - " + str(i_stickTotal), smallText)
			textRect.center = (1000,50)
			#win.blit(textSurf, textRect)

			smallText = pygame.font.Font("freesansbold.ttf",40)
			textSurf, textRect = text_objects("Взять", smallText)
			textRect.center = ((sbx+(sbw/2)),sby+(sbh/2))
			win.blit(textSurf, textRect)
			pygame.display.update()

pygame.init()
scw = 1138
sch = 520
win = pygame.display.set_mode((scw, sch))
clock = pygame.time.Clock()
pygame.display.set_caption("Sticks Game")
stick = pygame.image.load('res/stick.png')
bg = pygame.image.load('res/background.png')
startscreen = pygame.image.load('res/startscreen.png')
compwon = pygame.image.load('res/compwon.png')
humanwon = pygame.image.load('res/humanwon.png')
fade = pygame.Surface((scw, sch))
fade.fill((0,0,0))
fade.set_alpha(150)
LIGHT_GREEN = (20, 255, 42)
GREEN = (20, 200, 40)
LIGHT_RED = (255, 10, 10)
RED = (200, 20, 20)

intro()
game()
pygame.quit()
