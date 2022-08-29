# Holds

!!! warning "Not available in the Stable Version"

Holding patterns, as they are officially known, can be used as a delaying tactic for airborne aircraft. Typically holding patterns have a racetrack pattern that can easily be spotted on flight trackers. All holds are made up of segments. The segments are shown in the figure below. 

![DEFINITIONS](../../assets/advanced-guides/holds/Holddefinitions.png){loading=lazy}

## Why Hold?
Holds are always used to delay aircraft near a navigational fix in certain airspace. There are a lot of reasons airplanes might need to hold, where common examples would be:

- Bad weather passing over the airport
- Traffic
- To lose energy in the plane (altitude or speed)
- To burn off fuel

Sometimes holds are used because of topographical constraints. Innsbruck-Kranebitten International Airport (LOWI) is an excellent example of such a constraint because it is situated in a valley, as seen in the picture below.

![LOWI](../../assets/advanced-guides/holds/LOWI.png){loading=lazy}

## Identifying Holds

Aircraft can technically hold at any waypoint if given permission by or requested from ATC in advance. Holds that are published on aviation charts are called published holds. For this guide, we will only consider a published hold. Holds can be identified on charts in 2 different ways, where both options can be applied on the same chart. For example, look at the chart below.

![Hold types](../../assets/advanced-guides/holds/HOLD-types.png){loading=lazy}

Waypoints with published holds can be spotted by a racetrack pattern, or holds can be published and displayed in a diagram in one of the corners of the main navigation section on the chart. 

Now that you know where to hold, you should learn how to program the hold. Next, you will need to find information on the chart to enter into the FMS. The primary information you need to have are:

1. Name of the fix/waypoint
2. Inbound course
3. Turning direction
4. Length of the legs, either in time or distance (see Standards below)
5. Maximum airspeed (see Standards below)

!!! tip "Standards"
    There are standards for length of legs and airspeed that must be respected if no other information is present on the chart. The standards are published in [Hold Standards](#hold-standards).
 
 The inbound course/heading or the reciprocal of the hold is always depicted on the chart.

## Hold Examples    

??? info "Example charts to acquire hold information (click to expand)"

    === "1"

        ![HOLD1](../../assets/advanced-guides/holds/HOLD1.png){loading=lazy}

        | Hold information  | Details |
        |-------------------|---------|
        | Fix               | ARNUM   |
        | Inbound course    | 216°    |
        | Turning direction | Right   |
        | Leg distance      | STD     |
        | Max speed         | STD     |
        | Max alt           | FL140   |
        | Min alt (MHA)     | FL100   |

    === "2"

        >**_NOTE:_**  The altitude constraints of the fix SUGOL are not relevant for the altitude constraints of the hold at SUGOL. The same principle applies to speed restrictions as well.

        ![HOLD2](../../assets/advanced-guides/holds/HOLD2.png){loading=lazy}

        | Hold information  | Details |
        |-------------------|---------|
        | Fix               | SUGOL   |
        | Inbound course    | 110°    |
        | Turning direction | Right   |
        | Leg distance      | STD     |
        | Max speed         | STD     |
        | Max alt           | FL250   |
        | Min alt (MHA)     | FL70    |
        
    === "3"

        ![HOLD3](../../assets/advanced-guides/holds/HOLD3.png){loading=lazy}

        | Hold information  | Details |
        |-------------------|---------|
        | Fix               | OKLAX   |
        | Inbound course    | 149°    |
        | Turning direction | Left    |
        | Leg distance      | STD     |
        | Max speed         | 210KT   |
        | Max alt           | STD     |
        | Min alt (MHA)     | 8000FT  |

    === "4"

        >**_NOTE:_**  The chart's design makes it confusing what the leg length is for the DVN hold. You could argue that this is 3.4 NM. However, 3.4 is just the length between the D11.0 SPL and the DVN fix and does not influence the hold leg length.

        ![HOLD4](../../assets/advanced-guides/holds/HOLD4.png){loading=lazy}

        | Hold information  | Details |
        |-------------------|---------|
        | Fix               | DVN     |
        | Inbound course    | 053°    |
        | Turning direction | Right   |
        | Leg distance      | STD     |
        | Max speed         | 210KT   |
        | Max alt           | -       |
        | Min alt (MHA)     | 2900FT  |
    
    === "5"

        >**_NOTE:_**  Holds at BOTON and PANZE have a minimum hold altitude dictated by the minimum flight altitude of 6000FT of the earlier and following legs. 

        ![HOLD5](../../assets/advanced-guides/holds/HOLD5.png){loading=lazy}

        | Hold information  | Details | Details | Details |
        |-------------------|---------|---------|---------|
        | Fix               | BOTON   | PANZE   | CAMRN   |
        | Inbound course    | *049°   | *049°   | 041°    |
        | Turning direction | Right   | Left    | Left    |
        | Leg distance      | STD     | STD     | STD     |
        | Max speed         | STD     | STD     | 210KT   |
        | Max alt           | -       | -       | 14000FT |
        | Min alt (MHA)     | 6000FT  | 6000FT  | 6000FT  |
        
        *The inbound course can be calculated by subtracting or adding 180 to the reciprocal.

    === "6"

        ![HOLD6](../../assets/advanced-guides/holds/HOLD6.png){loading=lazy}

        | Hold information  | Details |
        |-------------------|---------|
        | Fix               | SKENS   |
        | Inbound course    | 274°    |
        | Turning direction | Right   |
        | Leg distance      | 10NM    |
        | Max speed         | STD     |
        | Max alt           | -       |
        | Min alt (MHA)     | 13000FT |

    === "7"

        ![HOLD7](../../assets/advanced-guides/holds/HOLD7.png){loading=lazy}

        | Hold information  | Details |
        |-------------------|---------|
        | Fix               | SNAAG   |
        | Inbound course    | 061°    |
        | Turning direction | Right   |
        | Leg distance      | 10NM    |
        | Max speed         | STD     |
        | Max alt           | -       |
        | Min alt (MHA)     | -       |

    === "8"

        ![HOLD8](../../assets/advanced-guides/holds/HOLD8.png){loading=lazy}

        | Hold information  | Details | Details |
        |-------------------|---------|---------|
        | Fix               | TIGER   | BIG     |
        | Inbound course    | 315°    | 302°    |
        | Turning direction | Right   | Right   |
        | Leg distance      | STD     | STD     |
        | Max speed         | STD     | STD     |
        | Max alt           | FL240   | FL150   |
        | Min alt (MHA)     | FL150   | FL70    |

    === "9"

        ![HOLD9](../../assets/advanced-guides/holds/HOLD9.png){loading=lazy}

        | Hold information  | Details | Details | Details |
        |-------------------|---------|---------|---------|
        | Fix               | DDM     | EGN     | KEA     |
        | Inbound course    | 059°    | 059°    | 335°    |
        | Turning direction | Left    | Left    | Right   |
        | Leg distance      | STD     | STD     | STD     |
        | Max speed         | 230KT   | 230KT   | 230KT   |
        | Max alt           | -       | -       | -       |
        | Min alt (MHA)     | 6000FT  | 4000FT  | 5000FT  |

    === "10"

        >**_NOTE:_**  The leg length for the CRS hold is presented as a distance from another navigational beacon

        ![HOLD10](../../assets/advanced-guides/holds/HOLD10.png){loading=lazy}

        | Hold information  | Details         |
        |-------------------|-----------------|
        | Fix               | CRS             |
        | Inbound course    | 001°            |
        | Turning direction | Left            |
        | Leg distance      | Until D34.0 CVO |
        | Max speed         | STD             |
        | Max alt           | -               |
        | Min alt (MHA)     | FL120           |
     
## Hold Standards

The Airbus FMS follows ICAO definitions for default holding pattern parameters. The default leg length for a computed hold is:

| Altitude (ft MSL)  | Leg distance |
|-------------------|--------------|
| <=14000           | 1 minute     |
| > 14000           | 1.5 minutes  |

The managed speed target in a hold is the lowest of:
- maximum endurance (approximately "green dot" speed)
- ICAO speed limit (see table below)
- speed constraint
- speed limit, if below speed limit altitude

The ICAO speed limits are as follows:

| Altitude (ft MSL) | Airspeed (KIAS) |
|-------------------|-----------------|
| < 14000           | 230             |
| 14000 - 20000     | 240             |
| 20000 - 34000     | 265             |
| > 34000           | .83 Mach        |

The default turn direction for a computed hold is **right**, in-line with ICAO specifications. 

## Programming Holds 
Now that all information about the hold is known, it is time to create a hold in the FMS via the MCDU. A step by step guide to hold at SKENS is provided below.

![HOLD6](../../assets/advanced-guides/holds/HOLD6.png){loading=lazy}

### MCDU Setup

!!! info "MCDU Setup"

    === "1"

        ![MCDU](../../assets/advanced-guides/holds/MCDU-hold-1.png){loading=lazy}

        Find the waypoint in the F-PLN page on the MCDU. Select the corresponding line. In this case, the 3rd from the top, SKENS, and push the left line selector key (LSK) for SKENS.
    
    === "2"

        ![MCDU](../../assets/advanced-guides/holds/MCDU-hold-2.png){loading=lazy}

        In this page, select the 3rd LSK to enter the hold section for the SKENS waypoint.

    === "3"

        ![MCDU](../../assets/advanced-guides/holds/MCDU-hold-3.png){loading=lazy}

        Notice the title of the page is called COMPUTED HOLD at SKENS. 
        
        Computed means that this is information provided by the simulator. This information can be wrong and can be edited by overwriting the computed data. 

    === "4"
        ![MCDU](../../assets/advanced-guides/holds/MCDU-hold-4.png){loading=lazy}

        As can be seen by the bigger symbols, the inbound course 274 is inserted in the FMS
        
        Note that the title has changed to HOLD, and a REVERT TO COMPUTED appeared.  REVERT TO COMPUTED will restore all hold settings and revert to the computed hold settings.

    === "5"

        ![MCDU](../../assets/advanced-guides/holds/MCDU-hold-5.png){loading=lazy}

        As can be seen in the chart, the hold has a leg length of 10NM. To enter this in the FMS type `/10` in the MCDU and select LSK3 to feed it in the TIME/DIST box. 
        The time needed to complete the leg is also re-calculated and is 3.3 minutes in this case. 

        If leg distance is constrained by time (as it is for a standard hold), this can be set by typing for example `1.5` in the MCDU and feeding it in the TIME/DIST box. Also, the leg distance will automatically be re-calculated.

        ![HOLD6](../../assets/advanced-guides/holds/HOLD6.png){loading=lazy}

    === "Last Exit"

        !!! warning "Not yet implemented"

        ![MCDU](../../assets/advanced-guides/holds/MCDU-hold-5.png){loading=lazy}

        In the bottom section of the MCDU screen, 'LAST EXIT' can be found. The section compromises a UTC and FUEL reading. Last exit gives information on how long the airplane can safely stay in the hold while still having the fuel for the rest of the approach, to go around, divert and the final reserve fuel. The UTC and FUEL will give you the time and minimum fuel needed when leaving the hold. 

    === "6"

        ![MCDU](../../assets/advanced-guides/holds/MCDU-hold-7.png){loading=lazy}

        If the inbound course, turning direction and leg distance are set correctly, press the 6th LSK on the right to insert the hold into the Flight plan. 

        Notice the white curved arrow in the ND. In this case, it is turned to the right; however, the arrow would turn left if left-hand turns were selected for the hold.
        Also, notice how the hold waypoint now appears for an additional time in the flight plan. This is needed for the FMS to calculate a good exit path when leaving the hold.

        Depending on the angle between the aircraft and the inbound course of the hold, aircraft need to fly different entry patterns. The A320 will automatically fly the correct entry pattern.

    === "7"
        ![MCDU](../../assets/advanced-guides/holds/MCDU-hold-8.png){loading=lazy}
        
        As soon as the aircraft is heading to the waypoint with the hold programmed, the hold will be calculated and completely shown on the ND. [IMM EXIT*](#leaving-the-hold) will also appear on the MCDU. 

    === "8"
        ![MCDU](../../assets/advanced-guides/holds/MCDU-hold-9.png){loading=lazy}

        Before the A320 passes the hold fix for the first time, it will slow down to 'green dot speed'. This is the speed at which the aircraft uses the minimum fuel per hour to ensure it can stay in the hold as long as possible. So make sure to set speed to managed speed to fly at green dot speed. 

        Also, the F-PLN page on the MCDU will continue to show IMM EXIT*. This is needed when [leaving the hold](#leaving-the-hold).

### Descending in the Hold
Altitude changes are done with the vertical speed mode set at 1000 ft/min. This is to make sure all aircraft are spaced out enough to comply with spacing safety standards.

The TCAS system should remain on TA/RA when flying in the hold. However, it might be convenient to switch to ALL or BLW.

### Leaving the Hold

The plane will continue to fly in the hold until a pilot gives the command to the FMS to leave. During the hold, the F-PLN page will display IMM EXIT in amber. The pilot has to press the right LSK next to IMM EXIT to leave the hold. The amber text will now change in RESUME HOLD. The aircraft will fly the shortest distance to the original hold fix and then exit, such as doing a tight circle or turning early on downwind. The aircraft will continue its flight plan when it reaches the hold fix again. 

RESUME HOLD can be pressed to cancel the hold exit. The aircraft will now stay in the hold, and IMM EXIT is shown again.

![Hold Modes](../../assets/advanced-guides/holds/MCDU-hold-14.png){loading=lazy}

## Video Tutorial by 320 Sim Pilot

<iframe width="826" height="465" src="https://www.youtube.com/embed/NYlSICln1So" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


