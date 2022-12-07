# Discontinuities

## What are Discontinuities?

Discontinuities are breaks in the flight plan and often separate two flight plan sections like the SID and first in-route waypoint or the STAR and the APPR. They are also often inserted when the flight plan is modified.

There are basically two types of discontinuities:

- Discontinuities between two waypoints in the flight plan
- Discontinuities after a MANUAL leg (Manual Termination)

### Special Case

!!! warning "STAR and Approach Discontinuity - Inaccuracy"
    If your STAR contains other waypoints after the IAF (initial approach fix) that you have selected via an approach transition (VIA), the FMS will not automatically connect 
    the STAR to the approach at at the IAF.

    This is a small problem with our current implementation. It will be corrected when we 
    update to version 2 (fms-v2) of our implementation which contains even better simulation of the 
    Honeywell FMS.

## Discontinuities Between Waypoints

These discontinuities <span style=color:red>should not</span> be cleared from the flight plan in normal operations. Typically, you will notice a discontinuity in the following 
instances:

- Between the SID and the rest of your route.
- Between the STAR and the selected approach.

!!! tip ""
    Approaches that are radar vectored without a MANUAL will also have a discontinuity by design. Please be aware of these approaches and follow the principles outlined below.

Ideally the NAV mode automatically reverts to the HDG (TRK) mode and pilots should follow ATC guidance (if on network) or use the DIR TO function to proceed to the next 
waypoint on your flight plan.

[Learn How to Use Direct Feature](direct.md){.md-button}

!!! info "Normal Discontinuity in the MCDU F-PLN Page"
     ![Normal Discontinuity](../../assets/advanced-guides/disco/mcdu-discontinuity-1.png "Normal Discontinuity")

## Discontinuities After MANUAL Leg

Sometimes discontinuities are also part of a procedure to indicate that manual guidance is required (mostly directed by ATC). The preceding legs are called MANUAL legs (Manual Termination leg).

A MANUAL leg stays on a constant TRK or HDG and has no termination point.

The core principle of a MANUAL leg is that air traffic control (ATC) will give the flight crew headings (vectors) or a direct-to instruction to guide the aircraft to the planned approach path.

If no ATC is available (or when using MSFS ATC) the user must use heading mode (Selected HDG) or direct to (DIR TO) to guide the aircraft to an appropriate intercept course for the approach.

[Learn How to Use Direct Feature](direct.md){.md-button}

<style>
    .md-typeset .admonition.block, .md-typeset details.block {
        text-align: center;
    }
</style>

!!! info "Discontinuities after MANUAL legs cannot be cleared from the flight plan."
    ![Manual Leg Discontinuity](../../assets/advanced-guides/disco/mcdu-discontinuity-2.png "Manual Leg Discontinuity"){width=45% loading=lazy}

!!! info "DIR TO to next waypoint or Selected HDG"
    !!! block ""
        ![DIR TO to next waypoint](../../assets/advanced-guides/disco/mcdu-discontinuity-dirto.png "DIR TO to next waypoint"){width=47% loading=lazy}
        ![Heading to intercept ILS](../../assets/advanced-guides/disco/mcdu-discontinuity-heading.png "Heading to intercept ILS"){width=48% loading=lazy}

If the aircraft is flying into a MANUAL leg, NAV mode remains engaged and predictions assume that the aircraft will fly a direct leg from its present position to the next waypoint.

### Illustrations for MANUAL Legs

!!! info "Conceptual principle of a MANUAL leg"
    ![Conceptual illustration of MANUAL leg and discontinuity](../../assets/advanced-guides/disco/mcdu-discontinuity-manual-conceptual.png "Conceptual illustration of MANUAL leg and discontinuity"){loading=lazy}

!!! info "Example chart with Manual leg"
    ![Manual leg discontinuity on chart](../../assets/advanced-guides/disco/mcdu-discontinuity-manual-chart.png "Manual leg discontinuity on chart"){loading=lazy}
    ![Manual leg discontinuity on chart](../../assets/advanced-guides/disco/mcdu-discontinuity-manual-chart_1.png "Manual leg discontinuity on chart"){loading=lazy}
    <sub>*Copyright © 2021 Navigraph / Jeppesen<br/>
    "Navigraph Charts are intended for flight simulation use only, not for navigational use."*


!!! info "Manual leg in ND Plan Mode and in ARC Mode"
    !!! block ""
        ![Manual leg discontinuity on ND plan mode](../../assets/advanced-guides/disco/mcdu-discontinuity-manual-nd-plan.png "Manual leg discontinuity on ND plan mode"){width=48% loading=lazy}
        ![Manual leg discontinuity on ND](../../assets/advanced-guides/disco/mcdu-discontinuity-manual-nd.png "Manual leg discontinuity on ND"){width=48% loading=lazy}
    !!! warning "MANUAL label to be removed!"
        The MANUAL label on the ND will be removed in a future version as it is not displayed in the real aircraft.




