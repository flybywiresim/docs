# flyPad Ground

## Ground Service

This page allows managing ground operation similar to the in-sim ATC ground services but without having to use the in-sim ATC.

It also has more and better features than the default sim ground services.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypad/flypad-ground.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.3%; top:  8.3%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 16.5%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 24.7%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.3%; top: 32.8%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 41.0%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.3%; top: 49.3%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 57.5%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 88.0%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Settings</span></div></a>
</div>

## Usage

### Pax

When standing at a gate this connects and disconnects the gate's jetway if a jetway is available at the current gate.

### Door Fwd

Opens and closes the forward door.

### Baggage

Calls the baggage service if available at the current airport and gate. Baggage service will open the cargo door, load baggage and then close the cargo door automatically.

### Ext. Power

Calls a ground power unit (GPU) if available at the current airport and gate or stand. This can be used if there is no external power available.

### Fuel

Calls the fuel truck if available at the current airport. It will take quite a while until the fuel truck while arrive. 5-10 minutes is not unusual. When the fuel truck arrives the MSFS fuel page appears.

!!! warning ""
    We recommend to not use the MSFS Fuel Page with the FlyByWire A32NX as fuel and payload should be loaded through the MCDU ([MCDU Load Fuel & Payload](../../../pilots-corner/beginner-guide/preparing-mcdu.md#load-fuel-and-payload)).

### Door Aft

Opens and closes the aft door.

### Catering

Calls the catering service if available at the current airport and gate. The catering service will open the aft door and automatically closes it after it has virtually supplied the aircraft.

### Call Tug

Calls the pushback tug to be connected to the aircraft. The button will become green if the pushback tug is connected to the aircraft. At some airports the pushback tug might not be visible (MSFS issue) but it will still be possible to pushback the aircraft.

To disconnect the pushback tug press this button again and the button turns blue again.

### Stop (hand symbol)

Press this button to stop any movement of the pushback tug.

### &ldca; (left)

Use this button to push the aircraft backwards and left.

### &darr; (straight)

Use this button to push the aircraft straight backwards.

### &rdca; (right)

Use this button to push the aircraft backwards and right.
