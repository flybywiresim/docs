# DATA: Data Index Page

!!! block ""

    ![MCDU Data 1 Page](../../assets/a32nx-briefing/mcdu/data-1-page.png "MCDU Data 1 Page"){loading=lazy align=left width=46%}

    ![MCDU Data 2 Page](../../assets/a32nx-briefing/mcdu/mcdu-048.png "MCDU Data 2 Page"){loading=lazy align=right width=46%}

## Description

The DATA INDEX pages give access to various systems and databases in the aircraft.

PAGE 1 is dedicated to navigation systems and corresponding sub pages.

PAGE 2 is dedicated to navigation data that is entered or stored in the FMGS.

!!! attention ""
    This section will not cover all DATA INDEX pages as most are not useful in a simulation anyway or not implemented yet in the FlyByWire A32NX.

## DATA INDEX page 1

### POSITION MONITOR

![MCDU Data Position Page](../../assets/a32nx-briefing/mcdu/data-position.png "MCDU Data Position Page"){loading=lazy}

List of all FMGC computed positions using various methods. The positions of the different methods should be nearly identical.

- FMGC 1 (1L)
    - FMGC 1 calculated latitude and longitude, and the methods used by the FMGC for the calculation (Example: “3 IRS/DME/DME”).
- FMGC 2 (2L)
    - FMGC 2 calculated latitude and longitude, and the methods used by the FMGC for the calculation.
- RADIO or GPS or GPIRS (3L)
    - Onside FMGC calculated latitude and longitude, calculated from selected radio NAVAIDs (Example: DME/DME, VOR/DME, or LOC) or from GPS or GPIRS.
- MIX IRS (4L)
    - Onside FMGC calculated latitude and longitude, of the weighted mean inertial reference system (IRS) calculated from the available IRSs.
- IRS 1,2,3 (5L)
    - Deviation in nautical miles of each IRS position from the onside FMGC position.
    - Displays the IRS mode, which can be INVAL, ALIGN, NAV or ATT.

        !!! note ""
            Displayed INVAL when an ADIRS has failed, or the IRS position is not refreshed.

- FREEZE/UNFREEZE (6L)
    - To freeze (or unfreeze) all the data displayed on the page.
    - When frozen, the title of the page specifies the time at which it was frozen.

- SEL NAVAIDS (6R)
    - Access to selected NAVAIDs page.

### IRS MONITOR

![MCDU Data IRS Page](../../assets/a32nx-briefing/mcdu/data-irs.png "MCDU Data IRS Page"){loading=lazy}

This page is used to display the current IRS data the aircraft has from the 3 IRS systems.

- DRIFT AT XXXX (TITLE)
    - Displays “DRIFT AT” runway identifier in amber, if at least one IRS average drift is displayed.

        !!! attention ""
            Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

- IRS 1-3 (1R, 2R, 3R)
    - Access to the associated IRS pages.
    - Label line displays the mode (NAV, ALIGN, ATT or INVAL), the average drift (upon transition to DONE phase), and the Time To NAV (if IRS in align) for each IRS.
    - Displays the status message of the associated IRS in small green font.
    - List of available messages:
        - IR FAULT
        - CHECK C/B
        - DELAYED MAINT
        - CDU FAULT
        - ENTER PPOS
        - ENTER HEADING
        - SELECT ATT
        - REENTER PPOS
        - EXCESS MOTION
        - SYS BELOW -15 °
        - SWITCH ADR

    !!! attention ""
        Currently only partly available in the FBW A32NX for Microsoft Flight Simulator.

- SET HDG (5R)
    - Displayed, if at least one IRS is in ATT mode.
    - It allows initialization of a heading for IRS in ATT mode:
        ‐ If a heading has been entered in this field, or on the ADIRS panel, the value is displayed in blue.
        ‐ If not, amber boxes are displayed.

        !!! attention ""
            Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

![MCDU Data IRS1 Page](../../assets/a32nx-briefing/mcdu/data-irs1.png "MCDU Data IRS1 Page"){loading=lazy}

Displays the IRS parameters and GPS/IRS hybrid parameters.

- TITLE
    - Displays the selected IRS in large white font. When frozen, IRS is replaced by “IRS FROZEN AT” and the time at which the pilot has frozen the display.

- POSITION (1L)
    - Latitude/longitude given by the selected IRS.

- TTRK (2L)
    - True track

- THDG (3L)
    - True heading

- WIND (4L)
    - True wind direction/velocity

- GPIRS (5L)
    - GPS/IRS hybrid position of the IRS

- FREEZE/UNFREEZE (6L)
    - Allows to freeze or unfreeze all data displayed on all three IRS pages. When frozen, the title of the page specifies the time at which it was frozen. It is automatically unfrozen when exiting the page.

- GS (2R)
    - Ground speed

- MHDG (3R)
    - Magnetic heading

- GPIRS ACCUR (4R)
    - GPS/IRS Figure of Merit (meters or feet)

- NEXT IRS (6R)
    - This prompt calls up the next IRS page

### GPS MONITOR

![MCDU Data GPS Page](../../assets/a32nx-briefing/mcdu/data-gps.png "MCDU Data GPS Page"){loading=lazy}

- GPS 1,2 POSITION (1L, 4L)

- TTRK GPS 1, 2 (2L, 5L)
    - true track

- MERIT GPS 1, 2 (3L, 6L)
    - figure of merit (meters or feet)

- GS GPS 1, 2 (2R, 5R)
    - ground speed

- MODE/SAT (3R, 6R)
    - Mode of GPS 1, 2 and number of satellites tracked.
        - INIT: System initialization
        - ACQ: Satellite acquisition
        - NAV: Normal mode
        - TEST: System test
        - FAULT: Invalid system
        - ALTAID/AIDED: Degraded modes. GPS uses aircraft inputs for computation purposes.

- UTC (2, 5)
    - GPS 1, 2 UTC

- GPS ALT (3, 6)
    - GPS altitude is displayed for information purposes. It is not used by the FMGS.

### A/C STATUS

![MCDU Data Status Page](../../assets/a32nx-briefing/mcdu/data-status.png "MCDU Data Status Page"){loading=lazy}

Automatically displayed this page at power up.  Pilots may also call it up by pressing the DATA key on the MCDU console.

!!! attention ""
    Currently only partly available in the FBW A32NX for Microsoft Flight Simulator.

- TITLE
    - Aircraft Type

- ENGINE TYPE (1L)
    -Used this to calculate predictions.

- ACTIVE DATABASE (2L)
    - Validity period and part number (large font).

- SECOND DATABASE (3L)
    - Validity period in small font.
    - A press to the 3L key switches to the second database as the active database.

- CHG CODE (5L)
    - Entry of code to change the IDLE and/or PERF factor, displayed in 6L.
    - Displayed in the PREFLIGHT and DONE phases.
    - Label is displayed in small white font.
    - The brackets, or the entered value, is displayed in large blue font.

- IDLE/PERF (6L)
    - Aircraft must be on ground to enter values.
    - FMS displays default values from the Airline Modifiable Information (AMI) file if nothing is entered.
    - Default values are displayed in small font.
    - Manually entered values are displayed in large font.
    - When it is necessary to modify the IDLE or the PERF factor:
        ‐ ENTER the change code in the CHG CODE field (5L).
        - Default value for the code is “ARM” but can be modified in the Airline Modifiable Information (AMI) file.
        - With a valid code, the IDLE and PERF factors are displayed in blue.
        ‐ ENTER the new IDLE and/or PERF factor(s) in the scratchpad.
        ‐ PRESS the (6L) key to insert the new IDLE and/or PERF factor.
        - The new IDLE and/or PERF factors are displayed in large blue font.

- STATUS/XLOAD (6R)
    - Calls up the P/N STATUS and P/N XLOAD pages.

### CLOSEST AIRPORTS

![MCDU Data Closest Airports 1 Page](../../assets/a32nx-briefing/mcdu/data-closest-airports-1.png "MCDU Data Closest Airports 1 Page"){loading=lazy}

Automatically selected closest 4 airports from the current position. The

Pilots can add a 5th airport.

Page 1 displays the bearing, distance, and time to go to each airport.

- (1L - 4L)
    - Closest four airports from the database ordered by distance from the current position.
- BRG
    - Current bearing to the airport.
- DIST
    - Current great-circle distance to the airport.
- UTC
    - Predicted time to the airport
    - Computed using the current wind or a wind vector entered on page 2, and the speed according to the current mode (managed or selected).
    - This is only computed in cruise phase.

- (5L)
    - A 5th airport ICAO can be entered.
    - Can by modified at any time, even when “LIST FROZEN” is displayed.
    - WHen ICAO is not in the database, then “NOT IN DATABASE” appears in the scratchpad.

- EFOB/WIND (6R)
    - Gives access to page 2.
    - Automatically freezes the list of the four closest airports when pressed.

![MCDU Data Closest Airports 2 Page](../../assets/a32nx-briefing/mcdu/data-closest-airports-2.png "MCDU Data Closest Airports 2 Page"){loading=lazy}

Page 2 displays the EFOB and allows the crew to enter an effective wind to be flown to each airport.

- EFF WIND (1-5)
    - EFOB at each airport.
    - EFOB is only computed in cruise phase.
    - Enter an anticipated headwind or tailwind along the bearing to the airport. If entry is preceded by +, T, or TL, a tailwind is assumed.
    - If entry is preceded by -, H, or HD, a headwind is assumed.
    - Default value may be displayed, based on the current wind.
    - Used to compute the EFOB and time to the airport.

        !!! attention ""
            Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

- FREEZE/UNFREEZE (6L)
    - This prompt enables the pilot to freeze and unfreeze the list of four airports.
    - The list is automatically frozen when accessing page 2. It will remain frozen upon returning to page 1.
    - The “LIST FROZEN” message is always displayed on page 2.

## DATA INDEX page 2

![MCDU Data Index 2 Page](../../assets/a32nx-briefing/mcdu/data-index-2.png "MCDU Data Index 2 Page"){loading=lazy}

- WAYPOINTS (1L)
- NAVAIDS (2L)
- RUNWAYS (3L)
- ROUTES (4L)

These keys call up details of waypoints, NAVAIDs, runways, and routes
stored in the database.

!!! attention ""
    Currently not all of these are available in the FBW A32NX for Microsoft Flight Simulator.

- STORED WAYPOINTS (1R)
- STORED NAVAIDS (2R)
- STORED RUNWAYS (3R)
- STORED ROUTES (4R)

These keys call up waypoints, NAVAIDs, runways, and routes that the pilot has stored, to review and store them in, or delete them from, the database. The airline can choose to have all pilot-stored data automatically erased in the done phase.

!!! attention ""
    Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.
