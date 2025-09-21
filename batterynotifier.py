import subprocess as sp
from time import sleep
from plyer import notification
notyetcharging = False #this tracks if the user hasnt begun charging, without this variable it will keep on sending notifications instead of once
while True:
     
    #this grabs the output from acpi to get info about the current battery state
    output = sp.run(["acpi"],capture_output=True,text=True)
    info = output.stdout.split()[2:5]
    try:
        info[1] = int(info[1][0:-2]) #convert the string percentage to integer to use more than less than operators
    except ValueError:
        continue #sometimes acpi returns the percentage as just charging, so if this happens we just continue
    if info[0] == 'Discharging,' and info[1] < 25 and notyetcharging != True:
        notyetcharging = True
        sp.run(["sudo","brightnessctl","s","5%"])
        sp.Popen(["paplay","lowbat.mp3"])
        sp.Popen(["notify-send","-a","python-battery","Battery low","Your battery is very low, please plug in now!"])
        
    elif info[0] == "Discharging," and info[1] < 10 and notyetcharging == True:
        sp.run(["sudo","brightnessctl","s","5%"])
        sp.Popen(["paplay","lowbat.mp3"])
        sp.Popen(["notify-send","-a","python-battery","Battery low","Your battery is very low, please plug in now!"])

    elif info[0] == "Charging," and notyetcharging == True:
        notyetcharging = False
        sp.run(["sudo","brightnessctl","s","20%"])
    sleep(0.1)

