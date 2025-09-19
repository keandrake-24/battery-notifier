import subprocess as sp
from time import sleep
from playsound import playsound
from plyer import notification
notyetcharging = False #this tracks if the user hasnt begun charging, without this variable it will keep on sending notifications instead of once
while True:
     
    #this grabs the output from acpi to get info about the current battery state
    #try except is for sometimes acpi gives weird output inbetween charging and discharging and the string percentage conversion doesnt work
    #when this happens we just continue, this only happens for 1 frame inbetween plugging and unplugging
    try:
        output = sp.run(["acpi"],capture_output=True,text=True)
        info = output.stdout.split()[2:5]
        info[1] = int(info[1][0:-2]) #convert the string percentage to integer to use more than less than operators
        print(info)
        if info[0] == 'Discharging,' and info[1] < 100 and notyetcharging != True:
            notyetcharging = True
            sp.run(["brightnessctl","s","5%"])
            playsound("lowbat.mp3",block=False)
            notification.notify(
	            title='Low Battery',
	            message='Your battery is running low, please plug in your laptop now!',
	            app_name='python-battery',
	            timeout=10  # seconds
            )
        elif info[0] == "Charging," and notyetcharging == True:
            notyetcharging = False
            sp.run(["brightnessctl","s","20%"])
            playsound("charging.mp3",block=False)
        sleep(0.1)
    except:
        continue
