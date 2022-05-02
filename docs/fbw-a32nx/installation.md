# Installation Guide

Please follow the information on this page to install the FlyByWire Simulations A32NX addon for Microsoft Flight Simulator 2020

*Last Update: {{git_revision_date_localized}}*

!!! warning "Important Notice"

    All FlyByWire Simulations A32NX versions are now independent from the default A320neo.

    We’d like to remind all users of the following two **important changes**:

    The folder in the Community directory is now:

      - `flybywire-aircraft-a320-neo`

    The airplane in the simulator is now titled:

      - `FlyByWire Simulations - A320neo (LEAP)`

!!! danger "MSFS Marketplace Version Discontinued"
    Please uninstall any marketplace version.

    You can reference [this issue](support/reported-issues.md#invisible-aircraft) in our reported issues page for more details.

---

## Downloads

### FlyByWire Installer

Download the new FlyByWire installer where you can select either the Stable, Development, or Experimental build. Our installer downloads and installs the add-on directly into your community folder.

The following commands can be used:

++ctrl+f5++ - Refreshes Installer

++ctrl+f12++ - Opens the debug tool

#### Installer Debug Logs

You can send us logs to our [Discord](https://discord.gg/flybywire){target=new} for support if you encounter issues with the installer. Please follow the steps below:

  * Open the debug tool ++ctrl+f12++.

  * Find and select ++"Console"++ in the top menu.

  * ++"Right Click"++ anywhere in the log displayed.

  * Click ++"Save as"++ and send the log to us.

[Download Installer](https://api.flybywiresim.com/installer){ .md-button target=new}

### Manual Installation

!!! info "Download"

    === "Latest Stable Version"

        **Current Stable Version - ** <img src="https://img.shields.io/github/v/release/flybywiresim/a32nx.svg?color=2F4E5B&style=flat" />

          Stable is our variant that has the least bugs and best performance. This version will not always be up to date but we gurantee its compatibility with each major patch from MSFS. 

          [Download Stable](https://cdn.flybywiresim.com/addons/a32nx/stable/full.zip){ .md-button target=new}

          You can see the changelog on the releases page: [View Here](https://github.com/flybywiresim/a32nx/releases){target=new}


    === "Development Version"

        Development will have the latest features that will end up in the next stable. Bugs are to be expected. 

        It updates whenever something is added to the 'master' branch on GitHub. 

         [Download Development](https://cdn.flybywiresim.com/addons/a32nx/master/full.zip){ .md-button target=new}
         
         [**IMPORTANT:** View information on Autopilot / Fly-By-Wire here](feature-guides/autopilot-fbw.md)

    === "Experimental Version"

        This version is similar to the development version, but contains custom systems early in the development phase - expect issues.

        Currently the new upcoming update to the FlyByWire Custom Flight Management System (cFMS) is available in the Experimental version.

        Please read [Experimental Version Support Page](support/exp.md) before using this version.
    
        It will be updated with the latest changes to the development version every week or so while new major features are tested (not guaranteed).

        [Download Experimental](https://cdn.flybywiresim.com/addons/a32nx/experimental/full.zip){ .md-button target=new}

        !!! danger "No Support for Experimental - use at own risk"
            Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues.

---

**Please follow ALL steps in this section if you encounter any issues with installation before seeking support.**

Open the zip that you downloaded from one of the links above, and drag the `flybywire-aircraft-a320-neo` folder inside the zip into your Community folder.

See below for the location of your Community folder.

## Recommended Settings for A32NX, MSFS and Windows

See [Recommended Settings](settings.md).

## Community Folder

### Microsoft Store and/or Game Pass Edition

- Copy the `flybywire-aircraft-a320-neo` folder into your community package folder.

It is located in:

* `C:\Users\[YOURUSERNAME]\AppData\Local\Packages\Microsoft.FlightSimulator_<RANDOMLETTERS>\LocalCache\Packages\Community`.

---

### Steam Edition

- Copy the `flybywire-aircraft-a320-neo` folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Roaming\Microsoft Flight Simulator\Packages\Community`.

---

### Boxed Edition

- Copy the `flybywire-aircraft-a320-neo` folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Local\MSFSPackages\Community`.

---

### Troubleshooting

If the above methods do not work:

![How to find the correct Community folder](assets/find-community-folder.png "How to find the correct Community folder")

To find the Community folder that MSFS is using please follow these steps:

1. Go to your General Settings in MSFS and activate Developer Mode.
2. Go to the menu and select 'Virtual File System'.
3. Click on 'Packages Folders' and select 'Open Community Folder'.

This opens the Community folder in a Windows Explorer. Please ensure that your addons are installed in the folder that is opened.

---

If your issue is not related to installation visit - [**Reported Issues**](support/reported-issues.md)

---

## Clean Install Steps

### Automatic Clean Install

FBW Installer version 3.0.0 introduced the `Uninstall` feature. To perform an automatic clean install:

- Ensure you have the latest FBW Installer on your machine. 
    - The installer updates itself. If you would like to 
    download our installer again see the [FlyByWire Installer Section](#flybywire-installer).
- Click on the "Uninstall" button.

!!! tip ""
    This removes the aircraft from your community folder and the extra files in `%appdata` or `%localappdata`.

    Your `Work` folder is retained to save your throttle configuration, FDR files, and any other presets we save. 
    (These are small files and do not need to be deleted to fulfill a "clean install" state.)

### Manual Clean Install

If you would like to manually perform a clean install you first have to delete the 
`flybywire-aircraft-a320-neo` folder from your community folder.

We also store additional information related to the aircraft in a separate directory which is built when you load the aircraft in the simulator. You also need to delete the contents of this folder but not the folder itself. 

These locations are found below:

- [Microsoft Store Version](#microsoft-store-version)
- [Steam Version](#steam-version)

If the above folders are hidden to you follow the directions on [Microsoft's support site](https://support.microsoft.com/en-us/windows/view-hidden-files-and-folders-in-windows-10-97fbc472-c603-9d90-91d0-1166d1d9f4b5).

Once in the correct directory delete the files show here:

![localstate folder](https://cdn.discordapp.com/attachments/838062729398976522/869736690695172156/unknown.png){ width=70% }

!!! info "Work Folder"
    The locations below contain a "work" folder. We store two important things here that you may not want to delete:

    - Your EFB throttle configuration.
    - Our flight data recorder (for debugging purposes which we may ask you to provide).

    **It is up to you to keep this folder or not.**

#### Microsoft Store Version

The folder can be found here:

`%LOCALAPPDATA%\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\LocalState\packages\flybywire-aircraft-a320-neo\`

To quickly locate the `%localappdata%`:

- Press start
- Type in run into the start menu and press ++enter++
- Type into the box `%localappdata%`
- Press ++"OK"++

!!! warning ""
    This is not your community directory

#### Steam Version

The folder can be found here:

`%APPDATA%\Microsoft Flight Simulator\Packages\flybywire-aircraft-a320-neo\`

To quickly locate `%appdata%`:

- Press start
- Type in run into the start menu and press ++enter++
- Type into the box `%appdata%`
- Press ++"OK"++

!!! warning ""
    This is not your community directory

***

## Contributing

[:fontawesome-brands-github:{: .github } **GitHub Contributing.md**](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md){ .md-button target=new }

More info [A32NX Development Overview](../dev-corner/dev-guide/index.md)

***

## SimBrief Airframe

The FlyByWire Simulations simBrief airframe with correct weights is available below. Please select and update your airframe according to the version you are flying.

!!! info ""
    The airframe below will always be **kept up-to-date** thanks to Navigraph's new sharable airframe feature.

    Please stay tuned to our social media for updates.

- **All Versions**: ✈ [SimBrief Airframe Link](https://www.simbrief.com/system/dispatch.php?sharefleet=337364_1631550522735){target=new} - Credits: [@sidnov](https://github.
  com/sidnov){target=new}

Pilot ID can be found in the Optional Entries section of the Dispatch Options page.

To learn how to use the various features related to our simBrief integration see the page below.

[SimBrief Integration Guide](feature-guides/simbrief.md){.md-button}

