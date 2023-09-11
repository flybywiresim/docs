---
title: Crossbleed Engine Start
---

# Crossbleed Engine Start

## Overview

This procedure is used when a normal APU Bleed start is not possible, usually due to the APU being inoperative. 

It may be prudent to inform ATC that you will be performing a crossbleed start as the procedures and process may take longer than a normal start and carry certain risks both 
to the ground crew and the airport infrastructure.

!!! warning "Realistic Situations"
    It is important to note that crossbleed engine starts **should not** be performed under the following conditions in real life:

    - During pushback operations
    - Situations where the thrust of the engine would endanger life or property

## Procedure

To explain this procedure we will assume that `ENG 1` is running and the flight crew will start `ENG 2` using the crossbleed procedure.

### Initial State

Before using this procedure ensure:

- One engine should already be started and AVAIL. This allows the bleed air from the running engine to be used to start the other engine.
- `APU BLEED` - `OFF`
- `ENG MODE` - `NORM`

!!! tip ""
    Currently the A32NX does not have the capability to air start the engines. This procedure is included for completeness and will be updated when the feature is implemented.

    For now you would have to start a single engine normally (`APU ON` and `APU BLEED ON`) before carrying on with a crossbleed start.

### Overhead Bleeds Configuration

`ENG BLEED` for the receiving engine needs to be switched `OFF`. This is to prevent the bleed air from the running engine from escaping through the receiving engine 
(reverse flow leakage).

The `X BLEED VALVE` should be switched to the `OPEN` position.

Ensure that `ENG 2 BLEED` is `OFF` for this sample procedure.

[crossbleed photo here]

### Engine Start

1. Begin by verifying the bleed page on the upper ECAM display. 
     - Crucially that the bleeds on both sides are connected via the `X BLEED` valve and that the `ENG 2 BLEED` valve is closed (indicated by the amber line above IP for engine 2).

2. Deselect the Bleeds page and turn the `ENG MODE` to `IGN/START`. 
     - This should display the ENGINE page on the upper ECAM display.

3. Ensure that the IGN Bleed PSI for `ENG 2` is at or above 30 PSI before attempting to start the engine. 
     - It is not unusual on the NEO to see the pressure be at or above 30 PSI at IDLE power. If the pressure is below 30 PSI, increase the thrust of the running engine. 

4. Switch `ENG MASTER 2` to the ON position. **Maintain at least 25 PSI during the entire start procedure**.  

!!! warning ""
    It is common to lose pressure during the start sequence. Advance the `THR LEVERS` of the supplying engine (`ENG 1` in this scenario) to maintain at least 25 PSI.

    If thrust required approachs 40% N1 to maintain at least 25 PSI, ensure the surrounding area continues to be clear of obstructions. If you exceed 40% N1 there maybe issues 
    with your configuration and consider aborting the procedure.

The engine should start normally if you have followed the procedure correctly.

### After Start Procedure

Once both engines are started ensure the following in order:

1. Set `ENG 1` thrust lever to `IDLE`
2. Turn the `X BLEED` switch on the overhead panel back to `AUTO`
3. Turn `ENG 2 BLEED` switch back to `ON`
4. Continue your regular flows and procedures before taxi out
