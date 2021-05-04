# Preparing the MCDU

This guide will help you prepare the MCDU in the A32NX for your departure. It includes a simple route so you can follow along easily and replicate in the simulator.

simBrief Route used in this guide - [View Here](https://www.simbrief.com/ofp/flightplans/EGFFEGCC_PDF_1620029221.pdf)

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

=== "Scroll Keys"

    These keys are referenced below. 

    ![Placeholder](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/638px-Placeholder_view_vector.svg.png)

    !!! info

        === "Left and Right"

            These keys allow you to scroll between certain page i.e. `INIT A` and `INIT B` when the INIT page is selected. 

        === "Up and Down"

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

The simBrief route used for this guide can be found - [here](https://www.simbrief.com/ofp/flightplans/EGFFEGCC_PDF_1620029221.pdf)

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

### Section 2

=== "FUEL PRED"

=== "SECONDARY FLIGHT PLAN"

=== "RADNAV"

### Section 3

=== "INIT B"

=== "PROG"

=== "PERF"


