# Converting Liveries Guide

*This guide is provided with no guarantee of compatibility and meant for conversion of liveries for personal use.*

To convert a livery of your choice you have to edit three files in that livery's' folder. 

!!! info "Step One"

    Open the aircraft.cfg in `..\SimObjects\AirPlanes\NAME_OF_THE_LIVERY\`

    The base container line should look like this:

        base_container = "..\FlyByWire_A320_NEO"

!!! info "Step Two"

    Open the texture.cfg in `..\SimObjects\AirPlanes\NAME_OF_THE_LIVERY\TEXTURE.XXX`

    There's a fallback which points to the Asobo A320. It should now look like this:

        fallback.X=..\..\FlyByWire_A320_NEO\TEXTURE

    (X = the number of the fallback)