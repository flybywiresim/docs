---
hide:
    - navigation
    - toc
---

# Flight Deck Overview

- Clickable overview of the A320neo flight deck.
- Move the mouse over the panels to get the name of the panel.
- Click on the panels to get a more detailed description of that panel (if available yet).

<style>
.imagemap {
    position: relative;
    background-color: rgba(0, 0, 0, .0);
    border: 0px solid yellow;
    display: inline-block;
}
.imagemap .imagemapname {
  visibility: hidden;

  background-color: rgba(0, 0, 0, .7);
  color: yellow;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;

  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
  width: 120px;
  bottom: 100%;
  left: 50%;
  margin-left: -60px; /* Use half of the width (120/2 = 60), to center the tooltip */
}
.imagemap:hover .imagemapname {
    visibility: visible;
}
.imagemap:hover {
    background-color: rgba(255, 0, 0, .25);
    border: 1px solid yellow;
}
</style>

<div style="position: relative;">
    <img src="/assets/a32nx-briefing/Cockpit-Overview-Map.png" style="width: 100%; height: auto;">
    <!-- OVHD AFT -->
    <a title="ELT Panel" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 2.55%; width: 12.5%; height: 1.7%;"><span class="imagemapname">ELT Panel</span></div></a>
    <a title="Cockpit Door Panel" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 4.25%; width: 12.5%; height: 2.1%;"></div></a>
    <a title="CAPT Light" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 9.9%; width: 12.5%; height: 3.3%;"></div></a>
    <a href="#"><div class="imagemap" style="position: absolute; left: 35%; top: 0%; width: 30.3%; height: 18%;"><span class="imagemapname">Circuit Breaker Panel</span></div></a>
    <a title="Pedestal Light" href="#"><div class="imagemap" style="position: absolute; left: 35%; top: 18%; width: 30.3%; height: 4.7%;"></div></a>
    <a title="Maintenance Panel" href="#"><div class="imagemap" style="position: absolute; left: 65.3%; top: 0%; width: 12.5%; height: 8%;"></div></a>
    <a title="F.O. Light" href="#"><div class="imagemap" style="position: absolute; left: 65.3%; top: 15.3%; width: 12.5%; height: 3.4%;"></div></a>
    <a title="FMS Load Panel" href="#"><div class="imagemap" style="position: absolute; left: 65.3%; top: 18.6%; width: 12.5%; height: 2.2%;"></div></a>
    <!-- OVHD FWD -->
    <a title="PA and Cockpit Door Video" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 23.8%; width: 12.5%; height: 1.7%;"></div></a>
    <a title="ADIRS Panel" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 25.5%; width: 12.6%; height: 4.5%;"></div></a>
    <a title="Flight Control Panel Left" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 31.2%; width: 12.6%; height: 1.7%;"></div></a>
    <a title="Evacuation Panel" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 32.9%; width: 12.6%; height: 1.6%;"></div></a>
    <a title="Emergency Electric Power Panel" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 34.5%; width: 12.6%; height: 1.7%;"></div></a>
    <a title="Ground Proximity Warning Panel" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 36.2%; width: 12.6%; height: 1.5%;"></div></a>
    <a title="Voice Recoder Panel" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 37.7%; width: 12.6%; height: 1.3%;"></div></a>
    <a title="Oxygen Panel" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 39%; width: 12.6%; height: 1.5%;"></div></a>
    <a title="Calls Panel" href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 40.5%; width: 12.6%; height: 1.45%;"></div></a>
    <a title="Wiper Panel Capt." href="#"><div class="imagemap" style="position: absolute; left: 22.5%; top: 41.95%; width: 12.6%; height: 2.2%;"></div></a>
    <a title="Fire Control Panel" href="/a32nx-briefing/ovhd/fire/"><div class="imagemap" style="position: absolute; left: 35.1%; top: 25.7%; width: 30%; height: 2.7%;"></div></a>
    <a title="Hydraulic Control Panel" href="/a32nx-briefing/ovhd/hyd/"><div class="imagemap" style="position: absolute; left: 35.1%; top: 28.4%; width: 30%; height: 2.3%;"></div></a>
    <a title="Fuel Control Panel" href="/a32nx-briefing/ovhd/fuel/"><div class="imagemap" style="position: absolute; left: 35.1%; top: 30.7%; width: 30%; height: 2.2%;"></div></a>
    <a title="Electricity Control Panel" href="#"><div class="imagemap" style="position: absolute; left: 35.1%; top: 32.9%; width: 30%; height: 3.6%;"></div></a>
    <a title="Air Condition Control Panel" href="#"><div class="imagemap" style="position: absolute; left: 35.1%; top: 36.5%; width: 30%; height: 3.9%;"></div></a>
    <a title="Anti Ice Control Panel" href="#"><div class="imagemap" style="position: absolute; left: 35.1%; top: 40.4%; width: 17.2%; height: 1.7%;"></div></a>
    <a title="Cabin Pressure Control Panel" href="#"><div class="imagemap" style="position: absolute; left: 52.3%; top: 40.4%; width: 12.8%; height: 1.7%;"></div></a>
    <a title="External Lights Panel" href="#"><div class="imagemap" style="position: absolute; left: 35.1%; top: 42.1%; width: 13.3%; height: 3.2%;"></div></a>
    <a title="APU Panel" href="#"><div class="imagemap" style="position: absolute; left: 48.4%; top: 42.1%; width: 3.2%; height: 3.2%;"></div></a>
    <a title="Internal Lighting Panel" href="#"><div class="imagemap" style="position: absolute; left: 51.6%; top: 42.1%; width: 13.5%; height: 1.4%;"></div></a>
    <a title="Sign Panel" href="#"><div class="imagemap" style="position: absolute; left: 51.6%; top: 43.5%; width: 13.5%; height: 1.6%;"></div></a>
    <a title="3rd Audio Control Panel" href="#"><div class="imagemap" style="position: absolute; left: 65.1%; top: 23.3%; width: 12.6%; height: 3.2%;"></div></a>
    <a title="Flight Control Panel Right" href="#"><div class="imagemap" style="position: absolute; left: 65.1%; top: 33%; width: 12.6%; height: 1.7%;"></div></a>
    <a title="Cargo Ventilation Panel" href="#"><div class="imagemap" style="position: absolute; left: 65.1%; top: 34.7%; width: 12.6%; height: 2.4%;"></div></a>
    <a title="Cargo Smoke Panel" href="#"><div class="imagemap" style="position: absolute; left: 65.1%; top: 37.1%; width: 12.6%; height: 1.65%;"></div></a>
    <a title="Ventilation Panel" href="#"><div class="imagemap" style="position: absolute; left: 65.1%; top: 38.75%; width: 12.6%; height: 1.6%;"></div></a>
    <a title="Engine Manual Start and N1 Mode Panel" href="#"><div class="imagemap" style="position: absolute; left: 65.1%; top: 40.3%; width: 12.6%; height: 1.75%;"></div></a>
    <a title="Wiper Panel F.O." href="#"><div class="imagemap" style="position: absolute; left: 65.1%; top: 42%; width: 12.6%; height: 2.2%;"></div></a>
    <!-- Flight Instruments and Glareshield -->
    <a title="Flight Control Unit" href="/a32nx-briefing/glareshield/fcu/"><div class="imagemap" style="position: absolute; left: 41.5%; top: 46.5%; width: 17%; height: 3.7%;"></div></a>
    <a title="EFIS Control Unit Capt." href="/a32nx-briefing/glareshield/efis_control/"><div class="imagemap" style="position: absolute; left: 31%; top: 47%; width: 10.5%; height: 3.2%;"></div></a>
    <a title="EFIS Control Unit F.O." href="/a32nx-briefing/glareshield/efis_control/"><div class="imagemap" style="position: absolute; left: 58.5%; top: 47%; width: 10.5%; height: 3.2%;"></div></a>
    <a title="Alarms and Warnings Capt." href="/a32nx-briefing/glareshield/warning/"><div class="imagemap" style="position: absolute; left: 0%; top: 47.5%; width: 31%; height: 3.2%;"></div></a>
    <a title="Alarms and Warnings F.O." href="/a32nx-briefing/glareshield/warning/"><div class="imagemap" style="position: absolute; left: 69%; top: 47.5%; width: 31%; height: 3.2%;"></div></a>
    <a title="EFIS Instruments Capt." href="#"><div class="imagemap" style="position: absolute; left: 8.5%; top: 51.5%; width: 27.5%; height: 5.5%;"></div></a>
    <a title="EFIS Instruments F.O." href="#"><div class="imagemap" style="position: absolute; left: 64%; top: 51.5%; width: 27.5%; height: 5.5%;"></div></a>
    <a title="StdBy Instruments" href="#"><div class="imagemap" style="position: absolute; left: 36%; top: 51.2%; width: 9%; height: 10.5%;"></div></a>
    <a title="ECAM" href="#"><div class="imagemap" style="position: absolute; left: 45%; top: 51.2%; width: 11%; height: 10.5%;"></div></a>
    <a title="Aurobrake and Gear" href="#"><div class="imagemap" style="position: absolute; left: 56%; top: 51.2%; width: 8%; height: 10.5%;"></div></a>
    <!-- Pedestal -->
    <a title="Switching Panel" href="#"><div class="imagemap" style="position: absolute; left: 41.2%; top: 62.5%; width: 17.6%; height: 3.2%;"></div></a>
    <a title="ECAM Control Panel" href="#"><div class="imagemap" style="position: absolute; left: 41.2%; top: 65.7%; width: 17.6%; height: 3.2%;"></div></a>
    <a title="MCDU Capt." href="#"><div class="imagemap" style="position: absolute; left: 28.9%; top: 62.5%; width: 12.3%; height: 9.9%;"></div></a>
    <a title="MCDU F.O." href="#"><div class="imagemap" style="position: absolute; left: 58.8%; top: 62.5%; width: 12.3%; height: 9.9%;"></div></a>
    <a title="RMP and Audio Control Capt." href="#"><div class="imagemap" style="position: absolute; left: 28.9%; top: 72.4%; width: 12.3%; height: 7.7%;"></div></a>
    <a title="RMP and Audio Control F.O." href="#"><div class="imagemap" style="position: absolute; left: 58.8%; top: 72.4%; width: 12.3%; height: 7.7%;"></div></a>
    <a title="Thrust Lever and Elevation Trim" href="#"><div class="imagemap" style="position: absolute; left: 41.2%; top: 70%; width: 17.6%; height: 11.7%;"></div></a>
    <a title="Engine Panel" href="#"><div class="imagemap" style="position: absolute; left: 45.5%; top: 81.7%; width: 8.9%; height: 3.3%;"></div></a>
    <a title="Lighting Capt." href="#"><div class="imagemap" style="position: absolute; left: 28.9%; top: 80.1%; width: 12.3%; height: 2.2%;"></div></a>
    <a title="Radar Panel" href="#"><div class="imagemap" style="position: absolute; left: 28.9%; top: 82.3%; width: 12.3%; height: 2.8%;"></div></a>
    <a title="Lighting, AIDS, DFDR F.O." href="#"><div class="imagemap" style="position: absolute; left: 58.8%; top: 80.1%; width: 12.3%; height: 2.2%;"></div></a>
    <a title="ATC and TCAS Panel" href="#"><div class="imagemap" style="position: absolute; left: 58.8%; top: 82.3%; width: 12.3%; height: 2.8%;"></div></a>
    <a title="Speed Brake" href="#"><div class="imagemap" style="position: absolute; left: 41.2%; top: 84%; width: 4.3%; height: 4.7%;"></div></a>
    <a title="Flaps" href="#"><div class="imagemap" style="position: absolute; left: 54.4%; top: 84%; width: 4.3%; height: 4.7%;"></div></a>
    <a title="Cockpit Door Panel" href="#"><div class="imagemap" style="position: absolute; left: 34%; top: 88.7%; width: 12.3%; height: 2.6%;"></div></a>
    <a title="Printer" href="#"><div class="imagemap" style="position: absolute; left: 54%; top: 88.7%; width: 12.3%; height: 2.6%;"></div></a>
    <a title="Rudder Trim" href="#"><div class="imagemap" style="position: absolute; left: 46.3%; top: 86.6%; width: 8%; height: 3%;"></div></a>
    <a title="Parking Brake" href="#"><div class="imagemap" style="position: absolute; left: 46.3%; top: 90.5%; width: 8%; height: 3.2%;"></div></a>
    <a title="Gravity Gear Extension" href="#"><div class="imagemap" style="position: absolute; left: 46.3%; top: 93.7%; width: 8%; height: 3.2%;"></div></a>

</div>



