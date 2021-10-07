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
        **Current Stable Version - v0.7.0**

    Stable is our version which has features that are the most mature and most tested. This should be a reliable version for those users preferring stability over newest features.

    This version will not always be up to date but we work hard at ensuring its compatibility with the current version from Microsoft Flight Simulator.

=== "Experimental Version"

    This version is similar to the development version, but contains custom systems in earlier development phases.
    
    Currently the new FlyByWire Custom Flight Management System (cFMS) is available in the Experimental version.
    
    The experimental version will be updated with the latest changes to the cFMS regularly and also with the latest changes to the Development version. Expect updates about once a week (not guaranteed).     
    
    !!! warning 

    Please read [Experimental Version Support Page](support/exp.md) before using this version.

    !!! danger "No Support for Experimental - use at own risk"
        Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues. You can report issues in the Discord channel "#ata-22-fms" in the thread "[CFMS LNAV ONLY Bugs + Issues](https://discord.com/channels/738864299392630914/876140343735771147/882442909918584862){ target=new }".

## Version Comparison

See [Release Notes for Stable 0.7.0](../release-notes/v070.md)

### New Features in the Development Version since Release of Stable 0.7.0

This is a curated list with the most important features for users and
will be updated at least once a month.

For all changes refer to the official [CHANGELOG](https://github.com/flybywiresim/a32nx/blob/master/.github/CHANGELOG.md){target=new} or commits on the [:fontawesome-brands-github:{: .github } - **GitHub A32NX Repository Master Branch**](https://github.com/flybywiresim/a32nx/commits/master){target=new}.

*Last Update: 7. Oct 2021*

- Added language translations ( [#5599](https://github.com/flybywiresim/a32nx/pull/5599){target=new} )
- Improved pitch/C* and ALT* laws ( [#5711](https://github.com/flybywiresim/a32nx/pull/5711){target=new} )
- EFB: Physical power button ( [#5697](https://github.com/flybywiresim/a32nx/pull/5697){target=new} )
- MCDU Keyboard settings moved to EFB ( [#5754](https://github.com/flybywiresim/a32nx/pull/5754){target=new} )
- PTU sounds, engine sound enhancements, and some fixes ( [#5796](https://github.com/flybywiresim/a32nx/pull/5796) )
- PFD: Correct roll indicator triangle height ( [#5803](https://github.com/flybywiresim/a32nx/pull/5803) )
- EFB: In-flight refueling capabilitie ( [#5775](https://github.com/flybywiresim/a32nx/pull/5775) )
- ADIRS: Use heading as track at low ground speeds ( [#5804](https://github.com/flybywiresim/a32nx/pull/5804) )
- Updated flight model weights and balances ( [#5547](https://github.com/flybywiresim/a32nx/pull/5547) )
- AP and FBW improvements v2 ( [#5781](https://github.com/flybywiresim/a32nx/pull/5781) )
- Move simBrief username input out of MCDU ( [#5813](https://github.com/flybywiresim/a32nx/pull/5813) )
- Change GPS ground speed on MCDU Data GPS Monitor page from meters/second to knots ( [#5848](https://github.com/flybywiresim/a32nx/pull/5848) )
- AP: Improved LOC-CPT, LOC-ALIGN, and ROLLOUT laws ( [#5862](https://github.com/flybywiresim/a32nx/pull/5862) )
- ARINC 429 Communication ( [#5598](https://github.com/flybywiresim/a32nx/pull/5598) )
- FBW: Improved speed dependent roll law model ( [#5842](https://github.com/flybywiresim/a32nx/pull/5842) )
- Model: Independent landing light animation ( [#5913](https://github.com/flybywiresim/a32nx/pull/5913) )
- HYD: Rigid body simulation for cargo door ( [#5341](https://github.com/flybywiresim/a32nx/pull/5341) )
- EFB/MCDU: Move telex prompt out of MCDU (MSFS now provides a warning) ( [#5902](https://github.com/flybywiresim/a32nx/pull/5902) )
- Lights: Sync Strobe/Beacon + EXT LT adjustments + LDG LT behavior ( [#5928](https://github.com/flybywiresim/a32nx/pull/5928) )
- AP: Improved SPD/MACH law model ( [#5918](https://github.com/flybywiresim/a32nx/pull/5918) )
- AP: Fixed roll law instability and improved behavior when using high sim rate and low performance ( [#5935](https://github.com/flybywiresim/a32nx/pull/5935) )

