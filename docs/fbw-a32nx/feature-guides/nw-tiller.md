# Nose Wheel and Tiller Operation

We have introduced a feature for using the tiller to steer the nose wheel independently of the rudder. As Microsoft Flight Simulator does not natively supports this feature yet we had to become creative to build a solution for this.

{--

Therefore this feature is deactivated per default. Before the tiller steering can be used it needs to be mapped to a controller input and activated in the flyPad Settings.

--}

This guides helps to set everything up and will also provide tips how to use it for taxi as this more realistic way of steering needs a bit of practice to master it.

## What is the Tiller

The tiller is the handwheel located next to the sidestick on the side consoles.

![Side Console with Handwheel and Sidestick](../assets/nw-tiller/side-console-handwheel.png "Side Console with Handwheel and Sidestick"){loading=lazy}

This handwheel is used on the ground for turning the nose wheel during taxi. It can turn the nose wheel up to 75° in either direction.

The rudder controls only can turn the nose wheel up to 6° and won't be sufficient for taxi operations.

The turn angle of the nosewheel is speed dependent and the limits to which angle it can be turned follows this graph:

![Nose wheel Steering Speed Reference](../assets/nw-tiller/nosewheel-steering-reference.png "Nose wheel Steering Speed Reference"){loading=lazy}

The nose wheel steering is operative when:

- Yellow pressure system is available and pressurized
- One engine is running
- Main landing gear is on the ground
- `A/SKID and N/W STRG` is ON
- Towing control is on normal position

The tiller has push button which allows to disconnect any rudder orders from the nose wheel.

The ground crew can deactivate the steering system by using a switch in the electrical towing box for towing. The upper ECAM then shows a MEMO on the upper ECAM "N/W STEER DISC" (in green while engines are off, in amber when at least one engine is running).

!!! warning "Microsoft Flight Simulator sometimes has an invisible towing tug attached to the aircraft. The ECAM MEMO helps you recognize this."

## Mapping of the Tiller Axis

### Using an Axis

As Microsoft Flight Simulator does not yet support a separate tiller axis we have used an unused axis to map the movement of you controller to the tiller handwheel.

!!! note "Although MSFS provides the option `SET STEERING` which is unfortunately broken."

We have chosen to use `MIXTURE 4 AXIS (-100% to 100%)` for this.

![MSFS Controller Options Mapping](../assets/nw-tiller/handwheel-controller-mapping.png "MSFS Controller Options Mapping")

Map `MIXTURE 4 AXIS (-100% to 100%)` to the controller axis you want to use for the tiller. It needs to be different from the axis you use for the rudder.

!!! tip "Example"
    If you have a twistable flight stick like the Thrustmaster TCA Sidestick Airbus Edition and you also have rudder pedals you can map the rudder to your hardware pedals (as it should be) and the sidestick's twist axis for the tiller.

If you use externally configured controls using SPAD.neXt, FSUIPC or Axis and Ohs you can use the `SIMCONNECT:AXIS_MIXTURE4_SET` event. The parameter for full left is -16383, for straight it is 0 and for full right it is +16383.

### Using Keyboard or Controller Buttons

As an alternative to mapping an axis you can also map keys from the keyboard or buttons from the controller.

Use these or similar mappings on your controller or keyboard:

![MSFS Controller Options Keyboard Mapping](../assets/nw-tiller/handwheel-keyboard-mapping.png "MSFS Controller Options Keyboard Mapping")

Decrease will turn the tiller and nose wheel to the left.

Increase will turn the tiller and nose wheel to the right.

If you use externally configured controls using SPAD.neXt, FSUIPC or Axis and Ohs you can use the `SIMCONNECT:STEERING_DEC` and `SIMCONNECT:STEERING_INC` events.

### Pedal Disconnect Button

The tiller handwheel has a button to disconnect any input from rudder pedals or autopilot so that only the tiller handwheel itself controls the nose wheel.

Again Microsoft Flight Simulator does not support this directly so we again reused an existing option to map a key or button to this.

The MSFS Controller Option we are using is `TOGGLE WATER RUDDER` and your mapping should look similar to this:

![MSFS Controller Option for Pedals Disconnect](../assets/nw-tiller/handwheel-disconnect-button-mapping.png "MSFS Controller Option for Pedals Disconnect")

!!! warning "This key/button is not used as a toggle! You need to hold the button/key for the disconnect to work!"


## Activating the Feature in the flyPad

To activate the tiller feature you need to go to the flyPad Settings page and enable the `Separate Tiller from Rudder` feature.

![flyPad Settings Sim Options Tiller](../assets/nw-tiller/flypad-settings-simoptions-tiller.png "flyPad Settings Sim Options Tiller")

## Using the Tiller and Rudder

### Taxi

As described above taxiing with the tiller controlling the nose wheel will be different than using the rudder and nose wheel steering before.

The most noticeable change is that steering with the rudder on the ground will only turn the nose wheel up to 6° which will not be sufficient for normal taxi operations and most turns.

The second important change is that you need to operate the tiller steering with foresight and slowly as the nose wheel is turning rather slow. This means you need to start steering earlier and slower to make your turns and also start earlier to end your turn steering.

It is much more important to watch the aircraft ground speed as the nose wheel angle is limited as a function of speed. So make sure to slow down before doing sharp turns.

We recommend to practice this a bit until you get used to it.

!!! tip "We recommend to use an axis for the tiller as keys or buttons are much harder to use for steering the nose wheel."

### Takeoff and Landing

During takeoff and landing you will usually only use the rudder and you need to be aware that this only gives some turning authority over the nose wheel (up to 6°). This is especially critical if you are at a slow speed when the rudder has not enough effect.

## Known Issues

As the currently solution is a workaround of a missing Microsoft Flight Simulator feature there are some small issues in the implementation:

- Full tiller one way and rudder the opposite way can move the steering even without hydraulic power
- Full rudder action can overcome to some extent our system implementation. It is possible to move the nose wheel even with no hydraulic power, as MSFS will turn the wheel even when our internal implementation is not moving at all.

Modifying steering animation so it shows our internal system state will mask those issues and allow for perfect visual behaviour. But it can cause strange plane rotation behaviour when these issues will be triggered.
