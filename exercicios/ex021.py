# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame
import time

pygame.init()
pygame.mixer.music.load('exercicios/ex021.mp3')
pygame.mixer.music.play()

time.sleep(10)