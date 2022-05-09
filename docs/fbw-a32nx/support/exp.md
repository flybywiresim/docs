# Experimental Version

The Experimental version is a test version to find problems, issues and to improve functionality based on your feedback. It is <span style=color:red>**not**</span> meant to be used for **daily use or serious flights with** an Online ATC service.

{--

Currently experimental is geared toward testing the initial version of VNAV. Please use the appropriate discord 
thread to report any issues - [How to Report Issues](#how-to-report-issues).

--}

!!! danger "Do not expect support for the experimental version - use at own risk!"
    Please ensure that you have at least read this page and the known issues before reporting issues in the appropriate threads on our Discord server.

    We ask that you understand that we may not offer support for any experimental issues due to the nature of this version. We will happily answer questions time permitting.

## Implemented Features for Testing

### Hydraulic Gear System

- Rigid body physics of doors and gears
- Dual LGCIU computers implementation with possible failures
    - Cycling gear handle will switch over to the other LGCIU if available
- Landing gear lever baulk lock mechanism (both unpowered LGCIUs will lock lever down)
- Unpowered LGCIU 1 will cause gear light indicator to fail
- All proximity sensors simulated and some (for now) can be failed
- Hydraulic system simulated
    - Security valve closed above 260kts
    - All doors / gears / uplock / downlock actuators
    - Mechanical system of gravity extension can control shut-off / vent valve and uplocks
- Gravity extension by keeping pressed in-game binding "GEAR EMERGENCY HANDLE TOGGLE" until all gears unlocked

### Vertical Guidance

- Speed and altitude predictions in the flight plan page, including magenta or amber asterisks.
- Reworked fuel burn and time predictions in the flight plan page (no flight plan B page).
- Pseudowaypoints in the flight plan (SPD/LIM, T/C, T/D, S/C, S/D, DECEL).
- Display of pseudowaypoints on the ND (T/C, T/D, predicted speed changes, etc.)
- Partial implementation of step climbs/descent.
- Linear deviation indication during the descent.
- Following of speed and altitude constraints in the climb phase (credits to tracernz).
- Partial implementation of descent guidance.
- Ability to enter winds for climb, cruise, and descent.

#### Vertical Guidance Planned Implementations

These features are not yet available but will be implemented at a later time.

- Time constraints, RTA
- Flight plan B
- Constant Mach segments
- Vertical guidance for RNAV approaches

### flyPadOS Version 3 (EFB)

- Completely new design
- Improved Dashboard
    - Flight info
    - Customizable info section for:
        - Weather
        - Pinned charts
        - Pinned checklists 
        - Maintenance 
- Stateful (remembers tabs and content of pages)
- Improved ground service pages
- Improved pushback tool
- Improved performance calculators
- Improved navigation charts page
    - Improved Navigraph chart support 
        - Current position on chart
        - Fullscreen mode
        - Easier search and selection
    - Support for pinning of charts
- Improved online ATC page
- Improved failure support incl. categories and search
- Interactive checklists incl. autofill and option to pin to dashboard
- Presets for customizable lighting settings and predefined aircraft states
- Improved settings (better structure and more configuration options)
- Onscreen keyboard
- Tooltips
- Themes
    - Blue
    - Dark
    - Light
- Multilingual - English, French, Spanish, German, Russian - more to come....

#### EFB Planned Implementations

These features are not yet available but are generally planned and might be implemented at a later time.

- Support for local files (PFD, images) - requires local-api server (not yet merged)
- Improvements to pushback page

## Known Issues

### Hydraulic Gear System Issues

- Doors animations are wrong due to default 3D model issues. Door positions are internally simulated correctly
    - Doors will appear closed after gravity extension visually, but they stay opened internally
- Gravity extension can't be reverted. It's possible internally but feature is turned off until handle animation works
- Wheels page not updated yet
- Sounds might have some issues, update is coming soon (and it's amazing)

### Vertical Guidance Issues

- There has been a large number of reports indicating that the T/D was placed too late. This will be investigated this further, but we ask you to please check your arrival routing for any odd path drawings. These are not unusual for the speed predictions of VNAV do not affect the LNAV path computations yet, which causes certain turns to be drawn at a larger radius than what will actually be flown. Consequently, VNAV will calculate a profile with more track mileage than what is realistically available and place the T/D too late.
- There is a problem with manually inserted constraints right now, where they are ignored or treated wrongly. Be aware of this and, if possible, advise if you have added any constraints manually when reporting an issue with the profile calculation. This is crucial in helping us identify and reproduce your issue.
- LNAV does not use VNAV speed predictions yet. This means that an approach path will not be forecasted properly. Furthermore, the T/D (Top of Descent) could be misplaced, since the system expects more track miles.
- The descent guidance does not use the speed margins properly yet. The aircraft does not speed up to catch a profile below it.
- The linear deviation indication (green "yoyo") on the PFD might jump around during the descent. This effect is particularly noticeable when new waypoints are sequenced.
- Layout inaccuracies in the MCDU, mostly on the PERF page.
- Predicted speed changes in the descent might seem to show up erratically. The same for the level off arrow while in descent mode.
- Fuel predictions in the MCDU are not very accurate.
- Descent guidance is sensitive to QNH changes. This is partially due to an inaccuracy in MSFS' atmospheric model.
- Winds are not yet taken into account for all phases of flight.

### flyPadOSv3 Issues

- Local files does not work yet. Needs additional feature PR ([local-api](https://github.com/flybywiresim/a32nx/pull/6411/){target=new})
- Pushback page: not yet fully functional or complete - changes to be expected
- Stuck notifications are caused by CSS animations being disabled.
    - Fix: `General Options` -> `Accessibility` -> Turn On `Menu Animations` under `User Interface` 
- Translations not yet complete / Missing translations and layout issues to be expected
- Tooltips not yet complete

## How to Report Issues

<!--
!!! warning
    We are not taking issue reports at this time.
-->

!!! warning
    Please read the above Known Issues list and also use the search of Discord to see if your issue has already been reported.

    At this time please only report issues via our Discord channel threads:

    [cFMS LNAV+VNAV Issue Reports [NO SUPPORT]](https://discord.com/channels/738864299392630914/926586416820011098){target=new .md-button}

    [flyPadOS3 Experimental - Issue Reports [NO SUPPORT]](https://discord.com/channels/738864299392630914/926586416820011098){target=new .md-button}

    [General Experimental Issue Reports [NO SUPPORT]](https://discord.
    com/channels/738864299392630914/965072479796215888){target=new .md-button}

    {--

    Support or immediate solutions for your issues is **not guranteed**. We will collect all issues to fix and improve features in testing continuously.

    --}

**Do not open any issues on GitHub for the Experimental Version!**

### Download and Install

See [Installation Guide](../installation.md#downloads).