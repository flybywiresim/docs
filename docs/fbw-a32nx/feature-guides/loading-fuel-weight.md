# Fuel and Weight

<link rel="stylesheet" href="/../../stylesheets/fuel-weight.css">

This section provides information on the A32NX weights configuration and insight on how to utilize and reference onboard/sim features to configure the aircraft appropriately for departure.

{==

There are differences when using our Stable version vs. Development version.<br/>
Please select the correct version below.

==}

[Development Version](#development-version){ .md-button }
[Stable Version](#stable-version){ .md-button }

---

??? "General Fuel and Weight Information (Click to expand)"
    ## General Fuel and Weight Information

    ### Operating Empty Weight
    
    It is important to understand that the term "operating empty weight" can seem a little generic. OEW is typically calculated as "manufacturer's empty weight + standard items + operator items". These items can be the following (not all inclusive):
    
    - Crew members
    - Manuals
    - Food and Beverage
    - Emergency Equipment
    - and any equipment/supplies considered standard by the operator
    
    When considering your ZFW below please keep into consideration the above information with OEW with particular regard that this weight does include the flight crew.
    
    ### Zero Fuel Weight
    
    In simple terms the zero fuel weight (ZFW) = OEW + payload.
    
    Payload is defined as passengers, baggage and cargo.
    
    In a situation where your payload would be something like 14000 kg - *based on our new airframe:* your ZFW would total - 56.500 kg (42.500kg + 14.000kg)
    
    You can reference this against any OFP you may have generated through simBrief. For usage of our simBrief integration - [read here](simbrief.md).
    
    ### Zero Fuel Weight Center of Gravity
    
    The A32NX will auto calculate the ZFW and ZFWCG on the INIT B page once the aircraft and associated payload is loaded into the simulator.
    
    !!! warning "This is not your Center of Gravity for trimming."
    
    - See our [Weights and Balance](loading-fuel-weight.md#weights-and-balance) section in the simBrief integration feature guide.
    - You can read about INIT B configuration [here](../../pilots-corner/beginner-guide/preparing-mcdu.md#init-b).
    
    ### Center of Gravity
    
    An acceptable range for takeoff CG in the A32NX is between 16-40%. The CG is balanced during the passenger loading process.

    Trimming the aircraft for takeoff is usually optional and technically not required. Please reference our the [FBW Checklist](../../pilots-corner/SOP.md) to set the appropriate trim should you wish to.
    
    Ideally, anything less than 25% CG is considered FWD load, and anything more than 25% is considered an AFT load. While opting to choose between either CG configuration (aft/fwd) please consider the information below.
    
    !!! info "Notes on Differing CG Configurations"
    
    There are a few arguments worth considering when it comes to favoring an aft CG or fwd CG. Generally an aft CG would provide for better aircraft performance (lower stall speed, drag, and angle of attack for a given lift coefficient) but generally worse for pitch stability.

    For a smaller aircraft as the A320neo, most operators would favor an aft CG loading for fuel consumption benefits when considering the lifetime of the a fleet and how easy the benefits can be obtained.

---

## Development Version

!!! danger "MSFS Fuel & Weights window in the toolbar"
    We have blocked the UI elements in the MSFS fuel and weights window. However, the sliders in the MSFS window are movable but in a matter of 1-3 seconds the fuel and payload levels should return to the initial value.

    {--

    **PLEASE NOTE** we have changed fuel and payload loading.

    --}

    - Fuel: Now done via the [EFB](flyPad/dispatch.md#fuel-page).
    - Payload: Done through the [W&B in the MCDU](#weights-and-balance)

### A32NX Configuration

Get our [simBrief Profile](../installation.md#simbrief-airframe) for the Development and Experimental versions.

- OEW (Empty Weight): 42.500 (in kilograms)
    - Also referred to as DOW (Dry Operating Weight) which can be seen in other simBrief OFP formats such as EZY
- MZFW (Max Zero Fuel Weight): 64.300 (in kilograms)
- MTOW (Max Takeoff Weight): 79.000 (in kilograms)
- MLW (Max Landing Weight): 67.400 (in kilograms)
- Max Fuel Capacity: 19.045 (in kilograms)
- Passenger Weight: 104 (in kilograms)
    - 84 kg for passenger (including clothing and carry-on bags)
    - 20 kg for checked luggage
- Passenger compartments: 4
    - ECONOMY ROWS 1-6 (seats: 36 max: 6670lbs/3024kg)
    - ECONOMY ROWS 7-13 (seats: 42 max: 7780lb/3530kg)
    - ECONOMY ROWS 14-21 (seats: 48 max: 8880lb/4032kg)
    - ECONOMY ROWS 22-29 (seats: 48 max: 8880lb/4032kg)
- Cargo Compartments: 4
    - FWD BAGGAGE/CONTAINER (max: 5600lb/2540kg)
    - AFT CONTAINER (max: 4000lb/1815kg)
    - AFT BAGGAGE (max: 3500lb/1585kg)
    - AFT BULK/LOOSE (max: 2750lb/1245kg)

### Loading Fuel and Weight

!!! danger "MSFS Fuel & Weights window in the toolbar"
    We have blocked the UI elements in the MSFS fuel and weights window. However, the sliders in the MSFS window are movable but in a matter of 1-3 seconds the fuel and payload levels should return to the initial value.

    **PLEASE NOTE** we have changed fuel and payload loading.

    - Fuel: Now done via the [EFB](flyPad/dispatch.md#fuel-page).
    - Payload: Done through the [W&B in the MCDU](#weights-and-balance)

#### Fuel

Fuel loading is now exclusively done via our EFB which has a great UI to see the status of fuel tanks and other options. [Guide Here](flyPad/dispatch.md#fuel-page).

#### Weights and Balance

In our development version we have introduced a new flight model paired with a new weight and balance payload method that incorporates seat rows and the correct center of gravity.

Get our [simBrief Profile](../installation.md#simbrief-airframe) for the Development and Experimental versions.

!!! warning "Fuel, Weights and Balance When not Starting Cold & Dark"
    The process described in this section is for starting the flight at a gate/ramp in a cold and dark state.

    If you start your flight on the runway or in the air the loading process will only work if the Boarding Time [settings](flyPad/settings.md#sim-options) in the flyPad EFB are set to `Instant`. This is deliberate as simulating fueling or boarding and loading when starting from the runway does not make sense.

??? info "Dynamic Fields and Colors"
    Payload, ZFW, ZFWCG are dynamic fields that are updated alongside the loading/boarding process.

    - Payload = Pax Weight + Baggage Weight + Cargo
    - ZFW (Zero Fuel Weight) = OEW (Operating Empty Weight) + Payload
    - ZFWCG = CG based on ZFW (**Not to be mistaken for takeoff CG**)

    Stations in <span style="color:cyan">CYAN</span> indicate they are reading/waiting to board/load.

    Stations that are fully loaded will turn <span style="color:green">GREEN</span>.

    See also [General Fuel and Weight Information](#general-fuel-and-weight-information)

??? info "AOC Menu"

    The AOC (Airline Operational Center) menu is found in the MCDU MENU and should be used for certain apsects of this guide.

    * Click on `MCDU MENU`
    * Click on `ATSU` (ATSU = Air Traffic Service Unit)
    * Click on `AOC MENU` (AOC = Airline Operational Center)
    * Click on `PERF/W&B`

##### Load OFP Payload Info

!!! block ""
    ![W&B 2](../assets/feature-guides/simbrief/wb2.png){align=right width=50% loading=lazy}

    Once on `W&B` page it should look like the sample image even if you have pressed OFP REQUEST in a different section.

    === "PAX Rows Format"
        - X (Y)
        - X denotes PAX already boarded into the relevant station
        - Y denotes PAX target (awaiting boarding) for the relevant station.

    === "Cargo Hold Format"
        - X (Y)
        - X denotes cargo loaded in the hold
        - Y denotes cargo target for the hold (includes baggage)

!!! block ""
    ![W&B 3](../assets/feature-guides/simbrief/wb1.jpg){align=right width=50% loading=lazy}

    Press OFP Request for this specific page and your `W&B` page will show total pax, pax per row and cargo hold (in metric tonnes) which populate automatically.

    Note: this does not start the boarding process. Also Cargo will be limited as a protection to a max capacity if the simBrief OFP cargo exceeds the cargo hold limits).

??? info "Loading Manually"

    ##### Loading Manually

    It is possible to input these values manually to customize your passenger loading. Please note the following information when customizing your pax loading manually:

    - To assign a value to a row (station) enter the amount into your scratchpad using the MDCU keyboard and press the relevant LSK next to the desired station.
    - If inputting a value into the `TOTAL PAX` using LSK1L this will automatically distribute passengers based on an ideal CG.
    - Make sure to input pax values (either total or individual row-wise values) BEFORE inputting cargo. Check-in baggage weight is calculated automatically (Pax * 20 KG).
    - Once the above weights are accounted for you can input remaining weight (cargo weight) in a `X.X` format denoting metric tonnes.
        - Cargo weight is limited to max capacity if it exceeds the cargo hold limits.

##### Board Passengers

!!! block ""
    ![W&B Boarding](../assets/feature-guides/simbrief/wb-boarding.jpg){align=right width=50% loading=lazy}

    You can now start boarding by selecting LSK6R (the indication will change from `START` to `STOP` in yellow) and watch as the passengers board the aircraft.

    **You do not need to remain on this page as boarding continues.**

    !!! warning ""
        Make sure boarding and loading is completed before filling the INIT B page's ZFW and CG!

    !!! tip ""
        [Setting boarding simulation time on the EFB](flyPad/settings.md#usage_2)

!!! block ""
    ![W&B Loaded](../assets/feature-guides/simbrief/wb-loaded.jpg){align=right width=50% loading=lazy}

    Once boarding has completed all rows and total pax should turn green and the boarding indication returns to `START`. Verify your ZFW on this screen and check your lower ECAM that GW has been updated.

##### Deboard Passengers

###### Complete Deboard

!!! block ""
    ![deboarding full](../assets/feature-guides/simbrief/deboarded1.jpg){align=right width=50% loading=lazy}

    Once you have completed your flight you can opt to deboard passengers from the aircraft. Return to the AOC MENU and head to page 2 of `W&B`.

    To perform a complete deboard (all pax and cargo) input 0 into the scratchpad and select `LSK1L` into the TOTAL PAX field.

    Press START to begin the process.

###### Partial Deboard

!!! block ""
    ![deboarding partial](../assets/feature-guides/simbrief/deboarding2.jpg){align=right width=50% loading=lazy}

    In case of a partial offload you can input the desired remaining pax and cargo for leg 2. The example to the right shows a planned retention of 142 passengers.

    **NOTE:** Cargo will show only bag weight for 142 pax. Please ensure that you re-add any additional cargo that you may have been carrying originally.

    Press START to begin the process.

---

## Stable Version

### A32NX Configuration

Get our [simBrief Profile](../installation.md#simbrief-airframe) for the stable version.

- OEW (Empty Weight): 46.262 (in kilograms)
    - Also referred to as DOW (Dry Operating Weight) which can be seen in other simBrief OFP formats such as EZY
- MZFW (Max Zero Fuel Weight): 64.300 (in kilograms)
- MTOW (Max Takeoff Weight): 79.000 (in kilograms)
- MLW (Max Landing Weight): 67.400 (in kilograms)
- Max Fuel Capacity: 19.045 (in kilograms)
- Passenger Weight: 104 (in kilograms)
    - 84 kg for passenger (including clothing and carry-on bags)
    - 20 kg for checked luggage

### Loading Fuel and Weight

#### Fuel

![MCDU ATSU AOC PERF/W&B](../assets/feature-guides/simbrief/mcdu3.png "MCDU ATSU AOC PERF/W&B"){loading=lazy}

You are presented with the `Fuel Page` first then the `Weights and Balance` page. On the first page you can automatically load your fuel.

* Press LSK5L to instantly load your planned simBrief fuel. (The load button will flash momentarily).
* You can verify fuel has loaded by looking at your upper ECAM FOB.

Using the horizontal slew keys you can switch to the weights and balance page.

Fuel loading can also be done via our EFB which has a great UI to see the status of fuel tanks and other options. [Guide Here](flyPad/dispatch.md#fuel-page)

#### Weights and Balance

Once on the `W&B` page (2/2) you can adjust payload here or accept the numbers provided to you via your simBrief OFP.

- Press LSK5L to instantly load your planned payload and pax.
- You can verify the weight has changed by looking at the lower ECAM towards the lower right-hand side.
