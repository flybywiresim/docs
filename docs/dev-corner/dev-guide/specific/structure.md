# Code Structure

## Folders

Fundamentally, there are three main components to the A32NX codebase.

- Displays are written in JavaScript/TypeScript, more and more also written in React
    - Older systems and instruments in JavaScript
    - More modern, usually rewritten instruments in TypeScript/React.
- Systems developed in Rust
- Autopilot, Fly-by-wire, and some engine-related systems in C++

Before making a contribution to the project, it is a good plan to have a general idea of which of these categories the change would fall into. For most people (including me, the author of this article), this will probably be a change to the displays. However, this might not always be the case.

In the `a32nx` repository, we can see a bunch of configuration files and folders concerning mostly the build pipeline and documentation. This part is used to get the source code into the simulator. We do not have to concern ourselves with this for now.

### The `src/` folder

Instead, we want to focus on the `src` folder. This is the heart of the project, most of the logic is contained in this folder. In it, we can also find representatives of the three main aspects mentioned above. Namely, `instruments/` for displays, `systems/` for -- you guessed it -- systems, and finally `fadec/` and `fbw/` for the Fly-by-wire and FADEC systems.

### The `flybywire-aircraft-a320-neo/` folder

We will roughly categorize the contents of this folder into "code" and "non-code" folders and files. What we call are JavaScript files, these are contained in the `html_ui` folders and further explained below. Non-code items are in all of the different folders.

#### `html_ui/`

There is quite a bit going on in this folder. This is where all of the code belonging to the category of "Older systems and instruments in JavaScript" is.

First off, there are the subfolders `CSS`, `Fonts`, `Images` which contain assets. You probably won't need to touch these if you're implementing something.

The `JS` folder contains mostly generated code, but good file to know about is the `A32NX_Util.js` file, which contain mostly some mathematical utility functions which you might need in if you're developing something in the JS area.

The `Pages` folder is definitely the most interesting one. The `A32NX_Core` subfolder contains any code that cannot strictly be associated with any screen in the aircraft. For example, there are some implementations of flight computers and systems are in there. Note that these implementations are becoming more and more redundant. Certain systems and computers that are still in there are probably going to be implemented as systems in Rust or TypeScript in the future.

`A32NX_Utils` contains more utility code that can be used in various places in the codebase.

`VCockpit` contains a folder `A32NX` which contains all of the transpiled TypeScript instrument code. You might not see this folder if you have not run the build script yet. The `Airliners/FlyByWire_A320_Neo` subfolder contains code related to screens of the aircraft. If you cannot find a specific screen here, it probably means that this has been rewritten in TypeScript/React and can be found in `/src/instruments/src`.

#### Other folders

You'll find some localization files lying around in here. Also assets related to the model, sounds, visual effects, `xml` defining the checklist items of the in-game checklist menu, and some `.flt` files to define starting states of the aircraft, i.e what systesm should be running when spawning on the runway for example.

## Displays

How would we change something in the displays section then? As an example, let's say we wanted the FMA on the PFD to say "MANUAL TOGA" instead of "MAN TOGA", where would we make this change?

We can find the FMA code in the correspondingly named `instruments/src/PFD/FMA.tsx` file. Note that we go into the `instruments/` directory for display code because this is not system-related, but only a visual change on the PFD. The `instruments/src/` holds any source code related to the instruments, with the code outside of it being, again, code used for the build pipeline. We then simply follow the logical path down to `instruments/src/PFD/FMA.tsx`. We can recognize this as being a TypeScript file using react from the `.tsx` extension.

Now that we've found the correct file, we're almost there. We can use `Ctrl+F` to look for the keyword "TOGA" and there we are! You might also find other FMAs apart from "MAN TOGA" such as "TOGA LK". We can now simply change "MAN" to "MANUAL", save, and rebuild the project to see the change reflected in the simulator.

# FAQ

Where would I find:

- Display code:
    - Either in `/flybywire-aircraft-a320-neo/html_ui/Pages/VCockpit/Instruments/Airliners/FlyByWire_A320_Neo/` for JavaScript code
    - Or in `/src/instruments/src/` for displays that have been rewritten in React.
- Systems: `/src/systems/`
- Autopilot code: `/src/fbw/`
- ModelBehaviors files, these are useful whenever you want to define what a switch does in the cockpit, or if you want to find out what it does:
    - Usually just in `/flybywire-aircraft-a320-neo/SimObjects/AirPlanes/FlyByWire_A320_NEO/model/A320_NEO_INTERIOR.xml`