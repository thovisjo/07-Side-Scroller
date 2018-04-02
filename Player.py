#!/usr/bin/python
import pygame
from Color import Color

class Player(pygame.sprite.Sprite):
	def __init__(self,position,size,gravity,friction):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill(Color.green_5)
		self.rect = self.image.get_rect()
		(self.rect.x,self.rect.y) = position

		(self.dx,self.dy) = (0,0)
		self.ramp_up = 1
		self.max_dx = 5

		self.gravity = gravity
		self.friction = friction
		
		self.on_ground = False
	
	def get_position(self):
		return (self.rect.x,self.rect.y)
	
	def move(self,direction):
		if abs(self.dx + (direction * self.ramp_up)) <= self.max_dx:
			self.dx += direction * self.ramp_up
	
	def update(self,enemies,floors):
		self.rect.x += self.dx
		self.rect.y += self.dy
		if self.dx > 0:
			self.dx -= self.friction
			self.dx = max(self.dx,0)
		elif self.dx < 0:
			self.dx += self.friction
			self.dx = min(self.dx,0)
		if not self.on_ground:
			self.dy += self.gravity
		if self.rect.x <= 0:
			self.rect.x = 0
		self.on_ground = False
		(pl,pr,pt,pb) = (self.rect.left,self.rect.right,self.rect.top,self.rect.bottom)
		for f in floors:
			(fl,fr,ft,fb,fc) = (f.rect.left,f.rect.right,f.rect.top,f.rect.bottom,f.rect.centery)
			if (pl >= fl and pl <= fr) or (pr >= fl and pr <= fr):
				if pb >= ft - 1 and pb <= fc:
					self.on_ground = True
					self.rect.bottom = ft - 1
				if pt <= fb + 1 and pt >= fc:
					self.rect.top = fb + 1
