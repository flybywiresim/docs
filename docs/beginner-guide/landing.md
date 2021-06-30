# Final Appraoch and ILS Landing

This guide will explain the correct procedures to fly a final approach and conduct an ILS landing.


!!! warning "Disclaimer"
    The level of detail in this guide is meant to get a FlyByWire A320neo
    beginner on approach to intercept the ILS and land the aircraft safely on the runway.

    A *beginner* is defined as someone familiar with flying a GA aircraft 
    or different types of airliners. Aviation terminology and know-how is 
    a requirement to fly any airliner even in Microsoft Flight Simulator.
    
    You will also find many great videos on YouTube on how to land the FlyByWire A32NX.<br/>
    Check out the FlyByWire YouTube Channel as well: [FlyByWire on YouTube](https://www.youtube.com/c/FlyByWireSimulations/playlists)

---

## Pre-requisites

Aircraft is on approach shortly before intercepting the ILS and is still in phase and state `DES` as per previous chapters.

[Download FlyByWire Checklist](../assets/FBW_A32NX_CHECKLIST.pdf){ .md-button }

## Chapters / Phases

This guide will cover these phases:

1. [Intercepting the ILS Localizer](#1-intercepting-the-ils-localizer)
2. [Intercepting the ILS Glideslope](#2-intercepting-the-ils-glideslope)
3. [Preparation and Checklist for Landing](#3-preparation-and-checklist-for-landing)
4. [Landing](#4-landing)
5. [Vacate Runway](#5-vacate-runway)

---

## 1. Intercepting the ILS Localizer

**Situation:**

- Aircraft is in `DES` phase
- Aircraft is setup for flight <10,000ft (`seat belt signs` on, `landing lights` on, etc.)
- We are either within the IAP (Instrument Approach) and at the correct altitude and speed or at a heading vector, altitude and speed instructed by ATC

At the end of the Instrument Approach (or by ATC vectoring) we will be on a path to the Final Approach Fix and/or a path to intercept the ILS localizer and eventually the ILS glideslope.

As a last instruction from ATC Approach we usually are instructed to contact Tower ATC when fully established on the ILS localizer.

To intercept the ILS Localizer follow these steps:

- Verify that the correct ILS frequency is tuned in the `MCDU-RNAV` page. We find the correct frequency on the approach chart<br/>

    === "Check ILS frequency"

        ![ILS frequency on ECAM RNAV page](../assets/beginner-guide/landing/ECAM_RNAV_page_ILS.png "ILS frequency on ECAM RNAV page"){align=right width=300}

        ![ILS frequency on approach chart](../assets/beginner-guide/landing/EDDM_26R_ILS_freq_chart.png "ILS frequency on approach chart"){align=left width=300}<br/>
        *<sub>Copyright © 2021 Navigraph / Jeppesen<br/>
        "Navigraph Charts are intended for flight simulation use only, not for navigational use."</sub>*

- Turn on the `ILS localizer and glideslope scales` with the `ILS` button on the glareshield.

    === "Turn on ILS scales"

        ![LS button on glareshield](../assets/beginner-guide/landing/GLARE_LS_button.png "LS button on glareshield"){align=left width=100}
      
        ![ILS Mode on PFD and ND](../assets/beginner-guide/landing/ILS_Mode.png "ILS Mode on PFD and ND"){align=right width=520}  

- Make sure we are on the correct altitude and we should not have an approach angle larger than 30°.<br/>

    ![EDDM ILS 26R chart](../assets/beginner-guide/landing/EDDM_ILS_26R_30_chart.png "EDDM ILS 26R chart")<br/>
    ![EDDM glideslope](../assets/beginner-guide/landing/EDDM_ILS_26R_GS_chart.png "EDDM glideslope")

- Optional: Turn on `ILS Mode` for the `ND` (can also be on F.O.'s side). The ILS ROSE Mode shows the deviation from the localizer approach heading path.

    ![ND ROSE ILS Mode](../assets/beginner-guide/landing/ND_ROSE_ILS_Mode.png "ND ROSE ILS Mode"){width=360}

- Activate the `APPR` phase in the `MCDU-PERF` page. This is usually automatically done by the aircraft at a certain point during approach but we make sure at the latest at this point that it is activated. In `APPR` phase the `Autopilot` together with "Managed Speed Mode" reliefs the pilot of a lot of stress by managing the speed according to flaps setting automatically.

    ![Activate APPR in ECAM PERF](../assets/beginner-guide/landing/ECAM_PERF_activate_APPR.png "Activate APPR in ECAM PERF"){width=360}

- Set `SPEED` to `Managed Speed Mode` (push the `Speed Selector`). The aircraft should now decelerate to `green dot` speed.
- Set `FLAPS` to 1 when speed is below V~FE~ for the first slat/flap configuration. The aircraft will decelerate further to prepare for the next flaps configuration.

    ![VFE for next configuration](../assets/beginner-guide/landing/PFD_Speedband_flaps_marker.png "VFE for next configuration")

- Turn on `LOC` in the `FCU` to command the aircraft to intercept the ILS localizer. The aircraft will keep the current heading until the localizer guides the aircraft towards the runway. The `lateral ILS localizer scale` shows the `deviation marker` moving towards the middle of the `lateral deviation scale`. Also the lateral `FMA` shows `LOC` in blue (armed).

    ![Activate LOC mode on FCU](../assets/beginner-guide/landing/FCU_LOC.png "Activate LOC mode on FCU")

    ![ILS lateral deviation marker moving inwards](../assets/beginner-guide/landing/PFD_ILS_deviation_scale.png "ILS lateral deviation marker moving inwards")

- When we are established on the ILS localizer (the lateral `FMA` shows `LOC` in green) we will contact Tower ATC and report that we are established on the ILS localizer (including call sign and runway).

    ![Established on ILS localizer](../assets/beginner-guide/landing/PFD_ND_established.png "Established on ILS localizer")

Tower ATC will the give us clearance for ILS approach for the target runway. This is the actual clearance that we are allowed to also descent along the ILS glideslope.

**Do not descent without explicit clearance from ATC.**

This concludes *Intercepting the ILS Localizer*

---

## 2. Intercepting the ILS Glideslope

**Situation:**

- Aircraft is in `APPR` phase
- Aircraft is established on ILS localizer
- Configuration is `FLAPS 1`

After ATC has given us clearance for ILS approach we can also start descending using the ILS glideslope.

![PFD glideslope deviation marker](../assets/beginner-guide/landing/PFD_ILS_glideslope.png "PFD glideslope deviation marker"){width=360}

Press the APPR button on the FCU to arm the ILS glideslope descent mode.

![Activating APPR mode](../assets/beginner-guide/landing/FCU_ILS_APPR.png "Activating APPR mode")

The vertical `FMA` will now show `G/S` (glideslope) in blue.

![PFD FMA showing G/S armed](../assets/beginner-guide/landing/PFD_FMA_GS_armed.png "PFD FMA showing G/S armed"){width=360}

 This is a good time to set `Flaps 2` (check that the speed is below the V~FE~ for the next flap setting) as slowing down once descending along the glideslope can be difficult. We need drag from the flaps if we do not want to let the gear down too early (which also would help us slowing down).

The aircraft will start descending when the deviation marker is in the middle (we have captured the ILS glideslope). The vertical `FMA` will now display `G/S` in green.

![PFD when G/S is activated](../assets/beginner-guide/landing/PFD_FMA_GS_active.png "PFD when G/S is activated"){width=360}

We are now descending along the glideslope. The radio altimeter comes alive at 2,500ft above the ground to display the actual precise altitude above ground.

![Radio altimeter alive](../assets/beginner-guide/landing/PFD_radio_alt.png "Radio altimeter alive"){width=360}

This concludes *Intercepting the ILS Glideslope*

---

## 3. Preparation and Checklist for Landing

**Situation:**

- Aircraft is established on ILS localizer and glideslope
- Flaps are set to 2

At this point we would prepare the aircraft for a possible go-around by setting the Go-Around altitude (see charts) in the FCU. We skip this for this beginner guide.

For the final approach we do the following steps:

- `Gear down`: Sometime between 2,500ft and 1,000ft , typically around 5-6NM from runway.
- Set `FLAPS 3` and shortly after `FLAPS FULL` (always check speed before setting flaps otherwise you get an overspeed alarm).
- Arm `Autobrakes` (`Low` when dry, `Med` in rain or snow or a short runway)
- Arm `Speedbrake` by pulling up the `Speedbrake` lever (Speedbrake must be retracted to arm)

**We need to be fully setup at 1,000ft above the ground.**

![Fully setup for landing](../assets/beginner-guide/landing/Landing_Cockpit.png "Fully setup for landing")

Complete the **Landing Checklist**

- Cabin Crew: advised
- A/THR: SPEED or OFF
- Autobrake: LO or MED
- ECAM Memo: LDG no blue
      - LDG GEAR DN
      - SIGNS ON
      - CABIN READY
      - SPLRS ARM
      - FLAPS SET

For the landing we have our hand on the thrust levers for a potential go-around so we can quickly push the levers forward into TOGO. **We do not move the levers until the last seconds before landing.**

This concludes *Preparation and Checklist for Landing*

---

## 4. Landing

**Situation:**

- Aircraft is fully setup for landing as per previous chapters
- Configuration is `FLAPS FULL`
- Aircraft is at about 1,000ft above the ground
- Wind is calm (no crosswind for this beginner guide)

Although the A320 can do an automatic landing (**Autoland**) we will do the a manual landing as this is more common and fun.

We **MUST** get landing clearance from ATC before we actually are allowed to land. Without landing clearance we must do a go-around (not part of this beginner guide). Usually ATC will have given us clearance at this point. Late clearance is rare and usually communicated to the us beforehand. If we have Minima we need to get ATC clearance before reaching the minimum. With no minimum as in our example we need to get clearance shortly before touchdown otherwise we have to do a go-around.

Next we turn of the **Autopilot** at about 500ft above the ground by pressing the `AP1` button on the `FCU`. We leave the **Autothrust** on so we don't have to worry about thrust and speed at all (Leaving **Autothrust** on for landing is common for the Airbus).

![Cockpit view when AP has been turned off](../assets/beginner-guide/landing/Cockpit_view_AP_off.png "Cockpit view when AP has been turned off")

Now look at the PAPIs which guide us vertically down to the correct touchdown point.  We want two white lights and 2 red lights.

![PAPI indication correct path](../assets/beginner-guide/landing/PAPI_2red2white.png "PAPI indication correct path")

See also [Wikipedia:PAPI](https://en.wikipedia.org/wiki/Precision_approach_path_indicato)

We correct our pitch only very carefully when too high (3-4 white) or too low (3-4 red). We don't need a lot of input to the sidestick to correct.

We aim for the middle of the touchdown zone which is marked by the touchdown zone markers.

![Runway touchdown zone](../assets/beginner-guide/landing/Runway_touchdown_zone.png "Runway touchdown zone")

Also we try to aim for the center line of the runway in a way that it points directly under us.

![Hold the runway center line pointing under us](../assets/beginner-guide/landing/Hold_Runway_Centerline.png "Hold the runway center line pointing under us")

Correct your final heading and bank very carefully. We should not need to correct much at this point.

!!!info "Crosswind landings"
    Crosswind landings are beyond the scope of this beginner guide. There are many good tutorials for crosswind landings in the A320 on Youtube.

 Once over the runway threshold we look towards the end of the runway to better judge our pitch especially for the so called **Flare**.

!!!info "Flare"
    The flare follows the final approach phase and precedes the touchdown and roll-out phases of landing. In the flare, the nose of the plane is raised, slowing the descent rate and therefore, creating a softer touchdown, and the proper attitude is set for touchdown. [..] In the case of tricycle gear-equipped aircraft, the attitude is set to touchdown on the main (rear) landing gear. (source: [Wikipedia: Landing flare](https://en.wikipedia.org/wiki/Landing_flare) )

 At the runway threshold we should be about 50ft above ground and prepare to set the thrust levers to idle and flare.

 ![Runway threshold](../assets/beginner-guide/landing/Runway_threshold.png "Runway threshold")

At about 30ft we start our flare by pulling back on the sidestick carefully. We only need a few degrees in positive pitch and hold the aircraft there. Too much flare will cause the aircraft to float down the runway, too little will cause a harder landing.

At about 10-20ft we pull back the thrust levers to idle (the aircraft also sounds the callout "retard retard ...") so the we are at idle thrust **before** we touch the ground.

![PFD during flare](../assets/beginner-guide/landing/PFD_Flare.png "PFD during flare"){width=360}

We hold the attitude of the aircraft until it settles on the ground. **Do not push the sidestick forward (nose down) once flared.** We let the aircraft settle to the runway while holding the pitch.

On touchdown of the main gear the `Speed Brakes` will deploy automatically (we have armed them earlier) and we pull the thrust levers into the reverse position.

![Reverse Thrust](../assets/beginner-guide/landing/Thrustlevers_Revers.png "Reverse Thrust")

We let the front gear settle gently on the runway (don't slam it down) and hold the center line of the runway while we are reducing speed. The speed reduction should be monitored on the `PFD` speedband and the speed trend arrow.

The `Autobrakes` should now have activated and started top further decelerate the aircraft. This can be checked by the `Autobrake` annunciators.

![Speed trend arrow](../assets/beginner-guide/landing/PFD_speedtrend.png "Speed trend arrow")
![Autobrake annunciator](../assets/beginner-guide/landing/Autobrake_annunciator.png "Autobrake annunciator")

The upper ECAM should now show the engines in reverse mode (`REV`) and
 the lower ECAM shows the `Speed Brakes` (spoiler) deployed. Also you should notice that the brakes actually get hotter.

![ECAM showing reverser and speed brakes](../assets/beginner-guide/landing/ECAM_Rev_SpeedBrk.png "ECAM showing reverser and speed brakes"){width=360}

At about 60knots we put the thrust levers back to idle and at about 40 knots we release the `Autobrakes` by braking manually which deactivates the `Autobrake`.

We retract the flaps and focus on the next possible runway exit.

This concludes *Landing*

---

## 5. Vacate Runway

**Situation:**

- Aircraft has landed and is still on the center line of the runway.
- Speed is < 40 knots
- Flaps are up

We look for the next runway exit and slow down to about 15 knots before we start turning off the runway.

We continue rolling forward until we passed the runway entry marker with the **full length** of our aircraft.

![Aircraft stopped after runway is vacated](../assets/beginner-guide/landing/Runway_vacated.png "Aircraft stopped after runway is vacated")

We can now safely stop the aircraft and do our "After Landing" checklist.

If ATC did not already contact us on the ground we would contact them now to let them now we have vacated the runway. They will give us taxi instructions so we can continue taxiing to our gate once we have done after landing tasks.

!!!info "After landing tasks in simulation"
    In real live the A320 will have two pilots which can actually do things in parallel. Talking to ATC, taxing the aircraft and do the after landing tasks. In the simulation we are typically alone so it is absolutely ok to stop once we have fully vacated the runway and do these things one after the other. Talking to ATC and getting taxi instruction, do the after landing tasks and checklist, taxiing to gate.

This concludes *Vacate Runway*

Please continue with [After Landing Steps](after-landing-steps.md)
