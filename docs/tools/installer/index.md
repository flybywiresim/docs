# Installer Guide

The installer will help you install the FlyByWire Simulation Addons into the right location for Microsoft Flight Simulator (2020 and 2024) to pick them up. It will also help you switch between versions and let you know when a new update is available.

## Capabilities

- Install the A32NX and A380X addons for both Microsoft Flight Simulator 2020 and 2024.
- Support all versions of the addons: Stable and Development, and multiple texture sizes for the A380X.
- Optimize downloads through our CDN, this downloads the files from a location close to you and only downloads the parts that needs updating.
- Supports both Microsoft Flight Simulator 2020 and 2024 in one installer, allowing you to switch between the two and support each of the community folders.
- Support other addons from partners.

## Microsoft Flight Simulator Version Support

![MSFS 2020 Installer View](assets/2020-view.png 'MSFS 2020 Installer View'){loading=lazy, width=310}
![MSFS 2024 Installer View](assets/2024-view.png 'MSFS 2024 Installer View'){loading=lazy, width=310}

The installer can be used to manage our addons for both simulators by switching between the two simulation versions. You can switch between versions by clicking the Microsoft Flight Simulator icon on the top left. It will switch between the logos of the the different simulator versions.

This will also change the Addon Developers shown in the menu. For Microsoft Flight Simulator 2024 the only enabled Addon Developer is FlyByWire Simulations. More will be added as they become available.

By switching simulator versions, the installer will look at the installed addons in the Community folder, as configured in the settings, for the selected simulator. This way, you can install the addons for both simulators at the same time, using their own Community folders (or a folder of your selection).

## Installer Settings

![FlyByWire Simulations Installer Settings](assets/settings.png 'FlyByWire Simulations Installer Settings'){loading=lazy}

Using the gear icon at the bottom left of the installer, you can open the settings. These settings should be set to a good value by default, but you can change them as you need them.

The following settings are available:

- **Microsoft Flight Simulator 2020** - Settings for Microsoft Flight Simulator 2020:
  - **Community Directory** - The Community folder of Microsoft Flight Simulator 2020, the installer will discover this folder automatically when you first start the installer, based on your MSFS 2020 installation. You can change it if it did not configure the correct folder.
  - **Install Directory** - The location where the addons will be installed. By default, this will point to the same Community folder. It can be changed if you want to place the files in a different folder.
- **Microsoft Flight Simulator 2024** - Settings for Microsoft Flight Simulator 2024:
  - **Community Directory** - The Community folder of Microsoft Flight Simulator 2024, the installer will discover this folder automatically when you first start the installer, based on your MSFS 2024 installation. You can change it if it did not configure the correct folder.
  - **Install Directory** - The location where the addons will be installed. By default, this will point to the same Community folder. It can be changed if you want to place the files in a different folder.
- **Separate location for temporary folders** - By default this will be disabled. By enabling it, you can set a different location where the installer will temporarily download and unpack the files, before moving them to the Install Directory for the selected simulator.
  - **Location for temporary folders** - The temporary location to download and unpack the files.
- **Disable Version Warnings** - When enabled, disables warnings in the installer about the developer version.
- **Use CDN Cache (Faster Downloads)** - When enabled, the installer will use our CDN solution to optimize downloads. This will be enabled by default, only disable it if you experience download issues.

## Troubleshooting

The following keyboard shortcuts can be used :

- **CTRL+F5** - Refreshes Installer
- **CTRL+F12** - Opens the debug tool

### Installer Debug Logs

You can send us logs to our [Discord](https://discord.gg/flybywire){target=new} for support if you encounter issues with the installer. Please follow the steps below:

- Open the debug tool **CTRL-F12**.
- Find and select **"Console"** in the top menu.
- **Right Click** anywhere in the log displayed.
- Click **"Save as"** and send the log to us.
