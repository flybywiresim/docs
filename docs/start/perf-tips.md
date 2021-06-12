# Performance Tips
---

!!! warning "Disclaimer"

    Your results may may vary depending on your hardware and other outside factors.

    This guide is for a simulator wide performance increase.

    **This guide is for Nvidia Graphics cards only**
---

##Windows Settings

Firstly you need to make sure your graphics drivers are up to date. You can do this by using NVIDIA GeForce Experience. Or downloading directly from their website.

!!! warning "Please note"

    After an update in MSFS, it isn't unheard of that your graphics drivers may become 'out of date' and cause some performance issues

    If this happens and you notice a decrease in performance, you can try rolling back your graphics driver until a new one is available.

    **Do this at your own risk**
---

!!! info "Graphics Settings - This may be less effective on a desktop than a laptop"

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

        `C:\Program Files (x86)\Steam\steamapps\common\MicrosoftFlightSimulator\FlightSimulator.exe`.

        (If you have it installed in another location, point it there instead)

        Click options, then select `High Performance`, save your selection.

        You can now close Windows Settings.

---

##NVIDIA Control Panel

Open NVIDIA Control Panel. This can be done by right clicking on your desktop and clicking `NVIDIA Control Panel`.

Once it is open, navigate to the `Manage 3D Settings` tab on the left, then navigate to `Program Settings`.

In the dropdown, select `Microsoft Flight Simulator (Microsoft Flight Simulator)`

Change the settings listed below:

- Power management mode - `Prefer maximum performance`
- Make sure Vertical sync is set to `Use the 3D application setting'

!!! info "Global Settings"

    These settings can be applied in the `Global Settings` tab instead of the `Program Settings` tab. This may give you an FPS increase in all of your games.

    If you decide to change settings in the `Global Settings` tab, make sure that Power management mode is set to `Adaptive`.

    You will then need to go into `Program Settings`, choose Microsoft Flight Simulator and change it to `Max Performance` as detailed above.

    This is important, as having it set to Max Performance globally will force your GPU to stay at its max clock speed causing excess heat and power draw, even at idle. 
    It is okay to have this setting in the `Program Settings` tab as we want the GPU to run at its highest clock speed for maximum performance when actually running the game.