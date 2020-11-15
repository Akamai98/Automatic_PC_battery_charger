'''
Automatic PC battery charger v1.9.9.4
AkamaiSoftware © - 2019. All rights reserved
'''

import sys,psutil,serial,time,ctypes
from colorama import Fore,Back,Style,init

init(autoreset = True)

softwareVersion = "v1.9.9.4"

ctypes.windll.kernel32.SetConsoleTitleW("Automatic PC battery charger " + softwareVersion + " - AkamaiSoftware") #Sets the windows title.

def welcome():
    print(Back.BLUE + Style.BRIGHT + "AUTOMATIC PC BATTERY CHARGER " + softwareVersion + "\n\nAKAMAISOFTWARE © 2019 - ALL RIGHTS RESERVED\n")
    print("////////////////////////////////////////////")

def portSelection(): #This function establishes the COM port where is connected the device. The user must enter the COM port to use.
    validInput = False
    firstInput = 0

    while not validInput:
        try:
            inputCOMPort = input("\nPlease, enter the COM port to use (only the number), or enter '0' to exit: ")
            
            firstInput = int(inputCOMPort)
    
            if firstInput == 0:
                print(Fore.CYAN + Style.BRIGHT + "\nProgram will shut down.")
                time.sleep(3)
                exit()
            elif firstInput < 1 or firstInput > 9:
                print(Back.RED + Style.BRIGHT + "\nERROR. Invalid entry.")
                time.sleep(1)
                continue
            else:
                validInput = True
        except ValueError:
            print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry. Please, enter a integer number.")
            time.sleep(1)

    return inputCOMPort

def connectionCheck(port):
    isConnected = False
    newPort = port
    
    while not isConnected: #Program checks if the device is connected to the PC. If it isn't, a warning message with mutiple options pops up until the device is plugged.
        try:
            device = serial.Serial(port,9600)
            isConnected = True
        except serial.serialutil.SerialException:
            print(Fore.RED + Style.BRIGHT + "\nWARNING: There is no device connected to " + port + " port.")

            validInput = False

            while not validInput:
                try:
                    inputNewCOMPort = input("If you want to check again the connection in the " + port + " port, please enter '1'.\nIf you want to set a different COM port to use, please enter '2'.\nIf you want to exit, please enter '3'.\nYOUR INPUT: ")

                    secondInput = int(inputNewCOMPort)

                    if secondInput == 1:
                        validInput = True
                    elif secondInput == 2:
                        newPort = "COM" + str(portSelection())

                        if port != newPort: #Program only changes the COM port where to check when the new COM port is different than the original.
                            port = newPort
                        
                        validInput = True
                        
                    elif secondInput == 3:
                        print(Fore.CYAN + Style.BRIGHT + "\nProgram will shut down.")
                        time.sleep(3)
                        exit()
                    else:
                        print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry.")
                        time.sleep(1)
                        continue
                except ValueError:
                    print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry. Please, enter a integer number.")
                    time.sleep(1)

    time.sleep(2) #Pause between the serial port connection and the data transferences.
    
    return device,newPort

def settings(CRITICAL_BATTERY_LEVEL,CHECK_LAPSE):
    inputCBL = input("If you want to set the critical battery percentage (i.e.: at what percentage of battery you want the charger to start working), please enter '1'.\n If you want to use the default level (5%), please enter '2'.\nIf you want to exit, please enter '3'.\nYOUR INPUT: ") #Here, the user determinates the critical level of battery. When the program detects this percentage, the device starts working.

    validChoice = False

    while not validChoice:
        try:
            thirdInput = int(inputCBL)

            validChoice = True

            if thirdInput == 1:
                validLevel = False

                while not validLevel:
                    NEW_CRITICAL_BATTERY_LEVEL = input("\nPlease, enter the new critical battery percentage: ")

                    try:
                        NCBL = int(NEW_CRITICAL_BATTERY_LEVEL)

                        if NCBL < 5 or NCBL > 95:
                            print(Fore.RED + Style.BRIGHT + "\nERROR: Invalid entry. Please, enter a integer number between 5 and 95.")
                            time.sleep(1)
                        else:
                            CRITICAL_BATTERY_LEVEL = NCBL
                            print(Back.CYAN + Style.BRIGHT + "\n>>>>>>>>>>  SETTED CRITICAL BATTERY LEVEL: " + str(CRITICAL_BATTERY_LEVEL) + "%  <<<<<<<<<<")
                            validLevel = True
                    except ValueError:
                        print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry. Please, enter a integer number.")
                        time.sleep(1)
            elif thirdInput == 2:
                print(Back.CYAN + Style.BRIGHT + "\n>>>>>>>>>>  DEFAULT CRITICAL BATTERY LEVEL: " + str(CRITICAL_BATTERY_LEVEL) + "%  <<<<<<<<<<")
                time.sleep(2)
            elif thirdInput == 3:
                print(Fore.CYAN + Style.BRIGHT + "\nProgram will shut down.")
                time.sleep(3)
                exit()
            else:
                print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry.")
                time.sleep(1)
                continue
        except ValueError:
            print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry. Please, enter a integer number.")
            time.sleep(1)

    inputCL = input("\nIf you want to set the PC battery percentage check lapse, please enter '1'.\nIf you want to use the default PC battery percentage check lapse (120 seconds), please enter '2'.\nIf you want to exit, please enter '3'.\nYOUR INPUT: ") #Here, the user determinates the critical level of battery. When the program detects this percentage, the device starts working.

    validChoice = False

    while not validChoice:
        try:
            fourthInput = int(inputCL)

            validChoice = True

            if fourthInput==1:
                validLapse = False

                while not validLapse:
                    NEW_CHECK_LAPSE = input("\nPlease, enter the new PC battery percentage check lapse (in seconds): ")

                    try:
                        NCL = int(NEW_CHECK_LAPSE)

                        if NCL<1:
                            print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry. Please, enter a number bigger than 1.")
                            time.sleep(1)
                        else:
                            CHECK_LAPSE = NCL
                            print(Back.CYAN + Style.BRIGHT + "\n>>>>>>>>>>  SETTED PC BATTERY PERCENTAGE CHECK LAPSE: " + str(CHECK_LAPSE) + " SECONDS  <<<<<<<<<<")
                            validLapse = True
                    except ValueError:
                        print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry. Please, enter a integer number.")
                        time.sleep(1)
            elif fourthInput==2:
                print(Back.CYAN + Style.BRIGHT + "\n>>>>>>>>>>  DEFAULT PC BATTERY PERCENTAGE CHECK LAPSE: " + str(CHECK_LAPSE) + " SECONDS  <<<<<<<<<<")
                time.sleep(2)
            elif fourthInput==3:
                print(Fore.CYAN + Style.BRIGHT + "\nProgram will shut down.")
                time.sleep(3)
                exit()
            else:
                print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry.")
                time.sleep(1)
                continue
        except ValueError:
            print(Back.RED + Style.BRIGHT + "\nERROR: Invalid entry. Please, enter a integer number.")
            time.sleep(1)

    return CRITICAL_BATTERY_LEVEL,CHECK_LAPSE

def batteryCheck(port,CRITICAL_BATTERY_LEVEL,CHECK_LAPSE,device):
    try: #Communication test. The program tries to set a communication between the PC and the device. If it's possible, the program continues. If not (e.g.: the device has been unplugged), a warning message pops up and the program shuts down itself for caution.
        device.write(b'0')
    except serial.serialutil.SerialException:
        print(Fore.RED + Style.BRIGHT + "\nFATAL COMMUNICATION ERROR: The device has been disconnected from " + port +" port. This program will shut down for caution.")
        time.sleep(5)
        exit(1)

    battery = psutil.sensors_battery() #Battery status resets every time this function is executed.

    message = "" #Message resets every time this function is executed.
    message += str(battery.percent) + "%"

    if battery.power_plugged: #This flag states if the PC battery is charging or not.
        message += " | Is charging"
    else:
        message += " | Is not charging"

    if battery.percent <= CRITICAL_BATTERY_LEVEL and not battery.power_plugged: #If the PC battery percentage is less than 100% and CRITICAL_BATTERY_LEVEL and the PC battery is not charging, a pulse is sent via the established USB port and the circuit starts working.
        device.write(b'1')
        message += " | " + Fore.MAGENTA + Style.BRIGHT + "Pulse sended. PC battery is now charging."
    elif battery.percent <= CRITICAL_BATTERY_LEVEL and battery.power_plugged: #If the PC battery percentage is less than 100% and CRITICAL_BATTERY_LEVEL and the PC battery is charging, we don't do anything.
        message += " | " + Fore.CYAN + Style.BRIGHT + "PC battery already charging."
    elif battery.percent == 100 and not battery.power_plugged: #If the PC battery percentage is 100% and the PC battery is not charging, we don't do anything.
        message += " | " + Fore.MAGENTA + Style.BRIGHT + "PC battery is full. There's no need to charge."
    elif battery.percent == 100 and battery.power_plugged: #If the PC battery percentage is 100% and the PC battery is charging, a pulse is sent via the established USB port and the circuit stops working.
        device.write(b'1')
        message += " | " + Fore.MAGENTA + Style.BRIGHT + "PC battery is full. Pulse sended. There's no need to charge."
    else: #If the PC battery percentage is between 100% and CRITICAL_BATTERY_LEVEL, we don't do anything.
        message += " | " + Fore.CYAN + Style.BRIGHT + "There's no need to charge."
        
    print(message)

    time.sleep(CHECK_LAPSE)

def main():
    welcome()
    
    port = "COM" + str(portSelection()) #COM port to use.

    CRITICAL_BATTERY_LEVEL = 5 #Default PC battery percentage where the device starts working.
    CHECK_LAPSE = 120 #Default PC battery percentage check lapse (in seconds).
    
    device,newPort = connectionCheck(port)

    print(Back.CYAN + Style.BRIGHT + "\nDEVICE SUCCESSFULLY CONNECTED IN PORT: " + newPort + ".")
    print("\n////////////////////////////////////////////\n")

    CRITICAL_BATTERY_LEVEL,CHECK_LAPSE = settings(CRITICAL_BATTERY_LEVEL,CHECK_LAPSE)
    
    time.sleep(3)

    print("\n////////////////////////////////////////////\n")

    while True:
        batteryCheck(port,CRITICAL_BATTERY_LEVEL,CHECK_LAPSE,device)

if __name__ == "__main__":
    main()
