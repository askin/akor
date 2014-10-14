#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

NOTES = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']

def lets_the_game_begin():
    index = int(random.random() * 70) % 7
    prev_note = index - 1
    next_note = index + 1

    if index == 0:
        prev_note = 6

    if index == 6:
        next_note = 0

    print "Nota: %s" % NOTES[index]

    var = raw_input("Önceki Nota Nedir : ")
    if var ==  NOTES[prev_note]:
        print "Doğru"
    else:
        print "Yanlış, Doğrusu: %s" % NOTES[prev_note]

    var = raw_input("Sonraki Nota Nedir: ")
    if var ==  NOTES[next_note]:
        print "Doğru"
    else:
        print "Yanlış, Doğrusu: %s" % NOTES[next_note]

if __name__ == '__main__':
    for i in range(10):
        lets_the_game_begin()
        print "-------------------\n"
