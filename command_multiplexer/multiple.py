#!/usr/bin/env python3
#please note that this script can cause fuckups, if not used with care
#Usage: python multiple.py ls -al
import os
import sys
if len(sys.argv) < 2:
    print("wtf dude, atleast enter some command:")
    exit(0)

#Enter the pane number on which you want to run this command
#You can get pane number using ctrl+b q
pane_list = [0,1,2]
for item in pane_list:
    os.system("tmux send-keys -t " + str(item) +  " '" + " ".join(sys.argv[1:]) + "' C-m")
