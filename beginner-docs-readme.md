## Contributing to Beginners Guide

### Requirements

The beginners guide is tailored towards novice pilots and those new to the Airbus equipment. Below is a short list of requirements if contributing to this project.

- Write documentation professionally and clearly.
- Use the full availability of features baked into `Material for MkDocs` to create readable and well formatted guides.
- Working and target branch is `beginner-guide`
  - Open a `draft PR` if you would like to work on something specific.
- Proofread your work before marking Ready for Review.
- Add the relevant `filename.md` to the `mkdocs.yml` and `overview.md` for beginners guide section. 
- Add image assets to `../assets/beginner-guide/`  
- If you have a local installation of MkDocs please look to include a zip file with a built version of your PR.
- Ensure relevant filenames are web friendly slugs.

**Note:** Images should be used to provide references. Tailor your documentation as such and feel free to use `(Image goes here)` to signify where. Reference images may already be available in `../assets/beginner-guide/`. Feel free to coordinate with `Valastiri#8902` on Discord to request additional images OR open an issue. Sample usage:

- Explaining the function of aligning ADIRS:
    - Provide an image of the overhead panel with key indicators highlighting the of location of ADIRS switches


### Resources

The current FlyByWire docs site has most extensions (plugins) enabled from previous work completed.

- [Material for MkDocs References](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
- [stackedit.io](https://stackedit.io/) - Create and edit markdown on the web
  - Useful if you don't have / can't setup MkDocs locally on your machine.     
  - Does not support material references. Please note this in your PR so a maintainer can double check your references render appropriately.

#### Recommended References

Below is a shortlist of useful features to use for building your docs.

- [Abbreviations](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
- [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
- [Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/)
- [Data tables](https://squidfunk.github.io/mkdocs-material/reference/data-tables/)
