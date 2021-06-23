# Installation guide

Please follow the information on this page to install the FlyByWire Simulations A32NX addon for Microsoft Flight Simulator 2020

*Last Update: {{git_revision_date_localized}}*

!!! warning "Important Notice"

    All FlyByWire Simulations A32NX versions are now independent from the default A320neo.

    We’d like to remind all users of the following two **important changes**:

    The folder in the Community directory is now:

      - `flybywire-aircraft-a320-neo`

    The airplane in the simulator is now titled:

      - `FlyByWire Simulations - A320neo (LEAP)` 

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

        **Current Stable Version - v0.6.1**

          Stable is our variant that has the least bugs and best performance. This version will not always be up to date but we gurantee its compatibility with each major patch from MSFS. 

          [Download Stable](https://api.flybywiresim.com/api/v1/download?url=https://flybywiresim-packages.b-cdn.net/stable/A32NX-stable.zip){ .md-button }

          You can see the changelog on the releases page: [View Here](https://github.com/flybywiresim/a32nx/releases)


    === "Development Version"

        **How to download**:

        Development will have the latest features that will end up in the next stable. Bugs are to be expected. 

        It updates whenever something is added to the 'master' branch on GitHub. 

         [Download Development](https://api.flybywiresim.com/api/v1/download?url=https://flybywiresim-packages.b-cdn.net/vmaster/A32NX-master.zip){ .md-button }
         
         [**IMPORTANT:** View information on Autopilot / Fly-By-Wire here](autopilot-fbw.md)

    === "Experimental Version"

        **How to download**:

        This version is similar to the development version, but contains custom systems. 

        Experimental is currently on **hold**. 

        **No support will be provided via Discord.**

        [Download Experimental](https://api.flybywiresim.com/api/v1/download?url=https://flybywiresim-packages.b-cdn.net/vmaster-cfbw-cap/A32NX-master-cfbw-cap.zip){ .md-button }

        [**IMPORTANT:** view warnings and info for the experimental version here](https://github.com/flybywiresim/a32nx/tree/autopilot/docs)

---
## Manual Installation

**Please follow ALL steps in this section if you encounter any issues with installation before seeking support.**

Open the zip that you downloaded from one of the links above, and drag the `flybywire-aircraft-a320-neo` folder inside the zip into your Community folder.

See below for the location of your Community folder:

---

### Microsoft Store and/or Game Pass edition

- Copy the `flybywire-aircraft-a320-neo` folder into your community package folder.

It is located in:

* `C:\Users\[YOURUSERNAME]\AppData\Local\Packages\Microsoft.FlightSimulator_<RANDOMLETTERS>\LocalCache\Packages\Community`.

---

### Steam edition

- Copy the `flybywire-aircraft-a320-neo` folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Roaming\Microsoft Flight Simulator\Packages\Community`.

---

### Boxed edition

- Copy the `flybywire-aircraft-a320-neo` folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Local\MSFSPackages\Community`.

---

### Troubleshooting

If the above methods do not work:

- You can find your community folder by going into Microsoft Flight Simulator general options and enabling developer mode. You will see a menu appear on top. 
    - Go to tools and virtual file system.
    - Click on watch bases and your community folder will be listed in one of the folders.
  
If your issue is not related to installation visit - [**Reported Issues**](reported-issues.md)

***

## Contributing

[:fontawesome-brands-github:{: .github } -  **GitHub Contributing.md**](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md)

More info [A32NX Development Overview](../a32nx-dev/overview.md)

***

## SimBrief Airframe

The FlyByWire Simulations SimBrief airframe with correct weights is available below.

✈ [SimBrief Airframe Link](https://www.simbrief.com/system/dispatch.php?sharefleet=eyJ0cyI6IjE2MDU4MjAwNzg5NDYiLCJiYXNldHlwZSI6IkEzMjAiLCJjb21tZW50cyI6IkZMWSBCWSBXSVJFIiwiaWNhbyI6IkEyME4iLCJuYW1lIjoiQTMyME5FTyBGQlciLCJlbmdpbmVzIjoiTEVBUC0xQTI2IiwicmVnIjoiQTIwTiIsImZpbiI6IiIsInNlbGNhbCI6IiIsImhleGNvZGUiOiIiLCJjYXQiOiJNIiwicGVyIjoiQyIsImVxdWlwIjoiU0RFM0ZHSElSV1kiLCJ0cmFuc3BvbmRlciI6IkxCMSIsInBibiI6IkExQjFDMUQxTzFTMSIsImV4dHJhcm1rIjoiIiwibWF4cGF4IjoiMTgwIiwid2d0dW5pdHMiOiJLR1MiLCJvZXciOiI0MTAwMCIsIm16ZnciOiI2MjUwMCIsIm10b3ciOiI3OTAwMCIsIm1sdyI6IjY2MDAwIiwibWF4ZnVlbCI6IjIxMjczIiwicGF4d2d0IjoiMTA0IiwiZGVmYXVsdGNpIjoiIiwiZnVlbGZhY3RvciI6IlAwMCIsImNydWlzZW9mZnNldCI6IlAwMDAwIn0-) Credits: [@viniciusfont](https://github.com/viniciusfont)

Pilot ID can be found in the Optional Entries section of the Dispatch Options page.

