# Installation guide

Please follow the information on this page to install the FlyByWire Simulations A32NX Mod for Microsoft Flight Simulator 2020

---

## Downloads

### A32NX Installer

Download the new A32NX installer where you can select either the Stable or Developer build, and download and install the mod directly into your community folder, [download here](https://github.com/Externoak/A32NX-installer/releases/latest/download/A32NX_Downloader.zip) ([source](https://github.com/Externoak/A32NX-installer/)).

---

### Traditional Download Methods

#### Latest Stable Release

>Current Stable Version - v0.5.2

* This is the recommended stable release, as it has been thoroughly tested.

 * [Download the stable release here.](https://github.com/flybywiresim/a32nx/releases/latest/download/flybywiresim-a32nx.zip)

 * You can see the changelog on the releases page: [View Here.](https://github.com/flybywiresim/a32nx/releases)

#### Unstable Master Branch Build

* This has the latest features, but is much more unstable, use at your own risk.

 * [Download developer build here.](https://github.com/flybywiresim/a32nx/releases/download/vmaster/A32NX-master.zip)

 * [View info about the latest build here.](https://github.com/flybywiresim/a32nx/releases/tag/vmaster)

#### Unstable Master Branch Build (with custom FBW)

* This version is the same as the regular master/development version, but with the WIP custom fly-by-wire system. Expect issues with flight directors/autopilot if you intend to use this version. No support will be provided via Discord.

* [Download custom FBW development build here.](https://flybywiresim-packages.nyc3.cdn.digitaloceanspaces.com/vmaster-cfbw/A32NX-master-cfbw.zip)

* [**IMPORTANT:** view warnings and info for the custom FBW build here.](https://github.com/flybywiresim/a32nx/tree/fbw/docs)

---
## Installation

**Please follow ALL steps in this README if you encounter any issues with installation before seeking support.**

Open the zip that you downloaded from one of the links above, and drag the A32NX folder inside the zip into your Community folder.

See below for the location of your Community folder:

For the Microsoft Store edition AND/OR Gamepass edition:

- Copy the "A32NX" folder into your community package folder.

It is located in:

* `C:\Users\[YOURUSERNAME]\AppData\Local\Packages\Microsoft.FlightSimulator_<RANDOMLETTERS>\LocalCache\Packages\Community`.

---

For the Steam edition:

- Copy the "A32NX" folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Roaming\Microsoft Flight Simulator\Packages\Community`.

---

For the Boxed edition:

- Copy the "A32NX" folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Local\MSFSPackages\Community`.


If the above methods do not work:
- You can find your community folder by going into FS2020 general options and enabling developer mode. You will see a menu appear on top. Go to tools and virtual file system. Click on watch bases and your community folder will be listed in one of the folders.
- Please make sure you're copying the "A32NX" folder into your community package folder, NOT the "flybywiresim-a32nx" folder.

***

## Contributing

See [Contributing.md](.github/Contributing.md)

### Known Issues

**(Please note that most issues are being worked on and some of them may even be fixed in the master branch)**

- Captain's PFD may occasionally turn off during flight
- No Smoking switch doesn't use a full range of motion.
- F/CTL page does not have working speedbrake integration
- BLEED page is not fully functional
- Automatic ECAM page switching has minor bugs
- APU/Engine fire covers cannot be retracted once opened
