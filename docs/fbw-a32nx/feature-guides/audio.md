# Audio Configuration

This page provides an overview of the various audio settings available in the A32NX and their respective functions.

These settings can be found on the EFB:

![EFB Audio Settings](../assets/flypados3/flypad-settings-audio.png)

For information on the other settings available on the EFB visit our [flyPad Settings](flypados3/settings.md) page.

## Passenger Simulation

!!! important "Cockpit Door"
    The cockpit door in the A32NX is simulating a real A320 cockpit door which in consequence dampens most of the sounds from the passenger cabin. 

    If you want to enjoy the Passenger Ambience sounds make sure it is open.

We have included various settings that simulate flight crew interactions with passengers on board.

### Passenger Ambience
If this setting is enabled the following ambience sounds are played:

- Boarding sound begins when the W/B in `MCDU-ATSU-AOC-W&B` boarding is started.
- Once passengers are on the plane, a constant passenger ambience background sound plays.
- Deboarding through the W/B section in `MCDU-ATSU-AO-W&B` triggers the deboarding sound.

### Announcements

!!! important "Customizations"
    Due to limitations with MSFS audio configurations adding user customizable announcements/sounds is not easily possible.

If this setting is enabled the following crew announcements are played.

| Trigger                                    | Audio Played                                    |     Speaker      |
|:-------------------------------------------|:------------------------------------------------|:----------------:|
| Boarding Completed                         | "Boarding Completed" announcement               | Flight Attendant |
| Boarding Completed + 30s                   | Captain makes a "Welcome on Board" announcement |     Captain      |
| Beacon Light set to `ON`                   | "Arm Doors" Announcement                        | Flight Attendant |
| "Arm Doors" Announcement + 30s             | Safety Demo                                     | On-Board System  |
| Landing Lights set to `ON`                 | "Prepare for Takeoff" Announcement              |     Captain      |
| Enter **Cruise Phase** + 30s               | "Cruise" Announcement                           |     Captain      |
| Enter **Descent Phase** + 30s              | "Descent" Announcement                          |     Captain      |
| Gear Down + **Approach Phase** Active      | "Prepare for Landing" Announcement              |     Captain      |
| **Done Phase** + Beacon Light set to `OFF` | "Disarm Doors" Announcement                     | Flight Attendant |

### Boarding Music
If enabled music will be played during boarding.

## Realism Settings

### PTU

The PTU is generally not heard in the cockpit. As a passenger we understand people may be used to this sound as it is very audible in the passenger cabin.

We have added a toggle to allow the PTU to be heard in the cockpit which in real life is not the case. 

## Engine and Wind

- Exterior Master Volume:
    - Volume for sounds audible when in external views.

- Engine Interiors Sounds:
    - Volume for engine sounds when in interior views.

- Wind Interior Volume:
    - Volume for wind sounds when in interior views.
