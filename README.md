# ds3-executor-nightreign

## Concept
This project is a Dark Souls III mod that reimagines the world of DS3 as the host game and introduces the Executor from Elden Ring: Nightreign as a playable character.

The first playable slice is intentionally small and safe:
- Host game: Dark Souls III
- Required route: ModEngine2
- Player mode: solo offline first
- Scope: one character, 3–4 signature abilities, one combat encounter or arena test
- Deferred: co-op / party play until the solo version is stable and tested

## Design direction
The mod is not a standalone game, browser mockup, or unrelated demo. It is a real project for the player's copy of Dark Souls III and will only be considered for Melty if it can launch through the host game and run in one click.

## Safety and scope
- This is offline-first only.
- No online anti-cheat workarounds.
- No direct attempt to host a multiplayer server or bypass game protections.
- We are building a real DS3 mod, not a separate game.

## Current status
- Project scaffolding complete
- Character sheet created
- Ability sheet created
- Systems sheet created
- Preflight checklist in place
- Not yet a packaged Melty release or tested game build

## Build order
1. Finish the design sheets and verify every cell is filled.
2. Build a single-player DS3 character prototype.
3. Test launch and stability in offline mode.
4. Expand to co-op only if the architecture and actual test environment support it.

## File structure
- design/characters.json — core character structure
- design/abilities.json — move set and ability rules
- design/systems.json — mod integration and host-game systems
- design/preflight-checklist.md — cross-sheet confirmation checklist
- mod/ — expected location for DS3 mod files
- tools/preflight.py — verifies design completeness before a build
