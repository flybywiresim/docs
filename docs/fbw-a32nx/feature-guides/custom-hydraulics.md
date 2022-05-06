# Custom Hydraulics

## Gear system
New gear system aims at replicating its real counterpart in the slightest details. While more improvements will come, the current system already features:
- Rigid body physics of gears and doors
- Hydraulic actuators simulation with "push to retract" main gears and "push to extend" nose gear. 
- All proximity sensors, one set per LGCIU computer
- LGCIU computers monitoring, sequence control state machine and their change-over mechanism
- Safety valve / Shut off valve / Vent valves controls
- Gear lever baulk lock mechanism powered by LGCIUs
- Emergency extension system

Non exhaustive list of features yet to come:
- Aerodynamic effects
- Complete fault monitoring and BITE tests of LGCIUs
- Complete set of failures
- Animated emergency gear crank handle
  

### Failures
Some first failures are provided, and while ECAM information impact is a temporary placeholder, consequences on the gear system are fully modeled.

- LGCIU power input failure will cause complete electrical loss of the computer and its outputs. Other LGCIU will take control to ensure gear control. 

Note 1: Power failure on LGCIU1 will cause the gear light indicator to be lost.

Note 2: A failed LGCIU can be reset by toggling this fault on and off, as would a circuit breaker cycle do.

- LGCIU internal error failure will cause the LGCIU to fail its internal continuous tests. It will declare a fault and Other LGCIU will take control to ensure gear control. Power input in that case is still present, so an internal error on LGCIU1 will still maintain the gear light indicator.

- Proximity sensor failure are physical issues on the considered LGCIU sensors. Those cannot be electrically detected by the computer, so it may cause gear retraction or extension sequence to fail and get stuck. A LGCIU fault will finally be declared because of too long sequence time. A gear lever recycling down to up will switch gear control to the other computer to complete current sequence.

Note: Only issues on LGCIU1 proximity sensors will show erroneous information on gear light indicator.


### Gravity extension
Gravity extension is already fully supported by our gear system. However, user experience is not perfect yet due to current model limitations.

While this feature will eventually be perfectly supported with a moving crank handle, for now gravity extension can be used by two means:
- Clicking and holding left mouse button on the red part of the crank handle.
    [ADD IMAGE]
- Using the ingame binding "EMERGENCY GEAR TOGGLE" by holding it.
  
Using either of those above methods, you need to click and hold until gear is released. 

If not holding long enough, you will end up with crank handle only doing one or two turns, which will have following consequences:
- After 1 turn, hydraulic supply to gear system is closed
- After 2 turns, doors uplocks will be released and door will stay opened

For now the process cannot be reverted, so once crank handle is used, there's no turning back. This will be subject to change when we find a suitable way to provide feedback about the handle position.

### Known issues
- Door visual position is not modeled yet due to 3D model issues. Their actual position is however fully simulated internally.
  Because of this:
  - Gear doors will start to visually open with a 2 to 3s delay, because actual doors are in fact already opening during those 2-3s while you cannot see them
  - Gear doors will visually close at end of gear extension even if actual doors stay open (for exemple after gravity extension)
  - Visual movement of doors is only coming from gear movement, thus causing strange door oscillations in some cases that are not real.
- Gear system can only be used through in game binding events or in cockpit lever. Writing to simvars to control gear is not supported
- If a hardware input is set to GEAR UP or GEAR DOWN, in cockpit lever cannot be clicked or mouse draged
