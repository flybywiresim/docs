---
hide:
    - navigation
---

# Flight Deck A32NX API

[A320neo Pilot Briefing](index.md){ .md-button }
[Clickable Flight Deck](flight-deck/index.md){ .md-button }

## ELEC Panel

Back to [ELEC Panel](flight-deck/ovhd/elec.md)

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
