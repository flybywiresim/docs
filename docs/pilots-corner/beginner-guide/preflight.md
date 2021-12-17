# Preflight

Before you start your flight in earnest, we have included various features in the A32NX that assist in configuring the aircraft and in-flight support. Some of these feature require the aircraft to be powered on and will be noted below. Additionally, these guides will be linked in the appropriate locations throughout the beginner guide. 

---

## Nav Data

MSFS Nav Data is updated during their patching process. It's important to take stock of what nav data you are currently using and if it matches the current AIRAC cycle. When using simBrief without a Navigraph subscription you may encounter `AWY/WPT Mismatch` OR the [flight plan import](#flight-plan-import) may fail due to outdated/incorrect AIRAC cycle. 

Owning a Navigraph subscription gives you access to their standalone nav data addon for MSFS that pairs with their simBrief flight planning. Not only does it provide you with an up-to-date AIRAC alongside any revisions, it will ensure compatibility when importing from simBrief or planning your flight manually.

## Flight Planning

We highly recommend **not** using the built-in MSFS flight planner. SimBrief is a great resources that provides routing and other information to successfully plan your flight. You can choose to use other software/websites to plan your route but when using simBrief we have a handy import feature as seen in the next section.

!!! tip "Important Links for Flight Planning"
    - [SimBrief Website](https://www.simbrief.com/) (Flight Planning) 
    - [Little Nav Map](https://albar965.github.io/littlenavmap.html) (Flight Planning and Charts)
    - [ChartFox](https://chartfox.org/) (Charts)
    - [Navigraph](https://navigraph.com/) (Flight Planning and Charts) *Requires Subscription*
    - See our [Custom Flight Management System](../../fbw-a32nx/feature-guides/cFMS.md) page and the [special notes section](../../fbw-a32nx/feature-guides/cFMS.md#special-notes) when using our development version of the aircraft.

## Flight Plan Import

If you wish to expedite the process of inputting your flight plan on the MCDU we have incorporated a simBrief import function on the MCDU. Our EFB can also display your generated OFP within MSFS.

!!! info "SimBrief Import Requires the Aircraft to be Powered"

[SimBrief A32NX Features](../../fbw-a32nx/feature-guides/simbrief.md){.md-button}

### Manual Flight Planning

!!! info "MCDU Interaction Requires Aircraft to be Powered"

The [Flight Plan Section](preparing-mcdu.md#flight-plan) in the "Preparing the MCDU" guide contains a sample routing to showcase how to input your waypoints, departure SID, and arrival STAR / procedure.

## Flight Plan Discontinuities

When inputting your flight plan into the MCDU, discontinuities appearing is an intended feature. The page below describes how to handle these when encountered during your preflight preparations.

!!! info "MCDU Interaction Requires Aircraft to be Powered"

[Flight Plan Discontinuities](preparing-mcdu.md#discontinuity){.md-button}

## Payload Management

In order to configure your aircraft we have provided options onboard the aircraft to load fuel (via the EFB) and passengers / baggage (via the MCDU). Please see the following page and note any advisories.

!!! info "Passengers and Baggage Require the Aircraft to be Powered"

[Fuel and Weights](../../fbw-a32nx/feature-guides/loading-fuel-weight.md){.md-button}

## EFB Navigraph Charts

To help with navigation during your flight our flyPad EFB can connect to your Navigraph account to provide access to all of your enroute charts!

[EFB Navgraph](../../fbw-a32nx/feature-guides/flyPad/charts.md){.md-button}