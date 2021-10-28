# Versions and Features

## Version Overview

=== "Development Version (recommended)"

    Development will have the latest features that will eventually end up in the next stable release. 
    
    In general this version has the latest fixes and newest features but also a slightly higher risk of containing bugs as features had less time to be used and tested by users.

    This version updates often and sometimes several times a days. We recommend to update this version via our installer before every start of the simulator.

    Every addition to the development version is code-reviewed and tested by several people, our QA Team and also interested users. In general it tends to be very stable and robust.

    Latest additions to this version can be seen either in the official [CHANGELOG](https://github.com/flybywiresim/a32nx/blob/master/.github/CHANGELOG.md) or the commits to the master branch of the project: [Github Commits to Master](https://github.com/flybywiresim/a32nx/commits/master){target=new}

=== "Stable Version"

    !!! info ""
        **Current Stable Version -** <img src="https://img.shields.io/github/v/release/flybywiresim/a32nx.svg?color=2F4E5B&style=flat" />

    Stable is our version which has features that are the most mature and most tested. This should be a reliable version for those users preferring stability over newest features.

    This version will not always be up to date but we work hard at ensuring its compatibility with the current version from Microsoft Flight Simulator.

=== "Experimental Version"

    This version is similar to the development version, but contains custom systems in earlier development phases. 
    
    Currently the new FlyByWire Custom Flight Management System (cFMS) is available in the Experimental version.
    
    The experimental version will be updated with the latest changes to the cFMS regularly and also with the latest changes to the Development version. Expect updates about once a week (not guaranteed).     
    
    !!! warning 
    
    The Experimental version has a less strict QA process and is used for actual QA testing. Bugs and Issues are to be expected. Please read [Experimental Version Support Page](support/exp.md) before using this version.

    !!! danger "No Support for Experimental - use at own risk"
        Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues. You can report issues in the Discord channel "#ata-22-fms" in the thread "[CFMS LNAV ONLY Bugs + Issues](https://discord.com/channels/738864299392630914/876140343735771147/882442909918584862){ target=new }".

## Version Comparison

See [Release Notes for Stable 0.7.1](../release-notes/v071.md)

### New Features in the Development Version since Release of Stable 0.7.1

This is a curated list with the most important features for users and
will be updated at least once a month.

For all changes refer to the official [CHANGELOG](https://github.com/flybywiresim/a32nx/blob/master/.github/CHANGELOG.md){target=new} or commits on the [:fontawesome-brands-github:{: .github } - **GitHub A32NX Repository Master Branch**](https://github.com/flybywiresim/a32nx/commits/master){target=new}.

*Last Update: 20. Oct 2021*

- EFB: Physical power button ( [#5697](https://github.com/flybywiresim/a32nx/pull/5697) )
- MCDU Keyboard settings moved to EFB ( [#5754](https://github.com/flybywiresim/a32nx/pull/5754) )
- PTU sounds, engine sound enhancements, and some fixes ( [#5796](https://github.com/flybywiresim/a32nx/pull/5796) )
- EFB: In-flight refueling capabilitie ( [#5775](https://github.com/flybywiresim/a32nx/pull/5775) )
- Move simBrief username input out of MCDU ( [#5813](https://github.com/flybywiresim/a32nx/pull/5813) )
- Model: Independent landing light animation ( [#5913](https://github.com/flybywiresim/a32nx/pull/5913) )
- HYD: Rigid body simulation for cargo door ( [#5341](https://github.com/flybywiresim/a32nx/pull/5341) )
- EFB/MCDU: Move telex prompt out of MCDU (MSFS now provides a warning) ( [#5902](https://github.com/flybywiresim/a32nx/pull/5902) )
- Lights: Sync Strobe/Beacon + EXT LT adjustments + LDG LT behavior ( [#5928](https://github.com/flybywiresim/a32nx/pull/5928) )
- AP: Fixed roll law instability and improved behavior when using high sim rate and low performance ( [#5935](https://github.com/flybywiresim/a32nx/pull/5935) )
- Lights: TAXI/TO logic, ambience for TAXI/TO/RW/LDG LT + min. fixes to STROBE/BEACON/NAV ( [#5973](https://github.com/flybywiresim/a32nx/pull/5973) )
- Engines: feat: correctly adapt fuel burn with sim rate ( [#5983](https://github.com/flybywiresim/a32nx/pull/5983) )
- EFB: Support all ofp formats ( [#5897](https://github.com/flybywiresim/a32nx/pull/5897) )
- ISIS: Add in.Hg and metric altitude pin programs ( [#5998](https://github.com/flybywiresim/a32nx/pull/5998) )
- PFD: Added beta target indication ( [#6019](https://github.com/flybywiresim/a32nx/pull/6019) )
- Lights: Add INTEG LT ambience, fix C&D, MAIN PNL flood and PED ambience ( [#6030](https://github.com/flybywiresim/a32nx/pull/6030) )
- MCDU: Annunciator Lights ( [#6008](https://github.com/flybywiresim/a32nx/pull/6008) )
- RMP: 25 khz vhf spacing option ( [#6037](https://github.com/flybywiresim/a32nx/pull/6037) )
- ECAM: Revised ECAM SD fuel page to match NEO ( [#5989](https://github.com/flybywiresim/a32nx/pull/5989) )
- EIS: New EIS2 font ( [#6009](https://github.com/flybywiresim/a32nx/pull/6009) )
