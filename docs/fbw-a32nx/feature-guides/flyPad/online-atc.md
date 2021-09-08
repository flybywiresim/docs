# flyPad Online ATC

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

## Description

The FlyByWire flyPad helps pilots managing the communication frequencies when using Online ATC services like VATSIM or IVAO.

It lists all currently available ATC stations which can then be activated in the RMP 1 by a single click.

## Usage

Go to the flyPad [ATSU/AOC settings page](settings.md#atsuaoc) and select your Online ATC service.

!!! warning ""
    Only VATSIM or IVAO are available at this time.

Go back to the ATC page and see the list of the currently available ATC stations. Click on a station to set this frequency in the Captain's RMP.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypad/flypad-online-atc-vatsim.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.3%; top:  8.3%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 16.5%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 24.7%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.3%; top: 32.8%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 41.0%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.3%; top: 49.3%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 57.5%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 88.0%; width: 5.8%; height: 8.1%;"><span class="imagemapname">Settings</span></div></a>
</div>

![Online ATC Frequency via click](../../assets/flypad/online-atc-frequency.png "Online ATC Frequency via click"){loading=lazy}
