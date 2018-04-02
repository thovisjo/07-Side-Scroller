#!/usr/bin/python
import pygame
from Color import Color

class Enemy(pygame.sprite.Sprite):
	def __init__(self,gravity,position,size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill(Color.red_5)
		self.rect = self.image.get_rect()
		(self.rect.x,self.rect.y) = position
		self.gravity = gravity
	
	def get_position(self):
		return (self.rect.x,self.rect.y)
	
	def update(self):
		'''
		update behavior
		'''