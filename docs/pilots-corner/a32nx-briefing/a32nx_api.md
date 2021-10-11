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

The order of the panels below is roughly done after the standard cold & dark setup procedure.

## Overhead Forward

### ELEC Panel

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

### External Lights Panel

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

### Interior Lights Panel

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

### Signs Panel

Flight Deck: [Signs Panel](flight-deck/ovhd/signs.md)

| Function     | API Usage                                    | Values | Read/Write | Type             | Remark              |
|:-------------|:---------------------------------------------|:-------|:-----------|:-----------------|:--------------------|
| SEAT BELTS   | CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE          | -      | -          | SIMCONNECT EVENT |                     |
|              | CABIN SEATBELTS ALERT SWITCH                 | 0 \| 1 | R          | SIMCONNECT VAR   |                     |
|              |                                              |        |            |                  |                     |
| NO SMOKING   | XMLVAR_SWITCH_OVHD_INTLT_NONSMOKING_POSITION | 0..2   | R/W        | Custom LVAR      | 0=ON, 1=AUTO, 2=OFF |
|              |                                              |        |            |                  |                     |
| EMER EXIT LT | XMLVAR_SWITCH_OVHD_INTLT_EMEREXIT_POSITION   | 0..2   | R/W        | Custom LVAR      | 0=ON, 1=AUTO, 2=OFF |

### ADIRS Panel

Flight Deck: [ADIRS Panel](flight-deck/ovhd/adirs.md)

!!! note "The below table shows the API for ADIR 1. Replace `1` with `2` or `3` for the other ADIRS."

| Function                 | API Usage                                | Values  | Read/Write | Type        | Remark               |
|:-------------------------|:-----------------------------------------|:--------|:-----------|:------------|:---------------------|
| ADIR 1 knob              | A32NX_OVHD_ADIRS_IR_1_MODE_SELECTOR_KNOB | 0..2    | R/W        | Custom LVAR | 0=OFF, 1=NAV, 2=ATT  |
|                          |                                          |         |            |             |                      |
| IR 1                     | A32NX_OVHD_ADIRS_IR_1_PB_IS_ON           | 0 \| 1  | R/W        | Custom LVAR |                      |
|                          | A32NX_OVHD_ADIRS_IR_1_PB_HAS_FAULT       | 0 \| 1  | R          | Custom LVAR |                      |
|                          |                                          |         |            |             |                      |
| ADR 1                    | A32NX_OVHD_ADIRS_ADR_1_PB_IS_ON          | 0 \| 1  | R/W        | Custom LVAR |                      |
|                          | A32NX_OVHD_ADIRS_ADR_1_PB_HAS_FAULT      | 0 \| 1  | R          | Custom LVAR |                      |
|                          |                                          |         |            |             |                      |
| Remaining Alignment Time | A32NX_ADIRS_REMAINING_IR_ALIGNMENT_TIME  | seconds | R          | Custom LVAR |                      |
|                          |                                          |         |            |             |                      |
| ON BAT light             | A32NX_OVHD_ADIRS_ON_BAT_IS_ILLUMINATED   | 0 \| 1  | R          | Custom LVAR |                      |

### APU Panel

Flight Deck: [APU Panel](flight-deck/ovhd/apu.md)

| Function  | API Usage                                | Values | Read/Write | Type        | Remark |
|:----------|:-----------------------------------------|:-------|:-----------|:------------|:-------|
| MASTER SW | A32NX_OVHD_APU_MASTER_SW_PB_IS_ON        | 0 \| 1 | R/W        | Custom LVAR |        |
|           | A32NX_OVHD_APU_MASTER_SW_PB_HAS_FAULT    | 0 \| 1 | R          | Custom LVAR |        |
|           |                                          |        |            |             |        |
| START     | A32NX_OVHD_APU_MASTER_SW_PB_IS_ON        | 0 \| 1 | R/W        | Custom LVAR |        |
|           | A32NX_OVHD_APU_MASTER_SW_PB_IS_AVAILABLE | 0 \| 1 | R          | Custom LVAR |        |

!!! note "Search for APU in our [list for all Custom LVARS](https://github.com/flybywiresim/a32nx/blob/master/docs/a320-simvars.md){target=new} for further variables."

### RCDR Panel

Flight Deck: [RCDR Panel](flight-deck/ovhd/voice-recorder.md)

| Function  | API Usage                    | Values | Read/Write | Type        | Remark |
|:----------|:-----------------------------|:-------|:-----------|:------------|:-------|
| GND CTL   | A32NX_RCDR_GROUND_CONTROL_ON | 0 \| 1 | R/W        | Custom LVAR |        |
|           |                              |        |            |             |        |
| CVR ERASE | N/A                          |        |            |             |        |
|           |                              |        |            |             |        |
| CVR TEST  | A32NX_RCDR_TEST              | 0 \| 1 | R/W        | Custom LVAR |        |

### Oxygen Panel

Flight Deck: [Oxygen Panel](flight-deck/ovhd/oxygen.md)

| Function    | API Usage                       | Values | Read/Write | Type        | Remark |
|:------------|:--------------------------------|:-------|:-----------|:------------|:-------|
| MASK MAN ON | A32NX_OXYGEN_MASKS_DEPLOYED     | 0 \| 1 | R/W        | Custom LVAR |        |
|             |                                 |        |            |             |        |
| PASSENGER   | A32NX_OXYGEN_PASSENGER_LIGHT_ON | 0 \| 1 | R/W        | Custom LVAR |        |
|             |                                 |        |            |             |        |
| CREW SUPPLY | PUSH_OVHD_OXYGEN_CREW           | 0 \| 1 | R/W        | Custom LVAR |        |

### Fire Panel

Flight Deck: [Fire Panel](flight-deck/ovhd/fire.md)

!!! note "The below table shows the API for ENG 1. Replace `1` with `2`for ENG 2."

| Function         | API Usage                        | Values | Read/Write | Type        | Remark                                   |
|:-----------------|:---------------------------------|:-------|:-----------|:------------|:-----------------------------------------|
| APU FIRE Test    | A32NX_FIRE_TEST_APU              | 0 \| 1 | R/W        | Custom LVAR |                                          |
|                  |                                  |        |            |             |                                          |
| APU FIRE GUARD   | A32NX_FIRE_GUARD_APU             | 0 \| 1 | R/W        | Custom LVAR |                                          |
|                  |                                  |        |            |             |                                          |
| APU FIRE         | A32NX_FIRE_BUTTON_APU            | 0 -> 1 | R/W        | Custom LVAR | Open Guard first. Can't be reset.        |
|                  |                                  |        |            |             |                                          |
| APU DISCH        | A32NX_FIRE_APU_AGENT1_DISCHARGE  | 0 -> 1 | R/W        | Custom LVAR | Press Fire button first. Can't be reset. |
|                  |                                  |        |            |             |                                          |
| ENG 1 FIRE TEST  | A32NX_FIRE_TEST_ENG1             | 0 \| 1 | R/W        | Custom LVAR |                                          |
|                  |                                  |        |            |             |                                          |
| ENG 1 FIRE GUARD | A32NX_FIRE_GUARD_ENG1            | 0 \| 1 | R/W        | Custom LVAR |                                          |
|                  |                                  |        |            |             |                                          |
| ENG 1 FIRE       | A32NX_FIRE_BUTTON_ENG1           | 0 -> 1 | R/W        | Custom LVAR | Open Guard first. Can't be reset.        |
|                  |                                  |        |            |             |                                          |
| ENG 1 AGENT 1    | A32NX_FIRE_ENG1_AGENT1_DISCHARGE | 0 -> 1 | R/W        | Custom LVAR | Press Fire button first. Can't be reset. |
|                  |                                  |        |            |             |                                          |
| ENG 1 AGENT 2    | A32NX_FIRE_ENG2_AGENT1_DISCHARGE | 0 -> 1 | R/W        | Custom LVAR | Press Fire button first. Can't be reset. |

### Fuel Panel

Flight Deck: [Fuel Panel](flight-deck/ovhd/fuel.md)

!!! note "The below table shows the API for PUMP 1. Replace `1` with `2..6` for the other pumps."
    L1=2, L2=5. C1=1, C2=4, R1=3, R2=6

| Function    | API Usage                 | Values | Read/Write | Type       | Remark |
|:------------|:--------------------------|:-------|:-----------|:-----------|:-------|
| Fuel Pump 1 | FUELSYSTEM_PUMP_TOGGLE    | 1..6   | -          | MSFS EVENT |        |
|             | FUELSYSTEM PUMP ACTIVE:1  | 0 \| 1 | R          | MSFS VAR   |        |
|             | FUELSYSTEM PUMP SWITCH:1  | 0 \| 1 | R          | MSFS VAR   |        |
|             |                           |        |            |            |        |
| X FEED      | FUELSYSTEM_VALVE_TOGGLE   | 3      | -          | MSFS EVENT |        |
|             | FUELSYSTEM VALVE SWITCH:3 | 0 \| 1 | R          | MSFS VAR   |        |
|             |                           |        |            |            |        |
| MODE SEL    | N/A                       |        |            |            |        |

### Air Condition Panel

Flight Deck: [AC Panel](flight-deck/ovhd/ac.md)

| Function       | API Usage                                                 | Values | Read/Write | Type        | Remark       |
|:---------------|:----------------------------------------------------------|:-------|:-----------|:------------|:-------------|
| APU BLEED      | A32NX_OVHD_PNEU_APU_BLEED_PB_IS_ON                        | 0 \| 1 | R/W        | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| ENG 1 BLEED    | ENGINE_BLEED_AIR_SOURCE_TOGGLE                            | 1      | -          | MSFS EVENT  |              |
|                | XMLVAR_MOMENTARY_PUSH_<br/>OVHD_AIRCOND_ENG1BLEED_PRESSED | 0 \| 1 | R          | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| ENG 2 BLEED    | ENGINE_BLEED_AIR_SOURCE_TOGGLE                            | 2      | -          | Custom LVAR |              |
|                | XMLVAR_MOMENTARY_PUSH_<br/>OVHD_AIRCOND_ENG2BLEED_PRESSED | 0 \| 1 | R          | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| X BLEED knob   | A32NX_KNOB_OVHD_AIRCOND_XBLEED_POSITION                   | 0..2   | R/W        | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| PACK 1         | A32NX_AIRCOND_PACK1_TOGGLE                                | 0 \| 1 | R/W        | Custom LVAR |              |
|                | A32NX_AIRCOND_PACK2_FAULT                                 | 0 \| 1 | R/W        | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| PACK 2         | A32NX_AIRCOND_PACK2_TOGGLE                                | 0 \| 1 | R/W        | Custom LVAR |              |
|                | A32NX_AIRCOND_PACK2_FAULT                                 | 0 \| 1 | R/W        | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| PACK FLOW knob | A32NX_KNOB_OVHD_AIRCOND_PACKFLOW_POSITION                 | 0 \| 1 | R/W        | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| COCKPIT knob   | A32NX_CKPT_TRIM_TEMP                                      | 18..30 | R          | Custom LVAR |              |
|                | A32NX_CKPT_TEMP                                           | 18..30 | R          | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| FWD CABIN knob | A32NX_FWD_TRIM_TEMP                                       | 18..30 | R          | Custom LVAR |              |
|                | A32NX_FWD_TEMP                                            | 18..30 | R          | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| AFT CABIN knob | A32NX_AFT_TRIM_TEMP                                       | 18..30 | R          | Custom LVAR |              |
|                | A32NX_AFT_TEMP                                            | 18..30 | R          | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| HOT AIR        | A32NX_AIRCOND_HOTAIR_TOGGLE                               | 0 \| 1 | R/W        | Custom LVAR |              |
|                | A32NX_AIRCOND_HOTAIR_FAULT                                | 0 \| 1 | R/W        | Custom LVAR |              |
|                |                                                           |        |            |             |              |
| RAM AIR        | A32NX_AIRCOND_RAMAIR_TOGGLE_LOCK                          | 0 \| 1 | R          | Custom LVAR | Switch Guard |
|                | A32NX_AIRCOND_RAMAIR_TOGGLE                               | 0 \| 1 | R/W        | Custom LVAR |              |

### Anit Ice Panel

Flight Deck: [Anti Ice Panel](flight-deck/ovhd/anti-ice.md)

| Function          | API Usage                                            | Values | Read/Write | Type             | Remark                  |
|:------------------|:-----------------------------------------------------|:-------|:-----------|:-----------------|:------------------------|
| WING              | TOGGLE_STRUCTURAL_DEICE                              | -      | -          | SIMCONNECT EVENT | Function & Button light |
|                   | STRUCURAL DEICE SWITCH                               | 0 \| 1 | R/W        | SIMCONNECT VAR   | Function & Button light            |
|                   | XMLVAR_MOMENTARY_PUSH_OVHD_<br/>ANTIICE_WING_PRESSED | 0 \| 1 | R/W        | Custom LVAR      | Button state            |
|                   |                                                      |        |            |                  |                         |
| ENG 1             | ANTI_ICE_TOGGLE_ENG1                                 | -      | -          | SIMCONNECT EVENT | Function & Button light            |
|                   | ENG ANTI ICE:1                                       | 0 \| 1 | R/W        | SIMCONNECT VAR   | Function & Button light            |
|                   | XMLVAR_MOMENTARY_PUSH_OVHD_<br/>ANTIICE_ENG1_PRESSED | 0 \| 1 | R/W        | Custom LVAR      | Button state            |
|                   |                                                      |        |            |                  |                         |
| ENG 2             | ANTI_ICE_TOGGLE_ENG2                                 | -      | -          | SIMCONNECT EVENT | Function & Button light            |
|                   | ENG ANTI ICE:2                                       | 0 \| 1 | R/W        | SIMCONNECT VAR   | Function & Button light            |
|                   | XMLVAR_MOMENTARY_PUSH_OVHD_<br/>ANTIICE_ENG2_PRESSED | 0 \| 1 | R/W        | Custom LVAR      | Button state            |
|                   |                                                      |        |            |                  |                         |
| PROBE/WINDOW HEAT | A32NX_MAN_PITOT_HEAT                                 | 0 \| 1 | R/W        | Custom LVAR      | Function & Button light            |
|                   | XMLVAR_MOMENTARY_PUSH_OVHD_<br/>PROBESWINDOW_PRESSED | 0 \| 1 | R/W        | Custom LVAR      | Button state            |

## Glareshield

## Instrument Panel

### Instrument Lighting Control Panel

Flight Deck: [ILCP Panel](flight-deck/front/ilcp.md)

| Function            | API Usage              | Values    | Read/Write | Type     | Remark |
|:--------------------|:-----------------------|:----------|:-----------|:---------|:-------|
| PFD Brt Cpt.        | LIGHT POTENTIOMETER:88 | 0..100    | R/W        | MSFS VAR |        |
|                     |                        |           |            |          |        |
| PFD/ND XFR Cpt.     | N/A                    |           |            |          |        |
|                     |                        |           |            |          |        |
| ND Brt Cpt.         | LIGHT POTENTIOMETER:89 | 0..100    | R/W        | MSFS VAR |        |
|                     |                        |           |            |          |        |
| WX/Terrain Brt Cpt. | LIGHT POTENTIOMETER:94 | 0..100    | R/W        | MSFS VAR |        |
|                     |                        |           |            |          |        |
| Loud Spkr Cpt.      | N/A                    |           |            |          |        |
|                     |                        |           |            |          |        |
| CONSOLE/FLOOR Cpt.  | LIGHT POTENTIOMETER:8  | 50 \| 100 | R/W        | MSFS VAR |        |
|                     |                        |           |            |          |        |
| PFD Brt F.O.        | LIGHT POTENTIOMETER:90 | 0..100    | R/W        | MSFS VAR |        |
|                     |                        |           |            |          |        |
| PFD/ND XFR F.O.     | N/A                    |           |            |          |        |
|                     |                        |           |            |          |        |
| ND Brt F.O.         | LIGHT POTENTIOMETER:91 | 0..100    | R/W        | MSFS VAR |        |
|                     |                        |           |            |          |        |
| WX/Terrain Brt F.O. | LIGHT POTENTIOMETER:95 | 0..100    | R/W        | MSFS VAR |        |
|                     |                        |           |            |          |        |
| Loud Spkr F.O.      | N/A                    |           |            |          |        |
|                     |                        |           |            |          |        |
| CONSOLE/FLOOR F.O.  | LIGHT POTENTIOMETER:9  | 50 \| 100 | R/W        | MSFS VAR |        |


## Pedestal

### Lighting Pedestal Captain Side Panel

Flight Deck: [Lighting Pedestal Cpt. Side Panel](flight-deck/pedestal/lighting-capt.md)

| Function      | API Usage              | Values | Read/Write | Type     | Remark       |
|:--------------|:-----------------------|:-------|:-----------|:---------|:-------------|
| FLOOD LT Cpt  | LIGHT POTENTIOMETER:83 | 0..100 | R/W        | MSFS VAR |              |
|               |                        |        |            |          |              |
| INTEG LT      | LIGHT POTENTIOMETER:85 | 0..100 | R/W        | MSFS VAR |              |
|               |                        |        |            |          |              |
| FLOOD LT F.O. | LIGHT POTENTIOMETER:76 | 0..100 | R/W        | MSFS VAR | On F.O. side |


