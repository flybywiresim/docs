# Calculating Takeoff Performance

This is an advanced guide on how to calculate takeoff performance in the A32nx. This is to supplement information provided in our flyPadOS 3 documentation and usage guide.

[flyPad Performance Calculator Page](../../../fbw-a32nx/feature-guides/flypados3/performance.md){ .md-button }

Clicking on the calculate button after all the input fields are filled properly will either result in takeoff speeds and Flex temperature (if Flex was selected and can be used) 
being displayed in the replica of the MCDU Takeoff Perf Pages provided on the right side of the calculator unless the takeoff weight exceeds the maximum takeoff weight for the 
input conditions or if any of the input conditions exceed any airplane limitations. If any of these conditions occur, a suitable error message will pop up.

## Examples

Information that can be obtained by Airport 10-9 charts:

[sample image goes here - EGLL CHART]

- Item 1 is the elevation for a takeoff from Runway 09L. 
- Item 2 shows an example of a relatively rare zero degree turn on angle from the taxiway to the runway. This is denoted by the gray taxiway extending far enough after the turn 
  to align the airplane with the runway direction before it gets the runway beginning (indicated by the beginning of the black runway diagram). 
- Item 3 is the elevation for a takeoff from Runway 27R. Item 4 shows a common 90-degree entry from the taxiway to the runway, which requires a portion of the runway to align the airplane in the direction of the runway for takeoff.

Since the elevation of both end of the runway are the same, the slope for takeoffs from both Runway 09L and 27R is zero. 

!!! info "Unmarked In Above Example"
    The magnetic varation for this airport is show by the arrow on the lower right side of the chart. 

The magnetic variation at EGLL is 0 degrees, so there is no difference between a true heading and a magnetic heading. No conversion is needed for the METAR wind direction when 
the wind is input manually for this airport.
