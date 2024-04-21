<link rel="stylesheet" href="/stylesheets/bg.css">
# After Landing and Taxi to Gate

This guide will explain the correct procedures after we have landed and vacated the runway, and will also cover taxiing to the designated gate.

!!! warning "Disclaimer"
    The level of detail in this guide is meant to get a Airbus A380 beginner from the runway to the designated destination gate.

    A *beginner* is defined as someone familiar with flying a GA aircraft or different types of airliners. Aviation terminology and know-how is a requirement to fly any airliner, even in Microsoft Flight Simulator.

    Further reading: [A320 Autoflight](https://www.smartcockpit.com/aircraft-ressources/A319-320-321-Autoflight.html)<br/> <p style="color:yellow; font-size:18px;">TODO: update/this link for 380</p>


---

??? tip "Prerequisites"
    Aircraft has vacated the runway completely and has been brought to a stop on the taxiway as per previous chapters.
    <p style="color:yellow; font-size:18px;">TODO: update/screenshot</p>
    [Download FlyByWire Checklist](../assets/sop/A32NX%20Documentation/FBW%20A32NX%20Checklist.pdf){ .md-button }
    <p style="color:yellow; font-size:18px;">TODO: update link</p>

## Chapters / Phases

This guide will cover these phases:

1. [After Landing](#1-after-landing)
2. [Taxi to Gate](#2-taxi-to-gate)

---

### 1. After Landing

??? tip "Situation"
    - Aircraft has vacated the runways completely and has come to a stop on the taxi way as per previous chapters.
    - Flaps and Ground Spoilers are still deployed.
    - ATC has been informed that we vacated the runway.

!!!info "Simulation vs. Real Life"
    In real life, the A380 will have two pilots who can actually do things in parallel. Talking to ATC, taxiing the aircraft and doing the after landing tasks.

    In the simulation we are typically alone, so it is perfectly fine to stop once we have fully vacated the runway and do these things one after the other.

??? tip "ATC after landing"
    ATC Tower will usually hand us off to ATC Ground, and they will give us taxi instructions for our destination gate. Write them down and read them back as usual, but you don't have to move immediately unless ATC explicitly tells you to. Online ATC understand that the after-landing- tasks do take some time.

??? tip "Immediate steps after vacating the runway"
    - Set your radio frequency to the one assigned by ATC or the airport charts.

    ![EDDM ATC frequencies](../assets/beginner-guide/after-landing/EDDM-frequency-chart.png "EDDM ATC frequencies"){ loading=lazy }

    ![RMP Panel](../assets/beginner-guide/after-landing/RMP-Panel.png "RMP Panel"){loading=lazy } <p style="color:yellow; font-size:18px;">TODO: update/screenshot</p>

    - Disarm the `Speed Brake` lever (Ground Spoilers) by pushing down on the lever.

    ![Spoiler armed and disarmed](../assets/beginner-guide/after-landing/Spoiler.png "Spoiler armed and disarmed"){loading=lazy } <p style="color:yellow; font-size:18px;">TODO: update/screenshot</p>

??? tip "What and why"
    After landing, we need to prepare the aircraft to taxi to our assigned gate. To do this, we need to follow a few steps and disable some systems that we will not need any longer since we are safely on the ground.
    <p style="color:yellow; font-size:18px;">TODO: update/screenshot. Insert more if needed</p>

`GROUND SPOILERS ................................................... DISARM`<br/>
`ENGINE START SELECTOR ......................................... CHECK NORM`<br/>
`FLAPS ............................................................ RETRACT`<br/>
`TCAS ............................................................. STANDBY`<br/>
`WEATHER RADAR ........................................................ OFF`<br/>
`PREDICTIVE WINDSHEAR SYSTEM .......................................... OFF`<br/>

??? tip "Why start the APU"
    Once we are safely off the runway and on to our assigned taxiway, we need to start the APU. We are doing this to ensure the aircraft will still have electrical power and air conditioning and circulation once we complete our navigation to our assigned gate. Upon reaching the gate, our engines will need to be shut down, and we are still going to need power for a little bit while we focus on shutting the airplane down.
    <p style="color:yellow; font-size:18px;">TODO: update/screenshot</p>

`AUXILLIARY POWER UNIT START ........................................... ON`<br/>
`ANTI-ICE ..................................................... AS REQUIRED`<br/>

??? tip "Exterior lights for taxi"
    Once we begin our taxi to the gate, we have to check our lights. We are doing this so we are A. Not a distraction to other pilots, and B. Not blinding the ground crews.
    <p style="color:yellow; font-size:18px;">TODO: update/screenshot</p>

`LANDING LIGHTS ....................................................... OFF`<br/>
`STROBE .............................................................. AUTO`<br/>
`OTHER EXTERIOR LIGHTS ........................................ AS REQUIRED`<br/>
`NOSE ................................................................ TAXI`<br/>
`RUNWAY TURN OFF LIGHTS ....................................... AS REQUIRED`<br/>

??? tip "Hot brakes"
    If you get a warning on your ECAM saying "brake temperature high", <p style="color:yellow; font-size:18px;">TODO: update with proper verbiage"</p> we're going to want to cool those brakes down. Press the switch labeled `BRAKE FAN` to help the brakes cool off. It is not uncommon for brakes to get very hot while decelerating after touchdown. 
    <p style="color:yellow; font-size:18px;">TODO: update/screenshot</p>

`BRAKE TEMPERATURE ................................................ MONITOR`<br/>
`BRAKE FAN .................................................... AS REQUIRED`<br/>

![After Landing Checklist](../assets/beginner-guide/after-landing/After-landing-checklist.png "After Landing Checklist"){loading=lazy width=50%}

This concludes *After Landing*

### 2. Taxi to Gate

??? tip "Situation"
    - Aircraft on taxiway directly after runway.
    - **After Landing** checklist is completed.
    - ATC Ground has given taxi instructions.

??? tip "Taxiing"
    Make sure to also read the Taxi section of the [Engine Start and Taxi](04_engine-start-taxi#taxi) chapter.
    Use your charts to follow the ATC taxi instructions to the designated gate.

??? tip "Crossing a Runway"
    When approved to cross a runway (active or not) perform the following actions:
    - Look out the windows and visually ensure that there are no visible aircraft to your left and right.
    - Turn on extra lights to ensure your aircraft is visible when crossing:
    - Strobe lights - `Set to ON`
    - Inform ATC you have vacated the runway if required.

!!! warning
    NEVER cross a runway without express permission from ATC and providing a read back of said instructions. Always ensure maximum safety when crossing.

`ATC CLEARANCE ..................................................... OBTAIN`<br/>
`STROBE LIGHTS ......................................................... ON`<br/>

??? tip "After crossing the runway"
    After you have crossed the runway and are on the adjacent taxiway, turn the strobe lights back off, and notify ATC you are clear of that runway.

`STROBE LIGHTS ........................................................ OFF`<br/>

??? tip "Turning into the Gate"
    When turning into the gate, turn off your `NOSE` light and your `RWY TURN OFF` lights to not blind the ground personnel. This of course is only done if enough lighting is available to safely navigate and park into the gate.
    <p style="color:yellow; font-size:18px;">TODO: update/screenshot</p>

`NOSE LIGHTS .......................................................... OFF`<br/>
`RWY TURN OFF LIGHTS .................................................. OFF`<br/>

This concludes *Taxi to Gate*

Continue with [Powering Down](09_powering-down)
