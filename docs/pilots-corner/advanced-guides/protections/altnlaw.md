# Alternate Law in the A320

Alternate Law is activated when the plane looses certain computers, avionics or sensors , you can tell Alternate Law is in effect by the ECAM Message: "ALTN LAW: PROT LOST".

On the PFD indications for protective limits are replaced by amber "x" indication when the associated system is unavailable.


Under Alternate Law the aircraft looses attitude, high angle of attack ([Alpha Floor](afloor.md)), high speed and low energy protection.

A recovery from Alternate Law may be possible if the causing failure can be rectified.

## „Failure Cases“ List
// Self Detection should be considered for addition
Following failures will lead to the activation of [Alternate Law with reduced protection](#Alternate-Law-with-Reduced-Protection)

- Failure of 2 ADRs
- Failure of both ELACs
- Failure of one elevator
- Failure of one sidestick
- Failure of 2 IRs
- Loss of ELAC 1 **and** either green or yellow hydraulic system 
- Loss of ELAC 2 **and** the blue hydraulic system
- Loss of all Spoilers
- Loss of all three SECs

Following failures will lead to the activation of [Alternate Law with reduced protection and mechanical yaw control](#Alternate-Law-with-Reduced-Protection)

- Failure of both FACs
- Failure of the green and yellow hydraulic system
- Failure of the yaw damper
- Emergency Electrical Configuration (On Batteries)

When EMER ELEC form RAT comes AVAIL and FAC 1 is reset, recovery to Alt Yaw is possible

Following failures will lead to the activation of [Alternate Law without Protection](#Alternate-Law-without-Protection)

- Failure of all three ADRs
- Failure of both SFCC Slat Channels 
- Failure of the green and blue hydraulic system

!!! warning „Approach and Landing with Alternate Law“
    When deploying the Landing Gear under Alternate Law **and** the Autopilot is disconnected
    the controls switch directly to [Direct Law](#Direct-Law).
    Loss of all protections on final approach should be anticipated and the flightcrew should prepare to take over pitch trimming for landing.  

Loss of all three IRs makes the plane fall back to [Direct](#Direct-Law) immediately
// Add Landing Dir stuff with Alt for Yaw instead of Mech
// Three following points still WIP

##Alternate Law with Reduced Protection

- Pitch is Alt
- Roll is Direct
- Yaw is Alternate, may be mechanical if conditions met

##Alternate Law without Protection

- Pitch is Alt (No Prot)
- Roll is Direct
- Yaw is Alternate

##Direct Law

- Pitch is Direct
- Roll is Direct
- Yaw is mechanical, may be alternate if conditions met


## System status under Alternate Law
- The Autopilot is inoperable
- Bank angle and [Alpha Floor](afloor.md) protection are lost, meaning the plane can be stalled or overbanked. 
- Protection speeds on the speed indicator are replaced by the "Barber Pole" on the airspeed indicator and the stall warning speed V~SW~
//Insert mention of Alpha Max and Alpha Min here 
- Autotrim is still operable.
- A "speed stability function" replaces the AOA protection, trying to pitch the plane down when speed is too low (about 5kts before reaching V~SW~) and pitch back up when speed is too high.
- The speed stability function can be overriden by inputs from the sidestick.
- Load factor limitation is fully operational.
//Also relevant for Failure list
Different failures can cause different systems to be unavailable deviating from this list. For example speed stability may be unavailable under certain failure conditions.

The ECAM will display which measures should be taken to subsidize the lost systems.

## Considerations for Flying under Alternate Law
- The sidestick translates all inputs directly, unlike in Normal Law where sidestick inputs are translated to "Load Demand". This means the sidestick is very direct, take care while maneuvering.
//Change this, sensitive is bad wording 
- When deploying the landing gear, the aircraft reverts to Direct Law. This means all protections along with load factor limitation and Auto Trim are lost, maneuvering with extreme care is necessary.

## Abnormal Alternate Law
//Always? or just under Altn Law in the first place
Unlike normal Alternate Law, Abnormal Alternate Law is activated when the plane is far outside the normal flight envelope and reaches abnormal attitudes.

Abnormal Alt. Law is meant to give the pilot the necessary control authority to recover the plane.

In Abnormal autotrim is turned off and Roll Control is switched to Direct Law.

When the plane has recovered autotrim is enabled again, pitch and yaw control remain in alternate.