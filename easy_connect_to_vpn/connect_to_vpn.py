#!/usr/bin/env python

# Imports
import pycountry
import os
import sys
import subprocess

# constants
# This program is dependent on the below path, files in this path are in format: tryVPN_<country_code>_<city>_TCP80.ovpn
VPN_FILE_PATH = "/home/harsh/mystuff/vpn"

def get_countries():
    country_list = list()
    for filename in os.listdir(VPN_FILE_PATH):
        cname = filename.split("_")[1]
        country_list.append(pycountry.countries.get(alpha_2=cname))
    return country_list

def connect_to_vpn(country_code):
    vpnfile = ""
    for filename in os.listdir(VPN_FILE_PATH):
        if country_code in filename:
            vpnfile = VPN_FILE_PATH + "/" + filename
            break
    if vpnfile == "":
        print("could not find the configuration for this country... exiting")
        sys.exit(1)
    try:
        result = subprocess.call("sudo openvpn --config " + vpnfile,timeout=15.0, shell=True)
        return True
    except subprocess.TimeoutExpired:
        print("Timeout of command expired, assuming it worked and returning true")
        return True
    return False


def disconnect_vpn():
    result = subprocess.check_output("ps aux | grep openvpn | awk '{print $2,$11}'", shell=True)
    cmd_output = result.decode("utf-8")
    for line in cmd_output.split("\n"):
        process_details = line.split()
        if len(process_details) == 0:
            continue
        if process_details[1].lower() == "openvpn":
            subprocess.check_output("sudo kill -9 " + str(process_details[0]), shell=True)

def is_already_connected():
    result = subprocess.check_output("ps aux | grep openvpn | awk '{print $2,$11}'", shell=True)
    cmd_output = result.decode("utf-8")
    for line in cmd_output.split("\n"):
        process_details = line.split()
        if len(process_details) == 0:
            continue
        if process_details[1].lower() == "openvpn":
            return True
    return False   

def main():
    if len(sys.argv) < 2:
        print("Usage: connect <countryname>")
    else:
        if sys.argv[1].lower() == "disconnect":
            disconnect_vpn()
            sys.exit(0)
        if is_already_connected():
            print("You are already connected to vpn, first disconnect")
            sys.exit(1)
        countries = get_countries()
        connect_flag = False
        for country in countries:
            if str(sys.argv[1]).lower() in str(country.name).lower():
                print("country found connecting....")
                connect_flag = connect_to_vpn(country.alpha_2)
                break
        if connect_flag == True:
            print("connected to " + str(sys.argv[1]))
        else:
            print("Failed to connect " + str(sys.argv[1]))
if __name__ == "__main__":
    main()
# ps aux | grep openvpn | awk '{print $2,$11}'