# Option 2: Real Custom Executor Asset Workflow for DS3

This is the real custom-character path for Dark Souls III using ModEngine2.

Important:
- This is not a one-click file.
- This workflow requires local asset extraction and modding on your Windows PC.
- The repo holds the design and workflow, but the actual custom files must be created on your machine inside the DS3 install.
- This is the honest path to a real custom Executor character, not a mockup.

## Goal
Build a custom Executor-inspired character in Dark Souls III using:
- an existing DS3 base model
- custom armor / texture pass
- custom weapon/appearance pass
- ModEngine2-based runtime loading

This is the real “custom mod” path.

## Required tools
Install these on your Windows PC:
- Dark Souls III on Steam
- ModEngine2
- Yabber (for extracting DS3 game files)
- DS3 model tooling such as DSMS / Blender workflow if needed
- Notepad++ or VS Code
- A backup tool or file copy tool

## Step 1: Back up your DS3 install
Before touching anything, make a copy of your DS3 folder.

Example:
- `C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III`
- backup to another folder or external drive

This is mandatory. Asset edits can break the game if done incorrectly.

## Step 2: Install ModEngine2 correctly
Place ModEngine2 in the DS3 root folder.

Expected structure:
```
C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III\
    modengine2\
    ...game files...
```

Then launch the game through ModEngine2 only.

## Step 3: Create the runtime mod folder
Inside the DS3 install root, create:
```
modengine2\mod\
    chr\
    parts\
    effect\
    menu\
    param\
    sound\
    scripts\
```

This is where the actual custom files go.

## Step 4: Extract DS3 base assets
Use Yabber to extract the relevant DS3 files.

The goal is to locate the base asset files for:
- character model
- armor
- weapon
- effects
- textures

You are not pulling random files — you are pulling the base assets you will modify and override.

## Step 5: Decide your base model
For the first real custom version, do not create a totally new model from scratch.

Use a DS3 humanoid base and recolor / rework it.

Best first approach:
- existing DS3 humanoid model
- dark leather / assassin-style armor set
- curved sword based on an existing DS3 blade
- crimson accent colors to suggest Executor identity

This is the fastest and most realistic custom version.

## Step 6: Build the Executor look with existing DS3 assets
Use an existing DS3 armor set as the base.

Suggested early combination:
- armor: Assassin Garb / Assassin Gauntlets / Assassin Leggings
- head: Hollow Warden Helm or dark hooded style
- weapon: Pontiff's Curved Sword or another fast curved sword base
- colors: black / ash / crimson trim

This gives you an Executor-like visual identity without needing a completely new model.

## Step 7: Edit the appearance
Use your texture/model tooling to:
- adjust the colors to dark ash or black
- add crimson trim accents
- darken leather textures
- make the weapon look like an execution blade
- tighten the silhouette so it reads as a Nightreign-style duelist

Keep it simple and readable.

## Step 8: Replace or override the DS3 runtime files
Place your edited asset files into:
```
modengine2\mod\
    chr\
    parts\
    effect\
```

This is the actual custom character runtime layer.

## Step 9: Test in offline mode
Launch DS3 through ModEngine2 and test:
- character creation
- character appearance
- weapon appearance
- armor appearance
- movement
- attack flow
- stability

This must be offline only.

## Step 10: Fix one issue at a time
When an asset fails, fix only one thing at a time.

Typical issues:
- wrong file path
- wrong model override
- broken texture mapping
- model not loading
- incompatible animation set
- DS3 crash caused by malformed asset override

If an issue appears:
- check the ModEngine2 log
- verify file names and paths
- verify the override matches the expected base asset
- revert and retry with one change at a time

## Step 11: Validate the real build
A real custom build is ready when:
- the game launches in ModEngine2
- the character loads in-game
- the custom appearance appears
- the game stays stable in offline mode
- you can move, attack, and play for a few minutes

That is the first real custom Executor mod.

## Step 12: Capture proof
Before you consider Melty, capture:
- one screenshot
- one short gameplay clip
- ideally 30–60 seconds of combat

This is required evidence that the mod actually works.

## What is still not included here
This custom workflow requires real local asset work on your Windows PC.

It does NOT include:
- a ready-made binary mod file
- a prebuilt custom character pack
- a one-click install package
- a remote asset pipeline from this environment

Because of that, the repo remains the design/workflow layer, while your game install contains the actual runtime files.

## Recommended milestone
For now, do not aim for a full custom model from scratch.

The realistic first milestone is:
- custom Executor-themed armor look
- custom weapon appearance
- custom character name and loadout
- stable offline gameplay

That is a valid first custom build.

## Final note
This is the honest route to a real custom Executor mod for DS3.

You can build it on your PC, test it locally, and only then prepare it for Melty.

If you want next, I can help with either:
- a simpler “Executor-themed DS3 build” version using existing assets only
- or the more advanced custom asset pipeline above, step by step with troubleshooting
