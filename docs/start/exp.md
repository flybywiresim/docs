# Experimental Version

!!! danger "No Support for Experimental - use at own risk"
    Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues. You can report issues in the Discord channel "#ata-22-fms" in the thread "Bugs and Issues".

---

## FlyByWire Custom Flight Management System (cFMS)

### Features

- Replaces the default Asobo Flight Plan Manager
- Editing of waypoints within SID/STAR/APPR
- Off-track indicator
- No more USR waypoints

### Known Issues

*Last Update: {{git_revision_date_localized}}*

- Approach Phase must be manually activated (MCDU PERF)
- Only 3 leg types (TF, RF and VM) and 1 transition type (type 1) supported at this time
- WX and TERR on ND INOP
- ARPT, VOR, NDB, WPTs filters INOP on ND
- Runaway sequencing issues involving type 1 transitions
- Sequencing also may not be aggressive enough at times
- Rendering of terminal procedure legs may be incorrect during flight
- No traffic shown, TCAS is INOP, elements are cosmetic only
- EFB Rate of descent now no longer syncs with ND
- MCDU flight plan INIT DEPARTURE/ARRIVAL page is sometimes cleared when DIRECT-TO is used
- Defining both from/to in MSFS Flight Planner (World Map) do show in the from/to init page but do not populate the airport list in METAR
- Flight plans defined in the MSFS Flight Planner (World Map) are loaded to the cFMS once but might contain issues.
- Any changes to the cFMS flight plan will not be synced back to the MSFS flight plan manager for now.
- Build-in ATC will not be supported with the cFMS for now.

### How to report issues

At this time please only report issues via our Discord channel "#ata-22-fms" in the thread "Bugs and Issues".

!!! warning
    Please read the above Known Issues list and also use the search of  Discord to see if you issue has already been reported.

**Do not open any issues on Github for the Experimental Version!**

<!--### Download and Install-->

<!--See [Installation Guide](../installation.md#downloads).-->

---

!!! danger "No Support for Experimental - use at own risk"
    Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues. You can report issues in the Discord channel "#ata-22-fms" in the thread "Bugs and Issues".
