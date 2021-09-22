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
    - This line shows the latitude and longitude, as calculated by the FMGC 1, and the navigation method used by the FMGC for that calculation (Example: “3 IRS/DME/DME”).
- FMGC 2 (2L)
    - This line shows the latitude and longitude, as calculated by the FMGC 2, and the navigation method used.
- RADIO or GPS or GPIRS (3L)
    - This line shows the latitude and longitude, calculated by the onside FMGC from selected radio NAVAIDs (Example: DME/DME, VOR/DME, or LOC) or from GPS or GPIRS.
- MIX IRS (4L)
    - This line shows the latitude and longitude of the weighted mean inertial reference system (IRS) calculated by the onside FMGC from the available IRSs.
- IRS 1,2,3 (5L)
    - This line shows the deviation in nautical miles of each IRS position from the onside FMGC position. It also displays the IRS mode, which can be INVAL, ALIGN, NAV or ATT.
      !!! note ""
          INVAL is displayed when an ADIRS has failed, or the IRS position is not refreshed.

- FREEZE/UNFREEZE (6L)
    - The pilot presses this key to freeze (or unfreeze) all the data displayed on the page. When the data is frozen, the title of the page specifies the time at which it was frozen.

- SEL NAVAIDS (6R)
    - The pilot presses this key to access the selected NAVAIDs page.

### IRS MONITOR

![MCDU Data IRS Page](../../assets/a32nx-briefing/mcdu/data-irs.png "MCDU Data IRS Page"){loading=lazy}

![MCDU Data IRS1 Page](../../assets/a32nx-briefing/mcdu/data-irs1.png "MCDU Data IRS1 Page"){loading=lazy}

### GPS MONITOR

![MCDU Data GPS Page](../../assets/a32nx-briefing/mcdu/data-gps.png "MCDU Data GPS Page"){loading=lazy}

### A/C STATUS

![MCDU Data Status Page](../../assets/a32nx-briefing/mcdu/data-status.png "MCDU Data Status Page"){loading=lazy}

### CLOSEST AIRPORTS

![MCDU Data GPS Page](../../assets/a32nx-briefing/mcdu/data-closest-airports.png "MCDU Data GPS Page"){loading=lazy}
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
