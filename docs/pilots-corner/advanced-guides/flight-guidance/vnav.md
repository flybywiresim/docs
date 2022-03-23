<link rel="stylesheet" href="/../../stylesheets/larger-admon-font.css">

# Vertical Guidance

![](../../../assets/UnderConstruction.jpg)

## Overview

Vertical guidance in the A320 is supporting the flight crew by providing guidance or automations for the vertical 
flight paths during a flight. This reduces the workload of the flight crew and allows for a nearly fully automated 
flight in combination with Lateral Guidance and Manged Speed.

Vertical guidance is available for TAKEOFF, CLIMB, CRUISE, DESCENT, and APPROACH phases of the flight plan. The flight 
planning capability lets the pilot enter published departure, arrival, and approach segments with individual pseudo
waypoints that include speed/altitude constraints. These constraints, as well as the entered cruise altitude and 
cost index, define the vertical profile.

Vertical guidance is managed by the Flight Management Guidance Systems (FMGS), in particular, the Flight Guidance 
Computer (FGC) which controls the Flight Directors (FD), the Autopilots (AP), and the Autothrust (A/THR).    

!!! warning "Real Life Considerations"
    It is the sole responsibility of the pilot to conduct proper flight planning and execution. It is not sufficient 
to solely rely on the automatic aircraft guidance and indications. All indications and guidance need to be 
reconfirmed with flight crew calculations. 

    This is especially true for indications like the **Top of Descent** which typically does not account for likely 
ATC interventions and often lead to late descents preventing ATC from issuing approach shortcuts and may even lead to 
forced holds to lose altitude. 

## Vertical Modes

Vertical guidance includes these modes:

| Guidance | MANAGED                   | SELECTED       |
|:---------|:--------------------------|:---------------|
| VERTICAL | SRS (TO and GA)           |                |
|          | CLB, DES                  | OP CLB, OP DES |
|          | ALT CST*, ALT CST         | ALT*, ALT      |
|          | ALT CRZ                   | EXPEDITE       |
|          | G/S*, G/S                 |                |
|          | FINAL, FINAL APP          |                |
|          | FLARE                     |                |

Find a detailed description of the modes in the blow chapters. 

Vertical guidance interacts closely with the autothrust system and the speed control modes selected in the FCU 
(managed vs. selected).

One of the main notable differences between Selected and Managed Vertical Guidance is that the managed mode accounts 
for altitude and speed constraints at waypoints and computes the vertical flight path accordingly.

## Selected Vertical Modes

### OP CLB

### OP DES

### V/S and FPA

### Expedite

### ALT/ALT*

## Managed Vertical Modes

- Accounts for altitude constraints at waypoints
- Accounts for speed constraints at waypoints (when in Managed Speed Mode)
- Energy and speed management
- Descent Profile Computation

### SRS 

### CLB

### ALT CST, ALT CST*

### ALT CRZ

### DES

#### Managed Speed in DES

- ECON DES speed or the descent speed manually entered in the PERF DES page of the FMS, or
- The speed constraint, or
- The manoeuvring speed of the current aircraft configuration, or
- VAPP.

### G/S, G/S*

### FINAL / FINAL APP

### FLARE

### Descent Strategies

#### Decelerated Approach (without CDA)

ILLUSTRATION
Source: [](https://safetyfirst.airbus.com/control-your-speed-during-descent-approach-and-landing/)

#### Continuous Descent Approach (CDA)

ILLUSTRATION

## Primary Flight Display Indications

- V/DEV Indication
- Speed Range 

## Navigation Display Indications

- symbols and explanations

## FMS (MCDU) PROG Page Indications

- V/DEV Indication

## Example Flight
