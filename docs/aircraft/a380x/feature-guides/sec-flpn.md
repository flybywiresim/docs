---
title: Secondary Flight Plan
description: Overview and usage of the A380X secondary flight plan feature.
---
# Secondary Flight Plan

The A380X now supports creating up to three secondary flight plans. This is a flight plan that exists in parallel with the primary flight plan.
On the A380, Secondary flight plans are primarily used to plan returns to the departure airfield, runway changes, or emergency scenarios in advance and can be activated when needed. In this section of the guide, we will go over example use cases for this feature.

??? info "Recommendations"

    It is recommended to use SEC 1 for an immediate return to the departure airfield and SEC 2 for alternate runway or procedure planning. SEC 3 should be left empty and dedicated to any route uplinks.

## Engine-out Departure Procedure
### Preparation

In real life, one of the most common use cases for the secondary flight plan is programming an alternative departure procedure in case of an engine failure at takeoff. For this guide, we assume that the FMS has been set up for a flight from Istanbul Airport (LTFM) to Vienna Airport (LOWW). In the primary flight plan, we have planned a departure from runway 35R following the TUBD4D SID.

(image of flight plan)

Due to the steep initial climb gradient requirements and airspace constraints in the vicinity of the airport, we cannot follow our planned SID out of Runway 35R in the event of an engine failure. Instead, we follow an alternative Engine-Out SID (EOSID) procedure. We will climb on runway track 354° to our engine-out acceleration altitude of 1,900 ft, continue straight ahead out over the Black Sea tracking 354° to 25 NM, and enter a holding pattern.

To program this in the secondary flight plan, we start by creating a copy of the active flight plan. We start on the SEC INDEX page, and then import our primary flight plan using the IMPORT button. This is one way of This is one way to create a secondary flight plan. Another option is to create one from scratch using the INIT button, or perform a CPNY F-PLN request.

(image of import flight plan)

First, we remove the SID and import our Engine Out waypoint. We do this by clicking the F-PLN button, and then clicking on our departure runway. We can then select insert next waypoint.