# ip_for_pi
1. Install python
2. Install smbus: "sudo apt install python3-smbus"
3. Change Rasberry Pi Configuration: "sudo raspi-config"
4. Reboot: "sudo reboot"
5. Make it run automatically on start up: "sudo nano /etc/rc.local"
More Info: https://raspberrytips.com/autostart-a-program-on-boot/
6. Adding /etc/local: If does not exist, add "#!/bin/bash" on top of file
7. Put path to python infront of "/usr/bin/python3 PATH_TO/Demo.py"
8. Add "exit 0" on bottom of the file and save
9. Allow executable: chmod a+x <PATH_TO/Demo.py>
