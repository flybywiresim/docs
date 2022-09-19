# FlyByWire Documentation Project

 [:fontawesome-brands-github:{: .github } -  **Documentation Project Github**](https://github.com/flybywiresim/docs){target=new .md-button}

## Background

The FlyByWire Documentation Project aims to provide all necessary information and documentation to successfully install and use the FlyByWire A32NX aircraft in Microsoft Flight Simulator.

For this we provide documentation about the A32NX add-on itself but also valuable additional documentation on how to fly an airliner on Microsoft Flight Simulator in general and even some specific A320neo documentation for the more involved user.

We apply very high standards to quality and accuracy of our documentation so that it is easy to read and understand but also as correct as possible. Therefore we have a strict quality process and everything is reviewed by several users and real pilots from our team.

## How to Contribute

### Contacts for FlyByWire Documentation Team

If you have questions or suggestions, or if you want to contribute to the FlyByWire Documentation project, please contact us on Discord:

[:fontawesome-brands-discord:{: .discord } - **Discord Link**](https://discord.gg/flybywire){target=new}

- Valastiri#8902
- Cdr_Maverick#6475

### Required Tools

To participate in the FlyByWire Documentation Project you need to have following tools installed:

- Github account and Git ([Github Quickstart](https://docs.github.com/en/get-started/quickstart){target=new})
- Python ([Python Downloads](https://www.python.org/downloads/){target=new})
- Install the following Python based tools (see install command below):
    - MkDocs ([MkDocs](https://www.mkdocs.org/){target=new})
    - mkdocs-awesome-pages-plugin
    - mkdocs-git-revision-date-localized-plugin
    - mkdocs-redirects
    - mkdocs-exclude-search
    - mkdocs-embed-external-markdown
    - mkdocs-video
    - mike
    - pillow
    - cairosvg
- Install with this single line command:

    ```title="Run In Terminal"
    pip install -r requirements.txt
    ```
!!! info "Pillow + Cairo Dependency"
    As part of the new social card feature released with `mkdocs-material 8.5.0` [Pillow](https://pillow.readthedocs.io/) and [Cairo Graphics](https://www.cairographics.org/) 
    dependencies were added. We bundle this as part of our `requirements.txt` to ensure the dependeices are installed when attempting to test [social cards locally](#social-cards-feature). If you encounter any issues with these python packages:

    - Install [GTK+](https://www.gtk.org/docs/installations/windows/) for Windows.

    For more information including other operating systems refer to the [Social Card Dependencies](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/#dependencies) Section on the `mkdocs-material` documentation.

- Editor / IDE:
    - Recommended: [Microsoft Visual Studio Code](https://code.visualstudio.com/docs#vscode){target=new}
        - recommended plugins to work with markdown:
            - any markdown helper plugin - e.g. [https://github.com/yzhang-gh/vscode-markdown](https://github.com/yzhang-gh/vscode-markdown)
            - especially for tables: [https://github.com/takumisoft68/vscode-markdown-table](https://github.com/takumisoft68/vscode-markdown-table)
    - Or any [Jetbrains](https://www.jetbrains.com/) IDE, e.g. IntelliJ IDEA or Clion.
    - Or any text editor (even Notepad.exe will do) in conjunction with [stackedit.io](https://stackedit.io/){target=new} - Create and edit markdown on the web. Useful if you don't have / can't setup MkDocs locally on your machine. Does not support material references. Please note this in your PR so a maintainer can double check your references render appropriately.

#### Social Cards Feature

!!! danger "Important Information"
    For general purposes you do not need to test or utilize this feature locally unless you want to develop or change configurations related to this feature. Please be aware of
    the information below if you intend to test this locally.

We have added the social cards feature to the FBW documentation project. When generating the social cards locally, the directory `.cache` is created where all the assets are
generated. See [Complete Local Builds](#complete-local-builds).

You may need to manually clean any files within the `.cache` directory if you encounter any build issues after generating / modifying configuration files related to this 
feature.

### Process

#### Preview your Local Clone

- Fork the [:fontawesome-brands-github:{: .github } -  **Documentation Project Github**](https://github.com/flybywiresim/docs){target=new} ([How to fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo){target=new}).
- Create a local clone ([How to cloning your forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository){target=new}).
- Checkout the "primary" branch - this is the main branch of the current FlyByWire Documentation Project.
- In a command line terminal go to the cloned repository folder and start `mkdocs.exe serve` to start the local preview server.

    This should look like this:

    ```
    > mkdocs.exe serve
    INFO     -  Building documentation...
    INFO     -  Cleaning site directory
    INFO     -  Documentation built in 4.03 seconds
    INFO     -  [12:05:30] Serving on http://127.0.0.1:8000/
    ```
  
!!! info "Faster Preview Server"
    You can opt to use a faster instance of the developer server by invoking the flag `--dirtyreload`. This just checks for any markdown that has changed since the HTML was rendered and will reconstruct any relevant pages only rather than rebuilding the entire website.

    ```
    mkdocs.exe server --dirtyreload
    ```

    !!! danger ""
        Navigation and new internal links may not get updated on other pages while using `--dirtyreload`. Verify links using the standard serve or build command.

- You can now browse the current checked out branch in a browser at this address: [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The site renders every time you save any `filename.md` you are working on.
- Optional: Build static site locally for testing:

    ```
    mkdocs build --clean --no-directory-urls
    ```

    - The site will be built locally under `/site` on in your local repo for user testing. Open`index.html` in the root of `/site` to preview.
    - Note: `--no-directory-urls` allows usage of reference links when browsing the locally built site. Prevents having to find each index.html related to every `filename.md` to preview the relevant page.

#### Make Changes or Additions to the Documentation

- Create a new branch based of branch "primary" (might differ for certain sub-projects) and checkout this new branch. Give a short but meaningful name to the branch.
- Make initial changes on your local branch.
- Create a [Draft Pull Request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-forkhttps://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork){target=new} (aka PR) early to let people know what you are working on.
    - Explain in the PR Description what you are changing/adding and how people should review your changes.
- Work on your changes locally, preview constantly and push your changes regularly to get a preview deployment for others to give feedback.
    - Every time you push changes to your PR a preview is generated with a URL. You can share this link in Discord for the team to provide feedback easily. The URL (by the vercel bot) is visible as a comment on your PR github page.
- When finished, push your final changes to the PR, update the PR description if required and mark it "[Ready for Review](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request#marking-a-pull-request-as-ready-for-review){target=new}".
- Someone from the documentation team will review your changes, give feedback, potentially ask for changes, and eventually approve and merge your changes.

#### Adding Plugins or Markdown Extensions

Please use the alternative "key/value" pairs method when adding plugins or markdown extensions with special note that an empty value must be provided when no options are defined.

```yaml title="Sample New Config"
plugins:
  search: {}
  awesome-pages: {}
```

```yaml title="Old Config"
plugins:
    - search
    - awesome-pages
```

### Build Pipeline and Config Changes

In order to facilitate smooth local development we have made some changes between production builds and local development.

Building for production now uses the `production.yml` file which deep merges with mkdocs.yml using the `INHERIT` function with mkdocs.

`mkdocs build --config-file production.yml`

#### Complete Local Builds

You can still follow the instructions to [preview your local clone](#preview-your-local-clone) to test and preview your changes locally.

If you would like to fully test the generation of the open graph cards (Social Cards Feature) you need to run the following:

- `mkdocs.exe serve --config-file production.yml` 
- `mkdocs.exe build --clean --no-directory-urls --config-file production.yml`

### How to Write Documentation for FlyByWire

#### Technical How-To

- You can edit existing pages simply by editing an existing `pagename.md`.
- To create a page simply create a new file "pagename.md" in an appropriate folder and start writing your documentation. Best practices it to look at other pages regarding the general structure (Headings, Material for MkDocs features, etc.).
- Create the page in the navigation folder you feel this page belongs to. The Documentation Team will be happy to support you with the best location and also how to create a navigation to your page.
- During the PR Review the page still can be moved and navigation can be changed/added. So don't worry too much about it and focus on the content for your page.
- Add images to the section's asset folder. Consider creating a folder for your page when using several images.
- Although the FlyByWire Documentation Team will take care of navigation it might still be of interest how the navigation is done. This is well explained on the [mkdocs-awesome-pages-plugin's README on their Github](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin#Features){target=new}

!!! tip "Embedding YouTube Videos"
    We have included the plugin `mkdocs-video` to streamline adding YouTube embeds into documentation. This removes the necessity to inline `<iframe>` information within 
    documentation pages. 

    The plugin uses the markdown image syntax with a custom marker defined in mkdocs.yml: `video-embed`.

    ```md title="Sample YouTube Embed Code"
    ![video-embed](https://www.youtube.com/embed/3i1FaGKOwII)
    ```

#### Tips to Work Effectively with `mkdocs` (Change, Previews, etc.)

- Have your editor and browser preview side-by-side on your screen.
- Every time you save your file the "mkdocs serve" should make your browser reload and you can preview your changes directly.
- Start with the structure of your documentation page. E.g. headlines first and maybe notes below the headlines of what the section should cover. Build up your page from there.
- How to do:
    - Links: `[Link-Text](https://www.target.domain/page)`
        - internal links need a relative path to the .md file
        - add `{target=new}` to external links
        - look into existing pages for examples
    - Other [Material for MkDocs features](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/){target=new}

#### Writing Good Documentation

- Write documentation professionally and clearly.
- Write for the targeted audience (Sim Beginner, Sim Veteran, Developers, etc.) and don't assume too much pre-knowledge on the reader's side.
- Use the full availability of features baked into [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/){target=new} to create readable and well formatted guides.
- Add illustrations where appropriate. Make sure you optimize images to be as small as possible (resize to their actually used size and use JPG Compression (50% is mostly ok).
- Ensure relevant filenames are web friendly slugs.
- Don't hesitate to get feedback from the FlyByWire Documentation Team early and often.
- Proofread your work carefully before marking "Ready for Review".

## Ideas and Issues

Please use Github's Issue tracker for any documentation request or issues you might have encountered.

 [:fontawesome-brands-github:{: .github } -  **Documentation Project Issues**](https://github.com/flybywiresim/docs/issues){target=new}

