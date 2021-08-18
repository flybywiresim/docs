# FlyByWire Documentation Project

 [:fontawesome-brands-github:{: .github } -  **Documentation Project Github**](https://github.com/flybywiresim/docs){target=new}

## Background

The FlyByWire Documentation Project aims to provide all necessary information and documentation to successfully install and use the FlyByWire A32NX aircraft in Microsoft Flight Simulator.

For this we provide documentation about the A32NX add-on itself but also valuable additional documentation on how to fly an airliner on Microsoft Flight Simulator in general and even some specific A320neo documentation for the more involved user.

We apply very high standards to quality and accuracy of our documentation so that it is easy to read and understand but also as correct as possible. Therefore we have a strict quality process and everything is reviewed by several users and real pilots from our team.

## How to contribute

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
    - mkdocs-material
    - mkdocs-material-extensions
- Install with this single line command:

    ```
    pip install mkdocs mkdocs-awesome-pages-plugin mkdocs-git-revision-date-localized-plugin mkdocs-material mkdocs-material-extensions
    ```

- Editor / IDE:
    - Recommended: [Microsoft Visual Studio Code](https://code.visualstudio.com/docs#vscode){target=new}
        - recommended plugins wot work with markdown:
            - any markdown helper plugin - e.g. [https://github.com/yzhang-gh/vscode-markdown](https://github.com/yzhang-gh/vscode-markdown)
            - especially ofr tables: [https://github.com/takumisoft68/vscode-markdown-table](https://github.com/takumisoft68/vscode-markdown-table)
    - or any [Jetbrains](https://www.jetbrains.com/) IDE, e.g. IntelliJ IDEA or Clion.
    - or any text editor (even Notepad.exe will do) in conjunction with [stackedit.io](https://stackedit.io/){target=new} - Create and edit markdown on the web. Useful if you don't have / can't setup MkDocs locally on your machine. Does not support material references. Please note this in your PR so a maintainer can double check your references render appropriately.

### Process

#### Preview your local Clone

- Fork the [:fontawesome-brands-github:{: .github } -  **Documentation Project Github**](https://github.com/flybywiresim/docs){target=new}) ([How to fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo){target=new}).
- Create a local clone ( [How to cloning your forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository){target=new}).
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

- You can now browse the current checked out branch in a browser at this address: [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The site renders every time you save any `filename.md` you are working on.
- Optional: Build static site locally for testing:

    ```
    mkdocs build --clean --no-directory-urls
    ```

    - The site will be built locally under `/site` on in your local repo for user testing. Open`index.html` in the root of `/site` to preview.
    - Note: `--no-directory-urls` allows usage of reference links when browsing the locally built site. Prevents having to find each index.html related to every `filename.md` to preview the relevant page.

#### Make changes or additions to the documentation

- Create a new branch based of branch "primary" (might differ for certain sub-projects) and checkout this new branch. Give a short but meaningful name to the branch.
- Make initial changes on your local branch.
- Create a [Draft Pull Request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-forkhttps://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork){target=new} (aka PR) early to let people know what you are working on.
    - Explain in the PR Description what you are changing/adding and how people should review your changes.
- Work on your changes locally, preview constantly and push your changes regularly to get a preview deployment for others to give feedback.
    - Every time you push changes to your PR a preview is generated with an URL you can share with the documentation team to get feedback. The URL (by the vercel bot) is visible on the PR github page.
- When finished, push your final changes to the PR, update the PR Description if required and mark it "[Ready for Review](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request#marking-a-pull-request-as-ready-for-review){target=new}".
- Someone from the documentation team will review your changes, give feedback, potentially ask for changes and eventually approve and merge your changes.

### How to write documentation for FlyByWire

#### Technical HowTo

- You can edit existing pages simply by editing an existing `pagename.md`.
- To create a page simply create a new file "pagename.md" in an appropriate folder and start writing your documentation. Best practices it to look at other pages regarding the general structure (Headings, Material for MkDocs features, etc.).
- Create the page in the navigation folder you feel this page belongs to. The Documentation Team will be happy to support you with the best location and also how to create a navigation to your page.
- During the PR Review the page still can be moved and navigation can be changed/added. So don't worry too much about it and focus on the content for your page.
- Add images to the section's asset folder. Consider creating a folder for your page when using several images.

#### Tips to work effectively with mkdocs (change, previews, etc.)

- Have your editor and browser preview side-by-side on your screen.
- Every time you save your file the "mkdocs serve" should make your browser reload and you can preview your changes directly.
- Start with the structure of your documentation page. E.g. headlines first and maybe notes below the headlines of what the section should cover. Build up your page from there.
- How to do:
    - Links: `[Link-Text](https://www.target.domain/page)`
        - internal links need a relative path to the .md file
        - add `{target=new}` to external links
        - look into existing pages for examples
    - Other [Material for MkDocs features](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/){target=new}

#### Writing good documentation

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

