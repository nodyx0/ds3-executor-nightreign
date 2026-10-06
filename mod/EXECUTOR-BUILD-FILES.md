# Executor Build: What Files Go Where

This is the exact guide for the first real Executor mod.

## Folder by folder breakdown

### mod/chr/
Purpose: Character model files

For the first build:
- LEAVE EMPTY for now
- DS3 will use the default player character model
- You will customize the appearance through armor/weapon/loadout, not model replacement

If you later want a custom character model:
- this is where .bnd and .dcx character model files go
- for v0.1, skip this

### mod/parts/
Purpose: Armor and weapon asset files

For the first build:
- LEAVE EMPTY for now
- DS3 will use default armor and weapon models from your chosen loadout
- You will customize through stat/loadout selection, not asset replacement

If you later want custom armor/weapon appearance:
- this is where .bnd files for armor and weapons go
- for v0.1, skip this

### mod/effect/
Purpose: Visual effects (spell effects, weapon trails, etc.)

For the first build:
- LEAVE EMPTY for now
- DS3 will use default effects
- You will use existing DS3 effects

If you later want custom spell/weapon effects:
- this is where .fxo and .fxr files go
- for v0.1, skip this

### mod/menu/
Purpose: UI and menu files

For the first build:
- LEAVE EMPTY for now
- DS3 will use default menus

If you later want custom menus:
- this is where menu customization files go
- for v0.1, skip this

### mod/param/
Purpose: Game parameter overrides (stats, item properties, etc.)

For the first build:
- You can put a simple loadout guide here
- Create a file called: executor_loadout.txt
- This file should contain the recommended starting gear for the Executor build

See executor_loadout.txt (below) for what goes in here.

### mod/sound/
Purpose: Audio files (voice, effects, music)

For the first build:
- LEAVE EMPTY for now
- DS3 will use default sounds

If you later want custom audio:
- this is where .wem audio files go
- for v0.1, skip this

### mod/scripts/
Purpose: Lua scripts for advanced modding

For the first build:
- LEAVE EMPTY for now
- DS3 will use default behavior

If you later want custom scripted behavior:
- this is where .lua scripts go
- for v0.1, skip this

## Files at the root (mod/)

Create these files in the mod/ root folder:

### 1. executor_loadout.txt
This is the recommended Executor starting gear.

Contents:
```
EXECUTOR BUILD - RECOMMENDED LOADOUT
====================================

Character Name: Executor

STATS (after character creation):
- Vigor: 18
- Attunement: 10
- Endurance: 16
- Strength: 12
- Dexterity: 20
- Intelligence: 8
- Faith: 7
- Luck: 12

WEAPON (Right Hand):
- Pontiff's Curved Sword (or similar fast curved sword)
- Moveset: fast light attacks, quick recovery
- Style: execution blade aesthetic

SHIELD / LEFT HAND:
- Small Leather Shield (or parry tool)
- For quick repositioning and guard breaks

Armor Set:
- Head: Hollow Warden Helm (dark, minimal)
- Chest: Assassin Garb (dark leather)
- Hands: Assassin Gauntlets (dark, tight fit)
- Legs: Assassin Leggings (dark, mobile)

Visual Theme:
- Dark ash / black base colors
- Crimson accents where possible
- Minimal bright colors
- Sharp, aggressive silhouette
- "Executioner" vibe

Rings (early game suggestions):
- Ring of Steel Protection (armor boost)
- Chloranthy Ring (stamina regen)
- Young Dragon Ring (dexterity boost)
- Any remaining ring

Starting Items:
- Estus Flask (healing)
- Firebomb (early damage)
- Throwing knife (ranged option)

Playstyle:
- Fast melee pressure
- Quick dodge repositioning
- Guard break punish
- Curved sword combos
- Aggressive, mobile duelist

Testing Area:
- Start in Firelink Shrine (safe hub)
- Test movement and attacks
- Move to Undead Settlement for combat practice
- Stay offline mode only
```

Where it goes:
- C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III\modengine2\mod\executor_loadout.txt

### 2. modengine.ini
This is the mod identifier file.

Contents:
```
[ModEngine]
Enabled=true
Name=ds3-executor-nightreign
Author=nodyx0
Version=0.1.0
Description=Executor from Elden Ring Nightreign as a playable DS3 character
```

Where it goes:
- C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III\modengine2\mod\modengine.ini

### 3. INSTALL.txt
This is the installation instructions.

Contents:
```
DS3 EXECUTOR MOD - INSTALLATION
===============================

1. Copy this mod folder to:
   C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III\modengine2\mod\

2. Make sure ModEngine2 is installed in:
   C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III\modengine2\

3. Launch the game through ModEngine2 only (not Steam):
   modengine2.exe

4. Create a new character:
   - Name: Executor
   - Follow the stat and gear recommendations in executor_loadout.txt

5. Play in OFFLINE MODE ONLY

6. Test in a safe area (Firelink Shrine)

Troubleshooting:
- If the game crashes, check the ModEngine2 log
- If the mod doesn't load, verify folder paths are correct
- If performance is poor, verify you're using default DS3 assets
- For further help, check the GitHub repo
```

Where it goes:
- C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III\modengine2\mod\INSTALL.txt

### 4. README.md
This is the mod description.

Contents:
```
# DS3 Executor Mod v0.1

A playable Executor character from Elden Ring: Nightreign in Dark Souls III.

## What is this?
This is a Dark Souls III mod that introduces the Executor as a playable character.

- Host Game: Dark Souls III (PC Steam)
- Mod Loader: ModEngine2
- Mode: Solo offline only
- Status: First playable prototype

## Installation
1. Copy the mod folder to your DS3 install
2. Launch through ModEngine2
3. Create an Executor character
4. Play in offline mode

See INSTALL.txt for detailed steps.

## Character Details
- Name: Executor
- Role: Dexterity duelist / mobile pressure fighter
- Weapon: Fast curved sword
- Armor: Dark leather / assassin style
- Playstyle: Quick attacks, repositioning, guard break punishes

## Recommended Loadout
See executor_loadout.txt for full details.

Quick summary:
- 20 Dexterity
- 18 Vigor
- Pontiff's Curved Sword
- Assassin Garb armor
- Dark ash / crimson theme

## Safety
- Offline mode only
- No online anti-cheat bypass
- Standard DS3 mod using ModEngine2
- Safe for single-player testing

## Status
v0.1 - First playable prototype using existing DS3 assets
v1.0 - TBD after testing and feedback

## Author
nodyx0

## Repository
https://github.com/nodyx0/ds3-executor-nightreign
```

Where it goes:
- C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III\modengine2\mod\README.md

## Summary: What files you actually need

For the first real Executor build, you need:

✓ Create these folders (empty for now):
- mod/chr/
- mod/parts/
- mod/effect/
- mod/menu/
- mod/sound/
- mod/scripts/

✓ Create these files in mod/ root:
- executor_loadout.txt (recommended gear guide)
- modengine.ini (mod identifier)
- INSTALL.txt (installation instructions)
- README.md (mod description)

✓ For param/ folder:
- Leave it empty or put executor_loadout.txt there as well

That's it. That is the complete first real Executor mod.

## Next step
Once these files are in place:
1. Launch DS3 through ModEngine2
2. Create a new character named "Executor"
3. Follow the executor_loadout.txt recommendations
4. Test in offline mode
5. Capture a screenshot and gameplay clip
6. Then prepare for Melty

That is the real custom Executor build workflow.
