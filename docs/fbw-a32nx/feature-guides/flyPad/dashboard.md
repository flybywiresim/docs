# flyPad Dashboard

<style>
.imagemap {
    position: relative;
    display: inline-block;
    /*background-color: rgba(255, 0, 0, .4);*/
    /*border: 1px solid yellow;*/
}
.imagemap .imagemapname {
  visibility: hidden;

  background-color: rgba(29, 30, 38, 0.9);
  color: rgba(212, 212, 213, 1);
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;
  border: 1px solid #00C2CC;

  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
  width: 200px;
  top: 5%;
  left: 300%;
  margin-left: -60px; /* Use half of the width (120/2 = 60), to center the tooltip */
}
.imagemap:hover .imagemapname {
    visibility: visible;
}
.imagemap:hover {
    background-color: rgba(10, 144, 153, 0.30);
    border: 1px solid #00C2CC;
}
</style>

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypad/flypad-dashboard.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.3%; top:  8.3%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 16.5%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 24.7%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.3%; top: 32.8%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 41.0%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.3%; top: 49.3%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 57.5%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 88.0%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Settings</span></div></a>
</div>

## Description

The Dashboard is the default flyPad page after starting it.

It has three sections:

- Left:
    - Shows the currently loaded flight plan or dashes if none is loaded.
- Right Top:
    - Shows current METAR information for the loaded origin and destination airport.
- Right Bottom:
    - Moving map with your current location marked by a blue plane symbol.
    - Shows the current weather on the map.

## Usage

### Load From simBrief

!!! block ""
    ![From simBrief](../../assets/flypad/load-from-simbrief.png)

If you have [configured](settings.md) your simBrief account correctly, you can click the above button to load your last simBrief flight plan into the flyPad. This does not load the flight plan into the MCDU - you need to load it there separately (see [MCDU simBrief Integration](../../../pilots-corner/beginner-guide/preparing-mcdu.md#a32nx-simbrief-integration)) .

### Map Zoom and Tools

!!! block ""
    ![Zoom Map](../../assets/flypad/zoom-map.png "Zoom Map"){align=left}

    Zooms the map in (+) and out (-).

!!! block ""
    ![Map Tools](../../assets/flypad/map-tools.png "Map Tools"){align=left}

    Distance measure tools. 

    !!! attention ""
        Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

### After loading of a simBrief flight plan

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypad/flypad-dashboard-simbrief.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.3%; top:  8.3%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 16.5%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 24.7%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.3%; top: 32.8%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 41.0%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.3%; top: 49.3%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 57.5%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 88.0%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Settings</span></div></a>
</div>
