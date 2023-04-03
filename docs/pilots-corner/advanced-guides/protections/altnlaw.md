# Alternate Law in the A320
Alternate Law is activated when the plane looses certain computers, avionics or sensors , you can tell Alternate Law is in effect by the ECAM Message: "ALTN LAW: PROT LOST".

On the PFD Indications for protective limits are replaced by amber "x" indication when the associated system is unavailable.

Alternate Law may be caused by the failure off all three SECs, both ELACs or 2 or 3 ADRs, but also failure of a sidestick, loss of 2 hydraulic systems and many more.

Under Alternate Law the aircraft looses attitude, high angle of attack ([Alpha Floor](afloor.md)), high speed and low energy protection.

A recovery from Alternate Law may be possible if the causing failure can be rectified (restarting computers, regaining hydraulic pressure).
## System status under Alternate Law
- The Autopilot is inoperable
- Bank angle and [Alpha Floor](afloor.md) protection are lost, meaning the plane can be stalled or overbanked. 
- [Alpha Floor](afloor.md) is replaced by the "Barber Pole" on the airspeed Indicator and the Stall Warning Speed V~SW~
//Fix above, it‘s not A Floor that‘s being replaced 
- Autotrim is still operable.
- A "speed stability function" replaces the AOA protection, trying to pitch the plane down when speed is too low (about 5kts before reaching V~SW~) and pitch back up when speed is too high.
- The speed stability function can be overriden by inputs from the sidestick.
- Load factor limitation is fully operational.

Different failures can cause different systems to be unavailable deviating from this list. For example speed stability may be unavailable under certain failure conditions.

The ECAM will display which measures should be taken to subsidize the lost systems.

## Considerations for Flying under Alternate Law
- The sidestick translates all inputs directly, unlike in Normal Law where sidestick inputs are translated to "Load Demand". This means the sidestick is very sensitive, take care while maneuvering.
//Change this, sensitive is bad wording 
- When deploying the landing gear, the aircraft reverts to Direct Law. This means all protections along with load factor limitation and Auto Trim are lost, maneuvering with extreme care is necessary.

## Abnormal Alternate Law
Unlike normal Alternate Law, Abnormal Alternate Law is activated when the plane is far outside the normal flight envelope and reaches abnormal attitudes.

Abnormal Alt. Law is meant to give the pilot the necessary control authority to recover the plane.

In Abnormal autotrim is turned off and Roll Control is switched to Direct Law.

When the plane has recovered autotrim is enabled again, pitch and yaw control remain in alternate.