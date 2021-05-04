# Preparing the MCDU

This guide will help you prepare the MCDU in the A32NX for your departure. It includes a simple route so you can follow along easily and replicate in the simulator.

The simBrief Route used in this guide - [Available Here](../assets/beginner-guide/sample-ofp.pdf)

***

## Pre-requisites 

Below are a few pre-requisites before programming the MCDU. Visit [Starting the Aircraft](#) to learn more. 

* Make sure the aircraft is powered up.
    * External Power OR APU
* Make sure the ADIRS are set to NAV. 
* Have a valid flight plan. 

***
  
## Understanding the MCDU

During the course of this guide we will be referring to a few key terms that which are defined below. 

=== "Left Select Key (LSK)"

    `LSK` for short. These are on the left hand side of the MCDU screen. They are highlighted in the image below and are referenced in descending order. Top being `LSK1` and the lowest key `LSK6`

    ![Placeholder](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/638px-Placeholder_view_vector.svg.png)

=== "Right Select Key (RSK)"

    `RSK` for short. Much like `LSK`, these are on the right hand side of the MCDU screen. They are highlighted in the image below and are referenced in descending order. Top being `RSK1` and the lowest key `RSK6`

    ![Placeholder](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/638px-Placeholder_view_vector.svg.png)

=== "Slew Keys"

    These keys are referenced below. 

    ![Placeholder](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/638px-Placeholder_view_vector.svg.png)

    !!! info

        === "Horizontal Slew Keys"

            These keys allow you to scroll between certain page i.e. `INIT A` and `INIT B` when the INIT page is selected. 

        === "Vertical Slew Keys"

            These keys allow to scroll vertically on certain pages i.e. `F-PLN` page. 

***

## MCDU Programming 

**D.I.F.F.S.R.I.P.P**

Pilots commonly use the acronym above when programming the MCDU. It represents the following:

`DATA - INIT A - FLIGHT PLAN - FUEL PRED - SECONDARY FLIGHT PLAN - RADNAV - INIT B - PROG - PERF`

For simplicity's sake this portion of the guide will be split into three sections.

* Section 1 - [DATA - INIT A - FLIGHT PLAN](#section-1)

* Section 2 - [FUEL PRED - SECONDARY FLIGHT PLAN - RADNAV](#section-2)

* Section 3 - [INIT B - PROG - PERF](#section-3)

The simBrief Route used in this guide - [Available Here](../assets/beginner-guide/sample-ofp.pdf)

***

### Section 1

=== "DATA"

    This MCDU page provides various data for the pilots. It has two pages (accessed by using the horizontal slew keys). It will not be used for this tutorial. 

    DATA includes the pages below:

    * Position Monitor
    * IRS Monitor
    * GPS Monitor
    * A/C Status
    * Closest Airports
    * Equitime Point
    * Waypoints
    * NavAids
    * Runway
    * Route

=== "INIT A"

    ![Placeholder](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/638px-Placeholder_view_vector.svg.png)

    ^^FROM/TO Field^^

      * Using the keypad type in `EGFF/EGCC`
      * Once this is in the scratch pad you can press RSK1.
      * This following screen would should you "company routes". Since there are none stored select `Return` using LSK6.

    ^^FLT NBR^^

    * Using the keypad type in `EZY123` and press LSK3. Feel free to use your own flight number here!
    * If you have the Free Text module enabled for your flight, this will enable other users flying the A32NX to send you messages. This will not be covered in this guide. 

    ^^COST INDEX^^

    [placeholder image]

    Your cost index can be found in the image above.

    * Using the keypad type in `44`
    * Press LSK5. 

    ^^CRZ FL/TEMP^^

    Input your desired cruise flight level in this field. On our OFP this is listed as `0240` or `FL240`. 

    * Using the keypad type in `240`
    * Press LSK6

    This will input FL240 and the temperature for you as well. 

    [Top of Section 1](#section-1)

=== "FLIGHT PLAN"

    Upon loading the flight plan page you should see three entries. Departure airport, `(DECEL)`, and arrival airport. 

    Our route for this flight found on the OFP is:

    `EGFF/30 BCN1A BCN N864 MONTY MIRSI1A EGCC/05R`

    ^^Inputting a SID^^

    !!! info "SID"
        Standard Instrument Departure Route

        These are procedures that are defined and published that takes a flight from the take-off phase to the enroute phase. 

    To program the Standard Instrument Depature (SID):

    * Press LSK1 or EGFF (your departure airport)
    * Select `DEPARTURE` shown next to LSK1
    * Select the runway you are departing from. In this case `30` using LSK3.
    * On the list of SIDs select the `BCN1A` depature

    The MCDU should now show you at the top of the screen in yellow what you have selected for your depature from EGFF. 

    * Press `INSERT` using RSK6 to program this into your flight plan. 

    Your flight plan should now have the associated waypoints for the `BCN1A` SID. You can scroll through your flight plan using the vertical slew keys. The SID terminates at `BCN` and this is where we can begin to fill out the rest of the flight plan. 

    ^^Enroute Flight Plan^^

    * Press the LSK that matches the location of `BCN` on the MCDU screen.
    * Select `AIRWAYS` using RSK5.
    * Using the keypad type in `N864` *(the airway)* and press LSK1.
    * Using the keypad type in `MONTY` *(waypoint)* and press RSK1. 
        * Remember: Airways are on the left and waypoints are on the right.

    ^^Planning Your Arrival^^

    For the purposes of this guide we will preplan our arrival into EGCC via the MIRSI1A STAR into 05R. 

    !!! info "STAR"
        Standard Terminal Arrival Route

        Similar to the SID, these are procedures that are defined and published that takes a flight from the last point in a route *(in our cause `MONTY`)* to the first point in the approach or the initial approach fix (IAF). 

    Find `EGCC` in green on your flight plan OR select `EGCC` in white under `DEST` using the corresponding LSK. 

    * Select `ARRIVAL` using RSK1
        * You will be shown the APPR's available designated by `Type``Rwy`. 
        * For this guide we will shoot for an ILS to keep it simple. 
    * Use the vertical slew keys to find `ILS05R` and select it using the corresponding LSK.
    * Again use the vertical slew keys to find the STAR for this flight `MIRSI1A` and select it using the corresponding LSK.
    * We won't have any vias for this flight. Select `NO VIAS` using LSK2. On the following page you can choose transitions if you have them, but for this flight we don't.
    * Insert this STAR into your flight plan using RSK6.

    Verify your flight plan by using the vertical slew keys to scroll through it. 

    !!! info "Viewing Flight Plan on ND"
        You can also verify the route looks correct by selecting `Plan` on the EFIS control panel and watching the ND as you scroll through.

    !!! warning "USR Waypoints"
        One thing to note are the USR waypoints the sim inputs into your flight plan. These are pseudo waypoints the simulator creates to draw the flight plan. 

        There is a small bug in the simulator where the USR waypoint on arrival may bug out and take you direct to runway. Please be aware and use selected HDG to mitigate this issue. 

    [Top of Section 1](#section-1)

***

### Section 2

=== "FUEL PRED"

=== "SECONDARY FLIGHT PLAN"

=== "RADNAV"

***

### Section 3

=== "INIT B"

=== "PROG"

=== "PERF"


