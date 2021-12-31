# Experimental Version

The Experimental version is a test version to find problems and issues and to improve functionality based on your feedback. It is not meant to be used for daily use or when you try to do a serious flight on an Online ATC service. We are currently testing updates to our cFMS LNAV, TCAS, and additional improvements -- see below for a full list.

!!! danger "No Support for Experimental - use at own risk"
    Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues.

## New Features to be Tested

!!! bug "TODO"

- Waypoint overfly support
- More procedure leg types are supported
- Path generation is more resilient
- ND data transmission is modelled after real-world EIS architecture
- Initial implementation of the Traffic Alert and Collision Avoidance System (TCAS)
- Improvements to the ATHR SPEED/MACH law

## Known Issues

!!! bug "TODO"

- Stringing issues from the flight plan manager might still occur - will be fixed by the upcoming flight plan manager rewrite
- Some path captures (sharp angle turn into a leg) might be off / intercept at the wrong position - will **not** affect guidance
- Course capture turns (course to altitude, INTCPT) and CX legs do not adapt to achieved turn radius
- Some turns might revert / de-revert right before they become active in case of speed changes
- Turn reversion heuristics are not tuned perfectly yet
- VM legs sometimes have the wrong course
- Holding patterns embedded in some procedures might not have perfect entries or turn radius
- AF, CD, VI, VR, FA, FM, FC, FD, PI legs are not supported

## How to Report Issues

!!! bug "TODO"
At this time please only report issues via our Discord channel ...

!!! warning
    Please read the above Known Issues list and also use the search of  Discord to see if your issue has already been reported.

**Do not open any issues on Github for the Experimental Version!**

### Download and Install

See [Installation Guide](../installation.md#downloads).
