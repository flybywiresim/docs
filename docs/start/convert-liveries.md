# Converting Liveries
***

*This guide is provided with no guarantee of compatibility and meant for conversion of liveries for personal use.*

To convert a livery made for the default A320neo to work with the new FBW A32NX, you have to edit three files in that livery's folder. 

!!! info "Step One"

    Open the aircraft.cfg in `..\SimObjects\AirPlanes\NAME_OF_THE_LIVERY\`

    The base container line should look like this:

        base_container = "..\FlyByWire_A320_NEO"

!!! info "Step Two"

    Open the texture.cfg in `..\SimObjects\AirPlanes\NAME_OF_THE_LIVERY\TEXTURE.XXX`

    There's a fallback which points to the Asobo A320. It should now look like this:

        fallback.X=..\..\FlyByWire_A320_NEO\TEXTURE

    (X = the number of the fallback)

!!! info "Step Three"

    Open the model.cfg in `..\SimObjects\AirPlanes\NAME_OF_THE_LIVERY\MODEL.XXX`

    The two model lines should look like this:

        exterior=../../FlyByWire_A320_NEO/model/A320_NEO.xml
        interior=../../FlyByWire_A320_NEO/model/A320_NEO_INTERIOR.xml

Ready to go! Launch the sim and see if it worked. 