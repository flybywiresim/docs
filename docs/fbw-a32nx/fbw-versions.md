# Versions and Features

## Version Overview

=== "Development Version (recommended)"

    Development will have the latest features that will eventually end up in the next stable release. 
    
    In general this version has the latest fixes and newest features but also a slightly higher risk of containing bugs as features had less time to be used and tested by users.

    This version updates often and sometimes several times a days. We recommend to update this version via our installer before every start of the simulator.

    Every addition to the development version is code-reviewed and tested by several people, our QA Team and also interested users. In general it tends to be very stable and robust.

    Latest additions to this version can be seen either in the official [CHANGELOG](https://github.com/flybywiresim/a32nx/blob/master/.github/CHANGELOG.md) or the commits to the master branch of the project: [Github Commits to Master](https://github.com/flybywiresim/a32nx/commits/master){target=new}

=== "Stable Version"

    !!! info ""
        **Current Stable Version - v0.7.0**

    Stable is our version which has features that are the most mature and most tested. This should be a reliable version for those users preferring stability over newest features.

    This version will not always be up to date but we work hard at ensuring its compatibility with the current version from Microsoft Flight Simulator.

=== "Experimental Version"

    This version is similar to the development version, but contains custom systems in earlier development phases.
    
    Currently the new FlyByWire Custom Flight Management System (cFMS) is available in the Experimental version.
    
    The experimental version will be updated with the latest changes to the cFMS regularly and also with the latest changes to the Development version. Expect updates about once a week (not guaranteed).     
    
    !!! warning 

    Please read [Experimental Version Support Page](support/exp.md) before using this version.

    !!! danger "No Support for Experimental - use at own risk"
        Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues. You can report issues in the Discord channel "#ata-22-fms" in the thread "[CFMS LNAV ONLY Bugs + Issues](https://discord.com/channels/738864299392630914/876140343735771147/882442909918584862){ target=new }".

=== "Marketplace Version"

    This version is similar to Stable but is available via the Microsoft Flight Simulator in-sim marketplace.

    !!! warning ""
        **Due to Sim Update 5 platform stability issues that are out of our control, we have withdrawn the A32NX from the MSFS marketplace until further notice.**

## Version Comparison

??? note "Included in Stable Version 0.7.0"
    - Standalone Aircraft
    - EFB
    - EFB Simbrief Integration
    - EFB Ground Handling
    - Printer
    - Custom Electrical System
    - Custom APU Simulation
    - Improved Flight Model Accuracy
    - Split RMP1 and RMP2 Radios
    - Custom Camera Views
    - Support for CONF 3 (flaps 3) Landings
    - TRK/SPA Mode
    - GPWS Improvements
    - Brake Fan
    - MCDU/FMC Improvements
    - Forced Usage of Modern Flight Model
    - Sim Update 5 (SU5) Fixes (Aug 9th)
    - Custom Hydraulic System (initial implementation)
    - Connection between Electrical Power and Hydraulics
    - VOR/ADF Needles on ND
    - New PFD (in react)
    - BRG/DIST Feature on ECAM PROG Page
    - Custom Fly-by-wire System
    - Custom Autopilot (with Autoland feature)
    - Custom Autothrust
    - EFB Throttle Calibration
    - Improved AP, ROLL OUT and Ground Spoiler Logic
    - Descent Initiation via FCU V/S Knob
    - Improvement to Custom Fly-by-wire System (Protections)
    - Push FCU V/S Knob during APPR to Level off
    - More EVENTS and LVARS for External Control
    - Seatbelt Sign Sync to FCUIPC
    - Hydraulics ECAM Page
    - OVHD ANN Lt DIM functionality
    - Brakes use Hydraulic System
    - Custom Autobrake
    - APU Heat Blur
    - ISIS and CHRONO Auto Brightness
    - ISIS Brightness Button Push & Hold
    - Support FD OFF Take-off Procedure
    - Improved FCU init values (SPD=100kts, HDG=0°, ALT=100ft)
    - ILS Auto-tuning for Departure and Approach
    - Scratchpad clear on CLR held
    - Improved Cold Engine Start-up Model
    - Adapted t.o. A/THR Engagement
    - ISA Deviation on ECAM SD
    - MCDU Keyboard Input
    - New Potentiometer for Lights and Screens
    - Improved CHRONO Logic
    - Pixelated Screens
    - Advanced ADIRs Implementation
    - Automatic and Improved Cabin Pressurization
    - Preselected Speeds in ECAM PERF Pages
    - Correct QNH Flashing at TL/TA
    - Several Sound Enhancements
    - Several Texture and Graphics Enhancements
    - Auto Print on Printer when PRINTER is Selected
    - EFB flyPadOS v2 New Layout, add. Settings and Features
    - EFB Navigraph Integration
    - EFB VATSIM/IVAO Frequencies, Landing Performance
    - EFB Landing Performance Calculator
    - Workaround for Altitude Issues of MSFS
    - Initial implementation of failures ( [#5359](https://github.com/flybywiresim/a32nx/pull/5359){target=new} )
    - EFB: Make OFP font size persistent ( [#5538](https://github.com/flybywiresim/a32nx/pull/5538){target=new} )
    - Un-mirror sharklet textures ( [#5490](https://github.com/flybywiresim/a32nx/pull/5490){target=new} )
    - Improved handling of rudder axis plus/minus ( [#5636](https://github.com/flybywiresim/a32nx/pull/5636){target=new} )
    - EFB: Power Button  ( [#5624](https://github.com/flybywiresim/a32nx/pull/5624){target=new})
    - EFB: Tabbed Settings Page and Auto-brightness Option ([#5524](https://github.com/flybywiresim/a32nx/pull/5524){target=new})
    - Completed custom sounds for all sounds
    - Cockpit door lock sounds
    - Realistic reduction of loudness of chimes in cockpit when door locked
    - Notification Popup when changes to settings need reload ([#5261](https://github.com/flybywiresim/a32nx/pull/5261){target=new})

### New Features in the Development Version since Release of Stable 0.7.0

*Last Update: 14. Sep 2021*

- Added language translations ( [#5599](https://github.com/flybywiresim/a32nx/pull/5599){target=new} )
- Improved pitch/C* and ALT* laws ( [#5711](https://github.com/flybywiresim/a32nx/pull/5711){target=new} )
- EFB: Physical power button ( [#5697](https://github.com/flybywiresim/a32nx/pull/5697){target=new} )
- MCDU Keyboard settings moved to EFB ( [#5754](https://github.com/flybywiresim/a32nx/pull/5754){target=new} )

