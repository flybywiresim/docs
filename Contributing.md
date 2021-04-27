# Contributing

Please reference the information below when contributing to this repository. 

## Requirements

* Write documentation professionally and clearly. 
* Use the full availability of features baked into `Material for MkDocs` to create readable and well formatted guides.
* Proofread your work before marking Ready for Review.
* Ensure relevant filenames are web friendly slugs.

## Pull Request Process
Reminder the main branch is `primary`

1. Fork repo
2. Clone to your local system
3. Make a new branch
4. Add or edit the `filename.md` you plan on working on
5. Use editor of choice to preview your `filename.md`
7. Submit PR (ensure merge conflicts are resolved if any)

Ideally you should test your build locally. If your Pull Request is rather large in nature or contains special formatting / images, please send a zip of the `../site` directory created or provide details in your Pull Request.

## Recommended Reading

Main documentation
* [MkDocs Documentation](https://www.mkdocs.org/)

Theme Documentation
* [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/)
* References for various styling through dependency integrations
    * [MkDocs-Material-References](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
* [stackedit.io](https://stackedit.io/) - Create and edit markdown on the web 
    * Useful if you don't have / can't setup MkDocs locally on your machine.
    * Does not support material references. Please note this in your PR so a maintainer can double check your references render appropriately.    

## Editing Methods

### Adding new Pages/Documentation

Recommend getting mkdocs setup locally to be able to preview your work via `mkdocs serve` and/or build a local copy of the site `mkdocs build --clean --no-directory-urls` for testing.

You can still build and add pages to repo by simply:

1. Adding the `filename.md` to the appropriate directory. 
2. Adding the `filename.md` to the `mkdocs.yml` to the appropriate nav section. More info below.

`mkdocs.yml` structure - Format is `Menu Title:` `filename.md`
```
nav:
 - Home: index.md
 - Installation Guide: # This is a section. Must NOT have a .md attached.
   - Downloads + Guide: guide.md # This is a nestled page under the section.
 - Donate: donate.md
 - FAQ: faq.md
 ```

Sample Directory Structure

```
├─ docs/
│  └─ index.md
│  └─ start/
│     └─ sample.md
│     └─ sample.md
│  └─ airliner-flying-guide/
│     └─ sample.md
│     └─ sample.md
│  └─ development-projects/
│     └─ sample.md
└─ mkdocs.yml
```

### Modify existing pages

You can edit existing pages simply by editing an existing `filename.md`. 

### Existing Material References

The following are material references used throughout the docs that are common and/or have existing custom CSS.

* [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
* [Data Tables](https://squidfunk.github.io/mkdocs-material/reference/data-tables/) 
* [Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/)