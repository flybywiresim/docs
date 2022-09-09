# Autoland

## Introduction

The FlyByWire A32NX has implemented the Airbus A320 Autoland feature. This guide shall give you a realistic description on when and how to use successfully.

!!! info "Standard Operation"
    The focus of this guide is on standard operations without failures as these are not yet implemented in the A32NX.

In flight simulation the Autoland feature is a very often requested feature as many simmers use it as a replacement to learn how to land manually. And for recreational flight simulation this is of course ok.

In real life autoland is very rarely used and requires extra training and certifications by the flight crew. In fact most pilots feel it's more stressful as they are not in control but need to monitor the systems very closely so they can take manual control at any time.

This is on top of the fact that autoland is mostly used in very bad visual situations where the pilots can't see anything and have to trust the autopilot to successfully perform the autoland.

In summary:

- Autoland is not a replacement for learning and training how to land manually.
- Special training and certifications are required for real pilots.
- Aircraft and airport and airport must have the appropriate capability.
- It requires a high amount of preparation and limiting conditions need to be checked constantly (e.g. maximum crosswind).
- Autoland requires high focus from the flight crew monitoring the systems and to always be ready to take over for a go around. Pilot monitoring (PM) usually will look outside the aircraft while pilot flying (PF) will watch the instruments.

## Real World Considerations

### When to Use Autoland

When low visibility operations (LVO) CAT III are enforced use of Autoland is required. LVO operations are either 
announced via ATIS are ATC. 

Performing an Autoland is permissible for CAT II / CAT III runways when low visibility procedures (LVP) are not 
enforced and this may even extend to CAT I runways. 

Autolands can also be subject to local procedures and authorities.

### When Not to Use Autoland

- ATC restrictions
- Airport capabilities missing or restrictions in place.
- Aircraft capabilities missing and limitations exceeded.
- If CAT1 is displayed on the FMA, Autoland is not authorized.

### Crew Requirements

Airbus requires an operator to be Low Visibility Operation (LVO) certified to perform an Autoland. Other training 
may also be required before being able to perform an Autoland. It is also the responsibility of the operator to 
maintain the LVO certification or any approvals by airworthiness authorities to perform automatic landings.

### Airport Requirements

The airport must be equipped with the appropriate ILS CAT (category) capability. 

- CAT III - LVP (Low Visibility Procedure) enforced
- CAT II / CAT III - LVP (Low Visibility Procedure) not enforced
- CAT I - Operators have a list of runways that are authorized to use Autoland with CAT I

!!! danger "Low Visibility Operations (LVO) Not Enforced"
    If the flight crew opts to perform an Autoland on a CAT II / CAT III capable runway when LVO is not enforced 
    (checked with ATIS or ATC) the runway **must be considered a CAT I runway**.

    Crews should be alert to ILS beam / signal contamination since the LOC/GS signal strength may not be guaranteed.

CAT I runway considerations before using Autoland:

- Pilots must be ready to disconnect the AP if any ILS fluctuations are detected.
- CAT II should at least be indicated on the FMA and the flight crew should apply the respective CAT II / CAT III 
  FCOM procedures.
- Visual contact should be established at the CAT I Minimum at the latest.

### Aircraft Limitations

All Airbus aircraft are certified to land automatically. However, limitations and conditions specified in the FCOM 
must be taken into account. Be aware that other not-so-obvious Autoland-limitations, such as maximum airfield 
altitude, maximum (minimum) GS angle or maximum runway slope, must also be considered. 

In addition, the flight crew must monitor possible day-to-day technical restrictions (stated in the MEL), or the 
consequence(s) of a failure that may have occurred during the flight and that may downgrade landing capability.

Autoland many not be performed outside of these limitations:

- Max. Crosswind: 20ft
- Max. Headwind: 30kt
- Max. Tailwind: 10kt
- Glide slope angle smaller than -2.5° or greater than -3.25°
- Airport elevation above 9 200 ft
- Aircraft weight below 44.000 kg (97.004 lb)
- Aircraft weight above the maximum landing weight
- Automatic landing is not allowed below -2.000 ft pressure altitude

## Autoland HowTo

### Preparations

- Check aircraft capability and limitations
- Check airport capability and limitations
- Check aircraft status
- Check Minima
  - ILS CAT II: MDH 100ft
  - ILS CAT III SINGLE: MDH 50ft
  - ILS CAT III DUAL: no DH (minimum RVR 75m)

### ILS Approach

- An autoland procedure is very similar to a normal ILS approach and landing
- Follow the Beginner Guide procedure until the end of this [chapter](../../beginner-guide/landing.md#3-preparation-and-checklist-for-landing)
- Instead of what is described in the [Beginner Guide for manual landing](../../beginner-guide/landing.md#4-landing) 
  you will not deactivate the Autopilot AP1 but instead you will activate the AP2 

### FMA Annunciations

The following FMA annunciations will be displayed during the approach and landing:

- SPEED
- G/S
- LOC
- CAT 3 DUAL (alarm when downgraded)
- AP 1+2
- 1 FD 2
- A/THR
- MINIMUM (or NO DH)
- At 350ft: LAND
- At 30ft: FLARE
- At 30ft: THRUST IDLE
- ROLL OUT (nosewheel touchdown)

### Flow From 1000ft

Autoland is technically not much different from a normal ILS landing apart from the fact that the Autopilot(s) will 
not be turned off for the landing but stay on and the flight crew "only" monitors the landing via the instruments.

Assuming that we are fully configured for landing at 1000ft above ground, with CONFIG 3 or CONFIG FULL, V~appr~ 
speed, gear down, autobrake armed, ground spoilers armed, ECAM landing memo no blue, landing checklist complete.

See [Beginner Guide Preparation and Checklist for Landing](../../beginner-guide/landing.md#3-preparation-and-checklist-for-landing)

- At 1000ft: callout "one thousand".
- At 500ft: now callouts every hundred feet.
- Shortly after the 400 callout and before 350ft the FMA must show LAND in green to signal that the aircraft is now 
  in landing mode.
- At 350ft: check the ILS course on the PFD.
- At 150ft: The white line signifying the ground on the PFD attitude indicator starts to move up.
- At 100ft: callout "hundred".
- At 50ft: callout "fifty" and now callouts every 10 ft
- At 40ft: the FMA must show FLARE or otherwise the flight crew needs to either perform a manual landing if 
  visual references are acquired or perform a go around.
- Autothrust FMA should switch to THRUST IDLE.
- Between about 20ft and 10ft the aircraft corrects its crosswind crab angle to bring its longitudinal axis in line 
  with the runway.
- At 10ft: callout "Retard" commands the PF to set the throttle levers to idle.
- At touchdown:
    - FMA shows ROLL OUT - autopilot keeps aircraft on center line
    - Both thrust levers to reverse thrust (idle or max as appropriate)
    - PM checks and calls out: "touchdown", "spoilers", "reversers", "auto brake", "descel".
- At 70kts: PM announces "70kts"
- At about 40-60kts: PF will set both thrust levers to idle 
- Before 20kts: the PF manually brakes to deactivate the autobrake and also 
  disconnect the autopilot.
- At taxi speed: disengage autopilots
- From here on it is a normal [runway exit](../../beginner-guide/landing.md#5-vacate-runway) and 
  [taxi procedure](../../beginner-guide/after-landing.md).


### When Things go Wrong

Always remember the Golden Rules: Fly, Navigate, Communicate!

- Fly the aircraft manually!
- Perform a [Go-Around](#go-around)
- Inform ATC and follow instructions

### Go-Around

!!! tip "We are planning an advanced guide for the Go-Around procedure. Stay tuned."

- Simultaneously apply the following three actions:
  - Thrust levers to TOGA to ensure SRS GA mode and then to FLX/MCT for a GA SOFT mode.
  - Rotate the aircraft towards 15° pitch up.
  - Announce "Go Around".
- Flaps: retract one step or as required.
- Check the FMA: MAN GA SOFT / SRS / GA TRK or NAV / A/THR (in blue).
  - If FMA does not display MAN GA SOFT or MAN TOGA set thrust levers to TOGA.
- Check positive climb and retract gear.
- Use NAV or HDG mode as required.
- Engage AP as required.
- At Go-Around Thrust Reduction Altitude set thrust levers to CL.
- At Go-Around Acceleration Altitude monitor that the target speed increases to green dot.
- Set flaps as required.
- At S speed: `FLAPS 0`, disarm `GND SPLRS`, turn off `NOSE` light, `RWY TURN OFF`, `LAND LIGHTS` as required. 
- Complete `After TakeOff Checklist`. 

See also [Beginner Guide Initial Climb](../../beginner-guide/takeoff-climb-cruise.md#3-initial-climb)

## Autoland Video

![video-embed](https://www.youtube.com/embed/Q1hACfew68Y)

