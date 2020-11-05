#!/usr/bin/python3

import pygame
file = '~/emily/Project/Hozier.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
