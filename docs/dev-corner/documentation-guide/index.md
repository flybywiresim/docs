---
title: Overview
description: Overview of the FlyByWire Documentation Guide
---

# FlyByWire Documentation Guide

 [:fontawesome-brands-github:{: .github } -  **Documentation Project GitHub**](https://github.com/flybywiresim/docs){target=new .md-button}

## Background

!!! info "Guides"
    If you would like to setup the documentation project locally please continue with this guide.

    If you would like to understand our guidelines on writing and different available features please see the [Writing Documentation](writing-documentation.md) Page instead.

!!! info "Docker Option"
    If you prefer not to install or manage a local Python environment, this repository also includes a Docker-based workflow for local preview and build validation. See [Docker Workflow](#docker-workflow).

The FlyByWire Documentation Project aims to provide all necessary information and documentation to successfully install and use the FlyByWire A32NX aircraft in Microsoft Flight Simulator.

For this, we provide documentation about the A32NX add-on itself, but also valuable additional documentation on how to fly an airliner on Microsoft Flight Simulator in general and even some specific A320neo documentation for the more involved user.

We apply very high standards to the quality and accuracy of our documentation so that it is easy to read and understand but also as correct as possible. Therefore, we have a strict quality process and everything is reviewed by several users and real pilots from our team.

## How to Contribute

### Contacts for FlyByWire Documentation Team

If you have questions or suggestions, or if you want to contribute to the FlyByWire Documentation project, please contact us on Discord:

[:fontawesome-brands-discord:{: .discord } - **Discord Link**](https://discord.gg/flybywire){target=new}

- valastiri
- cdr_maverick
- slein15

### Required Tools

To participate in the FlyByWire Documentation Project, you need to have the following tools installed:

- GitHub account and Git ([GitHub Quickstart](https://docs.github.com/en/get-started/quickstart){target=new})
- Python 3.11 ([Python Downloads](https://www.python.org/downloads/){target=new})
- From the repository root, create a virtual environment with Python 3.11.

    ```bash
    python -m venv venv
    ```

    Activate it with this command in Windows PowerShell.

    ```powershell
    .\venv\Scripts\Activate.ps1
    ```

    Use this command in Windows Command Prompt.

    ```cmd
    .\venv\Scripts\activate.bat
    ```

    Use this command on Linux or macOS.

    ```bash
    source venv/bin/activate
    ```

- Install the development dependencies. This also installs the packages pinned in `requirements.txt`.

    ```bash
    python -m pip install -r requirements-dev.txt
    ```

    `requirements-dev.txt` includes `requirements.txt`, which pins Zensical and installs its dependencies. Reactivate the virtual environment when you open a new terminal.

- Editor / IDE:
    - Recommended: [Microsoft Visual Studio Code](https://code.visualstudio.com/docs#vscode){target=new}
        - recommended plugins to work with Markdown:
            - any markdown helper plugin - e.g., [https://github.com/yzhang-gh/vscode-markdown](https://github.com/yzhang-gh/vscode-markdown){target=new}
            - especially for tables: [https://github.com/darkriszty/MarkdownTablePrettify-VSCodeExt](https://github.com/darkriszty/MarkdownTablePrettify-VSCodeExt){target=new}
            - any plugin to enter Unicode symbols like the narrow non-breakable space for the thousand separator in numbers - e.g., [https://github.com/brunnerh/insert-unicode](https://github.com/brunnerh/insert-unicode){target=new}
    - Or any [JetBrains](https://www.jetbrains.com/) IDE, e.g. IntelliJ IDEA or Clion.
    - Or any text editor (even Notepad.exe will do) in conjunction with [stackedit.io](https://stackedit.io/){target=new} to edit Markdown on the web. Mention in your PR if you could not preview locally so a maintainer can check the Zensical rendering.

#### Social Cards Feature

!!! danger "Important Information"
    For general purposes, you do not need to test or utilize this feature locally unless you want to develop or change configurations related to this feature. Please be aware of
    the information below if you intend to test this locally.

Use the production profile to generate social cards in `site/assets/images/social/`. See [Complete Local Builds](#complete-local-builds) for the clean build command.

### Process

#### Preview your Local Clone

- Fork the [:fontawesome-brands-github:{: .github } -  **Documentation Project GitHub**](https://github.com/flybywiresim/docs){target=new} ([How to fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo){target=new}).
- Create a local clone ([How to clone your forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository){target=new}).
- Checkout the "primary" branch - this is the main branch of the current FlyByWire Documentation Project.
- Start the local preview server from the repository root.

    ```bash
    zensical serve
    ```

- Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The preview reloads when you save changes.
- Before opening a PR, run the same strict build used by CI.

    ```bash
    zensical build --strict
    ```

!!! info "Internet Connection"
    The build fetches external content, so an internet connection is required. If an external fetch fails, the build fails. Restore access and retry the build.

#### Docker Workflow

If you do not want to create a local Python `virtualenv`, you can run the documentation site in Docker instead.

Run the preview server with Docker Compose from the repository root.

```bash
docker compose up --build
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

The repository is bind-mounted into the container, so saving changes locally will trigger Zensical reloads in the running container just like a native setup.

Use the Docker profile to run a one-off strict build.

```bash
docker compose run --rm docs zensical build --strict --config-file docker.mkdocs.yml
```

The Docker configuration inherits `mkdocs.yml` and disables image optimization for containerized local runs.

#### Make Changes or Additions to the Documentation

- Create a new branch based on branch "primary" (might differ for certain subprojects) and checkout this new branch. Give a short but meaningful name to the branch.
- Make initial changes to your local branch.
- Create a [Draft Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork){target=new} (aka PR) early to let people know what you are working on.
    - Explain in the PR Description what you are changing/adding and how people should review your changes.
- Work on your changes locally, preview constantly and push your changes regularly to get a preview deployment for others to provide feedback.
    - The GitHub PR build uploads `site/` as the `preview-build` artifact. The preview workflow downloads that artifact and deploys it to Cloudflare Pages. Share the preview URL with the team for feedback.
- When finished, push your final changes to the PR, update the PR description if required and mark it "[Ready for Review](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request#marking-a-pull-request-as-ready-for-review){target=new}".
- Someone from the documentation team will review your changes, provide feedback, potentially ask for changes, and eventually approve and merge your changes.

#### Adding Plugins or Markdown Extensions

Use key/value pairs when adding plugins or Markdown extensions so configuration profiles can inherit their settings. Zensical provides native implementations for the configured search, navigation, video, lightbox, and social features. Check [plugin compatibility](https://zensical.org/docs/compatibility/mkdocs/plugins/) before adding another plugin.

```yaml title="Sample New Config"
plugins:
  search: {}
  mkdocs-video: {}
```

### Build Pipeline and Config Changes

The local production-style configuration in `production.yml` inherits `mkdocs.yml` and enables social card generation. This configuration is separate from Cloudflare Pages dashboard settings.

#### Complete Local Builds

The production profile generates the full site, including social cards.

```bash
zensical build --clean --config-file production.yml
```

The generated site is in `site/`. Use the same profile if you want to preview it in the browser.

```bash
zensical serve --config-file production.yml
```

## Ideas and Issues

Please use GitHub's Issue tracker for any documentation request or issues you might have encountered.

 [:fontawesome-brands-github:{: .github } -  **Documentation Project Issues**](https://github.com/flybywiresim/docs/issues){target=new}
