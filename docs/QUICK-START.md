# Quick Start: Build Executor Mod in 10 Steps

This is the simple version. Follow these steps on your Windows PC.

## Step 1: Check your DS3 install
- Open: `C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III`
- If the folder exists, you're good
- If not, check your DS3 is installed

## Step 2: Check ModEngine2
- Make sure ModEngine2 is in the DS3 folder
- If not, download it from: https://github.com/soulsmods/ModEngine2
- Extract it into the DS3 root folder

## Step 3: Create the mod folder
Inside DS3, create this folder:
```
modengine2/mod/
```

If it doesn't exist, make it manually.

## Step 4: Create sub-folders
Inside `modengine2/mod/`, create:
```
chr/
parts/
param/
effect/
```

## Step 5: Get the design files
Go to your repo: https://github.com/nodyx0/ds3-executor-nightreign

Download these files:
- design/characters.json
- design/abilities.json
- design/systems.json

Save them to your local computer.

## Step 6: Copy the starter mod files
I will create a starter mod template and push it to the repo.

Download from: `mod/` folder in the repo
Copy all files into your local `modengine2/mod/` folder

## Step 7: Launch the game
- Open ModEngine2
- Click "Launch Dark Souls III"
- The game should start

## Step 8: Create a new character
- Start a new game
- Name: Executor
- Stats: 20 Dexterity, 18 Vigor, 16 Endurance
- Weapon: Curved Sword
- Armor: Dark/leather style

## Step 9: Test in game
- Walk around
- Attack with your weapon
- Use dodge moves
- Check that it feels responsive

## Step 10: Capture proof
- Take a screenshot (Press Print Screen)
- Record a 30-second video of combat
- Save it to a folder called `release/`

---

## If something breaks
1. Check the ModEngine2 log for errors
2. Verify the mod folder path is correct
3. Make sure the file names match exactly
4. Restart DS3 and try again

## When it works
- You have a real working DS3 Executor mod
- Take your screenshot/video
- Come back and we'll prepare the Melty release

That's it. Simple.
