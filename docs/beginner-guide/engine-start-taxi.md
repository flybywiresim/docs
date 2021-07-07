# Engine Start and Taxi

This guide will explain the correct procedures to accomplish a pushback with engine start and perform a safe taxi to the departure runway. 

---

## Pre-requisites

- BEFORE START checklist completed
- IFR clearance obtained
- The aircraft is secure
- EXT power has been disconnected
- APU MASTER SW - `Set to ON` and the APU is available
- APU BLEED - `Set to ON`
- Beacon light - `Set to ON`
  
At this time you may request for clearance to push and start from ATC.  

[Download FlyByWire Checklist](../assets/FBW_A32NX_CHECKLIST.pdf){ .md-button }

---

## Pushback

There are several options available to you in MSFS to achieve a successful pushback. 

- The flyPad (EFB) ground control screen
- MSFS built in ATC pushback controls
- Third party pushback addons

### Pushback Clearance

For this guide we will assume you are parked at gate 10 at EGFF (Cardiff). When you are ready to begin pushback, you should contact ground ATC and inform then you are ready for push and start. If you are on a network such as VATSIM, a typical response from ground would give you clearance for your request and a direction to face (or any direction). At EGFF you could expect the following push and start clearance from ground: 

"** Your Aircraft Callsign**, ground. You are clear to push and start onto Alpha 3 facing east."

At this point you may begin your pushback away from the terminal onto the taxiway Alpha 3.  

![parking stands](../assets/beginner-guide/taxi/parking-stands-guidelines.png)
<sub>Copyright © 2021 Navigraph / Jeppesen<br>
"Navigraph Charts are intended for flight simulation use only, not for navigational use."

---

### How to Use MSFS Pushback

For the purposes of this guide we will use the default MSFS pushback controls built into ATC.

1. Open the ATC menu using the toolbar at the top of your screen. 
   ![atc toolbar](../assets/beginner-guide/taxi/toolbar.png)
2. Locate `GROUND SERVICES` and select it.
3. Select `REQUEST PUSHBACK`.
    - You should hear your virtual pilot request pushback and ATC respond confirming. At this time the pushback tug should slowly make its way to your nose wheel. 
    - You will notice a slight "jerk" as it connects with your nose wheel. Verify `NWS STRG DISC` is listed on the ECAM memos.
4. Release your parking brake.
5. In the ATC window use `REQUEST PUSHBACK STEER TO THE LEFT` OR `REQUEST PUSHBACK STEER TO THE RIGHT` to turn the aircraft.
6. Select `REQUEST PUSHBACK STOP` to end pushback when you are satisfied with your position on the taxiway.
    
!!! info "Steering Commands"
    Please note when selecting other option this will "steer" the tail towards the specified direction. 

    For example, if your external camera is directly behind the aircraft and you request `STEER TO THE LEFT` the tail of your aircraft will be "steered" to the left. 

---

## Engine Start

Once you are clear of the terminal and/or the ground crew has notified you it is clear to start engines you can proceed with the following steps. 

Start the chronometer above the ND to help you monitor the start up time of your engines. 

![chrono button](../assets/beginner-guide/taxi/chrono.png)

!!! info "Using the Chronometer"
    The chrono button has three states depending on how many times you have pushed the button:

    1. First Push - Starts the timer on the ND
    2. Second Push - Stops the timer on the ND
    3. Third Push - Removes the timer from the ND

    Time is represented as *minutes*' *seconds*" i.e. 04'41" equates to 4 minutes and 44 seconds.

    Location on the ND:

    ![NDlocation](../assets/beginner-guide/taxi/nd.png)

**Differing airline SOP may have a different engine start order.**

For this guide will begin by starting engine 2.  

=== "Start Engine 2"
    1. Set the `ENG` mode selector to `IGN/START`
        - You should hear the packs turn off.
        - The lower ECAM should automatically display the engine parameters screen. 
    2. Set `ENG 2` Master to the ON position.
        - Pay attention to your ECAMs and note your engine parameters as ENG 2 starts up. 
        - The engine should take roughly 1 minute to complete its start up sequence - use the chronometer you started earlier to time this.
    
    Engine 2 will have successfully started when the following applies (at ISA sea level):

    - N1 is at roughly 19%
    - N1 reported `AVAIL`  
    - N2 is at roughly 68%
    - EGT settles at about 520°C
    - FF is at roughly 290 kg/h

=== "Start Engine 1"
    1. Set `ENG 1` Master to the ON position.
        - Pay attention to your ECAMs and note your engine parameters as ENG 1 starts up.
        - The engine should take roughly 1 minute to complete its start up sequence - use the chronometer you started earlier to time this.

    Engine 1 will have successfully started when the following applies (at ISA sea level):

    - N1 is at roughly 19%
    - N1 reported `AVAIL`  
    - N2 is at roughly 68%
    - EGT settles at about 520°C
    - FF is at roughly 290 kg/h

---

## After Engine Start

Complete the after start flow:

- Set the `ENG` mode selector to `NORM`
- FLAPS - `Set`
    - As defined in the MCDU Preparation guide.
    - Note: If taxiing in icing conditions with rain, slush or snow:
        - Maintain the flaps retracted until the aircraft reaches the holding point of the takeoff run. This action prevents contamination of the slats/flaps mechanism.
- GROUND SPOILERS - `Arm`
- APU BLEED - `Set to OFF`
- APU MASTER SW - `Set to OFF`
- ANTI ICE - `As required`
    - Consider when temperatures are less than 10C and visible moisture.
- PITCH TRIM - `Check`
- RUDDER TRIM - `Zero`

Perform the AFTER START checklist.

![after start checklist](../assets/beginner-guide/taxi/afterstart.png)

---

## Flight Controls Check

Airlines may perform the flight controls check at different points depending on their SOP. Most notably the common instances are:

- After completing the AFTER START checklist and before taxi.
- During taxi out.

### Performing a Flight Controls Check

Using the ECAM control panel press the `F/CTL` button to switch the lower ECAM to the flight controls. Ensure all flight controls are displayed in green.

The `F/CTL` ECAM page shows you a white scale and green index for the following positions:

- Left and right ailerons position
- Left and right elevator position
  
Fully deflect your sidestick in all directions and observe that the full range of motion is reflected on the ECAM page. You should note the upward arrows in the `SPD BRK` area when moving the ailerons and ensure those are displayed when deflecting your side stick. 

Move your rudders and pay attention to the rudder symbol to ensure it moves all the way to the left or right. 

**Sidestick right full deflection:**

![fctl](../assets/beginner-guide/taxi/f-ctl.png)

---

## Taxi

!!! info "Taxi Speed + Engine Thrust"
    The A32NX is perfectly capable taxiing with idle thrust and even gradually accelerate. In certain situations it may be required to provide some thrust to begin rolling. 

    Standard behavior is to allow the aircraft to reach 30kts and apply brakes to 10kts. Repeat as necessary.

Having charts or diagrams of the airport you are currently in will help you navigate efficiently and safely. There are many resources and applications available online that are either free or paid which you can utilize. 

For additional information on signs and markings on the ground please see [General Resources](#general-resources) below.

### Taxi Clearance

After you have successfully started your engines you can contact ATC to request your taxi clearance. As per our routing in the [Preparing MCDU Guide](preparing-mcdu.md) we should be expecting a takeoff from runway 30. As such a sample taxi clearance may be as follows:

"**Your Aircraft Callsign**, ground. Runway 30, taxi via Alpha, hold short of 30 on Alpha 2."

Referencing the airport chart below, your aircraft should be sitting on the Alpha taxiway near the Alpha 3 holding point. Luckily today our clearance is quite simple and we only have to taxi straight ahead and hold at Alpha 2.

![airport chart](../assets/beginner-guide/taxi/airport-chart-guidelines.png)
<sub>Copyright © 2021 Navigraph / Jeppesen<br>
"Navigraph Charts are intended for flight simulation use only, not for navigational use."

Make sure to pay attention to any warnings or notices on your respective taxi chart beforehand so you are aware of any important information while performing your taxi.

Once you have your routing from ATC and have read back your taxi clearance you are now free to taxi to the runway.

### Moving the Aircraft

Exterior Lights:

- RWY TURN OFF - `Set to ON`
- NOSE - `Set to Taxi`

![exterior lights](../assets/beginner-guide/after-landing-steps/After Landing-Taxi  Light .png)

Before Moving Safety Check:

- Verify the ground crew is safely away.
- Look to your left and right to ensure clearance from other aircraft or vehicles.
- Release your parking brake.
- Brakes pressure - `Check at Zero`

![brakes pressure](../assets/beginner-guide/taxi/brakes.png)

At this point the aircraft may start rolling. Depending on your weight you may need to add a little power to the engines to get going. Increase power to roughly ~25-30% N1. Be mindful that you are not blasting N1 towards or around the terminal.

- Leave a bit of thrust on and perform a quick brake check to ensure hydraulics and brakes are fully functioning.
    - You don't need to come to a complete stop but merely check the brake pressure status when performing the brake check.
- If an arc is shown above the brake temperature on the WHEEL SD page on your lower ecam, turn your brake fans on.

If you need to perform a sharp turn immediately you may need more than ~25-30% N1 and should set your thrust accordingly. Try not to perform the brake check while in a turn as you don't want to come a complete stop while turning.

### During Taxi

While underway to the runway during your taxi perform the following as part of your taxi flow:

- Use the tiller (currently not implemented) or rudder pedals to steer the aircraft.
- Perform a [flight controls check](#flight-controls-check) (if you haven't already).
- Verify your ATC clearance for departure.
  
It is important to verify and confirm the information in your MCDU as you taxi. This is increasingly important if your ATC clearance changes enroute to the runway.

#### ^^**Takeoff data/Conditions**^^

*In case of a runway or takeoff data change, perform the following:*

- FINAL TAKEOFF DATA - `Confirm or Recompute`
- FMS TAKEOFF DATA - `Check/Revise as RQRD`
- REVISED FMS TAKEOFF DATA - `Crosscheck`
- F-PLN (RUNWAY) - `Revise`
- FLAPS lever - `As Appropriate` *Select takeoff position*
- V1, VR, V2 - `Reinsert`
- FLX TO temperature - `Reinsert`

#### ^^**AFS/Flight Instruments**^^

Perform the following:

- F-PLN (SID, TRANS) - `Revise or Check`
    - Check to ensure that your ATC clearance agrees with your flight plan if you are departing using NAV mode.  
- INITIAL CLIMB SPEED AND SPEED LIMIT - `Modify or Check`
- CLEARED ALTITUDE ON FCU - `Set`
- HDG ON FCU - `If Required, Preset`
    - If ATC requires you to fly a heading after takeoff preset the heading on the FCU. NAV mode will be disarmed and RWY TRK mode will keep the aircraft on the runway track.
    
This is your FCU (more details are provided in the [Take off, Climb, and Cruise Guide](takeoff-climb-cruise.md)):
![FCU image](../assets/beginner-guide/takeoff-climb-cruise/FCU.png)

- BOTH FD (*flight directors*) - `Check on`
- PFD/ND - `Check`
- TAKEOFF BRIEFING - `Confirm`
- RADAR (if required) - `On`
  
    The current implementation of the weather radar in MSFS will show you precipitation on your route. Additional functions are unavailable at this time however you should set the Radar to Sys 1 if required for your departure. 
  
- PREDICTIVE WINDSHEAR SYSTEM - `Auto`
   
    Currently this only clears the warning on your ECAM and does not provide a function in the sim. You should perform this action regardless.

The weather panel is located on the bottom left of the lower pedestal and looks like the following: 

![weather panel](../assets/beginner-guide/takeoff-climb-cruise/Radar_small.png)

- ATC code/mode - `Confirm/Set for Takeoff`
- TERR ON ND - `As RQRD`
- AUTO BRK MAX pb-sw - `On`

![auto brake](../assets/beginner-guide/taxi/auto-brk.png){: style="width:462px;height:350px;" }

!!! info "Getting Ready for Take off"
    At this point in the guide you should have performed many of the essential flow items before you line up at the runway. The next guide [Take off, Climb, and Cruise](takeoff-climb-cruise.md) will instruct you on performing your final checks and before take off checklist. 

**For additional information:** See the sections below for extended taxi information and visit the [General Resources Section](#general-resources) on this page to help you understand the different signs and elements found on the ground at an airport. 

---

#### Speed While Taxiing

Pay attention to your ground speed (visible on the ND) while you taxi. This will provide you with your knots on the ground. 

- **Straight Line**
  
    Anything up to 30kts is reasonable, but some airports may carry their own local restrictions that you should be mindful of. This is not an absolute rule and is usually typical SOP for airlines in a straight line.
  
- **90° (Sharp) Turns**
  
    A good speed would be around 10kts. This provides safety for the flight crew as they perform their safety demonstration/checks.
  
- **Regular Turns**
  
    Around 15kts is an acceptable speed with a similar concept to providing safety as described above. 

#### Handy Tips While Taxiing

- **Maintaining Center Line**
  
    You can use the grey vertical bar in between the PFD and ND as a reference point and keep the taxi line in between the two screens.
  
- **Turning**
  
    Using the same bar mentioned above try to "over steer" (keep the nose wheel slightly ahead of the line while you turn). This helps keep you centered while performing a turn.
  
    Slow down while turning!
    
#### Crossing a Runway

When approved to cross a runway (active or not) perform the following actions:

- Look out the windows and visually ensure that there are no visible aircraft to your left and right. 
- Turn on extra lights to ensure your aircraft is visible when crossing:
    - Strobe lights - `Set to ON`
- Inform ATC you have vacated the runway if required.

!!! warning
    Never cross a runway without express permission from ATC and providing a read back of said instructions. Always ensure maximum safety when crossing.

---

## General Resources

This section provides you with information on understanding the different signs and markings you may see while taxiing at the airport.

### Airport Signage and Markings

!!! info "Scenery / Accuracy Issues"
    Please be aware that the default scenery or 3rd party sceneries may not be entirely accurate with the posted signage on the ground. However, this guide will explain how to read and understand them.

#### FAA Quick Reference Guide

The FAA has a handy guide available for download that contains images of all the pertinent signs you may encounter, their purpose, and location at the airport. 

[Download FAA Guide](https://www.faa.gov/airports/runway_safety/publications/media/QuickReferenceGuideProof8.pdf){ .md-button }

---

There are two types of signage at airports - operational guidance signs and mandatory instruction signs. 

#### Operational Guidance Signs 

^^Location Signs^^

- These signs are yellow text on a black background. Typically, indicates a specific taxiway or runway your aircraft is on or entering.

^^Direction/Runway Exit Signs^^
  
- Black text on a yellow background. These will have an arrow indicating direction to turn which helps pilots identify what taxiways they are approaching or runway exits towards a specified runway.

    ![signs1](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Ben_Gurion_International_Airport_taxiway_signs.JPG/640px-Ben_Gurion_International_Airport_taxiway_signs.JPG)

^^Stop Bar Signs^^

- White text on a blue background. These are non-standard signs that may appear at some airports usually indicating which taxiway a stop bar is positioned. Airports usually use more conventional traffic signs you may see on the road such a regular stop sign. See the [FAA Guide](#faa-quick-reference-guide) for samples. 

    ![signs2](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Ben_Gurion_International_Airport_4_taxiway_signs.JPG/639px-Ben_Gurion_International_Airport_4_taxiway_signs.JPG)

#### Mandatory Instruction Signs

^^Runway Signs^^ 

- White text on a red background. These signs inform pilots that a runway intersection is ahead.

^^Holding Position Signs / Markings^^

There are typically three very important holding position signs / markings that appear on the ground at airports. At various airports that operate with low visibility these positions are also paired with a line of red lights across a taxiway to help visually indicate the holding positions. 

1. Runway Holding Position
    - Two sets of solid yellow lines and two sets of dashed yellow lines indicate a holding position for a runway ahead. These **must never be crossed** without express permission from ATC.   
2. Taxiway Holding Position
    - Single dashed yellow line. If this is present along your taxi route it will indicate a position that ground control may request you stop and hold short prior to another taxiway.
3. ILS Critical Area
    - Solid yellow lines that look like a railroad or ladder. These are another form of hold short point but indicate a critical area where your aircraft would violate the ILS approach airspace while on the ground.

---

### Taxiway Lighting

Taxiway lighting helps the flight crew and ground crew navigate the airport at night or in low visibility and stop at the appropriate locations as given by ATC. 

There are usually two types of lighting on taxiways - centerline and edge. Depending on the airport operator the lightning may differ if the airport operates in low visibility conditions. 

- Centerline lighting is green on the principal taxiways located along the taxiway centerline. These lights can alternate between green and yellow when a taxiway crosses a runway or highlight a "lead-off" taxiway from a runway to join a taxiway. 
- Edge lighting is typically blue and characteristically appears at the edges of a taxiway. Spacing can range from 50 - 200ft apart usually condensing in distance when approaching an intersection. 

![taxiway lights](https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/ATL_TWY_B_-_RWY_Crossing_%2813534655025%29.jpg/640px-ATL_TWY_B_-_RWY_Crossing_%2813534655025%29.jpg)

<sub>John Murphy, [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0)</sub>


