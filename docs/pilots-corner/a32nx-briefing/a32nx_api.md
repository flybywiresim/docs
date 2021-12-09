---
hide:
    - navigation
---

# Flight Deck A32NX API

[A320neo Pilot Briefing](index.md){ .md-button }
[Clickable Flight Deck](flight-deck/index.md){ .md-button }

!!! note ""
    The below table might lag behind the current developments of the A32NX. It is
    based on the A32NX Development version and we try to keep it updated as best
    as possible. Some variables/events are only available in the Experimental
    version of A32NX and are marked as such.

    You can help us keep this up to date and improve this by reporting any errors
    or omissions on our [:fontawesome-brands-discord:{: .discord } - **Discord**](https://discord.gg/flybywire){target=new}
    in the **#support** channel or by creating an issue report here: [Docs Issues](https://github.com/flybywiresim/docs/issues){target=new}.

Find the complete list of Custom Event and Custom LVARS of the A32NX:

- [Custom LVARs](https://github.com/flybywiresim/a32nx/blob/master/docs/a320-simvars.md){target=new}
- [Custom Events](https://github.com/flybywiresim/a32nx/blob/master/docs/a320-events.md){target=new}

!!! note "The order of the panels below is roughly done after the standard cold & dark setup procedure."

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
|             | GENERAL ENG MASTER ALTERNATOR:1           | 0 \| 1 | R/W        | SIMCONNECT VAR   |                                            |
|             | A32NX_OVHD_ELEC_ENG_GEN_1_PB_HAS_FAULT    | 0 \| 1 | R          | Custom LVAR      |                                            |
| GEN 2       | TOGGLE_ALTERNATOR:2                       | -      | -          | SIMCONNECT EVENT |                                            |
|             | GENERAL ENG MASTER ALTERNATOR:2           | 0 \| 1 | R/W        | SIMCONNECT VAR   |                                            |
|             | A32NX_OVHD_ELEC_ENG_GEN_2_PB_HAS_FAULT    | 0 \| 1 | R          | Custom LVAR      |                                            |
|             |                                           |        |            |                  |                                            |
| APU GEN     | APU_GENERATOR_SWITCH_TOGGLE               | -      | -          | SIMCONNECT EVENT |                                            |
|             | APU_GENERATOR_SWITCH_SET                  | 0 \| 1 | -          | SIMCONNECT EVENT |                                            |
|             | APU GENERATOR SWITCH                      | 0 \| 1 | R/W        | SIMCONNECT LVAR  |                                            |
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

| Function     | API Usage             | Values | Read/Write | Type             | Remark                                                             |
|:-------------|:----------------------|:-------|:-----------|:-----------------|:-------------------------------------------------------------------|
| STROBE       | STROBES_SET           | 0 \| 1 | -          | SIMCONNECT EVENT | OFF and ON (no AUTO)                                               |
|              | STROBES_TOGGLE        | -      | -          | SIMCONNECT EVENT | OFF and ON (no AUTO)                                               |
|              | STROBES_ON            | -      | -          | SIMCONNECT EVENT | OFF and ON (no AUTO)                                               |
|              | STROBES_OFF           | -      | -          | SIMCONNECT EVENT | OFF and ON (no AUTO)                                               |
|              | LIGHT STROBE          | 0 \| 1 | R/W        | SIMCONNECT VAR   | OFF and ON (no AUTO)                                               |
|              | STROBE_0_AUTO         | 0 \| 1 | R/W        | Custom LVAR      | AUTO only when STROBES are ON                                      |
|              | LIGHTING_STROBE_0     | 0 \| 1 | R          |                  | 2=OFF, 1=AUTO, 0=ON                                                |
|              |                       |        |            |                  |                                                                    |
| BEACON       | BEACON_SET            | 0 \| 1 | -          | SIMCONNECT EVENT |                                                                    |
|              | BEACON_TOGGLE         | -      | -          | SIMCONNECT EVENT |                                                                    |
|              | BEACON_ON             | -      | -          | SIMCONNECT EVENT |                                                                    |
|              | BEACON_OFF            | -      | -          | SIMCONNECT EVENT |                                                                    |
|              | LIGHT BEACON          | 0 \| 1 | R/W        | SIMCONNECT VAR   |                                                                    |
|              |                       |        |            |                  |                                                                    |
| WING         | WING_SET              | 0 \| 1 | -          | SIMCONNECT EVENT |                                                                    |
|              | BEACON_TOGGLE         | -      | -          | SIMCONNECT EVENT |                                                                    |
|              | BEACON_ON             | -      | -          | SIMCONNECT EVENT |                                                                    |
|              | BEACON_OFF            | -      | -          | SIMCONNECT EVENT |                                                                    |
|              | LIGHT BEACON          | 0 \| 1 | R/W        | SIMCONNECT VAR   |                                                                    |
|              |                       |        |            |                  |                                                                    |
| NAV & LOGO   | NAV_LIGHTS_SET        | 0 \| 1 | -          | SIMCONNECT EVENT | LOGO needs to be set separately                                    |
|              | LIGHT NAV             | 0 \| 1 | R/W        | SIMCONNECT VAR   | LOGO needs to be set separately                                    |
|              | LOGO_LIGHTS_SET       | 0 \| 1 | -          | SIMCONNECT EVENT | LOGO does not move switch                                          |
|              | LIGHT LOGO            | 0 \| 1 | R/W        | SIMCONNECT VAR   | LOGO does not move switch                                          |
|              |                       |        |            |                  |                                                                    |
| RWY TURN OFF | CIRCUIT SWITCH ON:21  | 0 \| 1 | R/W        | SIMCONNECT VAR   | Left Rwy Turn Off Light + Switch                                   |
|              | CIRCUIT SWITCH ON:22  | 0 \| 1 | R/W        | SIMCONNECT VAR   | Right Rwy Turn Off Light                                               |
|              | LIGHTING_TAXI_2       | 0 \| 1 | R          | Custom LVAR      |                                                                    |
|              |                       |        |            |                  |                                                                    |
| LAND L + R   | LANDING_LIGHTS_ON     | 0..3   | -          | SIMCONNECT EVENT | 0=all, 1=NOSE, 2=L, 3=R                                            |
|              | LANDING_LIGHTS_OFF    | 0..3   | -          | SIMCONNECT EVENT | 0=all, 1=NOSE, 2=L, 3=R                                            |
|              | LANDING_LIGHTS_TOGGLE | 0..3   | -          | SIMCONNECT EVENT | 0=all, 1=NOSE, 2=L, 3=R                                            |
|              | CIRCUIT SWITCH ON:18  | 0 \| 1 | R/W        | SIMCONNECT VAR   | Left landing light                                                 |
|              | CIRCUIT SWITCH ON:19  | 0 \| 1 | R/W        | SIMCONNECT VAR   | Right landing light                                                |
|              | LIGHT_LANDING_1       | 0 \| 1 | R/W        | Custom LVAR      | Switch position of the NOSE switch: 2=OFF, 1=TAXI, 0=T.O.          |
|              | LIGHT_LANDING_2       | 0 \| 1 | R/W        | Custom LVAR      | Switch position of the left landing light: 2=RETRACT, 1=OFF, 2=ON  |
|              | LIGHT_LANDING_3       | 0 \| 1 | R/W        | Custom LVAR      | Switch position of the right landing light: 2=RETRACT, 1=OFF, 2=ON |
|              | LANDING_1_RETRACTED   | 0 \| 1 | R/W        | Custom LVAR      | No function - NOSE light can't be retracted                        |
|              | LANDING_2_RETRACTED   | 0 \| 1 | R/W        | Custom LVAR      | Retraction of left landing light: 0=extended, 1=retracted          |
|              | LANDING_3_RETRACTED   | 0 \| 1 | R/W        | Custom LVAR      | Retraction of right landing light 0=extended, 1=retracted          |
|              |                       |        |            |                  |                                                                    |
| NOSE         | TOGGLE_TAXI_LIGHTS    | -      | -          | SIMCONNECT EVENT | Also toggles RWY TURN OFF LIGHT                                    |
|              | LIGHT TAXI            | 0 \| 1 | R/W        | SIMCONNECT VAR   | Only switches TAXI light                                           |
|              | LANDING_LIGHTS_TOGGLE | 1      | -          | SIMCONNECT EVENT | Toggles switch between T.O. and OFF                                |
|              | CIRCUIT SWITCH ON:20  | 0 \| 1 | R/W        | SIMCONNECT VAR   | NOSE TAXI                                                          |
|              | CIRCUIT SWITCH ON:17  | 0 \| 1 | R/W        | SIMCONNECT VAR   | NODE T.O.                                                          |

!!! note "Landing and Taxi lights"
    The default behaviour of the SIMCONNECT events for landing lights and taxi
    lights is very weird for the A320 as SIMCONNECT does not really account for
    3 landing lights, one of them on the same switch as the taxi light and an
    independent RWY TURN OFF light.

    These events often trigger several lights and switches together and it is
    very hard to specifically map them to single button/switches.

    One solution we have found to be working is:

    - Landing Lights L
        - Set `LIGHT_LANDING_2` to 0 (sets the switch to ON)
        - Set `LANDING_2_RETRACTED` to 0 (extends the landing light)
        - Delay of 8-10sec (to simulate the time it takes to extend the lights)
        - Set `CIRCUIT SWITCH ON:18` to 1 (turns on the actual light)
    - Landing Lights R
        - Set `LIGHT_LANDING_3` to 0 (sets the switch to ON)
        - Set `LANDING_3_RETRACTED` to 0 (extends the landing light)
        - Delay of 8-10sec (to simulate the time it takes to extend the lights)
        - Set `CIRCUIT SWITCH ON:19` to 1 (turns on the actual light)
    - NOSE
        - Set `CIRCUIT SWITCH ON:17` (turns on TAXI lights and moves switch to TAXI)
        - Set `CIRCUIT SWITCH ON:20` (turns on T.O. lights and moves switch to T.O.)
        - Set `CIRCUIT SWITCH ON:17` `CIRCUIT SWITCH ON:20` to 0 to turn off all NOSE lights and move the switch to OFF)
    - RWY TURN OFF
        - Set `CIRCUIT SWITCH ON:21` to 1 (turns on left light)
        - Set `CIRCUIT SWITCH ON:22` to 1 (turns on right light)

    !!! warning "Doing it this way might break any third party software trying to read the status of the lights through SIMCONNECT."


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

### Calls Panel

Flight Deck: [Calls Panel](flight-deck/ovhd/calls.md)

| Function | API Usage                | Values | Read/Write | Type        | Remark |
|:---------|:-------------------------|:-------|:-----------|:------------|:-------|
| MECH     | PUSH_OVHD_CALLS_MECH     | 0 \| 1 | R/W        | Custom LVAR |        |
|          |                          |        |            |             |        |
| ALL      | PUSH_OVHD_CALLS_ALL      | 0 \| 1 | R/W        | Custom LVAR |        |
|          |                          |        |            |             |        |
| FWD      | PUSH_OVHD_CALLS_FWD      | 0 \| 1 | R/W        | Custom LVAR |        |
|          |                          |        |            |             |        |
| AFT      | PUSH_OVHD_CALLS_AFT      | 0 \| 1 | R/W        | Custom LVAR |        |
|          |                          |        |            |             |        |
| EMER     | A32NX_CALLS_EMER_ON_LOCK | 0 \| 1 | R          | Custom LVAR |        |
|          | A32NX_CALLS_EMER_ON      | 0 \| 1 | R/W        | Custom LVAR |        |

### Wiper Panel

Flight Deck: [Wiper Panel](flight-deck/ovhd/wipers.md)

| Function     | API Usage                            | Values | Read/Write | Type        | Remark                                 |
|:-------------|:-------------------------------------|:-------|:-----------|:------------|:---------------------------------------|
| WIPER L knob | CIRCUIT ON:77                        | 0 \| 1 | R          |             |                                        |
|              | ELECTRICAL_CIRCUIT_POWER_SETTING_SET | 77     |            |             | ~~Unclear how to set power correctly~~ |
|              | ELECTRICAL_CIRCUIT_TOGGLE            | 77     |            |             |                                        |
|              |                                      |        |            |             |                                        |
| WIPER R knob | CIRCUIT ON:88                        | 0 \| 1 | R          |             |                                        |
|              | ELECTRICAL_CIRCUIT_TOGGLE            | 88     |            |             |                                        |
|              | ELECTRICAL_CIRCUIT_POWER_SETTING_SET | 88     |            |             | ~~Unclear how to set power correctly~~ |
|              |                                      |        |            |             |                                        |
| RAIN RPLNT   | A32NX_RAIN_REPELLENT_LEFT_ON         | 0 \| 1 | R          | Custom LVAR |                                        |
|              | A32NX_RAIN_REPELLENT_RIGHT_ON        | 0 \| 1 | R          | Custom LVAR |                                        |

## Glareshield

### Lighting Knobs

Flight Deck: [Glareshield Lighting Knobs](flight-deck/glareshield/light-knobs.md)

| Function                    | API Usage              | Values | Read/Write | Type     | Remark |
|:----------------------------|:-----------------------|:-------|:-----------|:---------|:-------|
| Glareshield Integral Lights | LIGHT POTENTIOMETER:84 | 0..100 | R/W        | MSFS VAR |        |
|                             |                        |        |            |          |        |
| Glareshield LCD Lights      | LIGHT POTENTIOMETER:87 | 0..100 | R/W        | MSFS VAR |        |
|                             |                        |        |            |          |        |
| Table Light Capt.           | LIGHT POTENTIOMETER:10 | 0..100 | R/W        | MSFS VAR |        |
|                             |                        |        |            |          |        |
| Table Light F.O.            | LIGHT POTENTIOMETER:11 | 0..100 | R/W        | MSFS VAR |        |

### EFIS Control Panel

Flight Deck: [EFIS Control Panel](flight-deck/glareshield/efis_control.md)

| Function     | API Usage                        | Values           | Read/Write | Type             | Remark                                            |
|:-------------|:---------------------------------|:-----------------|:-----------|:-----------------|:--------------------------------------------------|
| Baro Display | KOHLSMAN SETTING MB:1            | 948-1084 (hPa)   | R          | MSFS VAR         |                                                   |
|              | KOHLSMAN SETTING HG:1            | 27.99-32.01 (Hg) | R          | MSFS VAR         |                                                   |
|              |                                  |                  |            |                  |                                                   |
| Baro knob    | KOHLMAN_INC                      | -                | -          | SIMCONNECT EVENT |                                                   |
|              | KOHLMAN_INC                      | -                | -          | SIMCONNECT EVENT |                                                   |
|              |                                  |                  |            |                  |                                                   |
| inHG / hPa   | XMLVAR_BARO_SELECTOR_HPA_1       | 0 \| 1           | R/W        | Custom LVAR      | 0=Hg, 1=hPa                                       |
|              |                                  |                  |            |                  |                                                   |
| FD           | AUTOPILOT FLIGHT DIRECTOR ACTIVE | 0 \| 1           | R          | SIMCONNECT VAR   |                                                   |
|              | TOGGLE_FLIGHT_DIRECTOR           | -                | -          | SIMCONNECT EVENT |                                                   |
|              |                                  |                  |            |                  |                                                   |
| LS Capt.     | BTN_LS_1_FILTER_ACTIVE           | 0 \| 1           | R          | Custom LVAR      | ~~Not working currently.~~                        |
| LS F.O.      | BTN_LS_2_FILTER_ACTIVE           | 0 \| 1           | R          | Custom LVAR      | ~~Not working currently.~~                        |
|              |                                  |                  |            |                  |                                                   |
|              |                                  |                  |            |                  |                                                   |
| ND Filter    | A32NX_EFIS_L_OPTION              | 0..5             | R/W        | Custom LVAR      | 0=none, 1=CSTR, 2=VOR, 3=WPT, 4=NDB, 5=ARPT       |
|              | A32NX_EFIS_R_OPTION              | 0..5             | R/W        | Custom LVAR      | 0=none, 1=CSTR, 2=VOR, 3=WPT, 4=NDB, 5=ARPT       |
|              |                                  |                  |            |                  |                                                   |
| ND MODE      | A32NX_EFIS_L_ND_MODE             | 0..4             | R/W        | Custom LVAR      | 0=ROSE ILS, 1=ROSE VOR, 2=ROSE NAV. 3=ARC, 4=PLAN |
|              | A32NX_EFIS_R_ND_MODE             | 0..4             | R/W        | Custom LVAR      | 0=ROSE ILS, 1=ROSE VOR, 2=ROSE NAV. 3=ARC, 4=PLAN |
|              |                                  |                  |            |                  |                                                   |
| ND RANGE     | A32NX_EFIS_L_ND_RANGE            | 0..5             | R/W        | Custom LVAR      | 0=10, ..., 5=320                                  |
|              | A32NX_EFIS_R_ND_RANGE            | 0..5             | R/W        | Custom LVAR      | 0=10, ..., 5=320                                  |
|              |                                  |                  |            |                  |                                                   |
| ADF-VOR      | A32NX_EFIS_L_NAVAID_1_MODE       | 0..2             | R/W        | Custom LVAR      | 0=OFF, 1=ADF, 2=VOR                               |
|              | A32NX_EFIS_L_NAVAID_2_MODE       | 0..2             | R/W        | Custom LVAR      | 0=OFF, 1=ADF, 2=VOR                               |
|              | A32NX_EFIS_R_NAVAID_1_MODE       | 0..2             | R/W        | Custom LVAR      | 0=OFF, 1=ADF, 2=VOR                               |
|              | A32NX_EFIS_R_NAVAID_2_MODE       | 0..2             | R/W        | Custom LVAR      | 0=OFF, 1=ADF, 2=VOR                               |

### FCU Panel

Flight Deck: [FCU Panel](flight-deck/glareshield/fcu.md)

| Function          | API Usage                           | Values           | Read/Write | Type             | Remark                                                                   |
|:------------------|:------------------------------------|:-----------------|:-----------|:-----------------|:-------------------------------------------------------------------------|
| SPD knob          | A32NX_AUTOPILOT_SPEED_SELECTED      | 0..399           | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_SPD_INC                   | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_SPD_DEC                   | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_SPD_SET                   | 0..399           | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_SPD_PUSH                  | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_SPD_PULL                  | -                | -          | Custom EVENT     |                                                                          |
|                   | AP_AIRSPEED_ON                      | -                | -          | SIMCONNECT EVENT | Push                                                                     |
|                   | AP_AIRSPEED_OFF                     | -                | -          | SIMCONNECT EVENT | Pull                                                                     |
|                   | AP_SPD_VAR_INC                      | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_SPD_VAR_DEC                      | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_MACH_VAR_INC                     | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_MACH_VAR_DEC                     | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |                  |            |                  |                                                                          |
| HDG knob          | A32NX_AUTOPILOT_HEADING_SELECTED    | 0..359           | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_HDG_INC                   | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_HDG_DEC                   | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_HDG_SET                   | 0..359           | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_HDG_PUSH                  | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_HDG_PULL                  | -                | -          | Custom EVENT     |                                                                          |
|                   | AP_HDG_HOLD_ON                      | -                | -          | SIMCONNECT EVENT | Push                                                                     |
|                   | AP_HDG_HOLD_OFF                     | -                | -          | SIMCONNECT EVENT | Pull                                                                     |
|                   | HEADING_BUG_INC                     | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   | HEADING_BUG_DEC                     | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |                  |            |                  |                                                                          |
| LOC               | A32NX_FCU_LOC_MODE_ACTIVE           | 0 \| 1           | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_LOC_PUSH                  | -                | -          | Custom EVENT     |                                                                          |
|                   | AP_LOC_HOLD                         | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |                  |            |                  |                                                                          |
| ALT knob          | AUTOPILOT ALTITUDE LOCK VAR:3       | 100..49000       |            | MSFS VAR         |                                                                          |
|                   | A32NX.FCU_ALT_INC                   | 0 \| 100 \| 1000 | R          | Custom EVENT         | 0=Use FCU Setting, 100=100, 1000=1000                                    |
|                   | A32NX.FCU_ALT_DEC                   | 0 \| 100 \| 1000 | R          | Custom EVENT     | 0=Use FCU Setting, 100=100, 1000=1000                                    |
|                   | A32NX.FCU_ALT_SET                   | 100..49000       | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_ALT_PUSH                  | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_ALT_PULL                  | -                | -          | Custom EVENT     |                                                                          |
|                   | AP_ALT_HOLD_ON                      | -                | -          | SIMCONNECT EVENT | Push                                                                     |
|                   | AP_ALT_HOLD_OFF                     | -                | -          | SIMCONNECT EVENT | Pull                                                                     |
|                   | AP_ALT_VAR_INC                      | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_ALT_VAR_DEC                      | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |                  |            |                  |                                                                          |
| ALT INC 100-1000  | A32NX.FCU_ALT_INCREMENT_TOGGLE      | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_ALT_INCREMENT_SET         | 100 \| 1000      | -          | Custom EVENT     |                                                                          |
|                   | XMLVAR_AUTOPILOT_ALTITUDE_INCREMENT | 100 \| 1000      | R          | Custom LVAR      |                                                                          |
|                   | AP_ALT_HOLD                         | -                | -          | SIMCONNECT EVENT | Repurposed event as Simconnect has no standard event for this otherwise. |
|                   |                                     |                  |            |                  |                                                                          |
| EXPED             | A32NX_FMA_EXPEDITE_MODE             | 0 \| 1           | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_EXPED_PUSH                | -                | -          | Custom EVENT     |                                                                          |
|                   | AP_ATT_HOLD                         | -                | -          | SIMCONNECT EVENT | Repurposed event as Simconnect has no standard event for this otherwise. |
|                   |                                     |                  |            |                  |                                                                          |
| V/S FPA knob      | A32NX_AUTOPILOT_VS_SELECTED         | -6000..6000      | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_VS_INC                    | -                | -          | Custom LVAR      | FPA: -9.9..9.9                                                           |
|                   | A32NX.FCU_VS_DEC                    | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_VS_SET                    | -6000..6000      | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_VS_PUSH                   | -                | -          | Custom EVENT     | FPA: -9.9..9.9                                                           |
|                   | A32NX.FCU_VS_PULL                   | -                | -          | Custom EVENT     |                                                                          |
|                   | AP_VS_HOLD_ON                       | -                | -          | SIMCONNECT EVENT | Push                                                                     |
|                   | AP_VS_HOLD_OFF                      | -                | -          | SIMCONNECT EVENT | Pull                                                                     |
|                   | AP_VS_VAR_INC                       | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_VS_VAR_DEC                       | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |                  |            |                  |                                                                          |
| APPR              | A32NX_FCU_APPR_MODE_ACTIVE          | 0 \| 1           | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_APPR_PUSH                 | -                | -          | Custom EVENT     |                                                                          |
|                   | AP_APR_HOLD                         | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |                  |            |                  |                                                                          |
| AP 1 + 2          | A32NX_AUTOPILOT_1_ACTIVE            | 0 \| 1           | R          | Custom LVAR      |                                                                          |
|                   | A32NX_AUTOPILOT_2_ACTIVE            | 0 \| 1           | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_AP_1_PUSH                 | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_AP_2_PUSH                 | -                | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_AP_DISCONNECT_PUSH        | -                |            | Custom EVENT     |                                                                          |
|                   | AP_MASTER                           | 1                | -          | SIMCONNECT EVENT | Toggles                                                                  |
|                   | AUTOPILOT_ON                        | -                | -          | SIMCONNECT EVENT | 1st call AP1, 2nd call AP2                                               |
|                   | AUTOPILOT_OFF                       | -                | -          | SIMCONNECT EVENT | Turns off any AP                                                         |
|                   | AUTOPILOT_DISENGAGE_SET             | -                | -          | SIMCONNECT EVENT | 1 for OFF                                                                |
|                   | AUTOPILOT_DISENGAGE_TOGGLE          | -                | -          | SIMCONNECT EVENT | Toggles                                                                  |
|                   |                                     |                  | -          |                  |                                                                          |
| A/THR             | A32NX_AUTOTHRUST_STATUS             | 0..2             | R          | Custom LVAR      | 0=Disengaged, 1=Armed, 2=Active                                          |
|                   | A32NX.FCU_ATHR_PUSH                 | -                |            | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_ATHR_DISCONNECT_PUSH      | -                | -          | Custom EVENT     |                                                                          |
|                   | AUTO_THROTTLE_ARM                   | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   | AUTO_THROTTLE_DISCONNECT            | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   | AUTO_THROTTLE_TO_GA                 | -                | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |                  |            |                  |                                                                          |
| SPD/MACH          | AUTOPILOT MANAGED SPEED IN MACH     | 0 \| 1           | R          | MSFS VAR         |                                                                          |
|                   | A32NX.FCU_SPD_MACH_TOGGLE_PUSH      | -                | -          | Custom EVENT     |                                                                          |
|                   | AP_MACH_HOLD                        | -                | -          | SIMCONNECT EVENT | Repurposed event as Simconnect has no standard event for this otherwise. |
|                   |                                     |                  |            |                  |                                                                          |
| HDG-TRK / V/S-FPA | A32NX_TRK_FPA_MODE_ACTIVE           | 0 \| 1           | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_TRK_FPA_TOGGLE_PUSH       | -                | -          | Custom EVENT     |                                                                          |
|                   | AP_VS_HOLD                          | -                | -          | SIMCONNECT EVENT | Repurposed event as Simconnect has no standard event for this otherwise. |

### Warning Panel

Flight Deck: [Warning Panel](flight-deck/glareshield/warning.md)

| Function            | API Usage                        | Values | Read/Write | Type                     | Remark |
|:--------------------|:---------------------------------|:-------|:-----------|:-------------------------|:-------|
| MASTER CAUTION      | A32NX_MASTER_CAUTION             | 0 \| 1 | R/W        | Custom LVAR              |        |
|                     |                                  |        |            |                          |        |
| MASTER WARNING      | A32NX_MASTER_WARNING             | 0 \| 1 | R/W        | Custom LVAR              |        |
|                     |                                  |        |            |                          |        |
| CHRONO              | H:A32NX_EFIS_L_CHRONO_PUSHED     | -      | -          | HTML Event (aka H Event) |        |
|                     | H:A32NX_EFIS_R_CHRONO_PUSHED     | -      | -          | HTML Event (aka H Event) |        |
|                     |                                  |        |            |                          |        |
| SIDE STICK PRIORITY | N/A                              |        |            |                          |        |
|                     |                                  |        |            |                          |        |
| AUTOLAND WARNING    | A32NX_AUTOPILOT_AUTOLAND_WARNING | 0 \| 1 | R/W        | Custom LVAR              |        |
|                     |                                  |        |            |                          |        |
| ATC MSG             | N/A                              |        |            |                          |        |


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

### Autobrake, Gear Lever and Gear Annunciation

Flight Deck: [Autobrake and Gear Panel](flight-deck/front/autobrake-gear.md)

| Function              | API Usage                   | Values | Read/Write | Type             | Remark                    |
|:----------------------|:----------------------------|:-------|:-----------|:-----------------|:--------------------------|
| Gear lever            | GEAR_UP                     | -      | -          | SIMCONNECT EVENT |                           |
|                       | GEAR_DOWN                   | -      | -          | SIMCONNECT EVENT |                           |
|                       | GEAR HANDLE POSITION        | 0 \| 1 | R/W        | SIMCONNECT VAR   |                           |
|                       |                             |        |            |                  |                           |
| LDG GEAR Annunciators | GEAR LEFT POSITION          | 0..100 | R          | SIMCONNECT VAR   |                           |
|                       | GEAR CENTER POSITION        | 0..100 | R          | SIMCONNECT VAR   |                           |
|                       | GEAR RIGHT POSITION         | 0..100 | R          | SIMCONNECT VAR   |                           |
|                       |                             |        |            |                  |                           |
| AUTO BRK LO/MED/MAX   | A32NX_AUTOBRAKE_ARMED_MODE  | 0..3   | R/W        | Custom LVAR      | 0=OFF, 1=LO, 2=MED, 3=MAX |
|                       |                             |        |            |                  |                           |
| BRK FAN               | A32NX_BRAKE_FAN_BTN_PRESSED | 0 \| 1 | R/W        | Custom LVAR      |                           |
|                       |                             |        |            |                  |                           |
| A/SKID & N/W STRG     | ANTISKID_BRAKES_TOGGLE      | -      | -          | SIMCONNECT EVENT |                           |
|                       | ANTISKID BRAKES ACTIVE      | 0 \| 1 | R/W        | SIMCONNECT VAR   |                           |

### ISIS

Flight Deck: [ISIS Panel](flight-deck/front/isis.md)

| Function   | API Usage             | Values | Read/Write | Type        | Remark                                      |
|:-----------|:----------------------|:-------|:-----------|:------------|:--------------------------------------------|
| BRIGHTNESS | A32NX_BARO_BRIGHTNESS | 0..100 | R/W        | Custom LVAR | Auto-brightness - will automatically change |

### Clock

N/A

### TERR ON ND

Flight Deck: [ND Panel](flight-deck/front/nd.md)

| Function       | API Usage             | Values | Read/Write | Type        | Remark                  |
|:---------------|:----------------------|:-------|:-----------|:------------|:------------------------|
| TERR ON ND L+R | BTN_TERRONND_1_ACTIVE | 0 \| 1 | R/W        | Custom LVAR | Currently not available |
|                | BTN_TERRONND_2_ACTIVE | 0 \| 1 | R/W        | Custom LVAR | Currently not available |

### DCDU

Flight Deck: [DCDU Panel](flight-deck/front/dcdu.md)

note "The below table shows the API for left DCDU. Replace `L` with `R` for the right DCDU."

| Function    | API Usage                     | Values | Read/Write | Type     | Remark |
|:------------|:------------------------------|:-------|:-----------|:---------|:-------|
| BRT / DIM L | A32NX_PANEL_DCDU_L_BRIGHTNESS | 0..100 | R/W        | MSFS VAR |        |

## Pedestal

### MCDU Panel

Flight Deck: [MCDU Panel](flight-deck/pedestal/mcdu.md)

!!! note "The below table shows the API for left MCDU. Replace `L` with `R` for the right MCDU."

| Function    | API Usage               | Values | Read/Write | Type     | Remark |
|:------------|:------------------------|:-------|:-----------|:---------|:-------|
| BRT / DIM L | A32NX_MCDU_L_BRIGHTNESS | 0..100 | R/W        | MSFS VAR |        |


??? note "MCDU API (Click to Expand)"
    The MCDU API is vast as it contains many buttons.

    ~~Currently most of the buttons don't have a PRESSED event/var. So a complete remote control is not yet possible.~~

    - A32NX_MCDU_CLR_MinReleaseTime
    - A32NX_MCDU_CLR_Pressed
    - A32NX_MCDU_L_BRIGHTNESS
    - A32NX_MCDU_R_BRIGHTNESS
    - A32NX_MCDU_MASK_OPACITY

    - A32NX_MCDU_PUSH_ANIM_1_0
    - A32NX_MCDU_PUSH_ANIM_1_1
    - A32NX_MCDU_PUSH_ANIM_1_2
    - A32NX_MCDU_PUSH_ANIM_1_3
    - A32NX_MCDU_PUSH_ANIM_1_4
    - A32NX_MCDU_PUSH_ANIM_1_5
    - A32NX_MCDU_PUSH_ANIM_1_6
    - A32NX_MCDU_PUSH_ANIM_1_7
    - A32NX_MCDU_PUSH_ANIM_1_8
    - A32NX_MCDU_PUSH_ANIM_1_9
    - A32NX_MCDU_PUSH_ANIM_1_A
    - A32NX_MCDU_PUSH_ANIM_1_AIRPORT
    - A32NX_MCDU_PUSH_ANIM_1_ATC
    - A32NX_MCDU_PUSH_ANIM_1_B
    - A32NX_MCDU_PUSH_ANIM_1_C
    - A32NX_MCDU_PUSH_ANIM_1_CLR
    - A32NX_MCDU_PUSH_ANIM_1_D
    - A32NX_MCDU_PUSH_ANIM_1_DARROW
    - A32NX_MCDU_PUSH_ANIM_1_DATA
    - A32NX_MCDU_PUSH_ANIM_1_DIR
    - A32NX_MCDU_PUSH_ANIM_1_DOT
    - A32NX_MCDU_PUSH_ANIM_1_E
    - A32NX_MCDU_PUSH_ANIM_1_F
    - A32NX_MCDU_PUSH_ANIM_1_FPLN
    - A32NX_MCDU_PUSH_ANIM_1_FUEL
    - A32NX_MCDU_PUSH_ANIM_1_G
    - A32NX_MCDU_PUSH_ANIM_1_H
    - A32NX_MCDU_PUSH_ANIM_1_I
    - A32NX_MCDU_PUSH_ANIM_1_INIT
    - A32NX_MCDU_PUSH_ANIM_1_J
    - A32NX_MCDU_PUSH_ANIM_1_K
    - A32NX_MCDU_PUSH_ANIM_1_L
    - A32NX_MCDU_PUSH_ANIM_1_L1
    - A32NX_MCDU_PUSH_ANIM_1_L2
    - A32NX_MCDU_PUSH_ANIM_1_L3
    - A32NX_MCDU_PUSH_ANIM_1_L4
    - A32NX_MCDU_PUSH_ANIM_1_L5
    - A32NX_MCDU_PUSH_ANIM_1_L6
    - A32NX_MCDU_PUSH_ANIM_1_LARROW
    - A32NX_MCDU_PUSH_ANIM_1_M
    - A32NX_MCDU_PUSH_ANIM_1_MENU
    - A32NX_MCDU_PUSH_ANIM_1_N
    - A32NX_MCDU_PUSH_ANIM_1_O
    - A32NX_MCDU_PUSH_ANIM_1_OVFY
    - A32NX_MCDU_PUSH_ANIM_1_P
    - A32NX_MCDU_PUSH_ANIM_1_PERF
    - A32NX_MCDU_PUSH_ANIM_1_PLUSMINUS
    - A32NX_MCDU_PUSH_ANIM_1_PROG
    - A32NX_MCDU_PUSH_ANIM_1_Q
    - A32NX_MCDU_PUSH_ANIM_1_R
    - A32NX_MCDU_PUSH_ANIM_1_R1
    - A32NX_MCDU_PUSH_ANIM_1_R2
    - A32NX_MCDU_PUSH_ANIM_1_R3
    - A32NX_MCDU_PUSH_ANIM_1_R4
    - A32NX_MCDU_PUSH_ANIM_1_R5
    - A32NX_MCDU_PUSH_ANIM_1_R6
    - A32NX_MCDU_PUSH_ANIM_1_RAD
    - A32NX_MCDU_PUSH_ANIM_1_RARROW
    - A32NX_MCDU_PUSH_ANIM_1_S
    - A32NX_MCDU_PUSH_ANIM_1_SEC
    - A32NX_MCDU_PUSH_ANIM_1_SLASH
    - A32NX_MCDU_PUSH_ANIM_1_SP
    - A32NX_MCDU_PUSH_ANIM_1_T
    - A32NX_MCDU_PUSH_ANIM_1_U
    - A32NX_MCDU_PUSH_ANIM_1_UARROW
    - A32NX_MCDU_PUSH_ANIM_1_V
    - A32NX_MCDU_PUSH_ANIM_1_W
    - A32NX_MCDU_PUSH_ANIM_1_X
    - A32NX_MCDU_PUSH_ANIM_1_Y
    - A32NX_MCDU_PUSH_ANIM_1_Z
    - A32NX_MCDU_PUSH_ANIM_2_0
    - A32NX_MCDU_PUSH_ANIM_2_1
    - A32NX_MCDU_PUSH_ANIM_2_2
    - A32NX_MCDU_PUSH_ANIM_2_3
    - A32NX_MCDU_PUSH_ANIM_2_4
    - A32NX_MCDU_PUSH_ANIM_2_5
    - A32NX_MCDU_PUSH_ANIM_2_6
    - A32NX_MCDU_PUSH_ANIM_2_7
    - A32NX_MCDU_PUSH_ANIM_2_8
    - A32NX_MCDU_PUSH_ANIM_2_9
    - A32NX_MCDU_PUSH_ANIM_2_A
    - A32NX_MCDU_PUSH_ANIM_2_AIRPORT
    - A32NX_MCDU_PUSH_ANIM_2_ATC
    - A32NX_MCDU_PUSH_ANIM_2_B
    - A32NX_MCDU_PUSH_ANIM_2_C
    - A32NX_MCDU_PUSH_ANIM_2_CLR
    - A32NX_MCDU_PUSH_ANIM_2_D
    - A32NX_MCDU_PUSH_ANIM_2_DARROW
    - A32NX_MCDU_PUSH_ANIM_2_DATA
    - A32NX_MCDU_PUSH_ANIM_2_DIR
    - A32NX_MCDU_PUSH_ANIM_2_DOT
    - A32NX_MCDU_PUSH_ANIM_2_E
    - A32NX_MCDU_PUSH_ANIM_2_F
    - A32NX_MCDU_PUSH_ANIM_2_FPLN
    - A32NX_MCDU_PUSH_ANIM_2_FUEL
    - A32NX_MCDU_PUSH_ANIM_2_G
    - A32NX_MCDU_PUSH_ANIM_2_H
    - A32NX_MCDU_PUSH_ANIM_2_I
    - A32NX_MCDU_PUSH_ANIM_2_INIT
    - A32NX_MCDU_PUSH_ANIM_2_J
    - A32NX_MCDU_PUSH_ANIM_2_K
    - A32NX_MCDU_PUSH_ANIM_2_L
    - A32NX_MCDU_PUSH_ANIM_2_L1
    - A32NX_MCDU_PUSH_ANIM_2_L2
    - A32NX_MCDU_PUSH_ANIM_2_L3
    - A32NX_MCDU_PUSH_ANIM_2_L4
    - A32NX_MCDU_PUSH_ANIM_2_L5
    - A32NX_MCDU_PUSH_ANIM_2_L6
    - A32NX_MCDU_PUSH_ANIM_2_LARROW
    - A32NX_MCDU_PUSH_ANIM_2_M
    - A32NX_MCDU_PUSH_ANIM_2_MENU
    - A32NX_MCDU_PUSH_ANIM_2_N
    - A32NX_MCDU_PUSH_ANIM_2_O
    - A32NX_MCDU_PUSH_ANIM_2_OVFY
    - A32NX_MCDU_PUSH_ANIM_2_P
    - A32NX_MCDU_PUSH_ANIM_2_PERF
    - A32NX_MCDU_PUSH_ANIM_2_PLUSMINUS
    - A32NX_MCDU_PUSH_ANIM_2_PROG
    - A32NX_MCDU_PUSH_ANIM_2_Q
    - A32NX_MCDU_PUSH_ANIM_2_R
    - A32NX_MCDU_PUSH_ANIM_2_R1
    - A32NX_MCDU_PUSH_ANIM_2_R2
    - A32NX_MCDU_PUSH_ANIM_2_R3
    - A32NX_MCDU_PUSH_ANIM_2_R4
    - A32NX_MCDU_PUSH_ANIM_2_R5
    - A32NX_MCDU_PUSH_ANIM_2_R6
    - A32NX_MCDU_PUSH_ANIM_2_RAD
    - A32NX_MCDU_PUSH_ANIM_2_RARROW
    - A32NX_MCDU_PUSH_ANIM_2_S
    - A32NX_MCDU_PUSH_ANIM_2_SEC
    - A32NX_MCDU_PUSH_ANIM_2_SLASH
    - A32NX_MCDU_PUSH_ANIM_2_SP
    - A32NX_MCDU_PUSH_ANIM_2_T
    - A32NX_MCDU_PUSH_ANIM_2_U
    - A32NX_MCDU_PUSH_ANIM_2_UARROW
    - A32NX_MCDU_PUSH_ANIM_2_V
    - A32NX_MCDU_PUSH_ANIM_2_W
    - A32NX_MCDU_PUSH_ANIM_2_X
    - A32NX_MCDU_PUSH_ANIM_2_Y
    - A32NX_MCDU_PUSH_ANIM_2_Z


### Switching Panel

Flight Deck: [Switching Panel](flight-deck/pedestal/switching.md)

| Function    | API Usage                        | Values | Read/Write | Type        | Remark                |
|:------------|:---------------------------------|:-------|:-----------|:------------|:----------------------|
| ATT HDG     | A32NX_ATT_HDG_SWITCHING_KNOB     | 0..2   | R/W        | Custom LVAR | 0=CAPT, 1=NORM, 2=F/O |
|             |                                  |        |            |             |                       |
| AIR DATA    | A32NX_AIR_DATA_SWITCHING_KNOB    | 0..2   | R/W        | Custom LVAR | 0=CAPT, 1=NORM, 2=F/O |
|             |                                  |        |            |             |                       |
| EIS DMC     | A32NX_EIS_DMC_SWITCHING_KNOB     | 0..2   | R/W        | Custom LVAR | 0=CAPT, 1=NORM, 2=F/O |
|             |                                  |        |            |             |                       |
| ECAM/NA XFR | A32NX_ECAM_ND_XFR_SWITCHING_KNOB | 0..2   | R/W        | Custom LVAR | 0=CAPT, 1=NORM, 2=F/O |

### ECAM Control Panel

Flight Deck: [ECAM Control Panel](flight-deck/pedestal/ecam-control.md)

| Function              | API Usage                        | Values | Read/Write | Type        | Remark                                                                     |
|:----------------------|:---------------------------------|:-------|:-----------|:------------|:---------------------------------------------------------------------------|
| Upper Display         | LIGHT POTENTIOMETER:92           | 0..100 | R/W        | MSFS VAR    |                                                                            |
|                       |                                  |        |            |             |                                                                            |
| Lower Display         | LIGHT POTENTIOMETER:93           | 0..100 | R/W        | MSFS VAR    |                                                                            |
|                       |                                  |        |            |             |                                                                            |
| ECAM SD Page button   | A32NX_ECAM_SD_CURRENT_PAGE_INDEX | -1..12 | R          | Custom LVAR | See below. <br/>~~(changes button, but does not switch ECAM page)~~        |
|                       |                                  |        |            |             |                                                                            |
| Left CLR  button      | A32NX_BTN_CLR                    | 0 \| 1 | R/W        | Custom LVAR |                                                                            |
|                       |                                  |        |            |             |                                                                            |
| Right CLR button      | A32NX_BTN_CLR2                   | 0 \| 1 | R/W        | Custom LVAR |                                                                            |
|                       |                                  |        |            |             |                                                                            |
| RCL button            | A32NX_BTN_RCL                    | 0 \| 1 | R/W        | Custom LVAR |                                                                            |
|                       |                                  |        |            |             |                                                                            |
| T.O. CONFIG button    | A32NX_BTN_TOCONFIG               | 0 \| 1 | R/W        | Custom LVAR |                                                                            |
|                       |                                  |        |            |             |                                                                            |
| EMER CANC button      | A32NX_BTN_EMERCANC               | 0 \| 1 | R/W        | Custom LVAR |                                                                            |
|                       |                                  |        |            |             |                                                                            |
| Page to show on error | A32NX_ECAM_SFAIL                 | -1..12 | R          | Custom LVAR | See below. <br/>Has the page index of the page called by the error message |

A32NX_ECAM_SD_CURRENT_PAGE_INDEX:

<style>
.md-typeset li {
    line-height: 1.0
}
</style>

- -1  = none
- 0  = ENG
- 1  = BLEED
- 2  = PRESS
- 3  = ELEC
- 4  = HYD
- 5  = FUEL
- 6  = APU
- 7  = COND
- 8  = DOOR
- 9  = WHEEL
- 10 = F-CTL
- 11 = STS
- 12 = CRUISE

### Thrust Lever and Trim Wheel

Flight Deck: [Thrust Lever Panel](flight-deck/pedestal/thrust-elev-trim.md)

| Function              | API Usage                   | Values        | Read/Write | Type             | Remark  |
|:----------------------|:----------------------------|:--------------|:-----------|:-----------------|:--------|
| Throttle 1 Axis       | THROTTLE1_AXIS_SET_EX1      | -16383..16384 | -          | MSFS EVENT       |         |
|                       |                             |               |            |                  |         |
| Throttle 1 Axis       | THROTTLE2_AXIS_SET_EX1      | -16383..16384 | -          | MSFS EVENT       |         |
|                       |                             |               |            |                  |         |
| AUTO THRUST DISENGAGE | AUTO_THROTTLE_ARM           | -             | -          | SIMCONNECT EVENT | Toggles |
|                       | A32NX_AUTOTHRUST_DISCONNECT | 0 \| 1        | R          | Custom LVAR      |         |

### RMP

Flight Deck: [RMP Panel](flight-deck/pedestal/rmp.md)

!!! note "The below table shows the API for RMP 1. Replace `1` with `2` or `3` for the other RMPs."

| Function         | API Usage                 | Values           | Read/Write | Type             | Remark                        |
|:-----------------|:--------------------------|:-----------------|:-----------|:-----------------|:------------------------------|
| Active Frequency | COM ACTIVE FREQUENCY:1    | 118.000..136.975 | R/W        | SIMCONNECT VAR   |                               |
|                  |                           |                  |            |                  |                               |
| Stdby Frequency  | COM STANDBY FREQUENCY:1   | 118.000..136.975 | R/W        | SIMCONNECT VAR   |                               |
|                  |                           |                  |            |                  |                               |
| XFER Frequency   | COM1_RADIO_SWAP           | -                | -          | SIMCONNECT EVENT |                               |
|                  |                           |                  |            |                  |                               |
| RMP MODE         | A32NX_RMP_L_SELECTED_MODE | 0..3             | R/W        | Custom LVAR      | 0=SEL, 1=VHF1, 2=VHF2, 3=VHF3 |
|                  |                           |                  |            |                  |                               |
| RMP ON/OFF       | A32NX_RMP_L_TOGGLE_SWITCH | 0 \| 1           | R/W        | Custom LVAR      |                               |
|                  |                           |                  |            |                  |                               |
| Transmit VHF1    | COM TRANSMIT:1            | 0 \| 1           | R          | SIMCONNECT VAR   |                               |
|                  |                           |                  |            |                  |                               |
| Transmit VHF2    | COM TRANSMIT:2            | 0 \| 1           | R          | SIMCONNECT VAR   |                               |
|                  |                           |                  |            |                  |                               |
| Transmit VHF3    | COM TRANSMIT:3            | 0 \| 1           | R          | SIMCONNECT VAR   |                               |

### Lighting Pedestal Captain Side Panel

Flight Deck: [Lighting Pedestal Cpt. Side Panel](flight-deck/pedestal/lighting-capt.md)

| Function      | API Usage              | Values | Read/Write | Type     | Remark       |
|:--------------|:-----------------------|:-------|:-----------|:---------|:-------------|
| FLOOD LT Cpt  | LIGHT POTENTIOMETER:83 | 0..100 | R/W        | MSFS VAR |              |
|               |                        |        |            |          |              |
| INTEG LT      | LIGHT POTENTIOMETER:85 | 0..100 | R/W        | MSFS VAR |              |
|               |                        |        |            |          |              |
| FLOOD LT F.O. | LIGHT POTENTIOMETER:76 | 0..100 | R/W        | MSFS VAR | On F.O. side |

### WX Radar

Flight Deck: [WX Radar Panel](flight-deck/pedestal/radar.md)

| Function   | API Usage                       | Values | Read/Write | Type        | Remark                      |
|:-----------|:--------------------------------|:-------|:-----------|:------------|:----------------------------|
| SYS        | XMLVAR_A320_WEATHERRADAR_SYS    | 0..2   | R/W        | Custom LVAR | 0=1, 1=OFF, 2=2             |
|            |                                 |        |            |             |                             |
| PWS        | A32NX_SWITCH_RADAR_PWS_POSITION | 0 \| 1 | R/W        | Custom LVAR | 0=OFF, 1=AUTO               |
|            |                                 |        |            |             |                             |
| MODE       | XMLVAR_A320_WEATHERRADAR_MODE   | 0..3   | R/W        | Custom LVAR | 0=WX, 1=WX+T, 2=TURB, 3=MAP |
|            |                                 |        |            |             |                             |
| GAIN       | N/A                             |        |            |             |                             |
|            |                                 |        |            |             |                             |
| MULTISCANS | N/A                             |        |            |             |                             |
|            |                                 |        |            |             |                             |
| GCS        | N/A                             |        |            |             |                             |
|            |                                 |        |            |             |                             |
| TILT       | N/A                             |        |            |             |                             |


### ATC-TCAS

Flight Deck: [ATC-TCAS Panel](flight-deck/pedestal/atc-tcas.md)

| Function     | API Usage                          | Values | Read/Write | Type        | Remark                                           |
|:-------------|:-----------------------------------|:-------|:-----------|:------------|:-------------------------------------------------|
| ATC MODE     | TRANSPONDER STATE:1                | 0 \| 4 | R/W        | MSFS VAR    | 0=STBY, 4=AUTO/ON<br/>~~(probably more states)~~ |
|              |                                    |        |            |             |                                                  |
| ATC XPDR 1/2 | N/A                                |        |            |             |                                                  |
|              |                                    |        |            |             |                                                  |
| ALT RPTG     | A32NX_SWITCH_ATC_ALT               | 0..2   | R/W        | Custom LVAR | 0=OFF, 1=?, 2=ON                                 |
|              |                                    |        |            |             |                                                  |
| IDENT        | N/A                                |        |            |             |                                                  |
|              |                                    |        |            |             |                                                  |
| TCAS MODE    | A32NX_SWITCH_TCAS_TRAFFIC_POSITION | 0..3   | R/W        | Custom LVAR | 0=THRT, 1=ALL, 2=ABV, 3=BLW                      |
|              |                                    |        |            |             |                                                  |
| TCAS TRAFFIC | A32NX_SWITCH_TCAS_POSITION         | 0..2   | R/W        | Custom LVAR | 0=STBY, 1=TA, 2=TA/RA                            |

### ENG Panel

Flight Deck: [ENG Panel](flight-deck/pedestal/engine.md)

| Function       | API Usage                    | Values | Read/Write | Type       | Remark                 |
|:---------------|:-----------------------------|:-------|:-----------|:-----------|:-----------------------|
| ENG 1+2 MASTER | FUELSYSTEN_VALVE_OPEN        | 1 \| 2 | -          | MSFS EVENT | Activates the switch   |
|                | FUELSYSTEN_VALVE_CLOSE       | 1 \| 2 | -          | MSFS EVENT | Deactivates the switch |
|                | FUELSYSTEM VALVE SWITCH:1    | 0 \| 1 | R          | MSFS VAR   |                        |
|                | FUELSYSTEM VALVE SWITCH:2    | 0 \| 1 | R          | MSFS VAR   |                        |
|                |                              |        |            |            |                        |
| MODE           | TURBINE_IGNITION_SWITCH_SET1 | 0..2   | -          | MSFS EVENT | 0=CRANK, 1=NORM, 2=IGN |
|                | TURBINE_IGNITION_SWITCH_SET2 | 0..2   | -          | MSFS EVENT | 0=CRANK, 1=NORM, 2=IGN |
|                | TURB ENG IGNITION SWITCH EX1 | 0..2   | R/W        | MSFS VAR   | 0=CRANK, 1=NORM, 2=IGN |
|                | TURB ENG IGNITION SWITCH EX2 | 0..2   | R/W        | MSFS VAR   | 0=CRANK, 1=NORM, 2=IGN |
|                |                              |        |            |            |                        |
| FIRE 1 + 2     | N/A                          |        |            |            |                        |

### Speed Brake

Flight Deck: [Speed Brake Panel](flight-deck/pedestal/speedbrake.md)

| Function         | API Usage                      | Values   | Read/Write | Type             | Remark                           |
|:-----------------|:-------------------------------|:---------|:-----------|:-----------------|:---------------------------------|
| SPEED BRAKE AXIS | SPOILER SET                    | 0..16384 | -          | SIMCONNECT EVENT |                                  |
|                  | A32NX_SPOILERS_HANDLE_POSITION | 0.0..1.0 | R          | Custom LVAR      | (add. SIMCONNECT VARS available) |
|                  |                                |          |            |                  |                                  |
| GND SPOILER ARM  | SPOILERS_ARM_TOGGLE            | -        | -          | SIMCONNECT EVENT |                                  |
|                  | SPOILERS ARMED                 | 0 \| 1   | R/W        | SIMCONNECT VAR   |                                  |
|                  | A32NX_SPOILER_ARMED            | 0 \| 1   | R          | Custom LVAR         |                                  |

### Flaps

Flight Deck: [Speed Brake Panel](flight-deck/pedestal/flaps.md)

| Function   | API Usage                  | Values   | Read/Write | Type             | Remark                        |
|:-----------|:---------------------------|:---------|:-----------|:-----------------|:------------------------------|
| Flaps Axis | FLAPS_SET                  | 0..16384 | -          | SIMCONNECT EVENT | 0=FLAPS UP, 16384=FLAPS FULL  |
|            | FLAPS_UP                   | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_1                    | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_2                    | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_3                    | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_DOWN                 | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_INC                  | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_DEC                  | -        | -          | SIMCONNECT EVENT |                               |
|            |                            |          |            |                  |                               |
|            | A32NX_FLAPS_HANDLE_INDEX   | 0..4     | R          | Custom LVAR      | 0=UP, 4=FULL                  |
|            | A32NX_FLAPS_HANDLE_PERCENT | 0.0..1.0 | R          | Custom LVAR      | 0.0=UP, 1.0=FULL (0.25 steps) |
|            |                            |          |            |                  |                               |
|            | FLAPS HANDLE INDEX         | 0..5     | R          | SIMCONNECT VAR   | 0=UP, 5=FULL, 1 is not used.  |
|            | FLAPS HANDLE PERCENT       | 0.0..1.0 | R          | SIMCONNECT VAR   | 0.0=UP, 1.0=FULL (0.2 steps)  |

### Parking Brake

Flight Deck: [Parking Brake Panel](flight-deck/pedestal/parking-brake.md)

| Function      | API Usage                  | Values | Read/Write | Type        | Remark |
|:--------------|:---------------------------|:-------|:-----------|:------------|:-------|
| PARKING BRAKE | A32NX_PARK_BRAKE_LEVER_POS | 0 \| 1 | R/W        | Custom LVAR |        |

### Rudder Trim

Flight Deck: [Rudder Trim Panel](flight-deck/pedestal/rudder-trim.md)

| Function | API Usage         | Values        | Read/Write | Type             | Remark                                                                         |
|:---------|:------------------|:--------------|:-----------|:-----------------|:-------------------------------------------------------------------------------|
| Display  | RUDDER TRIM PCT   | -1.0..1.0     | R          | SIMCONNECT VAR   | -1.0=20° left, 1.0=20° right                                                   |
|          | RUDDER TRIM       | -0.35..0.35   | R          | SIMCONNECT VAR   | Radians: 0.3490×180°/π = 19.99°                                                |
|          |                   |               |            |                  |                                                                                |
| RESET    | RUDDER TRIM SET   | -16383..16384 | .          | SIMCONNECT EVENT |                                                                                |
|          |                   |               |            |                  |                                                                                |
| RUD TRIM | XMLVAR_RUDDERTRIM | 0 \| 2        | R/W        | Custom LVAR      | ~~Knob jumps back. Needs to be set repeatately until target value is reached~~ |

### Cockpit Door

Flight Deck: [Cockpit Door Panel](flight-deck/pedestal/cockpit-door.md)

| Function     | API Usage                 | Values | Read/Write | Type        | Remark |
|:-------------|:--------------------------|:-------|:-----------|:------------|:-------|
| COCKPIT DOOR | A32NX_COCKPIT_DOOR_LOCKED | 0 \| 1 | R/W        | Custom LVAR |        |
|              |                           |        |            |             |        |
| VIDEO        | PUSH_DOORPANEL_VIDEO      | 0 \| 1 | R/W        | Custom LVAR |        |

## Flight Stick

| Function             | API Usage                 | Values        | Read/Write | Type             | Remark                         |
|:---------------------|:--------------------------|:--------------|:-----------|:-----------------|:-------------------------------|
| Aileron              | AILERON_SET               | -16383..16384 | -          | SIMCONNECT EVENT |                                |
|                      | AILERON POSITION          | -1.0..1.0     | R          | SIMCONNECT VAR   |                                |
|                      |                           |               |            |                  |                                |
| Elevator             | ELEVATOR_SET              | -16383..16384 | -          | SIMCONNECT EVENT |                                |
|                      | ELEVATOR POSITION         | -1.0..1.0     | R          | SIMCONNECT VAR   |                                |
|                      |                           |               |            |                  |                                |
| TAKE OVER pushbutton | A32NX_PRIORITY_TAKEOVER:1 | 0 \| 1        | R          | Custom LVAR      | Causes AP disconnection        |
|                      | A32NX_PRIORITY_TAKEOVER:2 | 0 \| 1        | R          | Custom LVAR      | Causes AP disconnection        |

## Rudder Pedals

| Function | API Usage                      | Values        | Read/Write | Type             | Remark |
|:---------|:-------------------------------|:--------------|:-----------|:-----------------|:-------|
| Rudder   | RUDDER_SET                     | -16383..16384 | -          | SIMCONNECT EVENT |        |
|          | RUDDER POSITION                | -1.0..1.0     | R          | SIMCONNECT VAR   |        |
|          |                                |               |            |                  |        |
| Brakes   | A32NX_LEFT_BRAKE_PEDAL_INPUT   | 0..100        | R          | Custom LVAR      |        |
|          | A32NX_RIGHT_BRAKE_PEDAL_INPUT  | 1..100        | R          | Custom LVAR      |        |
|          | SIMCONNECT:AXIS_LEFT_BRAKE_SET | -16383..16384 | -          | SIMCONNECT EVENT |        |
|          | SIMCONNECT:AXIS_LEFT_BRAKE_SET | -16383..16384 | -          | SIMCONNECT EVENT |        |
