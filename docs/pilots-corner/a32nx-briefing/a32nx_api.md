---
hide:
    - navigation
---

# Flight Deck A32NX API

[A320neo Pilot Briefing](index.md){ .md-button }
[Clickable Flight Deck](flight-deck/index.md){ .md-button }

!!! note ""
    The below table might lag behind the current developments of the A32NX. It is based on the A32NX Development version and we try to keep it updated as best as possible.

    If you find any errors please report them on our [:fontawesome-brands-discord:{: .discord } - **Discord**](https://discord.gg/flybywire){target=new} in the **#support** channel.

## ELEC Panel

Flight Deck:  [ELEC Panel](flight-deck/ovhd/elec.md)

| Function    | API Usage                                 | Values | Read/Write | Type             | Remark                                     |
|:------------|:------------------------------------------|:-------|:-----------|:-----------------|:-------------------------------------------|
| BAT 1       | A32NX_OVHD_ELEC_BAT_1_PB_IS_AUTO          | 0 \| 1 | R/W        | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_BAT_1_PB_IS_FAULT         | 0 \| 1 | R/W        | Custom LVAR      |                                            |
| BAT 2       | A32NX_OVHD_ELEC_BAT_2_PB_IS_AUTO          | 0 \| 1 | R/W        | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_BAT_2_PB_IS_FAULT         | 0 \| 1 | R/W        | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| EXT PWR     | TOGGLE_EXTERNAL_POWER                     | -      | -          | MSFS EVENT       |                                            |
|             | EXTERNAL POWER AVAILABLE                  | 0 \| 1 | R          | MSFS VAR         |                                            |
|             | EXTERNAL POWER ON                         | 0 \| 1 | R          | MSFS VAR         |                                            |
|             | A32NX_OVHD_ELEC_EXT_PWR_PB_IS_AVAILABLE   | 0 \| 1 | R          | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_EXT_PWR_PB_IS_ON          | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| GEN 1       | TOGGLE_ALTERNATOR:1                       | -      | -          | SIMCONNECT EVENT |                                            |
|             | GENERAL ENG MASTER ALTERNATOR:1           | 0 \| 1 | R/W        | SIMCONNECT VAR   | Alternative                                |
|             | A32NX_OVHD_ELEC_ENG_GEN_1_PB_IS_ON        | 0 \| 1 | R          | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_ENG_GEN_1_PB_HAS_FAULT    | 0 \| 1 | R          | Custom LVAR      |                                            |
| GEN 2       | TOGGLE_ALTERNATOR:2                       | -      | -          | SIMCONNECT EVENT |                                            |
|             | GENERAL ENG MASTER ALTERNATOR:2           | 0 \| 1 | R/W        | SIMCONNECT VAR   | Alternative                                |
|             | A32NX_OVHD_ELEC_ENG_GEN_2_PB_IS_ON        | 0 \| 1 | R          | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_ENG_GEN_2_PB_HAS_FAULT    | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| APU GEN     | APU_GENERATOR_SWITCH_TOGGLE               | -      | -          | SIMCONNECT EVENT |                                            |
|             | APU_GENERATOR_SWITCH_SET                  | 0 \| 1 | -          | SIMCONNECT EVENT | Alternative                                |
|             | APU GENERATOR SWITCH                      | 0 \| 1 | R/W        | SIMCONNECT LVAR  | Alternative                                |
|             | A32NX_OVHD_ELEC_APU_GEN_1_PB_IS_ON        | 0 \| 1 | R          | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_APU_GEN_1_PB_HAS_FAULT    | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| BUS TIE     | A32NX_OVHD_ELEC_BUS_TIE_PB_IS_AUTO        | 0 \| 1 | R/W        | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_BUS_TIE_PB_HAS_FAULT      | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| AC ESS FEED | A32NX_OVHD_ELEC_AC_ESS_FEED_PB_IS_NORMAL  | 0 \| 1 | R/W        | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_AC_ESS_FEED_PB_HAS_FAULT  | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| IDG 1       | A32NX_OVHD_ELEC_IDG_1_PB_IS_RELEASED      | 0 -> 1 | R/W        | Custom LVAR      | Cannot be undone - flight restart required |
| IDG 1       | A32NX_OVHD_ELEC_IDG_1_PB_HAS_FAULT        | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| IDG 2       | A32NX_OVHD_ELEC_IDG_2_PB_IS_RELEASED      | 0 -> 1 | R/W        | Custom LVAR      | Cannot be undone - flight restart required |
| IDG 2       | A32NX_OVHD_ELEC_IDG_2_PB_HAS_FAULT        | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| GALY & CAB  | A32NX_OVHD_ELEC_GALY_AND_CAB_PB_IS_AUTO   | 0 \| 1 | R/W        | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_GALY_AND_CAB_PB_HAS_FAULT | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| COMMERCIAL  | A32NX_OVHD_ELEC_COMMERCIAL_PB_IS_AUTO     | 0 \| 1 | R/W        | Custom LVAR      |                                            |
|             | A32NX_OVHD_ELEC_COMMERCIAL_PB_HAS_FAULT   | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |

## External Lights Panel

Flight Deck:  [EXT LT Panel](flight-deck/ovhd/ext-lt.md)

| Function     | API Usage             | Values | Read/Write | Type             | Remark                              |
|:-------------|:----------------------|:-------|:-----------|:-----------------|:------------------------------------|
| STROBE       | STROBES_SET           | 0 \| 1 | -          | SIMCONNECT EVENT | OFF and ON (no AUTO)                |
|              | STROBES_TOGGLE        | -      | -          | SIMCONNECT EVENT | OFF and ON (no AUTO)                |
|              | STROBES_ON            | -      | -          | SIMCONNECT EVENT | OFF and ON (no AUTO)                |
|              | STROBES_OFF           | -      | -          | SIMCONNECT EVENT | OFF and ON (no AUTO)                |
|              | LIGHT STROBE          | 0 \| 1 | R/W        | SIMCONNECT VAR   | OFF and ON (no AUTO)                |
|              | STROBE_0_AUTO         | 0 \| 1 | R/W        | Custom LVAR      | AUTO only when STROBES are ON       |
|              | LIGHTING_STROBE_0     | 0 \| 1 | R          |                  | 2=OFF, 1=AUTO, 0=ON                 |
|              |                       |        |            |                  |                                     |
| BEACON       | BEACON_SET            | 0 \| 1 | -          | SIMCONNECT EVENT |                                     |
|              | BEACON_TOGGLE         | -      | -          | SIMCONNECT EVENT |                                     |
|              | BEACON_ON             | -      | -          | SIMCONNECT EVENT |                                     |
|              | BEACON_OFF            | -      | -          | SIMCONNECT EVENT |                                     |
|              | LIGHT BEACON          | 0 \| 1 | R/W        | SIMCONNECT VAR   |                                     |
|              |                       |        |            |                  |                                     |
| WING         | WING_SET              | 0 \| 1 | -          | SIMCONNECT EVENT |                                     |
|              | BEACON_TOGGLE         | -      | -          | SIMCONNECT EVENT |                                     |
|              | BEACON_ON             | -      | -          | SIMCONNECT EVENT |                                     |
|              | BEACON_OFF            | -      | -          | SIMCONNECT EVENT |                                     |
|              | LIGHT BEACON          | 0 \| 1 | R/W        | SIMCONNECT VAR   |                                     |
|              |                       |        |            |                  |                                     |
| NAV & LOGO   | NAV_LIGHTS_SET        | 0 \| 1 | -          | SIMCONNECT EVENT | LOGO needs to be set separately     |
|              | LIGHT NAV             | 0 \| 1 | R/W        | SIMCONNECT VAR   | LOGO needs to be set separately     |
|              | LOGO_LIGHTS_SET       | 0 \| 1 | -          | SIMCONNECT EVENT | LOGO does not move switch           |
|              | LIGHT LOGO            | 0 \| 1 | R/W        | SIMCONNECT VAR   | LOGO does not move switch           |
|              |                       |        |            |                  |                                     |
| RWY TURN OFF | CIRCUIT SWITCH ON:21  | 0 \| 1 | R/W        | SIMCONNECT VAR   | Left Rwy Turn Off Light + Switch    |
|              | CIRCUIT SWITCH ON:22  | 0 \| 1 | R/W        | SIMCONNECT VAR   | Left Rwy Turn Off Light             |
|              | LIGHTING_TAXI_2       | 0 \| 1 | R          | Custom LVAR      |                                     |
|              |                       |        |            |                  |                                     |
| LAND L + R   | LANDING_LIGHTS_ON     | 0..3   | -          | SIMCONNECT EVENT | 0=all, 1=NOSE, 2=L, 3=R             |
|              | LANDING_LIGHTS_OFF    | 0..3   | -          | SIMCONNECT EVENT | 0=all, 1=NOSE, 2=L, 3=R             |
|              | LANDING_LIGHTS_TOGGLE | 0..3   | -          | SIMCONNECT EVENT | 0=all, 1=NOSE, 2=L, 3=R             |
|              |                       |        |            |                  |                                     |
| NOSE         | TOGGLE_TAXI_LIGHTS    | -      | -          | SIMCONNECT EVENT | Also toggles RWY TURN OFF LIGHT     |
|              | LIGHT TAXI            | 0 \| 1 | R/W        | SIMCONNECT VAR   | Only switches TAXI light            |
|              | LANDING_LIGHTS_TOGGLE | 1      | -          | SIMCONNECT EVENT | Toggles switch between T.O. and OFF |

## Interior Lights Panel

Flight Deck: [INT LT Panel](flight-deck/ovhd/int-lt.md)

| Function               | API Usage              | Values | Read/Write | Type             | Remark               |
|:-----------------------|:-----------------------|:-------|:-----------|:-----------------|:---------------------|
| OVHD INTEG Lt          | LIGHT POTENTIOMETER:86 | 0..100 | R/W        | MSFS VAR         |                      |
|                        |                        |        |            |                  |                      |
| ICE IND & STBY COMPASS | N/A                    |        |            |                  |                      |
|                        |                        |        |            |                  |                      |
| DOME                   | TOGGLE_CABIN_LIGHTS    | -      | -          | SIMCONNECT EVENT | Toggle OFF-DIM-BRT   |
|                        | LIGHT POTENTIOMETER:7  | 0..100 | R/W        | MSFS VAR         |                      |
|                        |                        |        |            |                  |                      |
| ANN LT                 | A32NX_OVHD_INTLT_ANN   | 0..2   | R/W        | Custom LVAR      | 2=DIM, 1=BRT, 0=TEST |

## Signs Panel

Flight Deck: [Signs Panel](flight-deck/ovhd/signs.md)

| Function     | API Usage                                    | Values | Read/Write | Type             | Remark              |
|:-------------|:---------------------------------------------|:-------|:-----------|:-----------------|:--------------------|
| SEAT BELTS   | CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE          | -      | -          | SIMCONNECT EVENT |                     |
|              | CABIN SEATBELTS ALERT SWITCH                 | 0 \| 1 | R          | SIMCONNECT VAR   |                     |
|              |                                              |        |            |                  |                     |
| NO SMOKING   | XMLVAR_SWITCH_OVHD_INTLT_NONSMOKING_POSITION | 0..2   | R/W        | Custom LVAR      | 0=ON, 1=AUTO, 2=OFF |
|              |                                              |        |            |                  |                     |
| EMER EXIT LT | XMLVAR_SWITCH_OVHD_INTLT_EMEREXIT_POSITION   | 0..2   | R/W        | Custom LVAR      | 0=ON, 1=AUTO, 2=OFF |

