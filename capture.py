#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
import pygame
import sys, os


def initialize():
    pygame.init()
    display_info = pygame.display.Info()
    screen_size = (display_info.current_w, display_info.current_h)
    display_surface = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
    return display_surface


def display_photo(surface):
    image = pygame.image.load("test.jpg")
    image_width = min(round(surface.get_height()/image.get_height()*image.get_width()),
                      surface.get_width())
    image_height = min(round(surface.get_width()/image.get_width()*image.get_height()),
                       surface.get_height())
    resized_image = pygame.transform.smoothscale(image, (image_width, image_height))
    surface.blit(resized_image, (0, 0))
    pygame.display.update()


def handle_inputs():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)
            else:
                print(event.key)


if __name__ == "__main__":
    display_surface = initialize()
    while True:
        display_photo(display_surface)
        handle_inputs()
