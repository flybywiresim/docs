# Custom Hydraulics

## Gear system

### Gravity extension
Gravity extension is already fully supported by our gear system. However, user experience is not perfect yet due to current model limitations.

While this feature will eventually be perfectly supported with a moving crank handle, for now gravity extension can be used by two means:
  -Clicking and holding left mouse button on the red part of the crank handle. [ADD IMAGE]
  -Using the ingame binding "EMERGENCY GEAR TOGGLE" by holding it.
  
Using either of those above methods, you need to click and hold until gear is released. 

If not holding long enough, you will end up with crank handle only doing one or two turns, which will have following consequences:
  - After 1 turn, hydraulic supply to gear system is closed
  - After 2 turns, doors uplockes will be release and door will stay opened

For now the process cannot be reverted, so once crank handle is used, there's no turning back. This will be subject to change when we find a suitable way to provide feedback about the handle position.

### Known issues
- Door visual position is not modeled yet due to 3D model issues. Their actual position is however fully simulated internally.
  Because of this:
  - Gear doors will start to visually open with a 2 to 3s delay, because actual doors are in fact already opening during those 2-3s while you cannot see them
  - Gear doors will visually close at end of gear extension even if actual doors stay open (for exemple after gravity extension)
- Gear system can only be used through in game binding events or in cockpit lever. Writing to simvars to control gear is not supported
- If a hardware input is set to GEAR UP or GEAR DOWN, in cockpit lever cannot be clicked or mouse draged
