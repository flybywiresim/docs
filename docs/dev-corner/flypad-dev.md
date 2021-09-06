# A32NX flyPad Development Guide Overview

[**Development Guide Overview**](https://docs.flybywiresim.com/dev-corner/development-guide){ .md-button target=new}
[:fontawesome-brands-github:{: .github } **GitHub Contributing.md**](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md){ .md-button target=new}


## Introduction

This guide has the objective of teaching you how to set up your development environment to efficiently contribute to the flyPad/EFB. This guide follows on from [A32NX Development Guide Overview](https://docs.flybywiresim.com/dev-corner/development-guide/) and 
[GitHub Contributing.md](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md), please familiarise yourself with the information, steps and requirements listed there before reading further.

## Setting up a Development Environment inside MSFS

Before you can load the project to test in your simulator, you first need to ensure you've created a fork of the [A32NX project on GitHub](https://github.com/flybywiresim/a32nx) and have cloned this in your code editor/IDE.
We recommend when making changes on your fork, you create a new branch, titled with the change you're looking to make or something similar.
Make sure you have also run the setup and build scripts shown below and explained in detail on [GitHub Contributing.md](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md).


```
git clone https://github.com/flybywiresim/a32nx.git
cd a32nx
.\scripts\dev-env\run.cmd ./scripts/setup.sh
.\scripts\dev-env\run.cmd ./scripts/build.sh
```

## Creating a Symlink and setting up instant-reload

Once you have the A32NX built, you'll need to link your newly compiled A32NX to your community folder to enable you to quickly update the flyPad with new changes made to your local branch without copying everything over manually again and reloading MSFS.
This is commonly referred to as a 'Symlink'.

To create your Symlink, open your command terminal and run the below command, substituting the correct file paths with your community folder, and the 'flybywire-aircraft-a320' folder from your new project.

Note: Make sure you remove any existing copy of the aircraft from your community folder before doing this.

```
mklink /J [Community folder path] [Project folder path]
```
Example:
``` 
mklink /J C:\Users\USERNAME\AppData\Local\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\Community\flybywire-aircraft-a320-neo C:\Users\USERNAME\IdeaProjects\a32nx\flybywire-aircraft-a320-neo
```

If this works, you'll receive the response:

"Function created for [Community folder] [Project Folder]" from the terminal.

## Quick reloading the flyPad

Now you've compiled and symlinked your Github fork to your community folder, you should be able to load into the aircraft as normal. Check everything is working with your compiled branch before progressing.

Now with your sim open, follow these steps:

- In your code editor/IDE, run the command:

```  npx rollup -wc src/instruments/buildSrc/simulatorBuild.mjs ```

- Navigate to **[http://127.0.0.1:19999](http://127.0.0.1:19999)** in your browser. You should see several options appear, select the below. A page similar to the below should be shown.

``` VCockpit16 - EFB_TEMPLATE [coui://html_UI/Pages/VCockpit/Core/VCockpit.html]```

- The refresh button at the top (also CTRL+R) will reload your flyPad, causing the display to switch off for a few moments. Once turned back on, any changes made and saved in your EFB project file will be updated to the EFB in your simulator session.

![image](../dev-corner/assets/EFBLoader.png){loading=lazy}

## Getting started with the EFB code

Now you're set up with your own fork, which you can reload instantly and test in MSFS, you're ready to get started making changes. When getting started it's a good idea to spend some time looking around the project and wrapping your head around the structure.

- You'll find the main EFB content under ``` src/instruments/src/EFB ``` of your Github fork, try making small changes at first to test, such as changing the colour of an icon, or changing a few words to make sure the reloading is working. 
- Take a look at previous commits made to the flyPad on the [A32NX Github Repository](https://github.com/flybywiresim/a32nx/commits/master) and see what changes were made to get the desired result.

## Troubleshooting 

If there is anything wrong with the code/files in your local branch, when reloading the flyPad, several issues may occur:

- The flyPad will turn on, but switch and stay off when clicking on an affected page a (Reloading the build in the browser will bring this back)
- Everything may show as normal but none of your changes have been applied. 
- The flyPad doesn't turn on at all.

In these cases, it's best to take a look back through changes you've made so far and track down the cause, or revert the last change made if that was the cause. 