import time
from LCD import LCD
import os

# Initialize the LCD with specific parameters: Raspberry Pi revision, I2C address, and backlight status
lcd = LCD(2, 0x27, True)  # Using Raspberry Pi revision 2 and above, I2C address 0x3f, backlight enabled

timeout = 20 # amount of seconds that the script waits

def generateLooking(number):
    dot = ""
    while number >= 0:
        dot += "."
        number -= 1
    return dot

def displayIP(lcd,ip):
    # Display messages on the LCD
    lcd.message("Current IP", 1)
    lcd.message(ip, 2)

    time.sleep(5)

    lcd = LCD(2, 0x27, False)
    lcd.message("Current IP", 1)
    lcd.message(ip, 2)

def findInternet(lcd):
    is_connected = False
    internet_test = os.system('wget -q --spider http://google.com')
    if internet_test == 0:
        lcd.message("Internet",1)
        is_connected = True
    else:
        lcd.message("No Internet",1)
    return is_connected

def findIP(lcd):
    is_found = False
    os.system("hostname -I")
    result = os.popen("hostname -I").read()
    result = result.split()
    if len(result) > 2:
        ip = result[0]
        displayIP(lcd, ip)
        is_found = True
    return is_found

i = 0
while timeout > 0:
    lcd.message(f"Finding IP{generateLooking(i % 3)}", 2)
    if findInternet(lcd):
        if findIP(lcd):
            break
    i += 1
    timeout -= 1 
    time.sleep(1)

