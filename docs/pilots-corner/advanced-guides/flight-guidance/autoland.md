# Autoland

??? info "Notes"
    - Technical How To
        - ILS capture
        - both APs (CAT IIIB)
        - FMA Info during the approach
            - LOC / GS
            - LAND (350ft)
            - FLARE (30ft)
            - ROLL OUT (nosewheel touchdown)
        - Crosswind correction / de-crabbing (~20ft)
        - Retard callout
        - Limits (<CAT IIIB)
        - Minimums (<CAT IIIB)
        - STATUS PAGE check for downgrades of CAT
        - Downgrade audio alarm
        - AUTOLAND alarm
        - GO AROUND conditions
        - PF/PM Call outs
        - Checks after touchdown
    - Real World considerations
        - When is it used in real life
        - Pilot training and certifications required
        - Airport readiness / airport need to prepare low vis procedures
        - Summary
            - Check aircraft, crew and airport capability
            - Minima - CAT??
            - both AP
            - Monitor FMAs
            - be prepared to GA any time if aircraft does not behave as expected

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

- weather conditions
    - cross wind <20ft
    - head wind ??
    - tail wind ??
- pilot training - pilots need to do this regularly to keep certification
    - 2 times a year in simulator in Germany
- CAT III in general and A/B/C types

### Crew Requirements

Airbus requires an operator to be Low Visibility Operation (LVO) certified to perform an Autoland. Other training may also be required before being able to perform an Autoland. It is also the responsibility of the operator to maintain the LVO certification or any approvals by airworthiness authorities to perform automatic landings.

### Airport Requirements

!!! info "Airport Requirement Misunderstandings"
    Performing an Autoland is permissible for CAT II/CAT III runways when low visibility procedures (LVP) are not enforced and this may even extend to CAT I runways. However, it is important to note that while LVO (CAT III) **requires** the use of Autoland.

    All of the above may also be subject to local procedures and authorities.

Below is a list of considerations before using of Autoland:

- CAT III - LVP Enforced
- CAT II/CAT III - LVP Not Enforced
- Operators have a list of runways that are authorized to use Autoland
  - List should cross checked with AFM/FCOM limitations and any precautions when performing an Autoland on CAT I runways

CAT I runway considerations before using Autoland:

- Pilots must be read to disconnect the AP if any ILS fluctuations are detected
- CAT II should at least be indicated on the FMA and the flight crew should apply the respective CAT II / CAT III FCOM procedures
- Visual contact should be established at the CAT I minimum at the latest

## Autoland HowTo

### Preparations

- Check aircraft capability
- Check airport capability
- Check Limitations - cross winds
- Check aircraft status
- Minima - CAT??

### ILS Approach

- normal ILS plus dual AP

### FMA Annunciations

- AP 1+2
- A/THR
- CAT IIIB (alarm when downgraded)
- MINIA (NO DH)
- LOC / G/S
- SPEED

- LAND (350ft)
- FLARE (30ft)
- THRUST IDLE (30ft)
- ROLL OUT (nosewheel touchdown)

### Crew Checks and Callouts

- LOC / GS
- LAND (350ft)
- FLARE (30ft)
- THRUST IDLE (30ft)
    - Retard Callout (10ft)
- Touchdown:
    - Spoilers
    - Reversers
    - Descel
- ROLL OUT (nosewheel touchdown)

### Flow From 1000ft

Autoland is not much different from a normal ILS landing apart from the fact that the Autopilot(s) will not be turned off for the landing but stay on the pilot only monitors the landing via the instruments.

Assuming that we are fully configured for landing at 1000ft above ground, with CONFIG 3 or CONFIG FULL, V~appr~ speed, gear down, autobrake armed, ground spoilers armed, ECAM landing memo no blue, landing checklist complete.

!!! bug "TODO - add screenshots"

- At 1000ft: callout "one thousand".
- At 500ft: Now callouts every hundred feet.
- Shortly after the 400 callout and before 350ft the FMA must show LAND n green to signal that the aircraft is now in landing mode.
- At 150ft: The white line signifying the ground on the PFD attitude indicator starts to move up.
- At 100ft: callout "hundred".
- At 50ft: callout "fifty" and now callouts every 10 ft
- Shortly after 50ft FMA must show FLARE or otherwise the flight crew needs to perform a go around.
- Also the autothrust FMA should switch to THRUST IDLE.
- Between about 20ft and 10ft the aircraft corrects its crosswind crab angle to bring it  longitudinal axis in line with the runway.
- At 10ft: Callout "Retard" commands the PF to set the throttle levers to idle.
- At touchdown:
    - FMA shows ROLL OUT - autopilot keeps aircraft on center line
    - PM checks and calls out: "touchdown", "spoilers", "reversers", "auto brake", "descel".
- At about 40-60kts the PF will manually brake to deactivate the autobrake and also disconnect the autopilot.
- From here on it is a normal runway exit and taxi procedure.

### Go Around

- when
- how

### When Things go Wrong

- fly manually
- do go around

### Miscellaneous

- CAT II/CAT III holding points on ground
