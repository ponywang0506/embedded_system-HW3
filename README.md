# Embedded System HW3
## Introduction
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
This is the program to let raspberry pi be a gatt client, which can find gatt server around and read/write data from it. 
1. Upload ```server.py``` to raspberry pi by ssh command.
2. Open the Gatt server for our program to find (for example, BLE Tool on Google Play)
3. Run command ```sudo python server.py``` on raspberry pi's command line.
4. Enter the index of the found server in the list  
<a href="https://imgur.com/WUrqlCS"><img src="https://i.imgur.com/WUrqlCS.png" title="source: imgur.com" /></a>

We will then modify  all descriptors' values whose ```uuid = 0x2902``` to 0x0002
(May change the code in the corresponding part to do more write/read operation)


## Result
### Reponse on Raspberry Pi
<a href="https://imgur.com/kLihSsK"><img src="https://i.imgur.com/kLihSsK.png" title="source: imgur.com" /></a>


### Server Log

<img width="50%" height="50%" src="https://i.imgur.com/tvgeMUq.jpg">

<img width="50%" height="50%" src="https://i.imgur.com/RQgeniV.jpg">
