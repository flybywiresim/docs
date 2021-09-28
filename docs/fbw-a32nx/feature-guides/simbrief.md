# SimBrief Integration

## Flight Planning

Flying IFR (Instrument Flight Rules) even in a simulation like Microsoft Flight Simulator always requires some level of flight planning.

In addition to the obvious route planning there are several other aspects which are critical to any good flight plan:

- Route Planning
    - Origin and Destination
    - Runways, SID and STAR
    - Compliance with ATC Requirements
    - Routing and Constraints
- Fuel Calculation
- Weather Forecast
- Cost and Time Optimization

See [Flight Planning](https://en.wikipedia.org/wiki/Flight_planning){target=new} on Wikipedia for more information.

Microsoft Flight Simulator tries to offer a simple way to do route planning (World Map before starting a flight) however this falls short, especially for users wanting a more realistic experience for airliner flying.

In real life airlines and pilots use dedicated software alongside various sources and services for creating their flight plans.

In the world of flight simulation simBrief does all that for the users based on real word databases and sources. SimBrief provides on average ~40.000 flight plans to users each day and is the most commonly used tool for flight planning for non-professional flight simulation.

It is absolutely possible to use the simBrief OFP (Operational Flight Plan) to configure and program the aircraft based on it without any special integration into the flight sim software or aircraft.

But as in real world aircraft it is common in flight simulation aircraft to integrate these systems directly with the aircraft's flight management system to be able to import all the relevant planning data. This includes the route, altitudes, constraints, fuel, payload (passengers, cargo), and other data points.

This is why FlyByWire has implemented our simBrief integration and will continue to improve this experience even further in the future.

### Flight Planning with SimBrief

This is best explained by simBrief itself - [simBrief User Guide](https://www.simbrief.com/system/guide.php){target=new}

---

## Using the flyPad simBrief Integration

### Setup A32NX simBrief Integration

See [Setup simBrief Integration](flyPad/settings.md#simbrief-integration)

### Importing the simBrief OFP to the flyPad

See [flyPad Guide - Load from simBrief](flyPad/dashboard.md#load-from-simbrief)

See [flyPad Guide - OFP](flyPad/dispatch.md#ofp-page) on how to view the simBrief Operational Flight Plan.

---

## Using the FMS (MCDU) and simBrief Integration

### Importing the simBrief OFP to the FMS (MCDU)

We've included a quick method to have your simBrief OFP automatically loaded into the MCDU. Please do not select an arrival airport on the MSFS world menu otherwise the integration will not work.

This portion of the guide assumes that you understand how to generate a simBrief OFP.

<!--#### ^^SimBrief MCDU Setup^^

Enter your simBrief username. Upon entering your username the MCDU will convert it into an ID number. Please ensure you have no special characters in your username OR use the ID number found before generating your OFP.

* Click on `MCDU MENU`
* Click on `OPTIONS`
* Click on `AOC`
* Click on `SIMBRIEF`-->

#### ^^Request Data from simBrief^^

* Return to `MCDU MENU`
* Click on `ATSU`
* Click on `AOC MENU`
* Click on `INIT/PRESS`
* Click on `INIT DATA REQ`

![MCDU ATSU AOC INIT REQ](../../fbw-a32nx/assets/feature-guides/simbrief/mcdu2.png "MCDU ATSU AOC INIT REQ"){loading=lazy}

This will prepare the MCDU to input the flight plan.

#### ^^Initialize Flight Plan^^

!!! warning "IMPORTANT"
    Do not select an arrival airport on the MSFS world menu or flight planner. Doing this "initializes" the `FROM/TO` field when loading into your flight removing the INIT REQ. option from the `INIT A` page. 

Head over to the `INIT A` page.

* Select `INIT REQUEST` by pressing LSK2R

This will load your flight plan from simBrief directly into the MCDU

![MCDU INIT A](../../fbw-a32nx/assets/feature-guides/simbrief/mcdu1b.png "MCDU INIT A"){loading=lazy}

To learn how to set up the MCDU you can read the [**^^F^^**LIGHT PLAN](../../pilots-corner/beginner-guide/preparing-mcdu.md#flight-plan) section in our beginner's guide.

### Loading Fuel and Weight

!!! info "Customizing Fuel and Weight"

    **NOTE:** There may be slight differences when using our Stable version vs. Development verson. Additionally these settings may be moved to our EFB in the future.    

    You can adjust the amount of fuel and weight manually on these pages. Type in your desired amounts and press the relevant LSK to input it into that field. 

    When you are happy with your changes press `LOAD` using LSK5L to load your custom fuel and weight.

    !!! danger "Please do not touch values in MSFS Fuel & Weights window in the toolbar."

As described in the previous section return to the AOC menu in MCDU menu.

* Click on `MCDU MENU`
* Click on `ATSU`
* Click on `AOC MENU`
* Click on `PERF/W&B`

#### ^^Fuel^^

!!! info "flyPad Fuel Loading"
    You may also perform fuel loading via our EFB which has a great UI to see the status of fuel tanks and other options. [Guide Here](flyPad/dispatch.md#fuel-page)

![MCDU ATSU AOC PERF/W&B](../../fbw-a32nx/assets/feature-guides/simbrief/mcdu3.png "MCDU ATSU AOC PERF/W&B"){loading=lazy}

You are presented with the `Fuel Page` first then the `Weights and Balance` page. On the first page you can automatically load your fuel.

* Press LSK5L to instantly load your planned simBrief fuel. (The load button will flash momentarily).
* You can verify fuel has loaded by looking at your upper ECAM FOB.

Using the horizontal slew keys you can switch to the weights and balance page.

#### ^^Weights and Balance^^

<style>
.md-typeset .admonition.info {
    display: flow-root;
    overflow: visible;
    padding-top: 0;
    font-size: 0.75rem;
}
.md-typeset .admonition-title, .md-typeset summary {
    background-color: rgba(68,138,255,.1);
    border-left: .2rem solid #448aff;
    font-weight: 700;
    font-size: 0.7rem;
    margin: 0 -.6rem 0 -.8rem;
    padding: .4rem .6rem .4rem 2rem;
    position: relative;
}
</style>

In our development version we have introduced a new flight model paired with a new weight and balance payload method that incorporates seat rows and the correct center of gravity. Please use the correct instructions for your corresponding installed version.

!!! warning "Read additional information on [Fuel and Weights](fuel-and-weight.md)"

=== "Development"
    !!! info "Dynamic Fields and Colors"
        Payload, ZFW, ZFWCG are dynamic fields that are updated alongside the loading/boarding process.

        - Payload = Pax Weight + Baggage Weight + Cargo
        - ZFW (Zero Fuel Weight) = OEW (Operating Empty Weight) + Payload
        - ZFWCG = CG based on ZFW (**Not to be mistaken for takeoff CG**)

        Stations in CYAN indicate they are reading/waiting to board/load.

        Stations that are fully loaded will turn GREEN.

    !!! block ""
        ![W&B 2](../assets/feature-guides/simbrief/wb2.png){align=right width=50% loading=lazy}

        Once on `W&B` page (2/2) it should look like the sample image even if you have pressed OFP REQUEST in a previous section.

        === "PAX Rows Format"
            - X (Y)
            - X denotes PAX already boarded into the relevant station
            - Y denotes PAX target (awaiting boarding) for the relevant station.

        === "Cargo Hold Format"
            - X (Y)
            - X denotes cargo loaded in the hold
            - Y denotes cargo target for the hold (includes baggage)

    ---

    !!! block ""
        ![W&B 3](../assets/feature-guides/simbrief/wb1.jpg){align=right width=50% loading=lazy}

        You will have to request OFP again for this specific page and your `W&B` page will show total pax, pax per row and cargo hold (in metric tonnes) which populate automatically. 

        Note: this not start the boarding process. (Cargo will be limited as a protection to a max capacity if the simBrief OFP cargo exceeds the cargo hold limits).

    !!! info "Loading Manually"
        It is possible to input these values manually to customize your passenger loading. Please note the following information when customizing your pax loading manually:

        - To assign a value to a row (station) enter the amount into your scratchpad using the MDCU keyboard and press the relevant LSK next to the desired station.
        - If inputting a value into the `TOTAL PAX` using LSK1L this will automatically distribute passengers based on an ideal CG.
        - Make sure to input pax values (either total or individual row-wise values) BEFORE inputting cargo. Check-in baggage weight is calculated automatically (Pax * 20 KG).
        - Once the above weights are accounted for you can input remaining weight (cargo weight) in a `X.X` format denoting metric tonnes.
            - Cargo weight is limited to max capacity if it exceeds the cargo hold limits.

    ---

    !!! block ""
        ![W&B Boarding](../assets/feature-guides/simbrief/wb-boarding.jpg){align=right width=50% loading=lazy}

        You can now start boarding by selecting LSK6L (the indication will change from `START` to `STOP` in yellow) and watch as the passengers board the aircraft. 

        **You do not need to remain on this page as boarding continues.**

        [Setting boarding simulation time on the EFB](flyPad/settings.md#usage_2)

    !!! block ""
        ![W&B Loaded](../assets/feature-guides/simbrief/wb-loaded.jpg){align=right width=50% loading=lazy}
    
        Once boarding has completed all rows and total pax should turn green and the boarding indication returns to `START`. Verify your ZFW on this screen and check your lower ECAM that GW has been updated.

    ---

    #### ^^Deboard Passengers^^

    ##### Complete Deboard

    !!! block ""
        ![deboarding full](../assets/feature-guides/simbrief/deboarded1.jpg){align=right width=50% loading=lazy}

        Once you have completed your flight you can opt to deboard passengers from the aircraft. Return to the AOC MENU and head to page 2 of `W&B`. 

        To perform a complete deboard (all pax and cargo) input 0 into the scratchpad and select `LSK1L` into the TOTAL PAX field. 

        Press START to begin the process.

    ---

    ##### Partial Deboard

    !!! block ""    
        ![deboarding partial](../assets/feature-guides/simbrief/deboarding2.jpg){align=right width=50% loading=lazy}

        In case of a partial offload you can input the desired remaining pax and cargo for leg 2. The example to the right shows a planned retention of 142 passengers. 

        **NOTE:** Cargo will show only bag weight for 142 pax. Please ensure that you re-add any additional cargo that you may have been carrying originally.

        Press START to begin the process.

    [Return to Top - Weights and Balance](#weights-and-balance){.md-button}

=== "Stable"
    Once on the `W&B` page (2/2) you can adjust payload here or accept the numbers provided to you via your simBrief OFP.

    - Press LSK5L to instantly load your planned payload and pax.
    - You can verify the weight has changed by looking at the lower ECAM towards the lower right-hand side.

