<link rel="stylesheet" href="/../../stylesheets/larger-admon-font.css">
<link rel="stylesheet" href="/../../stylesheets/toc-tables.css">

# Vertical Guidance

## Chapters

| Quick Links                                    |
|:-----------------------------------------------|
| [Vertical Modes](#vertical-modes-overview)     |
| [Selected Vertical Modes](./selected-modes.md) |
| [Managed Vertical Modes](./managed-modes.md)   |
| [Speed/Mach Control](./speed-control.md)       |
| [ND Symbols](./nd-symbols.md)                  |
| [PFD Indications](./pfd-indications.md)        |
| [Example Flight](./example.md)                 |

## Foreword
Vertical Guidance in the A320 is a huge topic and it will take a lot of time to master for many sim pilots. 

Also implementing it correctly and realistically is an enormous task and the FlyByWire team will be working 
continuously to extend and improve its implementation in the A32NX. 

Therefore, the level of detail in this guide is meant to provide FlyByWire A32NX users the ability to adequately use 
the vertical navigation features of the aircraft in the simulator without overburdening the user with an extreme 
level of detail.

If you have additional questions beyond the scope of this guide do not hesitate to come to the ([:fontawesome-brands-discord:{: .discord } - **FlyByWire Discord**](https://discord.gg/flybywire){target=new}) and visit our #flight-school channel. We have many real world pilots in our community who are happy to help and answer your 
questions.

## Overview

Vertical guidance in the A320 relieves the workload of the flight crew by providing guidance or automations for the 
vertical flight paths during a flight. This adds significantly to the safety of flights and allows for a nearly 
fully automated flight in combination with Lateral Guidance and Managed Speed.

Vertical guidance is managed by the Flight Management Guidance Systems (FMGS), in particular, the Flight Guidance
Computer (FGC) which controls the Flight Directors (FD), the Autopilots (AP), and the Autothrust (A/THR).    

Vertical guidance is available for TAKEOFF, CLIMB, CRUISE, DESCENT, and APPROACH phases of the flight plan. The flight
planning capability lets the pilot enter published departure, arrival, and approach segments with individual pseudo
waypoints that include speed/altitude constraints. These constraints, as well as the entered cruise altitude and
cost index, define the vertical profile.

!!! warning "Real Life and Online ATC Considerations"
    It is the sole responsibility of the pilot to conduct proper flight planning and execution. It is not sufficient 
    to solely rely on the automatic aircraft guidance and indications. All indications and guidance need to be 
    monitored and reconfirmed by the flight crew at all times.<p/> 
    This is especially true for Auto Flight where the flight crew must monitor all instruments and the flight in
    general constantly and they must be able to take over the flight manually at any moment.<p/>
    Always remember Airbus' Golden Rules:<p/>
    ![img.png](../../../assets/advanced-guides/vnav/goldenrules.png)

## Vertical Modes Overview 

The vertical modes are divided into two main modes:

- Selected Vertical Modes
- Manages Vertical Modes

One of the main notable differences between Selected and Managed Vertical Guidance is that the managed mode accounts
for altitude and speed constraints at waypoints and computes the vertical flight path accordingly. Selected mode on
the other hand ignore any constraints from the flight plan.

Vertical guidance includes these modes:

| [SELECTED](selected-modes.md)                                                | [MANAGED](./managed-modes.md)                                          |
|:-----------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [OP CLB](selected-modes.md#op-clb-open-climb)                                | [SRS](managed-modes.md#takeoff-srs-speed-reference-system) (TO and GA) |
| [OP DES](selected-modes.md#op-des-open-descent)                              | [CLB](managed-modes.md#clb-climb),                                     |
| [EXPEDITE](selected-modes.md#exp-expedite)                                   | [DES](managed-modes.md#des-descent)                                    |
| [V/S-FPA](selected-modes.md#vs-and-fpa-vertical-speed-and-flight-path-angle) | [ALT CST*](managed-modes.md#altitude-acquire-mode-alt-cst)             |
| [ALT*](selected-modes.md#altitude-acquire-mode-alt)                          | [ALT CST](managed-modes.md#altitude-hold-mode-alt-cst-alt-crz)         |
| [ALT](selected-modes.md#altitude-hold-mode-alt)                              | [ALT CRZ](managed-modes.md#altitude-hold-mode-alt-cst-alt-crz)         |
|                                                                              | [G/S*, G/S](managed-modes.md#gs-gs)                                    |
|                                                                              | [FINAL, FINAL APP](managed-modes.md#final-final-app)                   |
|                                                                              | [LAND](managed-modes.md#land)                                          |
|                                                                              | [FLARE](managed-modes.md#flare)                                        |
|                                                                              | [TCAS](managed-modes.md#tcas-mode)                                     |                                                              


Vertical guidance interacts closely with the Autothrust system and the speed control modes selected in the FCU
(managed vs. selected).

See the [Speed/Mach Control](speed-control.md) page for more information. 

## Additional Reading

We recommend this excellent "Safety First" article from airbus:<br/> 
[Control your Speed… During Descent, Approach and Landing](https://safetyfirst.airbus.com/control-your-speed-during-descent-approach-and-landing/){target=new}

## 320 Sim Pilot Video

<iframe 
    width="790" 
    height="480" 
    src="https://www.youtube-nocookie.com/embed/cFPgNqoV4GQ" 
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
