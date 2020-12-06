#!/usr/bin/env python3
import subprocess as sp
import re
import os
import pyfiglet
# twitter.com/Aditya0x34
# pwn0x80.github.io

class fix:
    def __init__(self):
        self.id =  'xsetwacom --list devices'
        self.screen = 'xrandr --listactivemonitors'

        self.id_array = []
        self.screen_array = []
        self.screen_choice =[]



    def id_selector(self, i, s):
        reg = re.compile(r'.*id:([^.][^.][^.]).*')
        self.id_array = reg.findall(i)
        reg_screen = re.compile('.*([^.][^.][^.]\D-\d).*')
        self.screen_array = reg_screen.findall(s)





    def detector(self):
        a = sp.getoutput(self.id)
        k = sp.getoutput(self.screen)
        self.id_selector(a, k)




    def screen_choices(self):
        total = len(self.screen_array)

        for i in range(total):
            print("ENTER {} for screen ~~ {} ~~".format(i, self.screen_array[i]))
        self.screen_choice = input("input your choice - ")




    def runs(self):
        id_loop = len(self.id_array)
        

        while 0< id_loop:

            id_loop -=1

            i = int(self.screen_choice[0])
            command = "xsetwacom --set" + self.id_array[id_loop] + " MapToOutput " +  self.screen_array[i]
            os.system(command)



def info():
    logo = pyfiglet.figlet_format("WaCoM Monitor Mapper :", font = "digital")
    print(logo)
    print("\033[95m {}\033[00m" .format("###############################"))
    print("\033[92m {}\033[00m" .format("twitter - @Aditya0x34"))
    print("\033[95m {}\033[00m" .format("website - pwn0x80.github.io"))
    print("\033[95m {}\033[00m" .format("###############################"))




if __name__ == "__main__":
    info()
    Object = fix()
    Object.detector()
    Object.screen_choices()
    Object.runs()




