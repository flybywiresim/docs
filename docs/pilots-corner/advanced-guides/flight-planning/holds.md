# Holds

!!! warning "Not available in the Stable Version"

## Overview

Holding patterns , as they are officialy known, can be used as a delaying tactic for airborn aircraft. Typically holding patterns have a racetrack pattern and can easily be spotted on flight trackers. All holds are made up out of segments, the segments are shown in the figure below. 

<!--- input composition of hold as the FAA doc shows
--->

### Why hold?
Holdings are typically used to delay aircraft, or less common, to burn of fuel for landing.
A good example usecase of a hold can be seen in Innsbruck (LOWI) in the picture below.


![LOWI](/assets/advanced-guides/holds/LOWI.png)



### Preparing the hold
Aircraft can technically hold, if given permission by ATC in advance, at any waypoint. Holds that are published on aviation charts are called published holds. For the purpose of this guide we will only take a published hold into condideration. Holds can be spotted on charts in 2 ways where both options can be applied on the same chart. For example look at the chart below. 

Waypoints with published holds can be spotted by a racetrack pattern or a white H in a black box drawn in a chart. Holds displayed by the white H in the black box will always be accompanied by a visual racetrack patern in a diagram on the side of the chart. 

Now that you know where to hold, you should know how to set up the hold. To do this you will need to find information on the chart and move it into the FMS. The main information you need to have is:
1. Name of the fix/waypoint
2. Inbound course
3. Turning direction
4. Length of the legs, eather in time or distance
 
 Eather the inbound course/heading or the reciprocal of the hold is always depicted on the chart.

 Below you will find samples of diffrent holds with the information filtered out.  

!!! info "Examples of holds in charts"

    === "1"

        Lorum ipsum

        | Fix           | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | ARNUM         | 216              |Right               | STD           | STD        |FL140  | FL100         |
      

        

    === "2"

        Lorum ipsum

        | Fix           | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | SUGOL         | 110              |Right               | STD           | STD        |FL250  | FL70          |
        
    === "3"

        Lorum ipsum

        | Fix           | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | OKLAX         | 149              |Left                | STD           | 210KT      |STD    | 8000FT        |

    === "4"

        Lorum ipsum

        | Fix           | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | DVN           | 053              |Right               | ????????      | 210KT      |-      | 2900FT        |
    
    === "5"

        Lorum ipsum

        | Fix           | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | BOTON         | *049             |Right               | STD           | STD        |-      | ????          |
        | PANZE         | *049             |Left                | STD           | STD        |-      | ????          |
        | CAMRN         | 041              |Left                | STD           | 210KT      |14000FT| 6001FT        |
        
       * the inbound course can be calulated by subtracting or adding 180 to the reciprocal.

    === "6"

        Lorum ipsum

        | Fix           | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | SKENS         | 274              |Right               | 10NM          | STD        |-      |13000FT        |

    === "7"

        Lorum ipsum

        | Fix           | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | SNAAG         | 061              |Right               | 10NM          | STD        |-      |?????          |

    === "8"

        Lorum ipsum

        | Fix           | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | TIGER         | 315              |Right               | STD           | STD        |FL240  | FL150         |
        | BIG           | 302              |Right               | STD           | ?????      |FL150  | FL70          |
    
    === "9"

        Lorum ipsum

        |Fix            | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | DDM           | 059              |Left                | STD           | 230KT      |-      | 6000FT        |
        | EGN           | 108              |Left                | STD           | 230KT      |-      | 4000FT        |
        | KEA           | 335              |Right               | STD           | 230KT      |-      | 5000FT        |

    === "10"

        Lorum ipsum

        |Fix            | Inbound course   |Turning direction   |Leg distance   |Max speed   |Max alt|Min Alt (MHA)  |
        | -----------   | -----------      |-----------         |  -----------  | --------   | ---   |-----          |
        | CRS           | 001              |Left                |Until CVO VOR reads 34.0 NM|STD|-   | FL120         |
     
### Entering the hold

### Leaving the hold
