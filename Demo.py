import time
from LCD import LCD
import subprocess

# Initialize the LCD with specific parameters: Raspberry Pi revision, I2C address, and backlight status
lcd = LCD(2, 0x27, True)  # Using Raspberry Pi revision 2 and above, I2C address 0x3f, backlight enabled

result = subprocess.run(["ifconfig"], capture_output=True, text=True)
result = result.stdout.split()
next_word = False
ip = None
for word in result:
    if word == "inet":
        next_word = True
    elif next_word:
        ip = word
        break
# Display messages on the LCD
lcd.message("Current IP", 1)        # Display 'NerdCave!' on line 1
lcd.message(ip, 2)    # Display '    - Tutoarials' on line 2

time.sleep(5)

lcd = LCD(2, 0x27, False)  # Using Raspberry Pi revision 2 and above, I2C address 0x3f, backlight enabled
lcd.message("Current IP", 1)        # Display 'NerdCave!' on line 1
lcd.message(ip, 2)    # Display '    - Tutoarials' on line 2