---
title: Crossbleed Engine Start
---

# Crossbleed Engine Start

This procedure is used when // 

!!! warning "Realistic Situations"
    It is important to note that crossbleed engine starts **should not** be performed under the following conditions in real life:

    - During pushback operations
    - Situations where the thrust of the engine would endanger life or property

## Procedure

To explain this procedure we will assume that ENG #1 is running and the flight crew will start ENG #2 using the crossbleed procedure.

### Initial State

Before using this procedure check:

- One engine should already be started and AVAIL. This allows the bleed air from the running engine to be used to start the other engine.
- APU BLEED - OFF
- ENG MODE - NORM

!!! tip ""
    Currently the A32NX does not have the capability to air start the engines. This procedure is included for completeness and will be updated when the feature is implemented.

    For now you would have to start a single engine normally with the APU ON and APU BLEED on before carrying on with a crossbleed start.

### Overhead Bleeds Configuration

ENG BLEED for the receiving engine needs to be switched to the OFF position. This is to prevent the bleed air from the running engine from escaping through the receiving engine 
(reverse flow leakage).

The X BLEED VALVE should be switched to the OPEN position.

[crossbleed photo here]

### Engine Start

Begin by verifying the bleed page on the upper ECAM display. Crucially that the bleeds on both sides are connected via the X BLEED valve and that the ENG 2 BLEED valve is 
closed (indicated by the amber line above IP for engine 2).

Deselect the Bleeds page and turn the END MODE to IGN/START. This should display the ENGINE page on the upper ECAM display.
