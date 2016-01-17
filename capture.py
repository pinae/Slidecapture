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
        self.mode = "normal"
        self.year = "2016"
        self.month = "01"
        self.tag = "Test"

    def display_photo(self):
        image = pygame.image.load("test.jpg")
        image_width = min(round(self.display_surface.get_height()/image.get_height()*image.get_width()),
                          self.display_surface.get_width())
        image_height = min(round(self.display_surface.get_width()/image.get_width()*image.get_height()),
                           self.display_surface.get_height())
        resized_image = pygame.transform.smoothscale(image, (image_width, image_height))
        self.display_surface.blit(resized_image, (0, 0))
        self.render_text()
        pygame.display.update()

    def render_text(self):
        font_size = 20
        font = pygame.font.SysFont("Courier", font_size, bold=True, italic=False)
        if self.mode == "year":
            font_color = (180, 255, 180)
        else:
            font_color = (255, 255, 255)
        font_surface = font.render(self.year, True, font_color, (0, 0, 0))
        self.display_surface.blit(font_surface, (5, self.display_surface.get_height()-font_size-5))
        if self.mode == "month":
            font_color = (180, 255, 180)
        else:
            font_color = (255, 255, 255)
        font_surface = font.render(self.month, True, font_color, (0, 0, 0))
        self.display_surface.blit(font_surface, (70, self.display_surface.get_height()-font_size-5))
        if self.mode == "tag":
            font_color = (180, 255, 180)
        else:
            font_color = (255, 255, 255)
        font_surface = font.render(self.tag, True, font_color, (0, 0, 0))
        self.display_surface.blit(font_surface, (110, self.display_surface.get_height()-font_size-5))

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                else:
                    print(pygame.key.name(event.key))


if __name__ == "__main__":
    capturer = Capturer()
    while True:
        capturer.display_photo()
        capturer.handle_inputs()
