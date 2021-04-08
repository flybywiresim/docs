# Installation guide

Please follow the information on this page to install the FlyByWire Simulations A32NX Mod for Microsoft Flight Simulator 2020

*Last Update: {{git_revision_date_localized}}*

---

## Downloads

### FlyByWire Installer

Download the new FlyByWire installer where you can select either the Stable, Development, or Experimental build. Our installer downloads and installs the mod directly into your community folder. 

The following commands can be used:

`Ctrl+F5` - Refreshes Installer

`Ctrl+F12` - Opens the debug tool

You can send us logs to our [Discord](https://discord.gg/flybywire) for support if you encounter issues with the installer. Please follow the steps below:
  * In the debug tool find and select `Console` in the top menu.
  * `Right+Click` anywhere in the log displayed. 
  * Click `Save as` and send the log to us.

[Download Installer](https://api.flybywiresim.com/installer){ .md-button }

---

### Traditional Download Methods

!!! info "Methods"

    === "Latest Stable Version"

        **How to download**:

        **Current Stable Version - v0.6.0**

          Stable is our variant that has the least bugs and best performance. This version will not always be up to date but we gurantee its compatibility with each major patch from MSFS. 

          [Download Stable](https://api.flybywiresim.com/api/v1/download?url=https://flybywiresim-packages.b-cdn.net/stable/A32NX-stable.zip){ .md-button }

          You can see the changelog on the releases page: [View Here](https://github.com/flybywiresim/a32nx/releases)


    === "Development Version"

        **How to download**:

        Development will have the latest features that will end up in the next stable. Bugs are to be expected. 

        It updates whenever something is added to the 'master' branch on GitHub. 

         [Download Development](https://api.flybywiresim.com/api/v1/download?url=https://flybywiresim-packages.b-cdn.net/vmaster/A32NX-master.zip){ .md-button }

         [View info about the latest build here](https://github.com/flybywiresim/a32nx/releases/tag/vmaster)

    === "Experimental Version"

        **How to download**:

        This version is similar to the development version, but contains custom systems (including fly-by-wire, autopilot, FADEC, etc.).

        This version is updated whenever the 'autopilot' branch on GitHub is updated, which is around every 12 hours. 

        **No support will be provided via Discord.**

        [Download Experimental](https://api.flybywiresim.com/api/v1/download?url=https://flybywiresim-packages.b-cdn.net/vmaster-cfbw-cap/A32NX-master-cfbw-cap.zip){ .md-button }

        [**IMPORTANT:** view warnings and info for the experimental version here](https://github.com/flybywiresim/a32nx/tree/autopilot/docs)

        This version is the same as the regular master/development version, but with the WIP custom fly-by-wire system. Expect issues with flight directors/autopilot if you intend to use this version. No support will be provided via Discord.



---
## Installation

**Please follow ALL steps in this section if you encounter any issues with installation before seeking support.**

Open the zip that you downloaded from one of the links above, and drag the A32NX folder inside the zip into your Community folder.

See below for the location of your Community folder:

---

### Microsoft Store AND/OR Gamepass edition

- Copy the "A32NX" folder into your community package folder.

It is located in:

* `C:\Users\[YOURUSERNAME]\AppData\Local\Packages\Microsoft.FlightSimulator_<RANDOMLETTERS>\LocalCache\Packages\Community`.

---

### Steam edition

- Copy the "A32NX" folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Roaming\Microsoft Flight Simulator\Packages\Community`.

---

### Boxed edition

- Copy the "A32NX" folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Local\MSFSPackages\Community`.


If the above methods do not work:

- You can find your community folder by going into FS2020 general options and enabling developer mode. You will see a menu appear on top. 
    - Go to tools and virtual file system.
    - Click on watch bases and your community folder will be listed in one of the folders.
- Please make sure you're copying the "A32NX" folder into your community package folder, NOT the "flybywiresim-a32nx" folder.

***

## Contributing

[:fontawesome-brands-github:{: .github } -  **GitHub Contributing.md**](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md)

More info [A32NX Development Overview](/a32nx-dev/overview)

***

## SimBrief Airframe

The FlyByWire Simulations SimBrief airframe with correct weights is available below.

✈ [SimBrief Airframe Link](https://www.simbrief.com/system/dispatch.php?sharefleet=eyJ0cyI6IjE2MDU4MjAwNzg5NDYiLCJiYXNldHlwZSI6IkEzMjAiLCJjb21tZW50cyI6IkZMWSBCWSBXSVJFIiwiaWNhbyI6IkEyME4iLCJuYW1lIjoiQTMyME5FTyBGQlciLCJlbmdpbmVzIjoiTEVBUC0xQTI2IiwicmVnIjoiQTIwTiIsImZpbiI6IiIsInNlbGNhbCI6IiIsImhleGNvZGUiOiIiLCJjYXQiOiJNIiwicGVyIjoiQyIsImVxdWlwIjoiU0RFM0ZHSElSV1kiLCJ0cmFuc3BvbmRlciI6IkxCMSIsInBibiI6IkExQjFDMUQxTzFTMSIsImV4dHJhcm1rIjoiIiwibWF4cGF4IjoiMTgwIiwid2d0dW5pdHMiOiJLR1MiLCJvZXciOiI0MTAwMCIsIm16ZnciOiI2MjUwMCIsIm10b3ciOiI3OTAwMCIsIm1sdyI6IjY2MDAwIiwibWF4ZnVlbCI6IjIxMjczIiwicGF4d2d0IjoiMTA0IiwiZGVmYXVsdGNpIjoiIiwiZnVlbGZhY3RvciI6IlAwMCIsImNydWlzZW9mZnNldCI6IlAwMDAwIn0-) Credits: [@viniciusfont](https://github.com/viniciusfont)

Pilot ID can be found in the Optional Entries section of the Dispatch Options page.

