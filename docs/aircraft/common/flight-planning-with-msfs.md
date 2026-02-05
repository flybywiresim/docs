---
title: Flight Planning With MSFS
description: Discover how to integrate MSFS' flight planning, ATC, and VFR Map with the FlyByWire A32NX and A380X.
---

# Flight Planning With MSFS

## Overview

Depending on which simulator you use, there are different flight planning tools to your disposal and their level of compatibility and integration vary. MSFS 2020 offers a built-in World Map flight planner, ATC system, and VFR Map. However, these features are simplified and may not fully align with the capabilities of complex aircraft like the FlyByWire A32NX and A380X.

MSFS 2024 introduced significant improvements to the built-in flight planning and ATC systems, enhancing their compatibility with complex aircraft. However, some limitations may still exist.

## MSFS 2024

Flight planning integration with MSFS 2024 revolves around the built-in EFB. This is different from our in-aircraft EFB, the [flyPad](../flypados3).

!!! tip "Opening the MSFS built-in EFB"
    The MSFS built-in EFB can be accessed either by pressing the `TAB` key or by selecting the EFB icon in the top in-game toolbar.
    
    ![EFB Toolbar Options](./assets/flight-planning-with-msfs/efb-toolbar-option.png "EFB Toolbar Option"){loading=lazy}

### Loading a route from the EFB into the aircraft

1. Plan your route in the MSFS EFB
2. Select the "SEND" menu at the top of the Route page
3. Select either "SEND TO AVIONICS" or "SEND TO AVIONICS AND ATC" depending on whether you want to [file the flight plan with ATC](#filing-a-flight-plan-with-atc) as well.

![Send to Avionics Options](./assets/flight-planning-with-msfs/send-to-avionics-options.png "Send to Avionics Options"){loading=lazy}

??? note "Loading the EFB route automatically"
    If you want the route to automatically load into the aircraft's FMS when spwaning in, enable the [`Automatically Load MSFS Route`](./flypados3/settings.md#sim-options) option in the flyPad "Sim Options" page.

### Loading a route from the online flight planner

Loading a route from the [online flight planner](https://planner.flightsimulator.com/) into the aircraft's FMS is done by first loading the route into the EFB, then following the steps to load a route from the EFB into the aircraft.

### Retrieving a route from the aircraft into the EFB

1. Select the "OPEN" (folder icon) menu at the top of the Route page in the EFB
2. Select "REQUEST FROM AVIONICS"

![Request from Avionics Option](./assets/flight-planning-with-msfs/request-from-avionics-option.png "Request from Avionics Option"){loading=lazy}

!!! note "Limitations of retrieved routes"
    As with real-world equivalents, there are limitations to the type of information that can be transmitted between flight planning systems and aircraft. Notably,
    a lot of modifications made in the aircaft FMS cannot be represented, such as adding holds, offsets, modifying/cutting procedures, adding fly-overs, and more.
    
    While our FMS tries its best to convert a full flight plan into a route description, some information may be lost in translation. Always double-check the route for accuracy and completeness.

### Filing a flight plan with ATC

Planning a route in the MSFS EFB or retrieving it from the aircraft does not automatically file it with ATC.

1. Plan your route in the MSFS EFB or retrieve it from the aircraft
2. Select the "SEND" menu at the top of the Route page
3. Select "SEND TO AVIONICS AND ATC" or "SEND TO ATC" depending on whether you want to also [load the route into the aircraft's FMS](#loading-a-route-from-the-efb-into-the-aircraft) as well.

![Send to Avionics Options](./assets/flight-planning-with-msfs/send-to-atc-options.png "Send to ATC Options"){loading=lazy}

## MSFS 2020

!!! warning "A32NX Only"
    The following instructions are specific to the FlyByWire A32NX. For information on flight planning with the A380X, please refer to the [A380X Flight Planning Guide](../a380x/feature-guides/flight-planning.md), or
    if using MSFS 2024, follow the [MSFS 2024 Flight Planning Guide](#msfs-2024).

Depending on how you want to use the A32NX in combination with the MSFS' World Map Planning, ATC and VFR Map, you can choose between different methods to load a flight plan into the FMS:

!!! tip ""
    - [Not Using MSFS World Map, MSFS ATC or MSFS VFR Map](#not-using-msfs-world-map-msfs-atc-or-msfs-vfr-map) (recommended)
    - [Loading a Flight Plan from the MSFS World Map](#using-the-msfs-world-map-flight-planner-to-create-and-load-a-flight-plan)
    - [Using MSFS World Map and MSFS ATC](#using-the-msfs-world-map-flight-planner-and-msfs-atc)
    - [Using a SimBrief Flight Plan and MSFS ATC](#importing-a-simbrief-flight-plan-and-using-msfs-atc)

See [Setting `Sync MSFS Flight Plan`](./flypados3/settings.md#sim-options) for more information.

### Not Using MSFS World Map, MSFS ATC or MSFS VFR Map

!!! note ""
    This is the ideal setup for users who want to use the aircraft in combination with Online ATC services (Vatsim, Ivao, PilotEdge,...), 3rd party ATC add-ons or no ATC at all.

We recommend using our built-in integration with [SimBrief](https://www.simbrief.com){target=_blank} for flight planning. This allows you to directly import flight plans from SimBrief into the FMS.

See our SimBrief Integration Guide for the [A32NX](../a32nx/feature-guides/simbrief.md) or [A380X](../a380x/feature-guides/simbrief.md) for more information.

As long as MSFS ATC and VFR Map are not required, the aircraft's flight plan does not have to be synchronized back to
the MSFS flight planner (set `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` to `None`).

The MSFS ATC and VFR Map will not be aware of the flight plan at all and cannot be used.

!!! warning "For SimBrief Import, Do Not Set a Destination in the MSFS World Map"
    If you plan to import a SimBrief flight plan, please do **not** set a destination airport in the MSFS World Map as otherwise the aircraft will import the MSFS World Map flight plan, and it will not offer the "INIT REQUEST" option.  

### Using the MSFS World Map Flight Planner to Create and Load a Flight Plan

!!! note ""
    This is the ideal setup for users who do not use Online ATC nor the MSFS ATC service and want to use the simplified flight planning of the MSFS World Map. Please do expect some issues, especially for procedures (SID, STAR, APPR).

If you want to use the MSFS World Map Flight Planner to build and load a flight plan, you need to set the `Sync MSFS Flight Plan` option in the `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` to `Load Only`.

This ensures the MSFS flight plan is loaded into the aircraft's flight plan when starting the flight.

Any changes made to the flight plan in the MCDU will **not** be saved back to the MSFS flight plan. This means the MSFS ATC and VFR Map will **not** be aware of these changes.

### Using the MSFS World Map Flight Planner and MSFS ATC

!!! note ""
    This is the ideal setup for users who want to use the simplified flight planning of the MSFS World Map and the MSFS ATC service (despite the known issues with MSFS ATC).
    Please do expect issues, especially for procedures (SID, STAR, APPR) and MSFS ATC instructions.

If you are using the MSFS Flight Planner to build and load a flight plan, and you also want to use the MSFS ATC even after making changes to the aircraft's flight plan, you need to set the `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` option to `Save`.

With this setting, the aircraft will attempt to save any changes to the flight plan made in the MCDU back to the simulator's flight plan. This will **not** always work as expected and may result in issues with the MSFS ATC. See the warning below for more information.

!!! warning "Synchronization Issues Expected"
    The aircraft's custom Flight Management System provides better accuracy and features over the default flight plan manager in Microsoft Flight Simulator which results in issues syncing the flight plan from the MCDU back into the simulator. Do not expect it to work properly in all cases.

### Importing a SimBrief Flight Plan and Using MSFS ATC

!!! note ""
    This is the ideal setup for users who want to use the advanced flight planning of SimBrief
    but still use the MSFS ATC service (despite the known issues with MSFS ATC).
    Please do expect issues, especially for procedures (SID, STAR, APPR) and MSFS ATC instructions.

If you are using the aircraft's built-in SimBrief integration to import a flight plan, and you also want to use the MSFS ATC, you need to set the `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` option to `Save`.

When importing a flight plan from SimBrief into the MCDU, do not select a destination airport and do not build a flight plan using the MSFS World Planner.

With this setting, the aircraft attempts to save the loaded SimBrief flight plan and any subsequent changes to the flight plan made in the MCDU back to the simulator's flight plan. This will **not** always work as expected and may result in issues with the MSFS ATC. See the warning below for more information.

!!! warning "Synchronization Issues Expected"
    The aircraft's custom Flight Management System provides better accuracy and features over the default flight plan manager in Microsoft Flight Simulator, which results in issues syncing the flight plan from the MCDU back into the simulator. Do not expect it to work properly in all cases.
