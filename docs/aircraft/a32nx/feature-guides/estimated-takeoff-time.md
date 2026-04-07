---
title: Estimated Takeoff Time
description: Overview of the estimated takeoff time feature
---

# Estimated Takeoff Time

The A32NX supports the insertion of an ETT on the MCDU. This time is used to initialize FMGS time predictions during preflight.

# Overview

A common use case for the ETT in real life is ATC delays. By knowing beforehand what the expected departure time will be, we can add it to the FMGS to adjust all the relevant time predictions.

!!! info "Prerequisites"
    ETT can only be inserted during the preflight phase if the flightplan is the active, or, a secondary flightplan created as a copy from active.
    No restrictions exist for manually created secondary flightplans.

# Usage Guide

In this scenario, we assume that Air Traffic Control has given us a delay, and we want to know what the new estimated time of arrival is. Our estimated takeoff time given by air traffic control is 12:30Z.
On the F-PLN page, we can check that all time predictions are related to the expected flight time and not to our expected departure time.


![fpln-no-ett](../assets/feature-guides/ett/fpln-no-ett.jpg){loading=lazy}

To enter an ETT, we must first perform a vertical revision on any waypoint of choice by pressing one of the right-side LSKs on the MCDU.

![vert-rev-rta](../assets/feature-guides/ett/vertical-revision-rta.jpg){loading=lazy}

From here, we can access the RTA page, which allows us to modify the ETT.

![rta-page](../assets/feature-guides/ett/rta-page.jpg){loading=lazy}

On this page, we can find the ETT prompt at LSK 3L, where we can add our ETT. The ETT can be inserted in HMM, HHMM, HHMMS, or HHMMSS format. Any entry that does not follow these rules will result in a "FORMAT ERROR".
Here, we will insert 1230 and upon doing so, the ETT is accepted and shown in magenta.

![rta-page-with-ett](../assets/feature-guides/ett/rta-page-with-ett.jpg){loading=lazy}

!!! warning "Valid ETT entries"
    We can insert any time as the ETT as long as it is at most 20 hours ahead of the present time. If that is not the case, an "ENTRY OUT OF RANGE" error will appear. For example, if the current time is 11:00Z, anything from 11:00 to 07:00 is accepted.

If we now go back to the F-PLN page, we can notice that our ETT is shown in magenta at the departure airport and the time predictions are relative to 12:30Z. While before we had flight times shown, now we have the expected time of arrival at each waypoint.

![fpln-with-ett](../assets/feature-guides/ett/fpln-with-ett.jpg){loading=lazy}


If we depart prior to the ETT, it will be automatically deleted and the predictions will be updated automatically based on the current time, as usual. On the other hand, if we don't depart by 12:30Z, the "CLK IS TAKE OFF TIME" scratchpad message appears on the MCDU as a reminder. At this point, time predictions are continuously updated based on the current time. If we wish to, we can insert a new one by repeating the whole process.

![clk-is-time](../assets/feature-guides/ett/clk-is-time.jpg){loading=lazy}
