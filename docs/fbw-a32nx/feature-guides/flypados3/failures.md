<link rel="stylesheet" href="../../../../../stylesheets/efb-interactive.css">
<link rel="stylesheet" href="../../../../../stylesheets/toc-tables.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">

# flyPad Failures

## Overview

Although far from complete, some A32NX systems are already capable of simulating failures.

To manage and trigger these failures, this flyPad page gives the user structured access to two types of systems:

- Simple on demand triggering of failures by mouse click.
- A more complex failure generator that can be customized to create failures at certain points during your flight for a more "randomized" feel. [Jump to Failure Generator](#failure-generator).

These two systems can be selected by clicking on the respective buttons in the top-right corner of the Failures page.

![flypad-failure-tab.png](../../assets/flypados3/flypad-failure-tab.png){loading=lazy}

There are further extensions planned for the failures feature, incl. more systems and trigger-based failures. This page will therefore change alongside the implementation of the failure system.

## On-Demand Failures

The on-demand failures are triggered by clicking on the respective buttons in the "On-Demand Failures" section of the page.

!!! info ""
    Please ensure that you are on the Failures tab to trigger on-demand failures.

    ![flypad-failure-tab.png](../../assets/flypados3/flypad-failure-tab.png){loading=lazy}

### Comfort View

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-failures.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="failures">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

### Compact View

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-failures-compact-view.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="failures">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

### System View

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-failures-system-view.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="failures">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

### Active Failure View

When a failure is actively simulated, the system will be highlighted with a red color. 

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-failures-active1-view.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="failures">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-failures-active2-view.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="failures">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

### Search

Enter a search term to filter for specific systems. 

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-failures-search-view.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="failures">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

## Failure Generator

The failure generator will trigger system failures automatically, depending on the rules set for the type of generator. There are several types of generators available that have 
different logics to trigger failures. Each generator has its own settings on its triggering conditions. 

They can be armed individually and can trigger a specific set of failures. You can verify the status of a generator based on the following symbol colors:

|                                                                                                                                    Symbol                                                                                                                                     | Status                     |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------|
|                         <div class="d-flex flex-column align-items-center icon-container"><span class="bi bi-airplane"></span></div><div class="d-flex flex-column align-items-center icon-container"><span class="bi bi-arrow-bar-up"></span></div>                          | The generator is not armed | 
| <div class="d-flex flex-column align-items-center icon-container"><span class="bi bi-airplane" style="color: #00E0FE;"></span></div><div class="d-flex flex-column align-items-center icon-container"><span class="bi bi-arrow-bar-up" style="color: #00E0FE;"></span></div>  | The generator is armed     |

These options are found on the "Failure Generators" tab on the Failure page. 

!!! info ""
    Please ensure that you are on the correct tab to trigger or set up the correct generator.

    ![flypad-failure-tab.png](../../assets/flypados3/flypad-failure-tab.png){loading=lazy}

![failures-select.png](../../assets/flypados3/failures-select.png){loading=lazy}

!!! info "Configuration Options"
    Each generator can be configured in the following 4 modes:
    
    |                                                                                                            Symbol                                                                                                            | Configuration | Description                                                                                                                                                        |
    |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    |                                                                                                    :bootstrap-toggle-off:                                                                                                    |      OFF      | Generator is disabled but settings are kept                                                                                                                        |
    |                                                                                                     :bootstrap-repeat-1:                                                                                                     |     ONCE      | The generator will trigger a set of failures only once and go to OFF mode                                                                                          |
    | <div class="d-flex flex-column align-items-center icon-container"><span class="bi bi-airplane"></span></div><div class="d-flex flex-column align-items-center icon-container"><span class="bi bi-arrow-bar-up"></span></div> |   TAKE OFF    | The generator will wait until FLEX or TOGA thrust is set while speed is low on the ground to arm itself |
    |                                                                                                                                                                                                                              |               | It will trigger a set of failures only once until the plane entirely stops and another take off event occurs                                                       |
    |                                                                                                      :bootstrap-repeat:                                                                                                      |    REPEAT     | The generator will trigger a set of failures everytime the conditions are met                                                                                     |



### Max Failures and Number of Failures

Each generator defines a specific number of failures to be triggered at the same time, and a maximum number of failures.

Failures will activate up to the total number of failures configured for the flight.

### Failure Pool Selection

Each failure generator allows to select specifically which failures can be triggered. You may select any combination of failures: 

- Individual failures
- Entire systems 
- or all at once. 
 
Only a specified number of failures, randomly picked from this set, will be triggered by the generator.

!!! tip ""
    You can create several failure generators of the same type so that specific failures may happen at specific conditions different to other sets of failures.

### Failure Generator Settings

You can access the settings of each failure generator by pressing the following icon -> :bootstrap-sliders2-vertical:

### Altitude Failure Generator

This generator triggers a set of failures among the selected failure pool when the airplane reaches a random altitude set between the specified minimum and maximum altitude.

It may be configured either to trigger while the plane climbs or descends.

!!! info "Conditions"
    This failure generator can only arm itself when the plane is outside the altitude activation range with an extra margin of 100 feet. 
    
    The generator mode icon will therefore stay white if the plane is within the altitude activation range.

![failures-altitude.png](../../assets/flypados3/failures-altitude.png){loading=lazy}

### Ground Speed Failure Generator

This generator triggers a set of failures among the selected failure pool when the airplane reaches a random ground speed set between the specified minimum and maximum ground speed.

It may be configured either to trigger while the plane accelerates or decelerates.

!!! info "Conditions"
    This failure generator can only arm itself when the plane is outside the speed activation range with an extra margin of 5 kts.

    The generator mode icon will therefore stay white if the plane is within the speed activation range.

![failures-speed.png](../../assets/flypados3/failures-speed.png){loading=lazy}

### Timed Failure Generator

This generator triggers a set of failures among the selected failure pool when the time since the arming of the generator reaches a random delay set between the specified minimum and maximum delay.

- When configured in the "repeat" or "Once" arming modes, the timer will start right away.
- When configured in the "Take Off" arming, the timer will start once FLEX or TOGA thrust is set for the first time and the plane moves.

!!! info "Timer Condition"
    The timer is running when the generator mode icon is Blue.

![failures-timed.png](../../assets/flypados3/failures-timed.png){loading=lazy}

### Probability Over Time Generator

At any moment, this generator may trigger a set of failures among the selected failure pool by using the probability specified through the average number of failure per hour.
The mean time to failure (MTTF) is provided as an indication of the delay it may take in average to trigger one failure for the probability of failure per hour specified.

!!! note ""
    Rates of failure in aviation vary between 10e-3 per hour and 10e-9 per hour depending on the criticality of the system.

For simulation purposes, it is advised to set this value at a much higher level, up to 10e-1 (0.1 failure / hour or 1 failure every 10 hours) in order to experience failures once every simulator session.

![failures-all-systems.png](../../assets/flypados3/failures-all-systems.png){loading=lazy}

### Take Off Failure Generator

This generator triggers a set of failures among the selected failure pool with a specified probability at each take off.
If a failure occurs during the next take-off, it may happen at any moment, during one of these three take off phases:

- Low ground speed phase :
    - The take-off phase when the plane exceeds the minimum ground speed and is slower than the low-med transition ground speed.
- Medium ground speed phase :
    - The take-off phase when the plane exceeds the low-med transition ground speed and is slower than the med-high transition ground speed.
- High ground speed & climb phase :
    - The take-off phase when the plane exceeds the med-high transition ground speed and is lower than the specified height above the runway. 

The choice between the 3 phases will be random, using the probability of each phase defined in the settings.

**Takeoff Settings TOP**
![failures-takeoff-1.png](../../assets/flypados3/failures-takeoff-1.png){loading=lazy}

**Takeoff Settings Scrolled**
![failures-takeoff-2.png](../../assets/flypados3/failures-takeoff-2.png){loading=lazy}
