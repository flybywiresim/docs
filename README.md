# FBW User Documentation

Repository for the FlyByWire Simulations Guides website.

[FlyByWire Simulations Guides Website](https://docs.flybywiresim.com/)

[FlyByWire Simulations A32NX Repo](https://github.com/flybywiresim/a32nx)

## Contributing

See [Contributing.md](Contributing.md)

## Testing Deployment Locally

If you want to preview your build while you edit follow the instructions below. This helps preview any changes to the style the of documents or propose changes to the branding of the mkdocs.

* Requires Python -> [Installer](https://www.python.org/downloads/windows/)
  * Supports Python 3.5, 3.6, 3.7, 3.8 and pyp3.
* Use pip installation for general compatibility with mkdocs-material theme. 

The following must be installed locally for this repo to build correctly.
* mkdocs-material
* mkdocs-git-revision-date-localized-plugin

### Python
  
Upgrade pip

``` 
pip install --upgrade pip
```
  
Install pip - recent versions of Python should come bundled with pip.

```
python get-pip.py
```

### MkDocs Material

Install Dependencies  

```
pip install mkdocs-material mkdocs-git-revision-date-localized-plugin
```

Spin up development server
```
mkdocs serve
```

You should be setup at this point to locally view your changes as you apply them.
* Visit `localhost:8000` to preview the documentation site as you make edits.
* Site renders as you save any `filename.md` you are working on or as you save changes to CSS stylesheets / `mkdocs.yml`.

To build site locally for testing

```
mkdocs build --clean --no-directory-urls
```

* The site will be built locally under `/site` on in your local repo for user testing. Open`index.html` in the root of `/site` to preview.
  * **Note:** `--no-directory-urls` allows usage of reference links when browsing the locally built site. Prevents having to find each index.html related to every `filename.md` to preview the relevant page.
  
***

[![Powered by Vercel](https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg)](https://vercel.com/?utm_source=[flybywiresim]&utm_campaign=oss "Powered by Vercel")

