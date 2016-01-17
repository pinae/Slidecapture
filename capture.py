#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
import pygame
import sys, os

shifted = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'H',
    'i': 'I',
    'j': 'J',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'n': 'N',
    'o': 'O',
    'p': 'P',
    'q': 'Q',
    'r': 'R',
    's': 'S',
    't': 'T',
    'u': 'U',
    'v': 'V',
    'w': 'W',
    'x': 'X',
    'y': 'Y',
    'z': 'Z',
    '0': '=',
    '1': '!',
    '2': '"',
    '3': '§',
    '4': '$',
    '5': '%',
    '6': '&',
    '7': '/',
    '8': '(',
    '9': ')',
    '<': '>',
    ',': ';',
    '.': ':',
    '-': '_',
    '#': "'",
    '+': '*',
    'ö': 'Ö',
    'ä': 'Ä',
    'ü': 'Ü',
    'ß': '?'
}


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
        self.shifted = False

    def display_photo(self):
        self.display_surface.fill((0, 0, 0))
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
            font_color = (0, 255, 0)
        else:
            font_color = (255, 255, 255)
        font_surface = font.render(self.year, True, font_color, (0, 0, 0))
        self.display_surface.blit(font_surface, (5, self.display_surface.get_height()-font_size-5))
        if self.mode == "month":
            font_color = (0, 255, 0)
        else:
            font_color = (255, 255, 255)
        font_surface = font.render(self.month, True, font_color, (0, 0, 0))
        self.display_surface.blit(font_surface, (70, self.display_surface.get_height()-font_size-5))
        if self.mode == "tag":
            font_color = (0, 255, 0)
        else:
            font_color = (255, 255, 255)
        font_surface = font.render(self.tag, True, font_color, (0, 0, 0))
        self.display_surface.blit(font_surface, (115, self.display_surface.get_height()-font_size-5))

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                    self.shifted = True
                if self.mode == "normal":
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                    elif event.key == pygame.K_t:
                        self.mode = "tag"
                    elif event.key == pygame.K_j:
                        self.mode = "year"
                    elif event.key == pygame.K_m:
                        self.mode = "month"
                elif self.mode == "year":
                    if event.key in [pygame.K_ESCAPE, pygame.K_RETURN]:
                        self.mode = "normal"
                    elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                       pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        self.year += pygame.key.name(event.key)
                    elif event.key == pygame.K_BACKSPACE:
                        self.year = self.year[:-1]
                elif self.mode == "month":
                    if event.key in [pygame.K_ESCAPE, pygame.K_RETURN]:
                        self.mode = "normal"
                    elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                       pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        self.month += pygame.key.name(event.key)
                    elif event.key == pygame.K_BACKSPACE:
                        self.month = self.month[:-1]
                elif self.mode == "tag":
                    if event.key in [pygame.K_ESCAPE, pygame.K_RETURN]:
                        self.mode = "normal"
                    elif event.key == pygame.K_SPACE:
                        self.tag += " "
                    elif chr(event.key) in shifted.keys():
                        if self.shifted:
                            self.tag += shifted[chr(event.key)]
                        else:
                            self.tag += chr(event.key)
                    elif event.key == pygame.K_BACKSPACE:
                        self.tag = self.tag[:-1]
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                    self.shifted = False


if __name__ == "__main__":
    capturer = Capturer()
    while True:
        capturer.display_photo()
        capturer.handle_inputs()
