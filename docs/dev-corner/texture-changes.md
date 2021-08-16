# Texture Map Changes

Changes made to the A32NX external model texturing will be documented below. The intended audience for this page is livery creators.

## Sharklet Un-Mirror

The A32NX sharklet model previously mapped both sharklets to the same location on the livery decal texture, despite a second set of sharklets existing on the texture. We have corrected the UV map to utilise the second set of sharklets, to allow accurate depictions of liveries with text, or other items that cannot be mirrored. It was necessary to make use of the existing decals from the original Asobo model because no method has been developed yet to attach new decals to animation bones, so the decals would move with the wing flex.

Some existing liveries making use of the `A320NEO_AIRFRAME_LIVERY_ALBD.png.dds` texture for sharklets did not paint the second set of sharklets. The left wing sharklet will appear unpainted, or partially painted in this case.

If you are the author of an affected livery please reference the following:

- Add the second set of sharklets to your `A320NEO_AIRFRAME_LIVERY_ALBD.png.dds` texture.
- For convenience, here is a copy of the [new sharklet UV map](assets/a32nx-dev/sharklet_uv_4k.png) that can be added as a layer in your workflow. The decals should be painted un-mirrored.

!!! warning ""
    For further context you can review [pull request #5490](https://github.com/flybywiresim/a32nx/pull/5490) on our GitHub if necessary.
