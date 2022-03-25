<link rel="stylesheet" href="/../../stylesheets/larger-admon-font.css">
<link rel="stylesheet" href="/../../stylesheets/toc-tables.css">

# Vertical Guidance

![](../../../../assets/UnderConstruction.jpg)

## Foreword
Vertical Guidance in the A320 is a huge topic and will take a lot of time for many sim pilots to master fully. 

Also implementing it correctly and realistically is an enormous task and the FlyByWire team will be working 
continuously to extend and improve its implementation in the A32NX. 

Therefore, the level of detail in this guide is meant to provide FlyByWire A32NX users the ability to adequately use 
the vertical navigation features of the aircraft in the simulator without overburdening the user with an extreme 
level of detail.

If you have additional questions beyond the scope of this guide do not hestitate to come to our Discord's 
\#flight-school channel. We have many real world pilots in our community who are happy to help and answer your questions.

![img.png](../../../assets/advanced-guides/vnav/goldenrules.png)


## Overview

Vertical guidance in the A320 supports the flight crew by providing guidance or automations for the vertical 
flight paths during a flight. This reduces the workload of the flight crew and allows for a nearly fully automated 
flight in combination with Lateral Guidance and Managed Speed.

Vertical guidance is available for TAKEOFF, CLIMB, CRUISE, DESCENT, and APPROACH phases of the flight plan. The flight 
planning capability lets the pilot enter published departure, arrival, and approach segments with individual pseudo
waypoints that include speed/altitude constraints. These constraints, as well as the entered cruise altitude and 
cost index, define the vertical profile.

Vertical guidance is managed by the Flight Management Guidance Systems (FMGS), in particular, the Flight Guidance 
Computer (FGC) which controls the Flight Directors (FD), the Autopilots (AP), and the Autothrust (A/THR).    

!!! warning "Real Life and Online ATC Considerations"
    It is the sole responsibility of the pilot to conduct proper flight planning and execution. It is not sufficient 
    to solely rely on the automatic aircraft guidance and indications. All indications and guidance need to be 
    reconfirmed by the flight crew with their own calculations.<p/> 
    This is especially true for indications like the **Top of Descent** which typically does not account for likely 
    ATC interventions and often lead to late descents preventing ATC from issuing approach shortcuts and may even lead to 
    forced holds to lose altitude.

!!! warning "Disclaimer"
    The level of detail in this guide is meant to provide FlyByWire A32NX users the ability to adequately use the  
    vertical navigation features of the aircraft.<p/>
    As this is a vast and complicated topic this guide can't cover everything. Additional sources and further 
    reading is recommended to master this topic.  

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
| [Descent Strategies](#descent-strategies)      |

## Vertical Modes Overview 

Vertical guidance includes these modes:

| [SELECTED](selected-modes.md) | [MANAGED](./managed-modes.md) |
|:------------------------------|:------------------------------|
|                               | SRS (TO and GA)               |
| OP CLB, OP DES                | CLB, DES                      |
| ALT*, ALT                     | ALT CST*, ALT CST             |
| EXPEDITE                      | ALT CRZ                       |
|                               | G/S*, G/S                     |
|                               | FINAL, FINAL APP              |
|                               | LAND, FLARE                   |

Find a detailed description of the modes in the sections below. 

Vertical guidance interacts closely with the Autothrust system and the speed control modes selected in the FCU 
(managed vs. selected).

One of the main notable differences between Selected and Managed Vertical Guidance is that the managed mode accounts 
for altitude and speed constraints at waypoints and computes the vertical flight path accordingly. Selected mode on 
the other hand ignore any constraints from the flight plan.

## Descent Strategies

### Continuous Descent Approach (CDA)

ILLUSTRATION
Source: [Airbus](https://safetyfirst.airbus.com/control-your-speed-during-descent-approach-and-landing/)


