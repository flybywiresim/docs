# Selected Vertical Modes

Selected modes guide the aircraft according to target values that the pilot selects and the
FCU windows display.

Selected modes disregard all altitude constraints.

## OP CLB (Open Climb)
The OPEN CLB mode uses the AP/FD pitch mode to maintain a SPD/MACH (selected or managed) while the Autothrust (if
active) maintains maximum climb thrust.

When OPEN CLB is engaged, the target speed/mach is maintained by adjusting the pitch with the
elevator, whereas thrust is maintained either by the A/THR, or manually by the flight crew. Speed
target may either be selected or managed.

The OPEN CLB mode disregards all altitude constraints up to the FCU selected altitude.

OPEN CLB mode can be engaged when:

- the aircraft has been in flight for more than 5 seconds
- LAND mode is not engaged
- the altitude selected in the FCU is higher than the present altitude

It is activated when:

- the flight crew pulls the FCU ALT knob
- guidance reverts to speed protection
- acceleration altitude is reached with CLB armed and lateral navigation (NAV) not engaged

## OP DES (Open Descent)
The OPEN DES mode maintains a SPD/MACH (selected or managed) with the AP/FD pitch mode while
Autothrust (if active) maintains IDLE thrust. It is not to be used for final approach.

When OPEN DES is engaged, pitch control maintains the target speed/Mach number, and Autothrust
maintains idle thrust (or the flight crew maintains it manually). The speed target may be either
selected or managed.

The OPEN DES mode disregards all altitude constraints.

OP DES mode can be engaged when:

- the aircraft has been in flight for more than 5 seconds
- LAND mode is not engaged
- the altitude selected in the FCU is lower than the present altitude

It is activated when:
- the flight crew pulls the FCU ALT knob
- Selecting a manual speed when EXPEDITE mode is engaged.

## V/S and FPA (Vertical Speed and Flight Path Angle)
The V/S-FPA mode acquires and holds the vertical speed or the flight path angle displayed
in the V/S-FPA window of the FCU. The HDG V/S-TRK FPA pb on the FCU allows the flight crew to select vertical speed
or flight path angle to be used.

The FMGC pitch mode guides the aircraft to the target V/S or FPA. The corresponding A/THR mode is SPEED or MACH. The
FMA displays V/S (FPA).

{--

The V/S (FPA) guidance has priority over the speed guidance. If the selected target V/S or FPA is too high (relative
to the current thrust condition and speed), the FMGC will steer the aircraft to the target V/S or FPA, but the
aircraft will also accelerate or decelerate.

When the speed reaches its authorized limit, V/S or FPA automatically decreases to maintain the
minimum (or maximum) speed limit.

--}

V/S-FPA can be manually engaged when:

- the aircraft has been in flight for more than 5 seconds
- the AP or FD are activated when they have been off
- changing target altitude by >250ft when in ALT^*^ mode
- selecting a higher altitude when in any descent mode
- selecting a lower altitude when in any climb mode

It engages automatically when:
- no other vertical mode is engaged after 5 seconds after lift off
  ‐ loss of G/S* or G/S mode
  ‐ loss of FINAL mode
  ‐ loss of LOC* or LOC mode
  ‐ loss of NAV mode when DES mode is engaged
  ‐ loss of vertical flight path in DES mode
  ‐ TCAS mode disengagement.

To immediately level off the aircraft the flight crew can push the FCU V/S-FPA knob or set the V/S-FPA to 0.

Note: If AP is engaged while a V/S is selected with only FD ON, the V/S will synchronise on the
current aircraft V/S.

## EXP (Expedite)
Expedite mode is used in climb or descent to reach the desired altitude with the
maximum vertical gradient.

When the aircraft is in EXP CLB, the target speed is Green Dot, which is maintained with pitch control. If
Autothrust is active it sets the thrust at CLB THRUST automatically.

When the aircraft is in EXP DES, the target speed is 340 kt or M 0.8 which is maintained with pitch control.
If Autothrust is active it sets the thrust at IDLE automatically.

When EXPEDITE is engaged, the system disregards speed constraints (SPD CSTR), altitude constraints (ALT CSTR), and
speed limits (SPD LIM).

EXPEDITE can be engaged when
‐ the aircraft has been in flight for more than 5 s
‐ managed speed is available.

It is engaged manually only when
‐ the FCU selected altitude is higher than present altitude, EXP CLB mode engages
‐ the FCU selected altitude is lower than present altitude, EXP DES mode engages

