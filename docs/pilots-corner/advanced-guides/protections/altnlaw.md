# Alternate Law in the A320
Alternate Law is activated when the plane looses certain computers, avionics or sensors , you can tell Alternate Law is in effect by the ECAM Message: "ALTN LAW: PROT LOST".

On the PFD Indications for protective limits are replaced by amber "x" indication when the associated system is unavailable.

Alternate Law may be caused by the failure off all three SECs, both ELACs or 2 or 3 ADRs, but also failure of a Sidestick, loss of 2 Hydraulic Systems and many more.

Under Alternate Law the Aircraft looses Attitude, High Angle of Attack ([Alpha Floor](afloor.md)), High Speed and Low Energy Protection.

A recovery from Alternate Law may be possible if the causing failure can be rectified (Restarting Computers, Regaining Hydraulic Pressure).
## System Status under Alternate Law
- The Autopilot is inoperable
- Bank Angle and [Alpha Floor](afloor.md) Protection are lost, meaning the Plane can be stalled or overbanked. 
- [Alpha Floor](afloor.md) is replaced by the "Barber Pole" on the Airspeed Indicator and the Stall Warning Speed V~SW~
- Autotrim is still operable.
- A "speed stability function" replaces the AOA Protection, trying to pitch the plane down when Speed is too low (about 5kts before reaching V~SW~) and pitch back up when speed is too high.
- The speed stability function can be overriden by inputs from the Sidestick.
- Load Factor Limitation is fully operational.

Different Failures can cause different Systems to be unavailable deviating from this list. For example speed stability may be unavailable under certain failure conditions.

The ECAM will display which measures should be taken to subsidize the lost systems.

## Considerations for Flying under Alternate Law
- The Sidestick translates all inputs directly, unlike in Normal Law where Sidestick inputs are translated to "Load Demand". This means the Sidestick is very sensitive, take care while maneuvering.
- When deploying the Landing Gear, the Aircraft reverts to Direct Law. This means all protections along with Load Factor Limitation and Auto Trim are lost, maneuvering with extreme care is necessary.

## Abnormal Alternate Law
Unlike normal Alternate Law, Abnormal Alternate Law is activated when the plane is far outside the normal flight envelope and reaches abnormal attitudes.

Abnormal Alt. Law is meant to give the Pilot the necessary control authority to recover the plane.

In Abnormal autotrim is turned off and Roll Control is switched to Direct.

When the Plane has recovered autotrim is enabled again, Pitch and Yaw Control remain in Alternate.