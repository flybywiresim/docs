# Resources

On this page you will find all the necessary resources, links and documentation you might need to work with and on the A32NX code.

## Github Repositories

The main Github repository for the A32NX aircraft is:

**[https://github.com/flybywiresim/a32nx](https://github.com/flybywiresim/a32nx){target=new}**

The Development version of the FlyByWire A32NX is done in the master branch. Whenever something is merged into the master branch an automatic build process builds the newest Development version and uploads it to the our CDN so users can download the latest Development version via the FlyByWire Installer.

The Stable version is a snapshot (in git terms a [Tag](https://github.com/flybywiresim/a32nx/tags){target=new}) of the development branch.

The experimental version is build in the branch [experimental](https://github.com/flybywiresim/a32nx/tree/experimental){target=new}. It is regularly manually updated with the latest commits from the master branch but its focus is on the development of special larger features like the custom fly-by-wire and autopilot system or the custom flight management system (cFMS).

While the development on the master branch (Development version) follows a very strict development, review and QA process, the development in the experimental branch is less strict and developers can relatively freely commit changes. This is why the Experimental version has a higher risk of bugs and issues and is only meant for testing and not supported on Discord.

The FlyByWire project has other repositories for sub projects like api, msfs-rs, installer, websire, docs, etc. Find them [here](https://github.com/orgs/flybywiresim/repositories){target=new}.

## Support from the FlyByWire Team on Discord

To get additional information and support please make sure you join our Discord. There are various channels dedicated to support developers (in fact most channels).

[:fontawesome-brands-discord:{: .discord } - **Discord Link**](https://discord.gg/flybywire){target=new}

First get yourself the "programmer" role in [#roles](https://discord.com/channels/738864299392630914/751780817772216401/816730253543604224){target=new}.

The most  general channel for getting help for development is [#dev-support](https://discord.gg/v3jAxJpwZm){target=new}.

There are many other channels for specific systems or sub projects. If you are working on the flyPad EFB for example the #efb channel would be an important channel for collaborating and support.

## Tech Stack

Our tech stack includes the following:

- Systems development for aircraft uses Rust and the `msfs-rs` library
- Avionics programming is done using JavaScript or TypeScript (depending on the project), with the `React.js` rendering library.
- Front-end web or desktop app development uses the same technologies outlined above
- Server-side development uses `nest.js` for the API and `MySQL` for the database backend

Knowledge of all items on this list is obviously not necessary, but this can hopefully give you a better insight into what your skills can fit into.

## Tools

A number of tools make development in Microsoft Flight Simulator easier.

- [WebUI-DevKit](https://github.com/dga711/msfs-webui-devkit){target=new} - In-game development overlay for html-ui content. Provides fast reload, console output, and more!
- [devtools-backend-refurb](https://github.com/dga711/devtools-backend-refurb){target=new} - Chrome devtools server targeting Coherent GT. Gives you devtools for html-ui content. WARNING: This is still a work in progress, and tends to be very finnicky.

## Additional resources

- [P3D XML Gauge Reference](http://www.prepar3d.com/SDK/SimObject%20Creation%20Kit/Panels%20and%20Gauges%20SDK/creating%20xml%20gauges.html) - still applies to FS2020.
