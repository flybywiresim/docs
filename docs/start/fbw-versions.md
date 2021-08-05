# FlyByWire A32NX Versions

## Version Overview

=== "Development Version (recommended)"

    Development will have the latest features that will end up in the next stable. In general this version has the latest fixes and newest features but also a slightly higher risk of containing bugs as features had less time to be used and tested be users.

    This version updates often and sometimes several times a days. We recommend to update this version via our installer before every start of the simulator.

    Every addition to the development version is code reviewed and tested by several people, our QA Team and also interested users. In general it tends to be very stable and robust.

    Latest additions to this version can be seen either in the official [CHANGELOG](https://github.com/flybywiresim/a32nx/blob/master/.github/CHANGELOG.md) or the commits to the master branch of the project: : [Github Commits to Master](https://github.com/flybywiresim/a32nx/commits/master)

=== "Stable Version"

    !!! info ""
        **Current Stable Version - v0.6.2**

    Stable is our variant which has features which are the most mature and most tested so that it should be a reliable version for the more conservative user preferring stability over newest features.

    This version will not always be up to date but we work hard at ensuring its compatibility with the current version from Microsoft Flight Simulator.

=== "Experimental Version"

    This version is similar to the development version, but contains custom systems.

    !!! info ""
        Experimental is currently on **hold**.

    !!! warning ""
        **No support will be provided via Discord for Experimental versions.**

=== "Marketplace Version"

    This version is similar to Stable but is available via the Microsoft Flight Simulator in-sim marketplace.

    !!! warning ""
        **Due to Sim Update 5 platform stability issues that are out of our control, we have withdrawn the A32NX from the MSFS marketplace until further notice.**

## Version Comparison

This is curated list with the most important features for users and will
be updated at least once a month.

For all changes refer to the official
[CHANGELOG](https://github.com/flybywiresim/a32nx/blob/master/.github/CHANGELOG.md).

| Feature                                                  |   Stable 0.6.2   | Development<br/>(up to 4th Aug 2021) |
|:---------------------------------------------------------|:----------------:|:------------------------------------:|
| Stand alone aircraft                                     | :material-check: |           :material-check:           |
| EFB                                                      | :material-check: |           :material-check:           |
| EFB Simbrief Integration                                 | :material-check: |           :material-check:           |
| EFB Ground Handling                                      | :material-check: |           :material-check:           |
| Printer                                                  | :material-check: |           :material-check:           |
| Custom Electrical System                                 | :material-check: |           :material-check:           |
| Custom APU Simulation                                    | :material-check: |           :material-check:           |
| Improved Flight Model Accuracy                           | :material-check: |           :material-check:           |
| Split RMP1 and RMP2 Radios                               | :material-check: |           :material-check:           |
| Custom Camera Views                                      | :material-check: |           :material-check:           |
| Support for CONF 3 (flaps 3) Landings                    | :material-check: |           :material-check:           |
| TRK/SPA Mode                                             | :material-check: |           :material-check:           |
| GPWS Improvements                                        | :material-check: |           :material-check:           |
| Brake Fan                                                | :material-check: |           :material-check:           |
| MCDU/FMC Improvements                                    | :material-check: |           :material-check:           |
| Forced Usage of Modern Flight Model                      | :material-check: |           :material-check:           |
| Sim Update 5 (SU5) Fixes                                 | :material-check: |           :material-check:           |
| Custom Hydraulic System (initial implementation)         |                  |           :material-check:           |
| Connection between electrical power and hydraulics       |                  |           :material-check:           |
| VOR/ADF needles on ND                                    |                  |           :material-check:           |
| New PFD (in react)                                       |                  |           :material-check:           |
| BRG/DIST feature on ECAM PROG page                       |                  |           :material-check:           |
| Custom fly-by-wire system                                |                  |           :material-check:           |
| Custom Autopilot (with Autoland feature)                 |                  |           :material-check:           |
| Custom Autothrust                                        |                  |           :material-check:           |
| EFB Throttle Calibration                                 |                  |           :material-check:           |
| Improved AP, ROLL OUT and ground spoiler logic           |                  |           :material-check:           |
| Descent initiation via FCU V/S knob                      |                  |           :material-check:           |
| Improvement to Custom fly-by-wire system (protections)   |                  |           :material-check:           |
| Push FCU V/S knob during APPR to level off               |                  |           :material-check:           |
| More EVENTS and LVARS for external control<br/>          |                  |           :material-check:           |
| Seatbelt Sign sync to FCUIPC                             |                  |           :material-check:           |
| Hydraulics ECAM page                                     |                  |           :material-check:           |
| OVHD ANN Lt DIM functionality                            |                  |           :material-check:           |
| Brakes use Hydraulic System                              |                  |           :material-check:           |
| Custom Autobrake                                         |                  |           :material-check:           |
| APU heat blur                                            |                  |           :material-check:           |
| ISIS and CHRONO auto brightness                          |                  |           :material-check:           |
| ISIS brightness button push & hold                       |                  |           :material-check:           |
| Support FD OFF take-off procedure                        |                  |           :material-check:           |
| Improved FCU init values (SPD=100kts, HDG=0°, ALT=100ft) |                  |           :material-check:           |
| ILS auto-tuning for departure and approach               |                  |           :material-check:           |
| Scratchpad clear on CLR held                             |                  |           :material-check:           |
| Improved Cold Engine start-up model                      |                  |           :material-check:           |
| Adapted t.o. A/THR engagement                            |                  |           :material-check:           |
| ISA deviation on ECAM SD                                 |                  |           :material-check:           |
| MCDU Keyboard Input                                      |                  |           :material-check:           |
| New potentiometer for lights and screens                 |                  |           :material-check:           |
| Improved CHRONO logic                                    |                  |           :material-check:           |
| Pixalated Screens                                        |                  |           :material-check:           |
| Advanced ADIRs implementation                            |                  |           :material-check:           |
| Automatic and improved Cabin Pressurization              |                  |           :material-check:           |
| Preselected Speeds in ECAM PERF pages                    |                  |           :material-check:           |
| Correct QNH flashing at TL/TA                            |                  |           :material-check:           |
| Several Sound Enhancements                               |                  |           :material-check:           |
| Several Texture and Graphics enhancements                |                  |           :material-check:           |
| Auto print on printer when PRINTER is selected           |                  |           :material-check:           |
| EFB flyPadOS v2 new layout, add. settings and features   |                  |           :material-check:           |
| EFB Navigraph Integration                                |                  |           :material-check:           |
| EFB VATSIM/IVAO frequencies, landing performance)        |                  |           :material-check:           |
| EFB landing performance calculator                       |                  |           :material-check:           |
| Workaround for altitude issues of MSFS                   |                  |           :material-check:           |

