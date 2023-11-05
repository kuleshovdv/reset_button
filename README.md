# Reset Button for RetroPie
This script controls the pressing of the Reset Button on your Rasblery Pi case like NESPi. One short press stops running game and returns you to Emulationstation reciprocally Hotkey+Select on your gamepad . A long press restarts the system.

`![Connect reset button to your GP23 and Ground on Raspberry Pi GPIO connector](reset_button.png "GPIO connection")`

The Reset Button normally must be open. Connect one wire to GP23 another to the ground.

# Installation

 1. Connect to your Retropie via ssh

 2. Install git if you haven't done it before 
 `sudo apt install git`

 3. Get this script, goto script folder and make it runnable
 ```
 git clone
 cd reset_button
 chmod +x reset_button.py
 ```
 4. If you connect Reset Button not to GP23 edit reset_button.py file
 `nano reset_buton.py`
 and change GPIO chanel for Reset Button in python script:
 ```
 # GPIO chanel for Reset Button
 # By default is GP23
 chanel = {put your GPIO channel here}
 ```
Press Ctrl-O for save changes and Ctrl-X for close editor

 5. Copy reset_button.service into /etc/systemd/system folder
` sudo cp reset_button.service /etc/systemd/system/`

 6. Enable and start service
 ```
 systemctl daemon-reload
 systemctl enable reset_button
 systemctl start reset_button
 ```
 7. Enjoy



