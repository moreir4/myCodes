import pygame
pygame.mixer.init()
pygame.mixer.music.load('my_studies/ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()