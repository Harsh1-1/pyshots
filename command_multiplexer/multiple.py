#!/usr/bin/env python3
#please note that this script can cause fuckups, if not used with care
#Usage: python multiple.py ls -al
#similar functionality is also provided by tmux synchronized-panes option 
import os
import sys
import subprocess

# This will return list of pane_ids except the active which can act as command center
def get_list_of_panes():
    pane_ids = list()
    result = subprocess.check_output("tmux list-panes",shell=True)
    panes_data = result.decode("utf-8")
    for pane_line in panes_data.strip().split("\n"):
        if "active" not in pane_line:
            pane_line_split = pane_line.split(":")
            pane_ids.append(int(pane_line_split[0]))
    return pane_ids

def main():
    if len(sys.argv) < 2:
        print("wtf dude, atleast enter some command:")
        exit(0)
    #Enter the pane number on which you want to run this command
    #You can get pane number using ctrl+b q
    pane_list = get_list_of_panes()
    print(pane_list)
    for item in pane_list:
        os.system("tmux send-keys -t " + str(item) +  " '" + " ".join(sys.argv[1:]) + "' C-m")

if __name__ == "__main__":
    main()
