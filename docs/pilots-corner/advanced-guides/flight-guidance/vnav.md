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

!!! warning "Real Life and Online ATC Considerations"
    It is the sole responsibility of the pilot to conduct proper flight planning and execution. It is not sufficient 
    to solely rely on the automatic aircraft guidance and indications. All indications and guidance need to be 
    reconfirmed by the flight crew with their own calculations.<p/> 
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

Selected modes guide the aircraft according to target values that the pilot selects and the
FCU windows display.

### OP CLB

### OP DES

### V/S and FPA

### Expedite

### ALT/ALT*

## Managed Vertical Modes
Managed modes guide the aircraft along the vertical profile according to the data the pilot inserts into the MCDU. 
Flight Management (in the Flight Management and Guidance Computer) computes the corresponding guidance targets.

Managed modes accounts for altitude constraints at waypoints and also for speed constraints at waypoints when speed 
is in managed mode.

### SRS 

### CLB

### ALT CST, ALT CST*

### ALT CRZ

### DES
The managed descent mode guides the aircraft along the FMS computed vertical flight path. The DES mode is preferred 
when conditions permit since it ensures the management of altitude constraints and reduces the operating cost when 
flying at ECON DES speed.

The DES mode is only available when the aircraft flies on the FMS lateral flight plan, i.e. when the aircraft uses 
the NAV horizontal guidance mode.

### Speed Target in Manged Vertical Modes
In flight, either the AP/FD pitch control, or autothrust may acquire and hold a target speed or Mach
number, depending on the engaged modes.

Speed control is:
‐ Managed when the target comes from the FMGS
‐ Selected when the target comes from the SPD/MACH FCU window.

During the descent, approach and landing the managed speed is equal to either:

- ECON DES speed or the descent speed manually entered in the PERF DES page of the FMS, or
- The speed constraint, or
- The manoeuvring speed of the current aircraft configuration, or
- V~APP~.

For this the AP and FD pitch modes can control a target SPD/MACH or a vertical trajectory, and the A/THR
mode can control a fixed thrust or a target SPD/MACH. However, the AP/FD and the A/THR cannot
both control a target SPD/MACH simultaneously.

Therefore, the AP/FD pitch modes and A/THR mode are coordinated as follows:
‐ If an AP/FD pitch mode controls a vertical trajectory, the A/THR mode controls the target SPD/MACH.
‐ If an AP/FD pitch mode controls a target SPD or MACH, the A/THR mode controls the thrust.
‐ If no AP/FD pitch mode is engaged, the A/THR mode reverts to controlling the SPD/MACH mode.

| AP/FD Pitch Modes                               | A/THR Modes          |
|-------------------------------------------------|----------------------|
| V/S - FPA                                       | SPEED/MACH MODE      |
| DES (geometric path)                            | SPEED/MACH MODE      |
| ALT*, ALT, ALT CRZ*. ALT CRZ, ALT CST*, ALT CST | SPEED/MACH MODE      |
| G/S*, G/S                                       | SPEED/MACH MODE      |   
| FINAL. FINAL APP                                | SPEED/MACH MODE      |
| TCAS                                            | SPEED/MACH MODE      |
| FD/AP OFF                                       | SPEED/MACH MODE      |
| CLB/DES (idle path)                             | THR (CLB, IDLE) MODE |
| OP CLB/OP DES                                   | THR (CLB, IDLE) MODE |
| EXP CLB/EXP DES                                 | THR (CLB, IDLE) MODE |
| SRS                                             | THR (CLB, IDLE) MODE |
| FLARE                                           | RETARD (IDLE)        |

### G/S, G/S*

### FINAL / FINAL APP

### FLARE

## Descent Strategies

### Decelerated Approach (without CDA)

ILLUSTRATION
Source: [](https://safetyfirst.airbus.com/control-your-speed-during-descent-approach-and-landing/)

### Continuous Descent Approach (CDA)

ILLUSTRATION

## Indications in Flight Instruments

###  Primary Flight Display Indications

- V/DEV Indication
- Speed Range 

### Navigation Display Indications

- symbols and explanations
- Energy Circle
- Level-off Arrow

### FMS (MCDU) PROG Page Indications

- V/DEV Indication

## Example Flight
