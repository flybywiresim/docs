# Remote SimBridge

This guide details how to run SimBridge on a different computer (remote machine) than the one running your simulator (local machine). 

## PC Requirements

- FlyByWire Installer running on the remote machine - See [Starting SimBridge](../install-configure/start-simbridge.md)
- SimBridge running on the remote machine - See [Starting SimBridge](../install-configure/start-simbridge.md)

## Configuring your aircraft

In order to let the aircraft know that SimBridge is running on a different machine, you will need to go the [EFB settings](../../fbw-a32nx/feature-guides/flypados3/settings/) and enter the 'Sim Options' page. 

Locate the 'SimBridge Host Machine' option. By default it will be set to 'This PC' as shown below:
{{image 1}}

Click the 'Remote PC' option, which will reveal a new field which is the Ip Address for the remote machine (defaults to `localhost`) 
{{image 2}}

Enter the IP Address for the Remote Machine in the field and hit enter to save. You will now have to disable and enable the SimBridge connection either via the same options page or the quick notifications panel of the EFB 
{{image 3 + 4}}

If everything is correct, you will receive a notification that SimBridge is connected and the WiFi icon on the EFB will also be displayed. 
{{image 5 + 6}}

##########################

## Finding your IP Address using SimBridge

Typically, if you are running SimBridge on the same network (via ethernet or WiFi) as the local (sim) machine, you will need to use your LAN IP Address in the EFB settings. 
But, if you are running SimBridge on a different network than your own, for example in another home or at a friend's computer, you will need to use the Public IP Address instead.

SimBridge will display the local IP address it's using. To find it, open the SimBridge console (right click on the SimBridge tray icon and click 'Show/Hide') and locate the following entry: `[NetworkService] Local IP is XXXXXXXXXXX`
{{image 9}}

The numbers displayed, is local IP address SimBridge is running on. You can set this value now in the EFB and the airplane will connect.


### Manually finding the LAN IP Address

!!! info 
    If for some reason you can not locate the Ip Address from SimBridge it self or you still can't connect, you can try finding it manually. 

You will need to perform the following instructions on the machine that is running SimBridge! 

#### Windows

Press `Win + R` at the same time, in the new window that opened, type `cmd` and hit enter/OK. You will now see a terminal window. Copy and paste the following command: 
`ipconfig` 
A list of your available internet connections will be printed. Typically, you should see one or two 'adapters'. 
Locate the one that an 'IPv4 Address', it should look something like this: 
{{image 7}}
Depending on your router, your IP may look similar to the one above, or `10.10.X.X` or similar. 

You can now copy the value next to 'IpV4 Address' and use it on the local machine running the simulator.  

#### Linux

Open a terminal (A common keybind for desktop operating systems is `CTRL + SHIFT + T`) and run the command: 
`ifconfig` 
A list with all the available connections will be printeded. Depending on your configuration, you will see more than two 'adapters'. Locate the one responsible for connecting to your local network (and router) and that contains an 'inet' field, as shown below: 
{{image 8}}
Depending on your router, your IP may look similar to the one above, or `10.10.X.X` or similar. 

You can now copy the value inside 'inet' and use it on the local machine running the simulator. 

### Manually fetching your public IP Address


To fetch the public IP address, on the remote PC open a website like https://ipchicken.com/ or https://whatismyipaddress.com/
The 'IPv4 IP Address' is the value you will need to copy and enter into the EFB settings.
