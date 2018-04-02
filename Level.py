import pygame
from Color import Color

class Level:
	def __init__(self,filename):
		self.block_size = (self.w,self.h) = (100,100)
		self.level = []
		self.screen_player_offset = (100,400)
		self.player_position = (0,0)
		self.enemies = []
		self.floor = []
		f = open(filename,'r')
		for l in f:
			self.level.append(l)
		if len(self.level):
			self.screen = pygame.Surface((len(self.level[0])*self.w,len(self.level)*self.h))
			self.screen.fill(Color.gray_7)
			j = 0
			for r in self.level:
				i = 0
				for c in r:
					pos = (i*self.w,j*self.h)
					if c == 'P':
						self.player_position = pos
					if c == 'E':
						self.enemies.append(pos)
					if c == '1':
						self.floor.append(pos)
					i += 1
				j += 1
		self.rect = self.screen.get_rect()
		self.master = pygame.Surface((self.rect.width,self.rect.height))
		self.master.blit(self.screen,(0,0),self.rect)
	
	def get_full_screen(self):
		self.screen.blit(self.master,(0,0),self.rect)
		return self.screen
	
	def get_player_starting_position(self):
		return self.player_position
	
	def get_enemies(self):
		return self.enemies
	
	def get_floor(self):
		return self.floor
		
	def get_screen(self):
		return self.screen
	
	def get_rect(self,dim,player):
		(ox,oy) = self.screen_player_offset
		(px,py) = player.get_position()
		(dx,dy) = dim
		rx = px - ox
		if rx < 0:
			rx = 0
		if rx + dx > self.rect.width:
			rx = self.rect.width - dx
		ry = py - oy
		if ry < 0:
			ry = 0
		if ry + dy > self.rect.height:
			ry = self.rect.height - dy
		rect = pygame.Rect(rx,ry,dx,dy)
		return rect

	def get_color(self,game_object):
		if game_object == '0':
			return Color.gray_2
		if game_object == '1':
			return Color.gray_1
		if game_object == 'P':
			return Color.green_5
		if game_object == 'E':
			return Color.red_5
		return Color.black
	
	def generate_empty_level(self,dimensions,block_size):
		(i,j) = dimensions
		(w,h) = block_size
		for k in range(j//h):
			temp = ''
			for l in range(i//w):
				temp += '0'
			print(temp)
		temp = ''
		for l in range(i//w):
			temp += '1'
		print(temp)

class Floor(pygame.sprite.Sprite):
	def __init__(self,gravity,position,size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill(Color.gray_9)
		self.rect = self.image.get_rect()
		(self.rect.x,self.rect.y) = position
		self.gravity = gravity
	
	def get_position(self):
		return (self.rect.x,self.rect.y)
	
	def update(self):
		'''
		update behavior
		'''	