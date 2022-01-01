# Experimental Version

The Experimental version is a test version to find problems and issues and to improve functionality based on your feedback. It is not meant to be used for daily use or when you try to do a serious flight on an Online ATC service.

We are currently testing updates to our custom FMS LNAV, and other additional improvements -- see below for a full list.

!!! danger "No Support for Experimental - use at own risk"
    Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues.

## New Features to be Tested

- Support for more legs types: CA (partially), CF, CR, DF, HX (partially), IF
- Better turn prediction algorithm with support for overfly, course capture, path capture, direct turn, reverse turn, reversions and more
- Support for marking waypoints as overfly in the F-PLN page
- Realistic ND rendering based on IRL hardware and software architecture
- Fixes for performance issues over long flights

## Known Issues

- Stringing issues from the flight plan manager might still occur - will be fixed by the upcoming flight plan manager rewrite
- Some path captures (sharp angle turn into a leg) might be off / intercept at the wrong position - will **not** affect guidance
- Course capture turns (course to altitude, INTCPT) and CX legs do not adapt to achieved turn radius
- Some turns might revert / de-revert right before they become active in case of speed changes
- Turn reversion heuristics are not tuned perfectly yet
- VM legs sometimes have the wrong course
- Holding patterns embedded in some procedures might not have perfect entries or turn radius
- AF, CD, VI, VR, FA, FM, FC, FD, PI legs are not supported

## How to Report Issues

!!! warning
    Please read the above Known Issues list and also use the search of  Discord to see if your issue has already been reported.

At this time please only report issues via our Discord channel thread:

 [Experimental - Issue Reports [NO SUPPORT]](https://discord.com/channels/738864299392630914/926586416820011098/926592547059531866){target=new .md-button}

Do not expect support or immediate solutions for your issues. We will collect all issues and fix and improve continuously.

**Do not open any issues on Github for the Experimental Version!**

### Download and Install

See [Installation Guide](../installation.md#downloads).

## Leg Types

| Type       | Supported            | Description                                                                                                                                                                                                                            |
|:-----------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TF         | CFMS 1.0             | Track to a fix defines a great circle track over ground between two known databases fixes.                                                                                                                                             |
| RF         | CFMS 1.0             | Constant Radius Arc defines a constant radius turn between two database fixes, lines tangent to the arc and a center fix.                                                                                                              |
| VM         | CFMS 1.0             | Heading to a manual termination defines a specified heading until a Manual termination.                                                                                                                                                |
|            |                      |                                                                                                                                                                                                                                        |
| CA         | CFMS 1.5 (partially) | Course to an altitude defines a specified course to a specific altitude at an unspecified position.                                                                                                                                    |
| CF         | CFMS 1.5             | Course To fix defines a specified course to a specific database fix.                                                                                                                                                                   |
| CR         | CFMS 1.5             | Course to a radial termination defines a course to a specified radial from a specific database VOR NAVAID.                                                                                                                             |
| DF         | CFMS 1.5             | Direct To fix defines an unspecified track starting from an undefined position to a specified fix.                                                                                                                                     |
| HA, HF, HM | CFMS 1.5 (partially) | Racetrack course reversal (Holds) or altitude termination (HA), single circuit terminating at the fix (base turn) (HF), or manual termination (HM) leg types define racetrack pattern or course reversals at a specified database fix. |
| IF         | CFMS 1.5             | Initial fix defines a database fix as a point in space and is only required to define the beginning of a route or procedure.                                                                                                           |
|            |                      |                                                                                                                                                                                                                                        |
| AF         | Planned              | Arc to a fix defines a track over the ground at a specified constant distance from a database DME NAVAID.                                                                                                                              |
| CD         | Planned              | Course to a DME distance defines a specified course to a specific DME distance that is from a specific database DME NAVAID.                                                                                                            |
| CI         | Planned              | Course to an intercept defines a specified course to intercept a subsequent leg.                                                                                                                                                       |
| FA         | Planned              | Fix to an Altitude defines a specified track over the ground from a database fix to a specified altitude at an unspecified position.                                                                                                   |
| FC         | Planned              | Track from a fix from a distance or FC leg—defines a specified track over the ground from a database fix for a specific distance.                                                                                                      |
| FD         | Planned              | Track from a fix to a distance measuring equipment (DME) distance defines a specified track over the ground from a database fix to a specific DME distance that is from a specific database DME NAVAID.                                |
| FM         | Planned              | Fix to a manual termination or FM leg— defines a specified track over the ground from a database fix until manual termination of the leg.                                                                                              |
| PI         | Planned              | Procedure turn or PI leg—defines a course reversal starting at a specific database fix and includes outbound leg followed by a left or right turn and 180° course reversal to intercept the next leg.                                  |
| VA         | Planned              | Heading to Altitude termination defines a specified heading to a specific altitude termination at an unspecified position.                                                                                                             |
| VD         | Planned              | Heading to a DME distance termination defines a specified heading terminating at a specified DME distance from a specific database DME NAVAID.                                                                                         |
| VI         | Planned              | Heading to a Next Leg Intercept defines a specified heading to intercept the subsequent leg at an unspecified position.                                                                                                                |
| VR         | Planned              | Heading to a radial termination defines a specified heading to a specified radial from a specific database VOR NAVAID.                                                                                                                 |

