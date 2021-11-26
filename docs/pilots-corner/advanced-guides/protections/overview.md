# Normal Law Protections in the A320

The A320 has various flight envelope protections which protect the aircraft from entering certain critical situations while Normal Law is active.

The guides in this section shall cover some of the main envelope protections of the A320's Normal Law.

??? info "Control Laws"
    The fly-by-wire principle of the A320 uses several "Laws" on how to control the flight control surfaces in relation to the pilot's input to side stick.

    - Normal Law:
        - normal conditions even after single failure of sensors, electrical system, hydraulic system or flight control computer
    - Alternate Law:
        - activated after certain double (or triple) failures
    - Direct Law:
        - Mainly after double or triple IRS failure
    - Mechanical Backup (after loss of all electrical power):
        - Trim wheel
        - Rudder pedals

    The different laws will support different types of protections and change the relationship between pilot's stick input and flight control interfaces.

##  Envelope Protections Overview:

- [Overspeed Protection](#overspeed-protection)
- [Angle of Attack Protection](#angle-of-attack-protection)
- Manoeuvre Protection
- Attitude Protection
- Windshear Protection
- Low Energy Protection
- Load Alleviation Function (LAF) (only for A320)

## Overspeed Protection

This protections aims to protect the aircraft from overspeed situation exceeding the V~mo~ or M~mo~ speeds (maximum operating speeds in knots or mach).

See also [V-Speeds](../..//beginner-guide/abbreviations.md#v-speeds)

### Indication and warnings

The overspeed limits are shown on the speed band on the PFD as a black and red strip and a pair of green lines.

!!! block ""
    ![Speedband Overspeed Limits](../../assets/advanced-guides/protections/speedband_overspeed.png "Speedband Overspeed Limits"){loading=lazy align=left width=12%}

    - 1: V~max~ = Lowest of V~mo~, M~mo~, V~LE~, V~FE~
    - 2: V~mo~ + 6kt or M~mo~ + 0.01 Overspeed Protection becomes active
    - 3: Current IAS (In Air Speed)
    - 4: Current Mach speed

Overspeed Protection triggers the following warnings

- Continuous repetitive chime
- Master warning light
- Overspeed red message on ECAM
- Red and black strip along the PFD scale

### Protectiive Actions

- Automatic AP disconnection
- When V~mo~ + 6kt or M~mo~ + 0.01 is reached a positive load factor demand automatically applied (pitch up action)
- When full nose-down stick is maintained speed is limited to around V~mo~ + 16kt and M~mo~ + 0.04 (pilot nose-down authority is reduced)

### Recommended Action to Recover

!!! bug "TODO: PILOT INPUT"

- Increase pitch
- Reduce thrust and/or activate A/THR

## Angle of Attack Protection

The Angle of Attack Protection in the A320 is in simple terms a protection against a too high angle of attack and in consequence stalling the aircraft.

??? info "Angle of Attack"
    "The Angle of Attack is the angle at which relative wind meets an Aerofoil. It is the angle formed by the Chord of the aerofoil and the direction of the relative wind or the vector representing the relative motion between the aircraft and the atmosphere."

    Based on the article [Angle of Attack (AOA)](https://skybrary.aero/articles/angle-attack-aoa){target=new}, Source: www.skybrary.aero.

The angle of attack is commonly called &alpha; (alpha) which we also shall use in the following.

### Indication and warnings

!!! block ""
    ![Angle of Attack Protection Speeds](../../assets/advanced-guides/protections/speedband_aoa.png "Angle of Attack Protection Speeds"){loading=lazy align=left width=15%}

    - 1: Green Dot Speed is the best lift-to-drag ratio speed
    - 2: V~LS~ is minimal selectable speed providing an appropriate margin to the stall speed. The autopilot will not go below this speed if autothrust is active.
    - 3: Selected speed in the FCU
    - 4: &alpha;~prot~ limit
        - this speed is maintained when side stick is neutral
        - if sidestick if deflected aft this will eventually activate &alpha;~floor~ protection. See below.
    - 5: &alpha;~max~ is the speed with the maximum angle of attack (AoA) without the aircraft stalling
        - this speed is maintained when side stick is deflected fully aft

!!! block ""
    ![A.FLOOR FMA](../../assets/advanced-guides/protections/alpha-floor-fma.png" A.FLOOR FMA"){loading=lazy align=left width=15%}

    If the &alpha;~floor~ (A.FLOOR) protection is triggered the Autothrust FMA shows this symbol with a flashing amber border.

### Protective Actions

- Automatic AP disconnection / AP cannot be activated
- If &alpha; becomes greater than &alpha;~prot~ then angel of attack wiull become will become proportional to stick deflection. Autotrim will stop which results in a nose-down tendency.
- If &alpha; reaches &alpha;~floor~ the autothrust system will apply go-around thrust.
- &alpha;~max~ cannot be exceeded even with the pilot pulling the stick full backward. In other words the cannot be stalled in Normal Law by the pilot's pitch up stick input.

### Recommended Action to Recover

- Push sidestick forward to reduce pitch and gain speed.

- If in A.FLOOR (&alpha;~floor~) protection see this guide: [A.FLOOR and TOGA LK](afloor.md)
