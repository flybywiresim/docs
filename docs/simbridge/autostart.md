# Starting Simbridge

## Autostart

Autostart is a feature provided by the FlyByWire Installer that allows SimBridge to be autostarted upon Windows start. SimBridge will live in the systems tray similiar to Navigraph Simlink. 


### Configuration

Upon installation of SimBridge you will be prompted to enable autostart, You can choose to enable or disable autostart. 
![autostart promp](assets/simbridge/autostart_prompt.png)

!!! info Notice
    If you choose to have autostart disabled you can still start simbridge from the installer

### Manual Start
If you choose to not enable autostart you can open Simbridge via the installer. Just select the `Start` button.
![simbridge running](assets/simbridge/manual_start_running.png)

If this is not your preference or it fails to start you can also open the tool by opening the `fbw-simbridge.exe` found in the folder, `flybywire-externaltools-simbridge`, in the [community folder](../fbw-a32nx/installation.md#Troubleshooting).
![simbridge executable location](assets/simbridge/exec_location.png)

# Stopping Simbridge
There's several avenues to stop simbridge to provide flexibility to you as the user, this also includes stopping simbridge from a remote device.

## Installer
- The simplest way is via the installer and selecting the stop button on the Simbridge page.

## Tray Icon
- By right-clicking the tray icon in your systems tray and selecting `Exit`, you can also stop SimBridge.

    ![quit simbridge](assets/simbridge/tray_stop.png)

## API Endpoint
- You can stop Simbridge by calling the health endpoint via http://{[host machine IP](troubleshooting.md#network-configuration)}:{[selected port](configuration.md#server-settings)}/health/kill
    - For example `https://192.168.1.21:8380/health/kill`


## Task Manager
- If you encounter issues when closing SimBridge normally, you can kill the `fbw-simbridge.exe` process in Task Manager.
![task manager stop](assets/simbridge/simbridge_stop_tm.png)