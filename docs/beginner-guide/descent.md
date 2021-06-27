# Descent Planning and Descent

This guide will explain the correct procedures to plan and fly a descent
from cruise altitude through STAR and Instrument Approach up to the final approach.

The actual final approach (ILS approach) will be covered by a separate chapter.

!!! warning "Disclaimer"
    The level of detail in this guide is meant to get a FlyByWire A320neo
    beginner safely from cruise level down to the ILS glideslope.

    A *beginner* is defined as someone familiar with flying a GA aircraft 
    or different types of airliners. Aviation terminology and know-how is 
    a requirement to fly any airliner even in Microsoft Flight Simulator.
    
    Further reading: [A320 Autoflight](https://www.smartcockpit.com/aircraft-ressources/A319-320-321-Autoflight.html)<br/>
    Also you will find many great videos on YouTube on how to fly the FlyByWire A32NX.<br/>
    Check out the FlyByWire YouTube Channel as well: [FlyByWire on YouTube](https://www.youtube.com/c/FlyByWireSimulations/playlists)

---

## Pre-requisites

Aircraft is in CRUISE state as per previous chapters

Download the [FlyByWire Checklist](../assets/FBW_A32NX_CHECKLIST.pdf) here.

## Chapters / Phases

This guide will cover these phases:

1. [Descent and Approach Planning](#1-descent-and-approach-planning)
2. [Starting the Descent](#2-starting-the-descent)
3. [Flying the STAR and Approach](#3-flying-the-star-and-approach)
4. [Intercepting ILS](#4-intercepting-ils)

---

## Base knowledge: Route, Star and Approach

- __Basics__<br/>
  As we have learned in previous chapters a flight route begins with an origin airport and a SID to safely guide the aircraft away from the airport to the first waypoint on their actual route. Similar to a SID the arrival to an airport is done via a STAR (Standard Terminal Arrival Route) and an IAP (Instrument Approach, often APPR) to safely bring the aircraft into a position to land on the destination airport with as little ATC communication as possible.

- __STAR__<br/>
  A Standard Terminal Arrival Route (STAR) ensures safe and efficient traffic from the last en-route waypoint to the initial approach fix (IAF) of the Instrument Approach (IAP). It separates aircraft, avoids conflicts and helps with noise abatement through specific routing, levels/altitudes, speed restrictions and checkpoints often with holding areas.

    One main objective is, to do this with a minimum of communication between the ATC controller and the pilot. As the STAR is part of the flight plan a pilot can simply continue from the normal route into the STAR if ATC has not given any other instructions. Sometimes ATC might give an explicit clearance for the STAR or change the STAR to manage traffic and landing situation (different runways, etc.).

    Often a STAR contains a clearance point which mustn't be passed without explicit clearance by ATC. If clearance is not given then a holding must be flown as described on the charts.

    The STAR which a pilot intends to use is usually included in the ATC flight plan and described in detail in navigational charts.

    Please also have a look at our airliner guide's SIDs and STAR section [SIDS and STARS](../airliner-flying-guide/navigation.md#sids-and-stars)

    Find a good overview over charts in our airliner guide: [Reading a Chart](../airliner-flying-guide/navigation.md#reading-a-chart)

- __Approach__<br/>
  The Instrument Approach (IAP or APPR) has similar objectives as a SID or STAR - safely bring an aircraft into a position to land while ensure separation between multiple aircraft.

    IAP are often designed for handling maximum traffic in even bad weather conditions. With only little traffic and good weather it is quite common that ATC instructs the pilot to leave the approach route by giving the pilot heading vectors for a more direct route to the final approach fix (FAF, also called final approach point).

    When flying with Online ATC (VATSIM, IVAO, PilotEdge, ...) expect being vectored to the FAF quite often.

    Find a commented ILS approach chart here: [Approach Chart](../airliner-flying-guide/navigation.md#chart-sample-1)

- __ILS__<br/>
  The Instrument Landing System (ILS) is one of several modern forms of helping an aircraft during its final approach to land even in not optimal weather situations. ILS uses a localizer for lateral guidance and a glideslope for vertical guidance from the final approach fix down to a minimum at which the pilots need perform the final landing sequence visually.

    Modern airlines like the A320 are even able to use the ILS to land fully automatically as long as the runway's ILS supports it.

    Find a commented ILS approach chart here: [Approach Chart](../airliner-flying-guide/navigation.md#chart-sample-1)

!!! info "Microsoft Flight Simulator and navigation charts"
    Although Microsoft Flight Simulator allows some flight planning through the user interface it is highly recommended to use navigational charts when flying airliners. MSFS' flight planning does not provide sufficient information to correctly fly a STAR or an approach.

    There are several good sources for charts - free or subscription based. A good free solution is [Chartfox](https://chartfox.org/) which only requires a free VATSIM account. One of the most known subscription based sources for charts is [Navigraph](https://navigraph.com/home). It is planned to integrate both solutions into the FlyByWire A32NX FlyPad in the future. 
    
    Also, often a simple Internet search will do the trick: Search for "&lt;airport icao code&gt; charts": E.g., "EDDM charts"  

---

### 1. Descent and Approach Planning

!!! warning "Pilot's responsibility"
    It is the sole responsibility of the pilot to conduct proper flight planning and especially proper descent planning. It is not at all ATC's task to do descent planning for pilots by giving descent instructions. On the other hand ATC often actually gives descent instructions, especially on common routes, as they want the aircraft in their responsibility to be at certain altitudes when approaching the destination airport. Nevertheless  pilots must know when to descent the latest and if necessary need to pro-actively request clearance to descent from ATC.

    Good descent and approach planning is the foundation for a successful landing. It has to be done early during the flight or even before the flight.

#### Important data points for descent planning:

- **Cruise Flight Level:** The higher we fly the earlier we need to start descending. Also for short flights a too high cruising altitude can make it impossible to actually descent to the destination airport in time.
- **Flight Plan Constraints:** STARs often have flight level (FL) or altitude constraints which we must adhere to. We must plan our descent so we can meet these altitude constraints even when they themselves are still far away from the destination airport.
- **Speed**: STARs also regularly have speed constraints which we need to take into consideration as slowing down will cost time and is hard while descending. If we start our descent too late we might not be able to slow down in time as required by a constraint.
- **Aircraft capability and passenger comfort:** Although not a big concern in the A320, general aircraft capabilities and passenger comfort also come into play. Descending with -4000ft/min is no fun for a passenger.

#### Step by step guide for descent planning:

1. Read the STAR chart and determine if there are altitude and/or speed constraints which we need to consider.
2. Consider the STAR and APPR route as optional and do not count on them to be flown and available for descending. ATC might want to vector us to a different runway or at least shortcut our approach. But they won't be able to if we are still too high for the final approach.
3. Determine the first constraint you need to meet. This could be a STAR waypoint with an altitude constraint, the final approach fix altitude or the airport elevation itself.
4. Calculate the required distance needed to descent to that waypoint with a standard descent angle of 3°. We can use the FlyByWire FlyPad in the cockpit or a simple rule of thumb calculation (details below).
5. Use the MCDU PROG page's DIST function to read out the current distance to this waypoint. It is also possible to use the ECAM flight plan, maps or the NDs distance rings to help determining the current distance.

    ![ECAM PROG page](../assets/beginner-guide/descent/ECAM_Progress_page.png "ECAM PROG page"){width=310 align=left}

    ![ND distance rings](../assets/beginner-guide/descent/ND_disctance_rings.png "ND distance rings"){width=310 align=right}

#### How to calculate the required distance for descent

**Example data:**

- Flight to EGKK via STAR TEBRA 2G
- Flight level FL320
- STAR constraint at waypoint ABTUM "at FL140"

**Example chart:**

![STAR EGKK TEBRA](../assets/beginner-guide/descent/STAR_EGKK_TEBRA.png "STAR EGKK TEBRA")<br/>
*Copyright © 2021 Navigraph / Jeppesen<br/>
"Navigraph Charts are intended for flight simulation use only, not for navigational use."*

**Using the FlyPad:**

Standard calculation with 3° descent path:
![Descent from FL320 to FL140](../assets/beginner-guide/descent/FlyPad_performance_TOD.png "Descent from FL320 to FL140")

Calculation with a specific distance to calculate the required descent velocity (V/S):
![Descent calculation with given distance](../assets/beginner-guide/descent/FlyPad_performance_TOD2.png "Descent calculation with given distance")

**Using "Rule of Thumb":**

```
Distance = "Altitude difference" * 3 / 1000 + margin**

Altitude difference: 32000 - 14000 = 18000
Times 3:             18000 * 3 = 54000
Divided by 1000:     54000 / 1000 = 54
Plus margin (~10%):  59 NM
```

Margin can be lower for headwind and larger for tailwind. Some also change the margin to compensate for slowing down while descending.

As can be seen on the chart there will be a further descent to TIMBA at FL70 and after that (not visible on the chart above) there will be a descent to the final approach which will be at 2000ft at the Final Approach Fix FF26L.

The same methodology/calculation as our initial descent can be applied to these descents as well but they require less planning as they are usually designed in a way that an aircraft with a 3° descent angle can make these descents with ease.

ATC will quite often instruct certain altitudes within the STAR and APPR which deviate from the STAR and APPR charts. Please expect such instructions at any time.

#### Advanced arrival planning

!!! warning "Advanced arrival planning"
    The following is a more advanced process for planning our arrival. It is obviously important when we want to have a more realistic experience but in Microsoft Flight Simulator you can skip this part for now. <br/>
    Also this process is best done with an Online ATC service as the build-in MSFS ATC does not provide the necessary information at the right time.

Before we descent we should also reconfirm our destination runway and input or update our destination data into the MCDU PERF APPR page.
This is typically done about 50NM before the starting the descent.

![ENTER DEST DATA Message on the MCDU](../assets/beginner-guide/descent/MCDU_Enter_dest_data.png "ENTER DEST DATA Message on the MCDU")

We can obtain this data from the destination airport's ATIS information and the airport charts.

From ATIS we get: QNH, TEMP and MAG WIND. Sometimes TRANS ALT - if not refer to the approach chart.

ATIS Example:
```
GATWICK INFORMATION K TIME 2020, RUNWAY IN USE 26L 
TRANSITION LEVEL FL70, SURFACE WIND 260,7 KNOTS 
CAVOK TEMPERATURE +16, DEW POINT +12, QNH 1018, 
ACKNOWLEDGE RECEIPT OF INFORMATION K AND ADVISE AIRCRAFT 
TYPE ON FIRST CONTACT
```

From the chart we get TRANS ALT and BARO (=MDA) or RADIO (=DH).

CAT 1 ILS uses MDA and is entered into the BARO field.

CAT 2/3 ILS use DH which is put in the RADIO field. The BARO is based on barometric altitude whereas the RADIO is based on radio altitude (distance to ground).

![Transistion alt on chart](../assets/beginner-guide/descent/EGKK_APPR_chart_1.png "Transistion alt on chart")<br/>
![ILS information on chart](../assets/beginner-guide/descent/EGKK_APPR_chart_2.png "ILS information on chart")<br/>
*Copyright © 2021 Navigraph / Jeppesen*

The A320neo is capable of a CAT IIIB ILS approach and has an approach category of "C"<br/>
(see [Wikipedia Aircraft approach category](https://en.wikipedia.org/wiki/Aircraft_approach_category)

In this chart for EGKK 26L ILS there is no DH for CAT IIIB defined - so we can enter "NO" into the RADIO field.

If we are using Microsoft Flight Simulator without any Online ATC services (VATSIM, IVAO, PilotEdge, ...), and using the MSFS build-in ATC, you usually can't request ATIS information for the destination airport at this point. MSFS ATC makes ATIS only available once close to the destination airport.

If we are flying with Online ATC you can request ATIS via the MCDU-ATSU-ACO page or your network's client at this time.

We can in any case request the METAR weather information for the destination airport via the same page.

![MCDU ATSU AOC page - WX and ATIS](../assets/beginner-guide/descent/MCDU_ATSU_AOC_WX.png "MCDU ATSU AOC page - WX and ATIS")

If we used Simbrief for flight planning we can also see METAR information on the FlyPad after importing the Simbrief plan to the FlyPad.

(TODO: FlyPadv2 screenshot)

Once we have confirmed the destination runway and the destination data you are set for the approach and can continue focus on the descent.

This concludes *Descent and Approach Planning*.

---

### 2. Starting the Descent

A few minutes before we reach our calculated descent point (TOD) we request clearance for descent from ATC if not already given a descent instruction before.

**Do NOT start the decent without clearance from ATC.**

!!! info "TOD marker A320"
    The FlyByWire A32NX has not implemented the TOD (top of descent) marker on the ND yet. Usually the A320 has a downward pointing arrow at the TOD to support the pilot with the decision when to descent. Ultimately it is still the pilot's responsibility to calculate and validate the TOD.
    (TODO: screenshot of marker)

When clearance is given we can start our descent to the flight level or altitude ATC has given us.

For descending we set the new flight level or altitude in the FCU with the altitude dial knob. We can then either push the knob for Managed Altitude Mode (constraints are respected) or pull the knob for Selected Altitude Mode (constraints are ignored). You can also use the V/S dial knob to set a specific descent vertical velocity. Pull the V/S knob to start the descent.

![FUC with ALT and V/S knobs](../assets/beginner-guide/descent/FCU_AP_knobs.png "FUC with ALT and V/S knobs")

ATC typically will not clear us to our final target altitude directly but will give us several step descents down to our required altitude.

Also ATC often still expect us to respect the STAR's constraints although they might have given us a lower clearance. We should then only descent to the constraint's altitude.

!!! info "VNAV in the FlyByWire A32NX"
    The scenario that we are cleared to a lower altitude or flight level with altitude constraints above the clearance is an ideal scenario for the called so "VNAV" autopilot mode which would be activated by using "Managed Altitude Mode" (pushing the ALT knob). The autopilot will automatically level off at the constraint and continue descending when the constraint is no longer valid.

    Unfortunately the current version of the FlyByWire A32NX does not yet support VNAV. This is planned to be implemented in one of the next versions.

We repeat the process until we have reached our desired final approach altitude.

This concludes *Starting the Descent*.

---

### 3. Flying the STAR and Approach

Flying the STAR and Approach is very similar to any other part of the route we have in the flight plan. Apart from descending and adhering to constraints the lateral flight path just follows the programmed route.<br/>
 Let the __Autopilot__ do this for you and just adjust altitude and speed according to the charts or the ATC instructions.

Be prepared for ATC instructions to also deviate laterally from the STAR or Approach route to separate from other aircraft or to shortcut the approach when there is little traffic. ATC will then typically give you new heading instructions (heading vectors) and will guide you the rest of the STAR and Approach with further heading instructions up until intercepting the ILS localizer.

**Example for shortcuts:**

ROKIL STAR/Transition EDDM (Munich) 26R - it is only in times with a lot of traffic that we would have to fly the whole downwind part of this transition.

![EDDM transition until vectored](../assets/beginner-guide/descent/EDDM_TRANS_chart.png "EDDM transition until vectored")<br/>
*Copyright © 2021 Navigraph / Jeppesen<br/>
"Navigraph Charts are intended for flight simulation use only, not for navigational use."*

---

### 4. Intercepting ILS

At the end of the Instrument Approach (or by ATC vectoring) we will be on a path to the Final Approach Fix and/or intercepting the ILS localizer and eventually the ILS glidescope.

To intercept the ILS we need to be on the correct altitude and should not have an approach angle larger than 30°.

![EDDM ILS 26R chart](../assets/beginner-guide/descent/EDDM_ILS_26R_chart.png "EDDM ILS 26R chart")<br>
![EDDM ILS 26R GS  chart](../assets/beginner-guide/descent/EDDM_ILS_26R_GS_chart.png "EDDM ILS 26R GS  chart")<br/>
*Copyright © 2021 Navigraph / Jeppesen<br/>
"Navigraph Charts are intended for flight simulation use only, not for navigational use."*

More details regarding the ILS approach and landing in the next chapter.

This concludes *Intercepting ILS*.

