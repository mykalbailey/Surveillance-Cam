# SurveillanceCam Build Instructions

By: Mykal Bailey

### Components needed

•	Raspberry Pi 3  
•	Power Supply  
•	SD card  
•	Raspberry pi Camera module and mount  
•	Pan/Tilt Bracket  
•	Two servos  
•	Connecter wires  

### Setting up Raspberry Pi

•	Download and install the latest version of Raspbian from the instructions [here](https://www.raspberrypi.org/help/noobs-setup/2/)  
•	Configure Wi-Fi settings  
•	SSH into Raspberry pi  
•	From the home directory create and Folder named “sCam” and a subfolder named” code” where you will be storing any code related to the SurveillanceCam  

### Configure Pi and enable Camera support

•	SSH into Raspberry pi or open a terminal window (your choice) and type and enter “sudo raspi-config”    
•	Browse through settings and find camera and enable  
•	Test camera by taking picture by typing the command “raspistill –v –o pictest.jpg”  
•	The file should be saved in current working directory  

### Hardware assembly

•	Assemble pan and tilt bracket with servos  
•	Assemble camera mount  
•	Build base  
•	Attach camera mount with camera to pan and tilt bracket  
•	Attach Hardware to base for sturdiness  
•	Connect servos to the Raspberry Pi  
  1.	Look over data sheet for your purchased servos.  
  2.	Locate the ground, power, and control connections on the servos.  
  3.	Locate GPIO ports on the Raspberry Pi  
  4.	Connect ground wires to ground on GPIO ports  
  5.	Connect Power wires to 5V GPIO ports  
  6.	For the servo moving the bracket upward and downward, connect the control wire to pin 11 (or GPIO 17)  
  7.	For the servo moving the bracket left and right, connect the control wire to pin 7 (or GPIO 4)  
•	Connect Camera module to RPI  
•	Hardware assembly complete  

### Putting it all together!

•	Setup motions (allows video streaming from raspberry pi)  
  1.	Update RPI then download, install, and configure Motions Package  
    a.	Download by typing “sudo apt-get update && sudo apt-get install motion”  
    b.	Configure by typing “sudo vim /etc/default/motion”  
    c.	You’ll see “start_motion_daemon=no”.  Change to “yes”.  This will allow motions to run in the background and on start-up.  
    d.	Some changes needed to be made to the configuration file which can be opened by typing “sudo vim etc/default/motion.conf”.  
    e.	Find and change the following settings in the configuration file  
      •	Daemon on  
      •	Width 640  
      •	Height 480  
      •	Framerate 100  
      •	Stream_localhost off  
    f.	Reboot raspberry pi  
    g.	Now that Pi has rebooted, to test the stream in a terminal window type ”sudo service motion start” to start motions streaming service.  
    h.	Now in a web browser type raspberry pi IP address followed by “:8080” (example: 192.0.0.1:8080)  
    i.	A video stream from the pi Camera should be available.  
  2.	Setup apache server to host website from raspberry pi by following the instructions found [here](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md)  
  3.	Once apache server has completed installation you should be able to access Rpi homepage by opening a browser and entering the IP address of the Raspberry Pi.  
  4.	Download all files from [here](https://github.com/mykalbailey/Surveillance-Cam/Scripts)  
  5.	From Raspberry Pi navigate to /var/www/html  
    a.  Delete index.html  
    b.  From downloads, copy the following files into the directory  
      •	Index.html  
      •	Sup.php  
      •	Sdown.php  
      •	Scenter.php  
      •	Sleft.php  
      •	Sright.php  
  6.	From directory /home/sCam/code copy the file cservo.py  
•	Type “sudo vim /var/www/html/index.html” and make the following changes  
•	Change IP address to your current RPI IP address  
•	Now open homepage from browser, you should now be able to control camera from the homepage.  
