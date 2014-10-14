#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

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
    if var.capitalize() ==  NOTES[prev_note]:
        print "%sDoğru%s" % (bcolors.OKGREEN, bcolors.ENDC)
    else:
        print "%sYanlış, Doğrusu: %s%s%s" % (bcolors.FAIL, bcolors.WARNING, NOTES[prev_note], bcolors.ENDC)

    var = raw_input("Sonraki Nota Nedir: ")
    if var.capitalize() ==  NOTES[next_note]:
        print "%sDoğru%s" % (bcolors.OKGREEN, bcolors.ENDC)
    else:
        print "%sYanlış, Doğrusu: %s%s%s" % (bcolors.FAIL, bcolors.WARNING, NOTES[next_note], bcolors.ENDC)

if __name__ == '__main__':
    for i in range(10):
        lets_the_game_begin()
        print "-------------------\n"
