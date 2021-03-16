# FBW User Documentation

Repository for the FlyByWire Simulations Guides website. 

[FlyByWire Simulations Guides Website](https://docs.flybywiresim.com/)

[Main FlyByWire Simulations Repo](https://github.com/flybywiresim/a32nx)

## Contributing
Reminder the main branch is `primary`

1. Fork repo
2. Clone to your local system
3. Make a new branch
4. Edit the .md you plan on adding changes too.
5. Use editor of choice to preview your .md
7. Submit PR.

**Note:** A build artifact can be created on demand by applying a **Build Artifact** label to a relevant PR. This provides support for reviewing PRs with added images, special formatting, or the PR is large in nature.

You may still and should test your build locally via the methods below.  

## Editing Methods

### Adding new Pages/Documentation

Recommend getting mkdocs setup locally to be able to preview your work via `mkdocs serve` and/or build a local copy of the site `mkdocs build --no-directory-urls` for testing.

You can still build and add pages to repo by simply:

1. Adding the sample.md to the appropriate location.
2. Adding the sample.md to the mkdocs.yml to the appropriate nav section. More info below. 
   
Format is `Title:` `filename.md`
```
nav:
 - Home: index.md
 - Installation Guide: # This is a section. Must NOT have a .md attached.
   - Downloads + Guide: guide.md # This is a nestled page under the section.
 - Donate: donate.md
 - FAQ: faq.md
 ```

## Testing Deployment Locally

If you want to preview your build while you edit follow the instructions below. This helps preview any changes to the style the of documents or propose changes to the branding of the mkdocs.

* Requires Python -> [Installer](https://www.python.org/downloads/windows/)
  * Supports Python 3.5, 3.6, 3.7, 3.8 and pyp3.
* Use pip installation for general compatibility with mkdocs-material theme.
  * Upgrade - `pip install --upgrade pip`
  * Install pip - `python get-pip.py` // recent versions of Python should come bundled with pip.
  
### Dependencies 
The following must be installed locally for this repo to build correctly.
* mkdocs-material
* mkdocs-git-revision-date-localized-plugin 

Run `pip install mkdocs-material mkdocs-git-revision-date-localized-plugin`

You should be setup at this point to locally view your changes as you apply them.
* Use `mkdocs serve` and visit `localhost:8000` to preview the documentation site as you made edits.
* Site renders as you save any .md you are working on or as you save changes to css stylesheets / mkdocs.yml.

If you want to test the build before pushing your PR upstream
* Use `mkdocs build --no-directory-urls` and the site will be built locally under `/site` on in your local repo for user testing. Open`index.html` in the root of `/site` to preview.
  * **Note:** `--no-directory-urls` allows usage of reference links when browsing the locally built site. Prevents having to find each index.html related to every `filename.md` to preview the relevant page. 

## Recommended Reading

Main documentation
* [MkDocs Documentation](https://www.mkdocs.org/)

Theme Documentation
* [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/)
* References for various styling through dependency integrations
  * [MkDocs-Material-References](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
