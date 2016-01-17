#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
import pygame
import sys, os


class Capturer(object):
    def __init__(self):
        pygame.init()
        display_info = pygame.display.Info()
        screen_size = (display_info.current_w, display_info.current_h)
        self.display_surface = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)

    def display_photo(self):
        image = pygame.image.load("test.jpg")
        image_width = min(round(self.display_surface.get_height()/image.get_height()*image.get_width()),
                          self.display_surface.get_width())
        image_height = min(round(self.display_surface.get_width()/image.get_width()*image.get_height()),
                           self.display_surface.get_height())
        resized_image = pygame.transform.smoothscale(image, (image_width, image_height))
        self.display_surface.blit(resized_image, (0, 0))
        pygame.display.update()

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                else:
                    print(event.key)


if __name__ == "__main__":
    capturer = Capturer()
    while True:
        capturer.display_photo()
        capturer.handle_inputs()
