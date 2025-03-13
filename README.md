# Setting up the IP recognization on startup for LCD
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
10. Schedule a crontab to obtain IP Address from ethernet on startup
    a. Type "sudo crontab -e" in command window
    b. Add "@reboot dhclient -v" to crontab

# Adding Ability for Remote Desktop
1. Type "sudo apt install xrdp" in command window
2. Type "sudo service xrdp start" in command window
3. Changing Viewer to X11:
    a. Type "sudo raspi-config" in command window (Set the viewer to X11 instead of Waland)
4. Fixing the messed up windows when connecting with Remote Desktop
    a. Type "sudo adduser xrdp ssl-cert" in the command window
    b. Type "sudo nano /etc/X11/xrdp/xorg.conf" in the command window
        i.Change Option DRMDevice line:
            (Option "DRMDevice" "")
        2. reboot
5. Docs to create an ethernet bridge
//Stuff for creating an ethernet bridge
https://www.informaticar.net/how-to-configure-virtualization-with-virt-manager-on-raspberry-pi-and-network-bridge/

