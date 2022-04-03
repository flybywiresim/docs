# Landing Calculations

This page provides additional information when utilizing the flyPadOS3 landing calculator.

## RWY Conditions

!!! danger "TODO"
    - Add matrix
    - Add additional information
    - Consider extra page

For runways that are not dry, a field condition report (or FICON) is included in the NOTAMs for that airport. See this example for a SimBrief prepared OFP for KPIT-KPHL.

!!! block ""
![Runway Condition](../../../fbw-a32nx/assets/flypados3/rwy-condition.png){align=left width=60%}

    This is a screenshot for the runways at the arrival airport. 

    It provides runway condition codes (the numbers X/X/X) for each third of the specified runway as well as a text description of the surface condition and the time of the report.

As for the condition codes, a dry runway is a 6 and would never be reported unless portions of the runway were codes less than 6. The lowest of the 3 reported codes should be used (unless you are certain that you would be not using the last third of the runway, for example).

For our landing perf calculator:

- 5 is Good
- 4 is Good-Medium
- 3 is medium
- 2 is Medium-Poor
- 1 is Poor