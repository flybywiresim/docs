<link rel="stylesheet" href="../../../../stylesheets/efb-interactive.css">

# flyPad Performance

## Top of Descent Calculator

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-performance-tod.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

This calculator helps the pilot to calculate when to start descending (aka the Top of Descent) based on various variables so that different scenarios can be calculated (e.g. descending with 3° descent rate, descending with a given vertical speed, etc.).

For more information about descent and approach planning see our guide: [Descent and Approach Planning](../../../pilots-corner/beginner-guide/descent.md#1-descent-and-approach-planning)

### Usage

There are several scenarios for the TOD Calculation:

1. Fixed Angle of Descent:
    - Descending from altitude X to altitude Y with a fixed descent angle (commonly 3°)
2. Fixed Distance to Navigation Fix:
    - Descending from altitude X to altitude Y within a fixed distance (e.g. 90NM)
3. Fixed Rate of Descent:
    - Descending from altitude X to altitude Y within a fixed vertical speed (e.g. -2.000ft/min)

Depending on the scenario, ground speeds are included in the calculation to take into account that we usually also slow down at some point during descent.

The flyPad TOD calculator can be used for all of these scenarios.

#### Angle of Descent

To calculate the TOD with a fixed angle of descent we simply have to enter the starting altitude and the desired target altitude.
We can also enter a certain angle other than 3°. But 3° is a common standard descent angle in aviation and rarely needs to be changed.

Example:

- Cruising altitude: 39.000ft
- Target altitude: 11.000ft
- Descent angle: 3°
- Ground Speed: has no impact on the calculation because of the fixed angle.

![flyPad Performance TOD Calculator](../../assets/flypados3/performance-tod-angle.png "flyPad Performance TOD Calculator"){loading=lazy}

**Result: We need to start our descent ^^88NM^^ before the target fix at which we want to reach 11.000ft.**

#### Distance to Fix

To calculate the TOD with a fixed distance to a specific fix we have to enter the starting altitude, the desired target altitude, and the distance to the target fix.

Example:

- Cruising altitude: 39.000ft
- Target altitude: 11.000ft
- Distance to fix: 90NM
- Ground Speed: 450 kt (constant)

![flyPad Performance TOD Calculator](../../assets/flypados3/performance-tod-distance.png "flyPad Performance TOD Calculator"){loading=lazy}

**Result: We need to start our descent 90NM before the target fix with either an average
^^vertical speed of -2.333ft/min^^ or an average ^^descent angle of -3.0°^^** during the descent distance.

!!! note ""
    The above result is averaged over the descent distance and the values are approximations. For more precision use one of the other two methods.

#### Rate of Descent

To calculate the TOD with a fixed vertical speed (rate of descent) we have to enter the starting altitude, the desired target altitude, and the desired vertical speed.

Example:

- Cruising altitude: 39.000ft
- Target altitude: 11.000ft
- Vertical Speed: -2.000ft/min
- Ground Speed: 450 kt (constant)

![flyPad Performance TOD Calculator](../../assets/flypados3/performance-tod-vs.png "flyPad Performance TOD Calculator"){loading=lazy}

**Result: We need to start our descent ^^105NM^^ before the target fix with a vertical speed of -2.000ft/min**

#### Ground Speed and Wind

To allow for different ground speeds during descent the calculator allows to enter
several altitude levels with the corresponding ground speed. This will be included in the calculations.

Example:

- Cruising altitude: 39.000ft
- Target altitude: 11.000ft
- Vertical Speed: -2.000ft/min
- Ground Speed: 420 kt at or above 10.000ft, 250kt below 10.000ft

![flyPad Performance TOD Calculator](../../assets/flypados3/performance-tod-gs.png "flyPad Performance TOD Calculator"){loading=lazy}

**Result: We need to start our descent ^^98NM^^ before the target fix with a vertical speed of -2.000ft/min**

!!! note "Wind"
    Wind is not a factor and can be ignored as these calculations are done based on ground speed which includes any 
    wind impacting an aircraft in the air.

## Landing Performance Calculator

The primary purpose of this calculator is to aid the flight crew in assessing whether a landing can be safely made within the given runway length in existing conditions. The pilot can also use this tool to determine the appropriate level of braking and whether reverse thrust is needed to stop within the available runway distance. 

The calculator results are shown both numerically and graphically. Variations in airplane configuration, approach 
speed, runway surface condition, and other parameters can also be investigated to see their effect on the airplane's landing distance. The landing distance results include a safety margin of 15% added to the calculated distance.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-performance-landing.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>


### Usage

Enter the required data into the calculator fields. The initial state of the calculator will have all input fields 
blank except for runway condition (Dry), flap setting (Full), overweight procedure (No), and reverse thrust (No). 
It is important to note that all fields must be filled in order to activate the "Calculate" button. The "Clear" 
button will return input fields to the initial state. 

Weather data can be automatically filled by entering an airport ICAO and pressing "Get METAR". How to get the 
information for all the fields is described in the following section.

- Wind, Temperature, QNH:
    - This information can be obtained from the METAR or ATIS.

- Rwy Altitude:
    - This information can be obtained from the airport chart (see example below).

- Rwy Heading:
    - This information can be obtained from the airport chart (see example below).

- Rwy Condition:
    - This information can be obtained from the METAR or ATIS and from NOTAMs on the OFP (Operational Flight Plan).
    - SimBrief provides field condition reports (FICONs) which helps populate appropriate data for this field.
        - For detailed information see the [RWY Conditions](../../../pilots-corner/airliner-flying-guide/runway-conditions.md#rwy-conditions)
          section on the landing calculator additional info page.

- Rwy Slope:
    - This information can be obtained from the airport chart (see example in [Landing Calculator Additional Info](../../../pilots-corner/airliner-flying-guide/runway-conditions.md#example-chart){target=new}) but requires a little calculation.
    - Formula: (((Runway elevation on touchdown side) - (Runway elevation on far side)) / Runway length) * 100.
    - Eg. EDDM 26R: 1.449ft - 1.467ft = -18ft.
    - Then -18ft / 13.123ft = -0.00137.
    - Then -0.00137 * 100 = -0.137% slope.

- Rwy LDA (Landing Distance Available):
    - This information can be obtained from the airport chart (see example below).

- Approach Speed: MCDU PERF APPR
    - This is part of the MCDU PERF APPR page and can be taken from there (V~APP~).

    ![MCDU PERF APPR page](../../assets/flypados3/performance-landing-mcdu-perf.png "MCDU PERF APPR page"){loading=lazy}

- Weight:
    - This information can be obtained from the ECAM SD bottom right corner (GW 59600 KG in the example below).

    ![ECAM SD](../../assets/flypados3/performance-landing-ecam-sd.png "ECAM SD"){loading=lazy}

- Flaps:
    - Planned landing flap setting (CONF FULL or CONF 3).

- Overweight Procedure:
    - Will the landing weight be greater than the maximum landing weight (Yes or No).
    - Reminder: maximum landing weight is 67400 KG.

- Reverse Thrust:
    - Will reverse thrust be used (Yes or No)?
    - Use of reverse thrust on a wet or contaminated runway would be considered necessary for safety reasons.
    - May be subject to airport requirements. If there are airport requirements regarding the use of reverse thrust, these can be found on the airport chart (see example below).

    ![Airport Chart Information](../../assets/flypados3/performance-landing-charts-reverser.png "Airport Chart Information"){loading=lazy}

- Autoland:
    - If an Autoland is planned then set this to Yes.

### Example Data

Below you can find an example of runway details and how to identify it to input data into the respective fields.

#### Example Chart:

![Airport Chart](../../../fbw-a32nx/assets/flypados3/performance-landing-chart.png "Airport Chart"){loading=lazy}

<sub>*Copyright © 2021 Navigraph / Jeppesen<br/>
"Navigraph Charts are intended for flight simulation use only, not for navigational use."*</sub>

#### Example 1

This runway can be used for landing with the given circumstances and full flaps in all braking configurations (low, medium, max manual).

![flyPad Performance Calculator Landing](../../../fbw-a32nx/assets/flypados3/performance-landing-ok.png "flyPad Performance Calculator Landing"){loading=lazy}

#### Example 2

This runway's landing distance available is long enough to be used for landing with full flaps only and with max manual
braking.
Be aware that there might be other restrictions that prohibit landing of an A320neo on this airport/runway.

![flyPad Performance Calculator Landing](../../../fbw-a32nx/assets/flypados3/performance-landing-maxok.png "flyPad Performance Calculator Landing"){loading=lazy}

#### Example 3

This runway can't be used for landing with the given circumstances. It is similar to Example 2 but has a higher weight and therefore higher approach speed.

![flyPad Performance Calculator Landing](../../../fbw-a32nx/assets/flypados3/performance-landing-notok.png "flyPad Performance Calculator Landing"){loading=lazy}
