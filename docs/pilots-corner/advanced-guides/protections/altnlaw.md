# Alternate Law in the A320

Alternate Law is activated when the plane looses certain computers, avionics or sensors , you can tell Alternate Law is in effect by the ECAM Message: "ALTN LAW: PROT LOST".

On the PFD indications for protective limits are replaced by amber "x" indication when the associated system is unavailable.


Under Alternate Law the aircraft looses attitude, high angle of attack ([Alpha Floor](afloor.md)), high speed and low energy protection.

A recovery from Alternate Law may be possible if the causing failure can be rectified.

## „Failure Cases“ List

[//]: # ( Self Detection should be considered for addition)
Following failures will lead to the activation of [Alternate Law with reduced protection](#Alternate-Law-with-Reduced-Protection)

- Failure of 2 ADRs (self detected)
- Failure of both ELACs
- Failure of one elevator
- Failure of one sidestick
- Failure of 2 IRs (self detected)
- Loss of ELAC 1 **and** either green or yellow hydraulic system 
- Loss of ELAC 2 **and** the blue hydraulic system
- Loss of all Spoilers
- Loss of all three SECs
- Jam of THS

Following failures will lead to the activation of [Alternate Law with reduced protection and mechanical yaw control](#Alternate-Law-with-Reduced-Protection)

- Failure of 2 ADRs (Failure of second ADR not self detected **and** Disagreement related to calculated airspeed (CAS) or Mach speed)
- Failure of both FACs
- Failure of the green and yellow hydraulic system
- Failure of the yaw damper

??? info "Self Detection"
    All flight systems are continuously monitored by the flight computers, when a peripheral system detects a fault it will inform the flight computers or shut down (self detected failure). 
    Some faults can not be detected by the peripheral system itself because it can only see its own data. 
    The flight computer can compare the data across systems, when detecting an abnormality it ignores the corresponding system. This is known as a "non self detected failure".     
Following failures will lead to the activation of [Alternate Law without Protection](#Alternate-Law-without-Protection)

- Failure of all three ADRs
- Failure of both SFCC Slat Channels 
- Failure of the green and blue hydraulic system

!!! warning "Approach and Landing with Alternate Law"
    When deploying the Landing Gear under Alternate Law **and** the Autopilot is disconnected
    the controls switch directly to [Direct Law](#Direct-Law).
    Loss of all protections on final approach should be anticipated and the flightcrew should prepare to take over pitch trimming for landing.  

Following failures will lead to the activation of [Direct Law](#Direct-Law)
- Failure of all three IRs

## Special Failure Conditions
Some failure conditions are caused by a combination or factors and can cause abnormal failure modes, some may allow recovery to a more stable state
- When the plane is in "Emergency Electrical Configuration (On Batteries)" Alternate Law with reduced protections is active, although yaw control is switched to the mechanical backup, after emergency power becomes available resetting FAC 1 allows recovery to Alternate control over yaw.
- When 2 IRs fail with the second not being self detected the flight crew has to identify and switch off the faulty IR before reseting **both** ELAC 1 and 2, the Plane will recover to Alternate Law with reduced protection.
- When the Radio Altimeters fail with Gear down **or** the plane is in CONF 2 and the LGCIUs have a data disagreement, Direct Law will be used. Abnormal from Direct Law Yaw Control will be kept in Alternate.

[//]: # (Three following points still WIP)

## Alternate Law with Reduced Protection

- Pitch is Alt
- Roll is Direct
- Yaw is Alternate, may be mechanical if conditions met

## Alternate Law without Protection

- Pitch is Alt (No Prot)
- Roll is Direct
- Yaw is Alternate

## Direct Law

- Pitch is Direct
- Roll is Direct
- Yaw is mechanical, may be alternate if conditions met

[//]: # (Subject for removal, move statuses to the respective subpoints above)
## System status under Alternate Law
- The Autopilot is inoperable
- Bank angle and [Alpha Floor](afloor.md) protection are lost, meaning the plane can be stalled or overbanked. 
- [Protection speeds](https://docs.flybywiresim.com/pilots-corner/advanced-guides/protections/overview/#high-speed-protection) on the speed indicator are replaced by the "Barber Pole" on the airspeed indicator and the stall warning speed V~SW~

[//]: # (Insert mention of Alpha Max and Alpha Min here )
- Autotrim is still operable.
- A "speed stability function" replaces the AOA protection, trying to pitch the plane down when speed is too low (about 5kts before reaching V~SW~) and pitch back up when speed is too high.
- The speed stability function can be overriden by inputs from the sidestick.
- Load factor limitation is fully operational.

[//]: # (Also relevant for Failure list)
Different failures can cause different systems to be unavailable deviating from this list. For example speed stability may be unavailable under certain failure conditions.

The ECAM will display which measures should be taken to subsidize the lost systems.


[//]: # ( - The sidestick translates all inputs directly, unlike in Normal Law where sidestick inputs are translated to "Load Demand". This means the sidestick is very direct, take care while maneuvering.)


## Abnormal Alternate Law

[//]: # (Always? or just under Altn Law in the first place)
Unlike normal Alternate Law, Abnormal Alternate Law is activated when the plane is far outside the normal flight envelope and reaches abnormal attitudes.

Abnormal Alt. Law is meant to give the pilot the necessary control authority to recover the plane.

In Abnormal autotrim is turned off and Roll Control is switched to Direct Law.

When the plane has recovered autotrim is enabled again, pitch and yaw control remain in alternate.