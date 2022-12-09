# Flight Planning

## Overview

Flying an airliner is usually done using IFR (Instrument Flight Rules). This means that you will be flying with an IFR 
flight plan. The IFR flight plan is usually created before the flight, and is then loaded into the aircraft's flight 
management system (FMS). 

See [MCDU F-PLN page](../../pilots-corner/a32nx-briefing/mcdu/f-pln.md) for more information on the aircraft's 
flight planning in the Multipurpose Control and Display Unit (MCDU).

There are various ways to load a flight plan into the aircraft. In real life pilots usually use an external data link 
to load flight plans made for the flight by their company. Or they use the MCDU to enter a flight plan manually from 
their flight briefing documents. 

In the A32NX for Microsoft Flight Simulator, we have these options to load a flight plan:

- [Entering a Flight Plan Manually](../../pilots-corner/beginner-guide/preparing-mcdu.md#--f---light-plan)
- [Loading a Flight Plan from SimBrief](simbrief.md) (recommended)
- Creating and Loading a Flight Plan from the MSFS World Map

As Microsoft Flight Simulator uses a very simplified flight planning system, we have created our own custom FMS 
(Flight Management System) which is used in the A32NX. It is much closer to the FMS in the real aircraft und 
understands and represents real world flight plans much more accurately. 

A custom FMS on the other hand results in issues syncing the flight plan from the aircraft back into the 
simulator. Therefore, simulator-features as the MSFS ATC or the VFR Map will not always work as expected. Especially 
flight plans with complex routing may have significant issues if saved backwards or loaded externally through 
simulator's simplified flight planning.

This is a general issue of all realistic and complex airliners in Microsoft Flight Simulator and unless the simulator's 
built-in flight planner and ATC is significantly improved this will always cause problems with realistic airliners.

## MSFS World Map Flight Planning, ATC, VFR Map

Depending on how you want to use the A32NX in combination with the MSFS' World Map Planning, ATC and VFR Map, you 
can choose between different methods to load a flight plan into the A32NX:

- [Not Using MSFS World Map, MSFS ATC or MSFS VFR Map](#not-using-msfs-world-map-msfs-atc-or-msfs-vfr-map) (recommended)
- [Loading a Flight Plan from the MSFS World Map](#using-the-msfs-world-map-flight-planner-to-create-and-load-a-flight-plan)
- [Using MSFS World Map and MSFS ATC](#using-the-msfs-world-map-flight-planner-and-msfs-atc)
- [Using a SimBrief Flight Plan and MSFS ATC](#importing-a-simbrief-flight-plan-and-using-msfs-atc)

See [Setting `Sync MSFS Flight Plan`](flypados3/settings.md#sim-options) for more information.

### Not Using MSFS World Map, MSFS ATC or MSFS VFR Map

We recommend to use our built-in integration with [SimBrief](https://www.simbrief.com){target=_blank} for flight 
planning. This will allow you to directly import flight plans from SimBrief into the MCDU.

See our [SimBrief Integration Guide](simbrief.md) for more information.

As long as MSFS ATC and VFR Map are not required, the aircraft's flight plan does not have to be synchronized back to 
the MSFS flight planner (set `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` to `None`).

The MSFS ATC and VFR Map will not be aware of the flight plan at all and cannot be used.

!!! note ""
    This is the ideal setup for users who want to use the A32NX in combination with Online ATC services (Vatsim, Ivao, 
    PilotEdge,...), 3rd party ATC add-ons or no ATC at all. 

### Using the MSFS World Map Flight Planner to Create and Load a Flight Plan

If you want to use the MSFS World Map Flight Planner to build and load a flight plan, you need to set the `Sync MSFS 
Flight Plan` option in the `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` to `Load Only`.

This ensures the MSFS flight plan is loaded into the aircraft's flight plan when starting the flight.

Any changes made to the flight plan in the MCDU will **not** be saved back to the MSFS flight plan. This means the MSFS
ATC and VFR Map will **not** be aware of these changes.

### Using the MSFS World Map Flight Planner and MSFS ATC

If you are using the MSFS Flight Planner to build and load a flight plan, and you also want to use the MSFS ATC even
after making changes to the aircraft's flight plan, you need to set the `flyPad's Setting > Sim Options > Sync MSFS 
Flight Plan` option to `Save`.

With this setting the aircraft will attempt to save any changes to the flight plan made in the MCDU back to the 
simulator's flight plan. This will **not** always work as expected and may result in issues with the MSFS ATC. See 
warning below.

!!! warning "Synchronization Issues Expected"
    The aircraft's custom Flight Management System provides better accuracy and features over the default
    flight plan manager in Microsoft Flight simulator which results in issues syncing the flight plan from the
    MCDU back into the simulator. Do not expect it to work properly in all cases.

### Importing a SimBrief Flight Plan and Using MSFS ATC

If you are using the aircraft's built-in SimBrief integration to import a flight plan, and you also want to use the
MSFS ATC you need to set the `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` option to `Save`.

With this setting the aircraft attempts to save the loaded SimBrief flight plan and any subsequent changes to the
flight plan made in the MCDU back to the simulator's flight plan. This will **not** always work as expected and may
result in issues with the MSFS ATC. See warning below.

!!! warning "Synchronization Issues Expected"
    The aircraft's custom Flight Management System provides better accuracy and features over the default
    flight plan manager in Microsoft Flight simulator which results in issues syncing the flight plan from the
    MCDU back into the simulator. Do not expect it to work properly in all cases.

