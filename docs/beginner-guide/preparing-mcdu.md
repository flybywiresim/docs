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

=== "Line Select Key (LSK)"

    `LSK` for short. These keys are on the left and right hand side of the MCDU screen. They are highlighted in the image below. 

    * Left hand keys are referenced (in descending order) as `LSK1L - LSK6L`. 
    * Right hand keys are referenced (in descending order) as `LSK1R - LSK6R`.

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
      * Once this is in the scratch pad you can press LSK1R.
      * This following screen would should you "company routes". Since there are none stored select `Return` using LSK6L.

    ^^FLT NBR^^

    * Using the keypad type in `EZY123` and press LSK3L. Feel free to use your own flight number here!
    * If you have the Free Text module enabled for your flight, this will enable other users flying the A32NX to send you messages. This will not be covered in this guide. 

    ^^COST INDEX^^

    [placeholder image]

    Your cost index can be found in the image above.

    * Using the keypad type in `44`
    * Press LSK5L. 

    ^^CRZ FL/TEMP^^

    Input your desired cruise flight level in this field. On our OFP this is listed as `0240` or `FL240`. 

    * Using the keypad type in `240`
    * Press LSK6L

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
    * Select `DEPARTURE` shown next to LSK1L
    * Select the runway you are departing from. In this case `30` using LSK3;.
    * On the list of SIDs select the `BCN1A` depature

    The MCDU should now show you at the top of the screen in yellow what you have selected for your depature from EGFF. 

    * Press `INSERT` using LSK6R to program this into your flight plan. 

    Your flight plan should now have the associated waypoints for the `BCN1A` SID. You can scroll through your flight plan using the vertical slew keys. The SID terminates at `BCN` and this is where we can begin to fill out the rest of the flight plan. 

    ^^Enroute Flight Plan^^

    * Press the LSK that matches the location of `BCN` on the MCDU screen.
    * Select `AIRWAYS` using LSK5R.
    * Using the keypad type in `N864` *(the airway)* and press LSK1L.
    * Using the keypad type in `MONTY` *(waypoint)* and press LSK1R. 
        * Remember: Airways are on the left and waypoints are on the right.

    ^^Planning Your Arrival^^

    For the purposes of this guide we will preplan our arrival into EGCC via the MIRSI1A STAR into 05R. 

    !!! info "STAR"
        Standard Terminal Arrival Route

        Similar to the SID, these are procedures that are defined and published that takes a flight from the last point in a route *(in our cause `MONTY`)* to the first point in the approach or the initial approach fix (IAF). 

    Find `EGCC` in green on your flight plan OR select `EGCC` in white under `DEST` using the corresponding LSK. 

    * Select `ARRIVAL` using LSK1R
        * You will be shown the APPR's available designated by `Type``Rwy`. 
        * For this guide we will shoot for an ILS to keep it simple. 
    * Use the vertical slew keys to find `ILS05R` and select it using the corresponding LSK.
    * Again use the vertical slew keys to find the STAR for this flight `MIRSI1A` and select it using the corresponding LSK.
    * We won't have any vias for this flight. Select `NO VIAS` using LSK2L. On the following page you can choose transitions if you have them, but for this flight we don't.
    * Insert this STAR into your flight plan using LSK6R.

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

    On this page, we can input our zero fuel weight (ZFW) and zero fuel weight center of gravity (ZFWCG). 

    The A32NX can auto populate this for you. 

    * Press LSK3R to load in the calculated ZFW/ZFWCG into the scratch pad at the bottom of the MCDU. 
    * Press LSK3R a second time to input the above calculation into the MCDU. (the empty orange boxes should now be filled in by the scratch pad entry). 

    At this time a few extra fields will appear filled in. Starting from the top:

    * Departure Airport - EGCC
    * Fuel on Board - FOB
    * ZFW + FOB = Gross Weight - GW 
    * Center of Gravity - CG

=== "SECONDARY FLIGHT PLAN"

    This page will allow you to input a secondary flight plan. This page is currently inoperable in the A32NX. We will update this portion of the guide when it is usable. 

=== "RADNAV"

    On this page, you would set any frequencies you would need for the departure and subsequently later enroute the frequencies required for your arrival. 

    For this flight the FCU on managed should handle your departure navigation. If you'd like to have additional navaids for your departure you can input the runway localizer for the initial procedure turn and the BRECON VOR (BCN) to verify your track enroute to BCN. This is a little bit more advance than this guide allows for but we will cover how to input frequencies. 

    ^^VOR^^

    On this depature we have the BCN VOR with a frequency of `117.45`

    * Using the keypad type in `117.45` and press LSK1L. This will autopopulate the identifier of the VOR when within range. 
    * You can also set the desired course to track `031` and press LSK2L to input it. 

    ^^ILS^^

    In a similar fashion you can also input the ILS/LOC frequency on this page if it hasn't been inputted already. Remember our arrival airport/rwy is `EGCC/05R` with ILS05R having a frequency of `111.55`

    When inputting a frequency and you are in range of the ILS it will autopopulate the indentifier and course for you there is no need to fill these fields. 

    * Using the keypad type in `111.55` and press LSK3 to input it. 

    ^^ADF^^

    This works much in the same way as the two above. 

    [Top of Section 2](#section-2)

***

### Section 3

=== "INIT B"

    To navigate to the `INIT B` page you first have to select the `INIT` button. Once on `INIT A` use the horizontal slew keys to switch the page to `INIT B`. 

    Once here, you'll notice that your ZFW/ZFWCG has been copied over from the `FUEL PRED` page. Now we can add our fuel on board (FOB). The amount you input in this field can be done in one of three ways:

    * Indicated FOB on the upper ECAM.
    * You can have the MCDU plan the amount of fuel required for you. 
        * We recommend loading this fuel via our EFB or using the AOC options. (link-to-add) 
    * The amount indicated in your OFP.
        * We recommend loading this fuel via our EFB or using the AOC options. (link-to-add)

    ^^ECAM FOB^^

    Look at your upper ECAM and note the FOB indicated. Let's say that amount is `3091 KG` currently. When inputting the block fuel into the MCDU it is referenced in "Tons" and you should round to the closes decimal point. 

    * Using the keypad type in `3.1` and press LSK2R.

    ^^MCDU Planning^^

    You can choose to have the MCDU provide a recommended amount of fuel for your planned flight. 

    * Press LSK3R to compute an amount of fuel. 
    
    The Block field will be populated with a calculated fueld amount. 

    * Press LSK3R again to confirm the fuel. 
    * You should load this amount of fuel via the EFB or AOC option.

    ^^simBrief OFP^^

    You can use the planned block fuel stated on your OFP which in this case is `3091 KG`. 

    * Using the keypad type in `3.1 and press LSK2R
    * You should load this amount of fuel via the EFB or AOC option.

    [Top of Section 3](#section-3)

=== "PROG"

=== "PERF"


