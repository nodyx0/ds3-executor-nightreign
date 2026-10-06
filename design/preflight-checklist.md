# Preflight checklist

This file is the source-of-truth check before any build attempt.

## Rule
Every row and column is a checkbox. If a cell is unfilled or unverified, the design is not ready to build.

## Character sheet
- [ ] Executor exists as a DS3 playable character concept
- [ ] Player role is defined and fits the DS3 combat model
- [ ] Weapon focus is chosen and consistent with the combat style
- [ ] Stat profile matches the intended melee role
- [ ] Loadout is defined

## Ability sheet
- [ ] At least 3 signature abilities are defined
- [ ] Each ability has input, effect and timing defined
- [ ] Cooldown and damage expectations are consistent with DS3 style
- [ ] The final finisher is visually distinct and readable in gameplay
- [ ] Abilities fit the host game without breaking fundamental combat rules

## Systems sheet
- [ ] Dark Souls III is confirmed as the host game
- [ ] ModEngine2 is the chosen mod route for the first build
- [ ] Solo offline is the first supported mode
- [ ] Co-op is explicitly deferred until tested
- [ ] The project stays within a real mod, not a standalone game

## Build gates
- [ ] Current design resolves cleanly across all sheets
- [ ] No missing references between design files
- [ ] Any required asset or hook is noted before coding starts
- [ ] Package/launch path is documented before Melty work begins

## Open work
- [ ] Build the actual DS3 character prototype
- [ ] Test launch with ModEngine2
- [ ] Capture a real gameplay screenshot or clip
- [ ] Prepare Melty title/tagline/description from the actual working build
