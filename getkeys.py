# -*- coding: utf-8 -*-
# Citation: Box Of Hats (https://github.com/Box-Of-Hats )
import win32api as wapi
import win32con as wcon
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    if wapi.GetAsyncKeyState(wcon.VK_UP):
        keys.append('up')
    if wapi.GetAsyncKeyState(wcon.VK_DOWN):
        keys.append('down')


    return keys   
