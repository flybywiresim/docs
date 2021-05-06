# Reported Known Issues

!!! info "Always Try This First"

    Please try and remove all other mods/liveries from the community folder and test our mod again. This will help rule out mod conflicts.

    <sub>Report back the result of this test on our Discord.

!!! warning "After Microsoft Flight Simulator Updates"

    Make sure you do a full reinstall A32NX. Delete either of the folders below from your community folder:

    * A32NX (old folder name)
    * flybywire-aircraft-a320-neo (new folder name)
    
    Do this before reporting bugs.

FBW Installer - [Download Here](https://api.flybywiresim.com/installer) / *Sim Version: 1.15.10.0*

*Last Update: {{git_revision_date_localized}}*

---

### ^^Latest Issues^^

!!! warning "Liveries incompatible due to package separation"

    **Affects all versions of the A32NX (Stable, Development, and Experimental**

    Liveries made for the default A320neo will no longer function in the new FlyByWire package. Liveries will need to be converted by their respective authors.

    While this might represent an inconvenience for a short amount of time, we are sure that 3rd party content authors will be quick to provide you with updated liveries and programs.

    **Convert Your Liveries:**
    
    - See our guide to [convert liveries](convert-liveries.md)
    - Visit Flightsim.to with updated liveries [here](https://flightsim.to/c/liveries/flybywire-a32nx/)

* In development/experimental versions, the engine startup sound is bugged due to a fuel flow issue. This will be fixed when engine startup procedures will be implemented.

* Package separation or "fork" issues (*All Versions*):
    -  Default aircraft showing
        - Solution: Select the *FlyByWire Simulations A320neo (LEAP)* in the aircraft selector instead of the Asobo one.
    - Invisible plane / Sounds not working / Installation issues
        - Workaround: Reinstall A32NX, delete any old version from your Community Folder. Ensure you are on Installer v1.2.0 or above.
    
* Autopilot, FADEC, electrical system unwanted behavior
    - In rare cases the above mentioned systems may not start or behave erratically. This is in part due to `UTF-8` language support beta not enabled on your machine.
        - Solution:
            - Open Windows Control Panel -> Region.
            - Go to the Administrative tab and click Change system locale...
            - Make sure the check mark next to `Beta: Use UTF-8 for worldwide language support is selected`.
            - Click OK and restart your computer.
    
* ADIRS not aligned when spawning anywhere except cold & dark at a gate (*intermittent issue*)
    - Workaround: Restart the flight
    
* Wipers don't function correctly on FSX Liveries

***

#### MSFS Issues

* The simulator FPS stutters since World Update 4.
    * Solution: Turn off in-game multiplayer in MSFS settings.

***
    
#### Installer Issues

![installer issue](https://media.discordapp.net/attachments/831654046405230652/832741603940237362/unknown.png)

* If there is an issue with your community directory our installer will display the error above. This means the installer detects a certain directory as your community directory even though it does not exist anymore.
    - Solution: 
        - Create the specified directory stated in the error message
        - Restart the installer 
        - Change the community directory in the installer settings
    
* Installer Memory Leak
    - Commonly happens when our installer updates. Currently being investigated.
        - Workaround: Exit out of the FlyByWire Installer. Open `Task Manager` and find FlyByWire Installer. End Task.
    
* Instructions to send us installer logs can be found [here](installation.md#flybywire-installer)

***

### ^^Common Issues^^

* AP not following the flight plan (leaking input values affect, but doesn't disconnect the AP)
    - Workaround: Set dead-zones for your input device higher
        - Go to your settings
        - Controls and select your yoke/joystick/controller.
            - After that click the sensitivity button on the top left which should take you to the menu where you can adjust your deadzones. Start with 20% deadzone, if the problem persists keep increasing it. If it's fine with 20% you can then slowly decrease it too.

* Autopilot goes direct to RWY on APP (same with the default A320)
    - Workaround: Use DIR to a waypoint or selected heading

* CTD when pressing **FLY** on world menu
    - Check your content manager for missing packages

* Plane is invisible
    - Check your content manager for missing packages
    - Livery/Mod Conflict

* Rudder keybindings not working
    * You have to set your keybinding to rudder axis right and left

* Wing dips on landing (due to bad transition to direct law in flare, same with the default A320)
    * Workaround: use minimal aileron input on landing

* Black screens / unable to start
    * Conflict with another mod/livery or incorrect installation of the A32NX mod
    * Use our [installer](https://api.flybywiresim.com/installer)

* Upper ECAM displays wrong THR levers position / N1 rating

* ASOBO *Aviator/Beta Club* A320 liveries are incompatible with the A32NX mod

***

### ^^Fixed Issues^^

* Installer v1.1.1 potential issues: *(fixed)*
    - Getting default version or black screens after using installer on v1.1.0
        - Workaround: Delete the `flybywire-aircraft-a320-neo folder`, then install it again.
    - Installer not showing your existing installation:
        - This is due to the new modular system which requires a new full installation.
        - Workaround: Install the mod again via the installer.

* VOR/ADF indicators not showing on the ND *(fixed)*
  
* Unable to climb / flaps 1 issue *(fixed)*
  
* EFB not clickable *(fixed in development version)*
  
* V/S mode stuck at 1500 fpm or inoperable *(fixed)*
    
* ILS not showing on approach / does not auto populate in RADNAV *(fixed)*
    - Workarounds (may apply to 3rd party sceneries):
        - Manually input your ILS frequency into RADNAV. Type in the frequency found on your chart and press the key next to LS/Freq. Sample: 111.30

* Left PFD lagging / freezing *(fixed)*
    - The team is aware of the issue and is working hard to resolve it, potential fixes are being tested

* PFD artificial horizon freezes *(fixed)*
    - Workaround:
        - Turn off PFD, wait >10 seconds and turn PFD back on.
    
---

If you are here from our social media please visit our discord for support.

[:fontawesome-brands-discord:{: .discord } - **Discord Link**](https://discord.gg/flybywire)
