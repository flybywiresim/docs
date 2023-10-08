# Reported Issues

<link rel="stylesheet" href="/stylesheets/toc-tables.css">
!!! danger  "STOP - Read this First"

    Please try removing all other mods/liveries from the community folder and test our add-on again. This will help rule out conflicts.

    *Most reported issues are caused by conflicts with other mods and liveries. If this does not resolve your issue, please continue below.*

    **Throttle Calibration is Required** - [Guide Here](../feature-guides/flypados3/throttle-calibration.md)

    ---

    <img src="https://img.shields.io/github/v/release/flybywiresim/aircraft.svg?color=2F4E5B&style=flat" /> <img src="https://img.shields.io/badge/dynamic/json?color=00848A&label=Development&query=shortSha&url=https%3A%2F%2Fapi.flybywiresim.com%2Fapi%2Fv1%2Fgit-versions%2Fflybywiresim%2Faircraft%2Fbranches%2Fmaster&style=flat" alt="Development Version" />

    FBW Installer - [Download Here](https://api.flybywiresim.com/installer){target=new} / *Latest Sim Version: 1.34.16.0*

!!! warning "Read our Support Guide"

    1. [Learn how to fly an A32NX](index.md#1-learn-how-to-fly-the-a32nx)
    2. [Troubleshoot](index.md#2-how-to-troubleshoot)
    3. [Research Known Issues](index.md#3-research-known-issues)
    4. [Report Issue on Discord](index.md#4-report-issue-on-discord)
    5. [Report Issue on the FBW Aircraft GitHub](index.md#5-report-issue-on-the-a32nx-github)
    6. [Collecting Support Information](index.md#collecting-support-information)

    ---

    Due to the complex nature of our custom autopilot, please visit the dedicated ^^Custom Autopilot / Fly-By-Wire^^ page for more information:

    - [**Main Page**](../feature-guides/autopilot-fbw.md)
    - [**Typical Issues + Solutions**](../feature-guides/autopilot-fbw.md#typical-issues-and-how-to-solve-them)
    - [**Known Issues**](../feature-guides/autopilot-fbw.md#known-issues)

    ---

    Please visit the ^^Dedicated Custom Flight Management System^^ page for more information:

    - [**Features + Issues**](../feature-guides/cFMS.md)
    - [**Special Notes**](../feature-guides/cFMS.md#special-notes)

    ---

    If you're having issues with ^^SimBridge^^, please follow our dedicated guide for it:
    
    - [**SimBridge Troubleshooting Guide**](../../simbridge/troubleshooting.md)

    ---

    Do this before reporting bugs.
---

<!--

TEMPLATE

??? issue "Issue Headline"

!!! tip ""
    *Affected versions: Stable, Development*

^^Description^^
^^Root Cause^^
^^Possible Solution or Workaround^^
^^Additional Information^^

-->

##  Index

| Quick Links                                                                            |
|:---------------------------------------------------------------------------------------|
| [Commonly Reported Issues](#commonly-reported-issues)                                  |
| [Solutions to Commonly Reported Issues](#solutions-to-commonly-reported-issues)        |
| [FBW Installer Issues](#fbw-installer-issues)                                          |
| [Incompatible and Problematic Add-ons/Mods](#incompatible-and-problematic-add-onsmods) |

## Use the Browser's Search Function

On Desktop, press ++ctrl+'F'++ to search for an issue within the current page.

## Legend

!!! bug "Breaking Issue / Bug"
!!! warning "Non-Breaking Issue / Inconvenience"
!!! tip "Config Issue / Usage Issue"

## Commonly Reported Issues
The following list of issues are commonly reported on our Discord support channel. Please check these before reporting any other issue on Discord.

*Last Update: {{git_revision_date_localized}}*

## FBW Installer Issues

??? bug "Download Issues - FBW Products"
### Download Issues - FBW Products

    ^^Description^^

    In certain situations, your ISP may block our CDN (Content Distribution Network) served by Cloudflare. Cloudflare allows us to save costs when users download our aircraft from our installer to 
    provide a seamless installation process for a variety of our products.

    Additionally, any disturbance to the stability of your connection may cause any downloads to fail and may need to be retried when you have a more stable connection.

    ^^Common Error Codes^^

    - ECONNRESET
    - ETIMEDOUT
    - ENOTFOUND
    - HTTP 403

    ^^Possible Solution or Workaround^^

    We recommend one of the following actions:

    1. TEMPORARY Solution: Try a VPN - a great free one that's reliable is [ProtonVPN](https://protonvpn.com/).
        - Please do your own due diligence and research when utilizing a VPN, even with our recommended one above.
    2. Download a full build from our website [here]() - Please ensure you follow our [manual installation instructions](../installation.md#manual-installation).
    3. Contact your ISP to check with them if there are any existing issues utilizing Cloudflare on their network.

    ^^Additional Information^^

    Below is a list of countries that are possibly affected by this issue. Please note that it may not be *every* ISP in the country.

    - Brazil
    - China
    - Iberia
    - Portugal
    - Saudi Arabia
    - Spain

??? bug "Installer Permission Problems"
### Installer Permission Problems

    ^^Description^^

    During installation of a product a "Windows Permission Error" with the error code EPERM shows up and the installation is aborted.

    ^^Root Cause^^
    
    Sometimes the permissions of the community folder are set to not allow the current user to install addons in it.
    This might be set since the installation of MSFS or MSFS might have changed it at some point.
    
    ^^Possible Solution or Workaround^^

    One of the following solutions usually lets the desired addon be installed

    * Check the permissions of the community folder and correct them.
    * Rename the current community folder, create a new one with the same name and move your installed addons into the new community folder.
    * Start the installer with admin permissions.
