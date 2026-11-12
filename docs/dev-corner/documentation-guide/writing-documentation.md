# Writing Documentation

## How to Write Documentation for FlyByWire

### Technical How-To

- You can edit existing pages simply by editing an existing `pagename.md`.
- To create a page, simply create a new file "pagename.md" in an appropriate folder and start writing your documentation. Best practices it to look at other pages regarding the general structure (Headings, Zensical features, etc.).
- Create the page in the navigation folder you feel this page belongs to. The Documentation Team will be happy to support you with the best location and also how to create a navigation to your page.
- During the PR Review, the page can still be moved and navigation can be changed/added. So don't worry too much about it and focus on the content for your page.
- Add images to the section's asset folder. Consider creating a folder for your page when using several images.

### Navigation

Zensical's built-in `awesome-nav` reads `.nav.yml` files in the documentation directories. The Documentation Team can help place new pages in the appropriate section.

The Documentation Guide uses this file to set its section title and put the overview first. The quoted `"*"` includes the remaining pages in that directory.

```yaml title="docs/dev-corner/documentation-guide/.nav.yml"
title: Documentation Guide
nav:
    - index.md
    - "*"
```

To choose a label and position for a page, add an explicit entry such as `- Writing Documentation: writing-documentation.md` before the wildcard. A section can use `hide: true` in its `.nav.yml` to keep it out of navigation. Its pages remain accessible by URL. Use `search.exclude: true` in a page's front matter to exclude it from search, as shown below.

See the [Awesome Nav compatibility guide](https://zensical.org/docs/compatibility/mkdocs/plugins/#awesome-nav) for supported options.

### External Content

External content requires an internet connection and failed fetches block the build. For a full-file live include, use PyMdown Snippets with a URL and the line range `:2:` to omit the first line. See the [Discord bot page](../flybywire-projects/discord-bot.md) source for the directive syntax. Use the `external_markdown` macro for a section or for content that needs link rewrites. The macro is enabled only for configured paths. See the [A32NX Developer API](../../aircraft/a32nx/a32nx-api/a32nx-systems-api.md) source for an example of mapping upstream fragments to their local anchors.

### Extra Features

Zensical provides features for documentation layout and media. The external Markdown macro described above is maintained in this repository.

!!! tip "Embedding YouTube Videos"
    Zensical renders video embeds using its built-in `mkdocs-video` compatibility support. The `mkdocs.yml` configuration sets the marker to `video-embed`.

    Use Markdown image syntax with a YouTube embed URL. YouTube NoCookie URLs using `https://www.youtube-nocookie.com/embed/` also work.

    ```md title="Sample YouTube Embed Code"
    ![video-embed](https://www.youtube.com/embed/3i1FaGKOwII)
    ```

    See the [Zensical video documentation](https://zensical.org/docs/compatibility/mkdocs/plugins/#video) for the supported settings.

!!! tip "Search Exclusion"
    While writing documentation, you may want to include pages in the final build as part of the `docs/` directory, but not have these pages referenced within the search index.

    Add this front matter to keep the page out of the search index.

    ```md title="Search Exclusion Meta Snippet"
    ---
    search:
        exclude: true
    ---
    ```
#### Card Grids

Use card grids to group links to other pages or external resources.

For more information visit the [Zensical card grids documentation](https://zensical.org/docs/authoring/grids/){target=new}.

---

Below is an example of our current use case in the FlyByWire Documentation Project utilizing an ordered list with markdown elements. 

**Option 3 and 4** showcase that you can add additional text and markdown elements to each ordered item. Ensure that the `div` defines `markdown` as an attribute and you can freely add arbitrary markdown within the elements of each card grid.

```html title="Card Grid Ordered"

<div class="grid cards" markdown>

- Option / Text 1
- Option / Text 2
- :fontawesome-brands-github:{: .github } - Option / Text 3

    ---

    This is a `markdown` element that can be added to the [card grid](#card-grids).

- :fontawesome-brands-github:{: .github } - Option / Text 4

    ---

    This is a markdown element that can be added to the card grid.
</div>
```

!!! info "Rendered Example From Code Above"
    <div class="grid cards" markdown>
    
    - Option / Text 1
    - Option / Text 2
    - :fontawesome-brands-github:{: .github } - Option / Text 3
    
          ---
    
         This is a `markdown` element that can be added to the [card grid](#card-grids).
    
    - :fontawesome-brands-github:{: .github } - Option / Text 4
    
          ---
    
          This is a markdown element that can be added to the card grid.
    </div>

<span id="tips-to-work-effectively-with-mkdocs-change-previews-etc"></span>

### Editing and Previewing Changes

- Have your editor and browser preview side-by-side on your screen.
- Every time you save your file, the "zensical serve" should make your browser reload, and you can preview your changes directly.
- Start with the structure of your documentation page. E.g., headlines first and maybe notes below the headlines of what the section should cover. Build up your page from there.
- How to do:
    - Links: `[Link-Text](https://www.target.domain/page)`
        - internal links need a relative path to the .md file
        - add `{target=new}` to external links
        - look into existing pages for examples
    - Other [Zensical authoring features](https://zensical.org/docs/authoring/){target=new}

### Writing Good Documentation

- Write documentation professionally and clearly.
- Write for the targeted audience (Sim Beginner, Sim Veteran, Developers, etc.) and don't assume too much pre-knowledge 
  on the reader's side.
- Use [Zensical](https://zensical.org/docs/){target=new} features to create readable, well-formatted guides.
- Add illustrations where appropriate. Make sure you optimize images to be as small as possible (resize to their 
  actually used size and use PNG Compression).
  See [Image Assets Process](#image-assets-process) for more information.
- Ensure relevant filenames are web-friendly slugs.
- Don't hesitate to get feedback from the FlyByWire Documentation Team early and often.
- Proofread your work carefully before marking "Ready for Review".

### Image Assets Process

- Create the image as PNG (e.g. screenshots) with the highest resolution possible
    - JPEG is also acceptable but preference towards PNG.
- Edit the image (e.g. add comments, lines, boxes, arrows, etc.)
    - If you think the original is worth it store it in `/src/assets` - but most images aren't worth it as screenshots 
      are quickly retaken (Keeping a local copy of all your screenshots is good practice just in case - but it is not 
      worth to clutter the repo with them)
- Put the edited image in the folder for the topic - e.g. `\docs\pilots-corner\assets\advanced-guides\vnav` for images 
  related to the VNAV topic
- Link the image in the markdown document - decide on the size you need (See admonition below for references)
- Please lazy load images that are not in the viewport (e.g. images at the bottom of the page) - this is done by adding 
  `loading=lazy` to the image tag.

   ```md title="Sample Image Markdown with Lazy Loading"
   ![image](directory/image.png){loading=lazy}
   ```
  
#### Image Optimization

Zensical optimizes images during CI builds. This project's configuration disables PNG optimization, so compress PNG files before adding them.

!!! note "Bundled Optimization and Best Practices"
    Image optimization runs during CI builds. The Docker configuration disables optimization for local runs.

    We do still highly recommend the following for all images uploaded to the project:

    - Make sure size and quality are good - usually < 100 kB
    - Compress the png/jpeg image with a tool - [Shortpixel Image Compressor](https://shortpixel.com/online-image-compression){target=new}

!!! tip ""
    Width of images on docs based on the responsive layout.

    - Change the size according to the table - max width is 826 px
    - Zensical's built-in lightbox lets readers enlarge images. Images with the `skip-lightbox` class are excluded. Use a reasonable image size even when readers can enlarge it.
    
    | Size     | Width   |
    |:---------|:--------|
    | zoomable | 1024 px |
    | 100%     | 826 px  |
    | 95%      | 785 px  |
    | 90%      | 743 px  |
    | 85%      | 702 px  |
    | 80%      | 661 px  |
    | 75%      | 620 px  |
    | 70%      | 578 px  |
    | 65%      | 537 px  |
    | 60%      | 496 px  |
    | 55%      | 454 px  |
    | 50%      | 413 px  |
    | 45%      | 372 px  |
    | 40%      | 330 px  |
    | 35%      | 289 px  |
    | 30%      | 248 px  |
    | 25%      | 206 px  |
    | 20%      | 165 px  |
    | 15%      | 124 px  |
    | 10%      | 83  px  |
    | 5%       | 41  px  |

### Style

- Use the units of measurement and their abbreviations as used by ICAO Annex 5. This document can be downloaded, for example, on the website of the [Swiss Federal Office of Civil Aviation](https://www.bazl.admin.ch/bazl/en/home/themen/legislation/anhaenge-icao.html){target=new}.
- If the [current de facto measurement unit](https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization#Use_of_the_International_System_of_Units){target=new} differs from the recommended one or different units are used in some regions, use the most widespread unit and add the recommended or regional one(s) in brackets.
- Regarding typography of numbers and units, the [ISO Conventions](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9.pdf/fcf090b2-04e6-88cc-1149-c3e029ad8232?version=1.21&t=1671101063858&download=true){target=new} summarized in [this checklist](https://physics.nist.gov/cuu/Units/checklist.html){target=new} should be followed, e.g., addition of a [non-breaking space (Unicode 160)](https://en.wikipedia.org/wiki/Non-breaking_space){target=new} between the number and the unit, except for degree, minute of arc, and second of arc, and the use of a [thin or narrow non-breaking space (Unicode 8239)](https://en.wikipedia.org/wiki/Non-breaking_space#Encodings){target=new} as a thousand seperator, as well as between the number and the sign (+, - etc.).

---

[Back to Documentation Development Environment](index.md){.md-button}
