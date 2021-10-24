# F-PLN: Flight Plan Page

The MCDU F-PLN page is actually a series of page for the management of
the aircraft's active flight plan.

Revisions to the lateral and vertical flight plans can be made from
these pages. For lateral revision press the left LSK and for vertical
revision press the right LSK.

## Flight Plan A Page

![F-PLAN A Page](../../assets/a32nx-briefing/mcdu/f-plan-a-page.jpg
"F-PLAN A Page")

### General

The flight plan page A lists all waypoints of the active flight plan in sequence providing time, speed and altitude predictions.

The FROM waypoit (last waypoint overflown) is listed at the top and TO waypoint is listed in white as the second entry. This FROM-TO is called the active leg.

To scroll through the flight plan the vertical slew keys can be used. To return to the beginning of the flight plan page, the F-PLN key can be pressed.

The AIRPORT key serves as a fast slew key. It can be pressed to call up the next airport (DEST, ALTN, ORIGIN) to be displayed on the flight plan page.

!!! attention "AIRPORT key"
    Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

Between two waypoints the display shows:

- Name of the leg
- Bearing from the aircraft position to the TO waypoint
- Distance between the waypoints
- During an approach, this in-between line also defines the angle of the final descent path. For example, “2-3°” indicates that the leg is two nautical miles long, and the flight path angle is -3 °.
- Shows track (TRK) between the waypoints in lines 2 and 3. This is the outbound track of the next leg.

If the route contains a published missed approach procedure,it is shown in blue after the destination runway. It turns green when the go-around phase becomes active. After the last waypoint of the missed approach, the display shows the alternate flight plan in NAV mode.

!!! attention "Missed Approach Procedure and ALTN Flight Plan"
    Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

In NAV mode, the TO waypoint can only be cleared by using the DIR key .

#### Predictions
Predictions for all waypoints are calculated based on the current and predicted winds and displayed.

#### Constraints

For the climb, descent, and approach phases the nav database might define constraints for altitude and speed. Constraints can also be manually added by the flight crew ((except at origin, destination, FROM, and pseudo-waypoints).

Constraints are displayed in magenta, as long as predictions are not completed.

Once predictions are calculated, constraints are replaced by speed and altitude predictions, preceded by stars. If the STAR is magenta, the system predicts that the aircraft will match the constraint (altitude within 250 ft, speed not more than 10 kt above the constraints). If the star is amber, the system predicts that the aircraft will miss the constraint and the MCDU displays: “SPD ERROR AT WPT”.

Note: SPD and ALT CSTR may either be entered on the VERT REV page or directly on the F-PLN A page, whereas TIME CSTR may only be entered from the RTA page.

!!! attention "RTA Page"
    Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

#### Pseudo Waypoints

!!! bug "TODO"

Pseudo-waypoints are geographical positions corresponding to an event in the vertical flight plan:

- T/C (top of climb)
- T/D (top of descent),
- SPD/LIM (speed limit),
- DECEL (deceleration for approach), etc.

The display shows them as waypoints in parentheses.

#### Approach Display

The flight crew cannot enter an altitude constraint at destination or Missed Approach Point (MAP).

### Elements

- TITLE FLIGHT NUMBER
    - If no flight number has been entered, this is blank.
    - May display:
        - TMPY in yellow if a temporary flight plan exists
        - OFST in white, if a lateral offset is flown; or,
        - OFST in yellow, if a lateral offset revision is pending.

- Line 1 to Line 5 WPT, UTC, SPD, ALT
    - Display consecutive waypoints with associated predictions of time,
        speed or Mach and altitude.
    - Before takeoff TIME is displayed, and after takeoff UTC. UTC is
        displayed, if the pilot enters an estimated takeoff time (ETT).
    - The FROM waypoint (first line of the flight plan) displays values
        that the system memorized at waypoint sequencing.

- SPD/ALT (1R)
    - The field dedicated to SPEED or MACH is blank at the FROM
        waypoint, except at the departure airport. V1 associated with
        runway elevation, is displayed.
    - Note: When the HOLD marker is slewed, the HOLD SPD Label will
        overwrite the TIME/UTC title.
    - Note: The predicted altitude at a waypoint is related to the QNH
        below the transition altitude, and is given as a flight level
        above the transition altitude.

- DEST UTC/TIME DIST, EFOB (6)
    - DIST: Distance to destination along the displayed flight plan.
    - EFOB: Estimated fuel on board at destination. EFOB at destination
        will turn to amber, if it becomes less than the MIN DEST FOB
        value.
    - Line is permanent and displayed in white font once predictions are
        available. Not visible when a TMPY F-PLN is displayed or in some
        cases when an ALT CSTR is entered (“*CLB or DES*” prompt
        appears).

## Flight Plan B Page

## Lateral Revision Pages

## Vertical Revision Pages



## Fix Info Page

## Offset Page

## Airways Page

## Departure Pages

## Hold Pages

