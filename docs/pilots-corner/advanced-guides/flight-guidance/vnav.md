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
The OPEN CLB mode is a selected mode. It uses the AP/FD pitch mode to maintain a SPD/MACH
(selected or managed) while the autothrust (if active) maintains maximum climb thrust.

When OPEN CLB is engaged, the target speed/Mach is maintained by adjusting the pitch with the
elevator, whereas thrust is maintained either by the A/THR, or manually by the flight crew. Speed
target may either be selected or managed.

The OPEN CLB mode disregards all altitude constraints up to the FCU selected altitude.

OP CLB mode can be engaged when:

‐ the aircraft has been in flight for more than 5 seconds
- LAND mode is not engaged
- the altitude selected in the FCU is higher than the present altitude

It is activated when:

- the flight crew pulls the FCU ALT knob
- guidance reverts to speed protection
- acceleration altitude is reached with CLB armed and lateral navigation (NAV) not engaged
- 

### OP DES
The OPEN DES mode is a selected mode. It maintains a SPD/MACH (selected or managed) with the AP/FD pitch mode while 
autothrust (if active) maintains IDLE thrust. It is not to be used for final approach.

When OPEN DES is engaged, pitch control maintains the target speed/Mach number, and autothrust
maintains idle thrust (or the flight crew maintains it manually). The speed target may be either
selected or managed.

The OPEN DES mode disregards all altitude constraints.

OP DES mode can be engaged when:

‐ the aircraft has been in flight for more than 5 seconds
‐ LAND mode is not engaged
- the altitude selected in the FCU is lower than the present altitude

It is activated when:
- the flight crew pulls the FCU ALT knob
‐ Selecting a manual speed when EXPEDITE mode is engaged.

### V/S and FPA
The V/S - FPA mode is a selected mode. It acquires and holds the vertical speed or the flight path angle displayed 
in the V/S - FPA window of the FCU. The HDG V/S -TRK FPA pb on the FCU allows the flight crew to select either type 
of reference to be used for guidance and for display on the PFD.

The FMGC pitch mode guides the aircraft to the target V/S or FPA. The corresponding A/THR mode is SPEED or MACH. The 
FMA displays V/S (FPA).

{--

The V/S (FPA) guidance has priority over the speed guidance. If the selected target V/S or FPA is too high (relative 
to the current thrust condition and speed), the FMGC will steer the aircraft to the target V/S or FPA, but the 
aircraft will also accelerate or decelerate.

When the speed reaches its authorized limit, V/S or FPA automatically decreases to maintain the
minimum (or maximum) speed limit.

--}

V/S-FPA can be engaged when:

- the aircraft has been in flight for more than 5 seconds
- the AP or FD are activated when they have been off
- changing target altitude by >250ft when in ALT^*^ mode
- selecting a higher altitude when in any descent mode
- selecting a lower altitude when in any climb mode

It engages automatically when:
- no other vertical mode is engaged after 5 seconds after lift off
‐ loss of G/S* or G/S mode
‐ loss of FINAL mode
‐ loss of LOC* or LOC mode
‐ loss of NAV mode when DES mode is engaged
‐ loss of vertical flight path in DES mode
‐ TCAS mode disengagement.

To immediate level off the aircraft the flight crew can push the FCU V/S knob or set the V/S to 0.

Note: If AP is engaged while a V/S is selected with only FD ON, the V/S will synchronise on the
current aircraft V/S.

### Expedite
Expedite mode is an OPEN mode used in climb or descent to reach the desired altitude with the
maximum vertical gradient.

When the aircraft is in EXP CLB, the target speed is Green Dot, which is maintained with pitch control. Autothrust, 
if active, sets the thrust at CLB THRUST automatically.

When the aircraft is in EXP DES, the target speed is 340 kt or M 0.8 which is maintained with pitch control. 
Autothrust, if active, sets the thrust at IDLE automatically.

When EXPEDITE is engaged, the system disregards SPD CSTR, ALT CSTR, and SPD LIM.

EXPEDITE can be engaged when
‐ the aircraft has been in flight for more than 5 s
‐ managed speed is available.

It is engaged manually only when
‐ the FCU selected altitude is higher than present altitude, EXP CLB mode engages
‐ the FCU selected altitude is lower than present altitude, EXP DES mode engages

### ALT/ALT*

## Managed Vertical Modes
Managed modes guide the aircraft along the vertical profile according to the data the pilot inserts into the MCDU. 
Flight Management (in the Flight Management and Guidance Computer) computes the corresponding guidance targets.

Managed modes accounts for altitude constraints at waypoints and also for speed constraints at waypoints when speed 
is in managed mode.

### SRS 

### CLB
CLB mode guides the aircraft in a managed climb, at either a managed or a selected target speed, to an FCU selected
altitude, taking into account altitude constraints at waypoints. The system also considers speed constraints if the
target speed is managed.

Climb mode gives the aircraft managed vertical guidance to the FCU selected altitude. It meets altitude constraints 
at waypoints either with managed speed incorporating speed constraints or with selected speed as target speed. The 
AP/FD pitch controls the speed or Mach number target and the A/THR is in thrust mode (CLB) corresponding to maximum 
climb thrust. The flight path may include several segments. The flight crew can arm the CLB mode during the takeoff, 
go-around, climb, and cruise phases and engage it during the climb and cruise phases.

The CLB mode can be armed under the following conditions:

- On ground or when in SRS mode
    - if no other vertical mode is activated
    - the acceleration altitude defined in the MCDU PERF TO or GA page is below the lowest altitude constraint and
      also below the altitude selected in the FCU
- In flight in climb or go-around phase
    - if lateral navigation (NAV) is engaged
    - if the altitude selected in the FCU is above the current altitude and the aircraft captures or flies an
      altitude constraint.

The CLB mode can be engaged when:

‐ the aircraft has been in flight for more than 5 seconds
- the altitude selected in the FCU is above the current altitude
- not in descent, approach, or go-around phase
- Lateral navigation (NAV) is engaged
- Not in G/S mode#

It is automatically engaged at acceleration altitude (ACC ALT) or when a waypoint with an altitude constraint is
passed while CLB mode was armed.

It can be manually engaged by pushing the FCU ALT knob while the CLB mode is not armed and the current altitude is
not at an altitude constraint.

- When CLB mode is engaged, the system arms ALT and displays the applicable target altitude on
  the ALT scale.
    - Magenta for another altitude constraint
    - Blue for a FCU selected altitude
- The guidance does not modify the target speed in order to satisfy an altitude constraint. Therefore, the
  constraint may not be met and may be predicted as missed
  ‐ When the aircraft levels off at the ALT CSTR, CLB mode arms automatically, then engages when the aircraft passes
  the constrained waypoint (if the FCU altitude is above the constraint altitude).

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

## TCAS Mode 
The TCAS mode is an Auto Flight System (AFS) guidance mode that provides vertical guidance in the case of a Traffic
Alert and Collision Avoidance System (TCAS) Resolution Advisory (RA). When a Traffic Advisory (TA) is triggered, the TCAS mode arms.

When a RA is triggered, the TCAS mode engages. The TCAS mode provides vertical guidance in accordance with the TCAS
RA order.

When clear of conflict (the “CLEAR OF CONFLICT” aural alert sounds), the TCAS mode disengages.

The AFS provides guidance toward the latest target altitude set on the FCU.

See or detailed guide for TCAS: [Traffic Alert and Collision Avoidance System](tcas.md)

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
- Target Alt (magnenta, blue) 
- FMA (link to PFD briefing?)

### Navigation Display Indications

- symbols and explanations
- Energy Circle
- Level-off Arrow

### FMS (MCDU) PROG Page Indications

- V/DEV Indication

## Example Flight

>> take off - press button until TOD; watch Netflix; press button again, autoland <<