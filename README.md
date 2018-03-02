# runLED

Control the colors and text on my Raspberry Pi display using Flask!!


# Images

SSH splash screen

![alt img](http://i.imgur.com/kP7z2Tt.png)
      
Raspberry Pi panel is powered with two 2.4v power adapters plus a Raspberry Pi HAT that does the hard work for panel display graphics. Link to product: [Adafruit Page](https://www.adafruit.com/product/2345) No need to wire each gpio pin to the led panel.
Panels are 32x16 and daisy chained together to make a 64x16 display
![alt img](http://i.imgur.com/429Vw6T.jpg)
 
Flask Web interface, can run a Webserver on a local networked device to manage the colors of the LEDs and even includes a Web form.
![alt img](https://i.imgur.com/VLfXBLF.png)

# To do

      Stop using Flask built in Web server -- deploy on NGINX
