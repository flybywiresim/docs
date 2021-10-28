# Code Structure

Fundamentally, there are three main components to the A32NX codebase.

- Displays are written in JavaScript/TypeScript, more and more also written in React
- Systems developed in Rust
- Autopilot, Fly-by-wire, and some engine-related systems in C++

Before making a contribution to the project, it is a good plan to have a general idea of which of these categories the change would fall into. For most people (including me, the author of this article), this will probably be a change to the displays. However, this might not always be the case.

In the `a32nx` repository, we can see a bunch of configuration files and folders concerning mostly the build pipeline and documentation. This part is used to get the source code into the simulator. We do not have to concern ourselves with this for now.

Instead, we want to focus on the `src` folder. This is the heart of the project, all of the logic is contained in this folder. In it, we can also find representatives of the three main aspects mentioned above. Namely, `instruments/` for displays, `systems/` for -- you guessed it -- systems, and finally `fadec/` and `fbw/` for the Fly-by-wire and FADEC systems.

## Displays

How would we change something in the displays section then? As an example, let's say we wanted the FMA on the PFD to say "MANUAL TOGA" instead of "MAN TOGA", where would we make this change?

We can find the FMA code in the correspondingly named `instruments/src/PFD/FMA.tsx` file. Note that we go into the `instruments/` directory for display code because this is not system-related, but only a visual change on the PFD. The `instruments/src/` holds any source code related to the instruments, with the code outside of it being, again, code used for the build pipeline. We then simply follow the logical path down to `instruments/src/PFD/FMA.tsx`. We can recognize this as being a TypeScript file using react from the `.tsx` extension.

Now that we've found the correct file, we're almost there. We can use `Ctrl+F` to look for the keyword "TOGA" and there we are! You might also find other FMAs apart from "MAN TOGA" such as "TOGA LK". We can now simply change "MAN" to "MANUAL", save, and rebuild the project to see the change reflected in the simulator.