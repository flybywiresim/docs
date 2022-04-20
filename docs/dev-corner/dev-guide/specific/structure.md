# Code Structure

## Folders

Fundamentally, the A32NX codebase is written in three languages:

- Displays are written in JavaScript. However, a lot of these are being rewritten in TypeScript.
    - Older systems and instruments in JavaScript
    - More modern, usually rewritten, instruments in TypeScript/React.
- Systems developed in Rust
- Autopilot, Fly-by-wire, and some engine-related systems in C++

Before making a contribution to the project, it is a good plan to have a general idea of which of these categories the change would fall into. For most people (including me, the author of this article), this will probably be a change to the displays. However, this might not always be the case.

We will now be going over some of the subfolders of the repository with the goal that you will be able to identify the correct location for your contribution.

In the `a32nx` top-level directory, we can see a bunch of configuration files and folders concerning mostly the build pipeline and documentation. This part is used to get the source code into the simulator. We do not have to concern ourselves with this for now. Instead, we want to focus on two subfolder of the top-level directory, namely the `flybywire-aircraft-a320-neo/` and the `src/` folder.

### The `flybywire-aircraft-a320-neo/` folder

We will roughly categorize the contents of this folder into "code" and "non-code" folders and files. What we call "code" are JavaScript files, these are contained in the `html_ui/` folders and further explained below. Non-code items are in all of the different folders.
It is worth noting that a lot of the JavaScript code that is part of this folder is due to be rewritten as a system in Rust or convert to TypeScript code. Let's have a look at the subfolders.

#### `html_ui/`

There is quite a bit going on in this folder. This is where all of the code belonging to the category of "Older systems and instruments in JavaScript" is.

First off, there are the subfolders `CSS/`, `Fonts/`, `Images/` which contain assets. You probably won't need to touch these if you're implementing something.

The `JS/` folder contains mostly generated code, but a good file to know about is the `A32NX_Util.js` file. This contains mathematical utility functions which you might need if you're developing something in the JS area.

The `Pages/` folder is more interesting than the ones previously mentioned. It contains three subfolders we want to look at:

- The `A32NX_Core/` subfolder contains any code that cannot strictly be associated with any screen in the aircraft. For example, some initial implementations of flight computers and systems are in there. Note that these implementations are becoming more and more redundant. Certain systems and computers that are still in there are probably going to be implemented as systems in Rust or TypeScript in the future.

- `A32NX_Utils/` contains more utility code that can be used in various places in the codebase.

- `VCockpit/instruments/` contains a folder `A32NX/` which contains all of the transpiled TypeScript instrument code. You might not see this folder if you have not run the build script yet. The `Airliners/FlyByWire_A320_Neo/` subfolder contains code related to the screens of the aircraft. If you cannot find a specific screen here, it probably means that this has been rewritten in TypeScript/React and can be found in `/src/instruments/src/`.


#### Other folders

You'll find some localization files lying around here. Also, assets related to the model, sounds, visual effects, `.xml` defining the checklist items of the in-game checklist menu, and some `.flt` files to define starting states of the aircraft, i.e what systems should be running when spawning on the runway for example.

### The `src/` folder

This is the heart of the project, most of the logic is contained in this folder. In it, we can also find representatives of the three main aspects mentioned above. Namely, `instruments/` for displays, `systems/` for -- you guessed it -- systems, and finally `fadec/` and `fbw/` for the Fly-by-wire and FADEC systems. Most of the subfolders here are self-explanatory, however, we will point out some notable ones.

- The `src/instruments/` subfolder contains all the ECAM pages.

- The `src/fmgc/` subfolder is where all the FMS code, such as LNAV and VNAV resides.

- `src/systems/` contains all system code written in Rust.

# FAQ

Where would I find:

- Display code:
    - Either in `/flybywire-aircraft-a320-neo/html_ui/Pages/VCockpit/Instruments/Airliners/FlyByWire_A320_Neo/` for JavaScript code
    - Or in `/src/instruments/src/` for displays that have been rewritten in React.
- Systems: `/src/systems/`
- Autopilot code: `/src/fbw/`
- ModelBehaviors files: These are useful whenever you want to define what a switch does in the cockpit, or if you want to find out what it does:
    - Usually just in `/flybywire-aircraft-a320-neo/SimObjects/AirPlanes/FlyByWire_A320_NEO/model/A320_NEO_INTERIOR.xml`