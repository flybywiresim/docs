# Traffic Alert and Collision Avoidance System

{==

The initial implementation of TCAS is available in the development and experimental branch at this time. Please note details about this system and it's functions will come at a later time.

Our TCAS supports online network traffic services (Vatsim / IVAO).

==}

## Overview

Traffic Collision Avoidance System (TCAS) is a system available on Airbus aircraft that help reduce airborne collisions and risks. Numerous improvements have been made to this system over the years that enhances the pilot interface and decreases non-optimum pilot handling of advisories from TCAS. The FlyByWire A32NX uses the AP/FD TCAS mode function developed by Airbus.

There are two typical procedures pilots will encounter when TCAS detects an intruder in the flight path of the aircraft.

- Traffic Advisory (TA)
- Resolution Advisory (RA)

The TCAS panel can be found on the lower pedestal to the right of the throttle quadrant.

For more information on how ensure TCAS is active for your flight and the corresponding controls please see the [ATC TCAS PANEL](../../a32nx-briefing/flight-deck/pedestal/atc-tcas.md) page.

## AP/FD TCAS

!!! warning "Manual Flight Assumptions"
    The operating flight crew should always be able to take command of hte aircraft manually by disconnecting the autopilot and flight directors to respond to a TCAS RA by flying the verticial speed out of the red zone in the vertical speed indicator.

AP/FD TCAS includes vertical guidance as part of the Auto Flight System (AFS) to support pilots during a TCAS RA. It provides control of the vertical speed via the AFS which is specifically tailored to each target that generated an RA. One of the major benefits of this system is to assist flight crews perform optimal maneuvers when a conflict arises.

Essentially this feature allows the flight crew to resolve TCAS RAs with the autopilot and flight directors engaged. It is entirely possible to complete a TCAS RA maneuver manually by using the flight director guidance with the autopilot switched off as well.

!!! info "AP/FD TCAS Conditions"
    There are conditions that happen when a TCAS RA is triggered causing the AP/FD TCAS mode to do the following:

    === "AP + FD Engaged"
        Any vertical mode will revert to `TCAS` in the FMA and the autopilot will fly the TCAS maneuver

    === "AP Disengaged / FD Engaged"
        TCAS mode will be engaged and supercede the flight directory guidance. Flight crews should ensure they are centered on the pitch bar and bring the vertical speed of the aircraft into the green zone indicated on the vertical speed indicator on the PFD.

    === "AP + FD Disengaged"
        The FD bars will appear automatically. TCAS mode will be engaged and provide guidance and flight crews should perform actions as stated in above.

### Traffic Advisory

This advisory is generated when TCAS detects an intruder along the current flight path it would consider a potential threat. Flight crews will receive multiple cues from TCAS that identifies a TA. No specific action is mandatory during a TA but the flight crew should remain vigilant of intruders and anticipate a potential RA. 

- Visual amber cues on the navigation display (ND providing information about the potential threat
- "*Traffic, Traffic*" aural warning

[**Images of different TA icons on ND Here**]

Once a TA is triggered the AP/FD TCAS will arm itself to notify the crew (alongside other visual cues noted above). This ensures that if the intruder would turn into a threat that triggers an RA the system is ready.

### Resolution Advisory

When a traffic advisory becomes collision threat an RA is generated. AP/FD TCAS shines in this regard allowing for fully automated flight in the case of an RA. Pilots will now have additional information provided to them on the performance display (PFD) and navigation display depending on what actions the flight crew need to perform to clear the conflict.

- Visual red cues on the ND providing information about the potential threat
- Aural commands instruction pilot of what type of vertical maneuver to perform
- Visual green and red zones on the vertical speed indicators on the PFD

[**Images of different RA icons on ND Here**]

There are generally two types of behaviors associated with an RA - preventative and corrective

#### Preventative

This behavior starts with the vertical speed out of the red zone of the VSI. It requires the flight crew or commands the autopilot to maintain the current vertical speed and is coupled with an audible alert to "Monitor V/S". This would help increase the safety margin before any further measures would need to be taken and allow for safe capture of a selected flight level clear of any conflicts. The following conditions will apply:

- TCAS will maintain a safe V/S target
- Longitudinal modes previously armed will automatically be disarmed except ALT^*^
- In the situation that conditions for altitude capture are met a preventative RA will allow for safe capture of the targeted altitude.
    - This prevents the aircraft from exceeding a commanded altitude
- "Adjust V/S" RA will safely maintain a vertical speed when attempting to level-off
- To ensure a safe speed during any maneuvers A/THR will engage SPEED/MACH

#### Corrective

This behavior starts with the vertical speed in the red zone of the VSI. As the behavior denotes this RA will require active corrective measure automatically via the autopilot or manually from the flight crew to fly out of the red zone towards the edge of the green / red zone on the VSI. It is usually coupled with audiable alerts such as "Climb, Descend".

- TCAS will engage and ensure vertical guidance to avoid conflict. It will target the zone mentioned above.
- Targets a V/S of 200ft/min inside of the green band on the VSI.
- Longitudinal modes previously armed will automatically be disarmed except ALT^*^
    - This prevents the aircraft from exceeding a commanded altitude / prevent excursions
    - A V/S of 0 ft/min is always within the safe zone for a corrective RA which allows for TCAS to capture a targeted flight level if capture conditions are met
- To ensure a safe speed during any maneuvers A/THR will engage SPEED/MACH

---

## External Resources

Airbus' Safety First publication has great resources further explaining their systems in-depth with supporting graphics and statistics. We've provided a link below to a great article detailing TCAS Alert Prevention (TCAP) and the AP/FD TCAS function.

[Safe Handing of TCAS Alerts](https://safetyfirst.airbus.com/safe-handling-of-tcas-alerts/){.md-button primary}

---

## TCAS Known Issues

- No support for offline AI traffic (sim limitation)
- No support of multiplayer (MSFS) traffic (sim limitation)
- Possible false detection of ground traffic
- Possible ghost TA / RA due to jumping traffic (*improvements and changes expected*)

!!! tip "A Quick Note on TCAS Performance"
    TCAS relative altitude is now based on plane altitude (true altitude) for both airplanes. This should work exactly as intended for MSFS airplanes relative to one another (though not as the IRL TCAS works). It can still be somewhat of an issue when on a network with non-MSFS airplanes.

    The reason for this is that MSFS is the only sim that should correctly compute the true altitude. Depending on the atmospheric conditions, an MSFS airplane flying in the same weather and with the same baro setting as a non-MSFS airplane may be at a different true altitude than the non-MSFS airplane. Said differently, each aircraft could be at the same altitude in their respective simulator, but TCAS would show them at different altitudes.

    {==

    This is not just a TCAS issue. It is an issue that VATSIM and all the other networks are struggling with so that ATC sees all airplanes, regardless of sim, at the right altitudes, at least relative to one another.

    ==}