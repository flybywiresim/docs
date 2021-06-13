# Performance Tips
---

!!! warning "Disclaimer"

    Your results may may vary depending on your hardware and other outside factors.

    This guide is for a simulator wide performance increase.

    **This guide is for Nvidia Graphics cards only**
---

## Windows Settings

- Make sure your graphics drivers are up to date. You can do this by using NVIDIA GeForce Experience. Or downloading directly from their website.

- Make sure windows itself is up to date. This can be done under the `Update & Security` tab in Windows settings.

- Under the `Gaming` tab in Windows settings, navigate to `Captures`. I would recomend turning off `Background Recording`.

- Then, navigate to the `Game Mode` tab. Make sure it is set to `On`.

- Set graphics performance to `High Performance` (This may be less effective on a desktop than a laptop).

!!! info "Methods - Graphics Performance"

    === "Windows Store Version"
        Open Windows settings and search for `Graphics Settings`.

        Under 'Choose an app to set preferecne', select `Microsoft Store App`. 

        In the dropdown below, find and select `Microsoft Flight Simulator`, then add.

        Click options, then select `High Performance`, save your selection.

        You can now close Windows Settings.
        


    === "Steam Version"
        Open Windows settings and search for `Graphics Settings`.

        Under 'Choose an app to set preferecne', select `Desktop App` anc click Browse

        You will need to locate the Microsoft Flight Simulator executable.

        The default location for steam is:

        `C:\Program Files (x86)\Steam\steamapps\common\MicrosoftFlightSimulator\FlightSimulator.exe`

        (If you have it installed in another location, point it there instead)

        Click options, then select `High Performance`, save your selection.

        You can now close Windows Settings.

- Lastly, I would recomend closing any programs running in the background that you don't need. This can be done in your system tray (the upwards pointing arrow to the right side of the task bar). Right click the icon of the program you would like to close and close it. 
    - You may have a lot of programs open here that you don't use often but start with Windows. You can stop them automatically runing by going to task manager, navigating to the `Start-up` tab and disabling programs you don't want to start with Windows.


!!! warning "Please note"

    After an update in MSFS, it isn't unheard of that your graphics drivers may become 'out of date' and cause some performance issues

    If this happens and you notice a decrease in performance, you can try rolling back your graphics driver until a new one is available.

    **Do this at your own risk**
---

## NVIDIA GeForce Experience

Open GeForce Experience and navigate to the settings cog. Under `General` turn off the `In-Game Overlay`.

This disables a feature called ShadowPlay, which is similar to the background recording we talked about in Windows settings.

If you particularly want to use the overlay, you can turn off ShadowPlay individually by pressing `Alt + Z` and making sure `Instant Replay` Is set to off. I would recommend disabling the overlay entirely though.

(The less overlays you have running, the better performance you will get. Examples of overlays are Steam Overlay, Windows Game Bar etc.)
---

## NVIDIA Control Panel

Open NVIDIA Control Panel. This can be done by right clicking on your desktop and clicking `NVIDIA Control Panel`.

Once it is open, navigate to the `Manage 3D Settings` tab on the left, then navigate to `Program Settings`.

In the dropdown, select `Microsoft Flight Simulator (Microsoft Flight Simulator)`

Change the settings listed below:

- Power management mode - `Prefer maximum performance`
- Vertical Sync - `On`
    - Add about Gsync
- Texture Filtering Quality - `High Performance`
    - This setting may mean you loose a small amount of quality in textures with the benefit of more FPS, you can experiment with this to get an acceptable balance.

!!! info "Global Settings"

    These settings can be applied in the `Global Settings` tab instead of the `Program Settings` tab. This may give you an FPS increase in all of your games.

    If you decide to change settings in the `Global Settings` tab, make sure that Power management mode is set to `Adaptive`.

    You will then need to go into `Program Settings`, choose Microsoft Flight Simulator and change it to `Max Performance` as detailed above.

    This is important, as having it set to Max Performance globally will force your GPU to stay at its max clock speed causing excess heat and power draw, even at idle. It is okay to have this setting in the `Program Settings` tab as we want the GPU to run at its highest clock speed for maximum performance when actually running the game.

---

##Microsoft Flight Simulator

Up to you 

Settings and how they affect performance