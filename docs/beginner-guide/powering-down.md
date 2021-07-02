# Powering Down

This guide will explain the correct procedures to power down the aircraft when at the gate after arriving at the destination and taxi to the designated gate.

Obviously this is not strictly required in a simulator but for interested sim pilots this might be an interesting process for a more realistic experience.

!!! warning "Disclaimer"
    The level of detail in this guide is meant to help a FlyByWire A320neo
    beginner to correctly shut down the aircraft.

    A *beginner* is defined as someone familiar with flying a GA aircraft
    or different types of airliners. Aviation terminology and know-how is
    a requirement to fly any airliner even in Microsoft Flight Simulator.

    Check out the FlyByWire YouTube Channel as well: [FlyByWire on YouTube](https://www.youtube.com/c/FlyByWireSimulations/playlists)

    You will find many great videos on YouTube on how to fly the FlyByWire A32NX.<br/>

---

## Pre-requisites

- Aircraft is at the gate after landing and taxi as per previous chapters.

[Download FlyByWire Checklist](../assets/FBW_A32NX_CHECKLIST.pdf){ .md-button }

## Chapters / Phases

This guide will cover these phases:

1. Parking at the Gate
2. Disembarking Passengers and Baggage
3. Securing the Aircraft

---


## Preface
Shutting down and securing an aircraft is an important part of the overall procedure. Obviously less important in a simulator as the next flight will have the aircraft start in a cold and dark state again.

If we want to actually do a turn around and start a new flight directly the procedure will be different as we would not turn of certain systems and at some point simply start with the preparation of the aircraft procedure again. We will add notes to the steps what to do in case of a turn around.

## Parking at the Gate

**Situation**

- We arrived at the designated gate after taxiing from the runway where we landed.
- Aircraft is in taxi state as per previous chapters.
- Engines are still running
- Lights are still in taxi configuration (`RWY TURN OFF` set to on and `NOSE` is to taxi, `LAND`-ing lights are off)
- `APU` has been turned on during taxi and is `AVAIL`, `APU BLEED` is off.
- **After Landing** checklist is completed

Steps after arriving at the gate:

- Set parking break (`PARK BRK`)
- `NOSE TAXI` and `RWY TURN OFF` lights are usually turned off even before we turn into the gate to not blind the ground personnel. This of course is only done if enough lighting is available to safely park into the gate. Turn the, off if not done so before.
- Turn on `APU BLEED` before we turn off the engines
- Shut down the engines by setting the `ENG 1` and `ENG 2` master switches to off.
- Wait until N2 is below 5% (<== TODO check this)
- Turn off `Seat Belt` sign
- Turn off all external lights: `BEACON`, `NAV & LOGO`, `STROBE`
- Turn off all fuel pumps
- Complete **Parking** checklist.

(TODO: add images)

If external power is available the ground crew would have connected it by now and we can turn on `EXT PWR`. If we would turn off the APU depends on the turn around time. For a shutdown we do this after the passengers have disembarked to still have airflow in the cabin. See last chapter.

This concludes *Parking at the Gate*.

## Disembarking passengers and baggage

**Situation:**

- **Parking** checklist is completed

In real life there a many things starting automatically after parking at the gate. The jetway is connected to the aircraft, doors are opened, passengers disembark, cargo is unloaded, etc. The pilots don't have to do much to trigger these steps.

In the simulator though we would have to trigger them by ourselves. For this we use the FlyByWire FlyPad's ground functionality or the Microsoft Flight Simulator's build-in ATC to start these procedures. There are also some nice add-on tools out there which help with this.

Taking care of passengers and luggage with the FlyByWire FlyPad:

- Go to the FlyPad (view can be activated by `Ctrl+0`)
- Connect the jetway
- Call cargo/baggage

(TODO: add images)

Obviously this would take a while in real life and we would not be able to shut down the aircraft before everybody is disembarked.

For a turn around we would start preparing the aircraft for the next flight and the cabin crew would coordinate everything from disembarking the passengers, cleaning and resetting the cabin.

After refuelling the pilot would signal the cabin crew that they could let the new passengers board the aircraft once the cabin is ready.

This concludes *Disembarking passengers and baggage*.

## Securing the Aircraft

**Situation:**

- **Parking** checklist is completed
- Aircraft is empty (no passengers or cargo)
- Cabin is cleaned and ready for shutdown

To secure the aircraft we follow these steps:

- Turn off the `ADIRS`
- Turn off `OXYGEN`
- Turn off `APU BLEED`
- Turn off emergency exit lights `EMER EXIT LT`
- Turn off cabin sign: `NO SMOKING`
- Optional or depending on airline SOPs: Reset A/C, lighting and screen brightness
- Turn off `APU MASTER`
- Turn off `BAT 1` and `BAT 2` (some airlines require to wait 2 minutes before turing off batteries after the APU has been shut down)

(TODO: add images)

Now the aircraft is back in a cold and dark state.

This concludes *Securing the Aircraft*

