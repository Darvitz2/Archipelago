# Important stuff


# 0.4.0

## APWorld

- make dexsanity hints correctly replace grass with cave etc.
- somehow fix problem with patch backwards compatibility for patch file altering versions that actually can support older versions (e.g. 0.3.99 not accepting 0.3.0)
- reduce different forms weight in randomization
- remove arceus types
- master ball sellers falsely unset?
- fix bianca being spelled "Bianka" on some location names
- update UT fixes
- add "for seeing 25 species" to location name in Castelia City
- Fix Guidance Chamber items being called "Mistralton Cave 3F..."
- add missing hidden item in chargestone cave b2f and change the other hidden item's name
- Fill levelup movesets
- More modifiers
  - Randomize Wild Pokémon
    - Prevent overpowered pokémon 
      - Other modifiers take priority, some op species are even required all the time
      - Base stat total threshold adjustable
    - Prevent early Wonder Guard and fixed HP attacks
  - Randomize Trainer Pokémon 
    - Prevent overpowered pokémon
      - Base stat total threshold adjustable
    - Force fully evolved 
      - Level threshold adjustable
    - Type themed
    - Themed gym trainers (also make gym leaders and elite 4 always have themed teams)
    - Prevent early Wonder Guard and fixed HP attacks
- Randomization Blacklist
  - Wild pokémon 
    - This will throw an OptionError if any blacklisted is base stage but required
    - Ignores Encounter Plando
  - Trainer pokémon

## Rom

- fix gym leaders not being present in their gyms
- fast travel npc in chargestone cave from south to north if battled N at north exit
- maybe juniper seen count locations can check for national seen? look at cedric in mistralton city and both other dex seen locations
- make mom stop the player at the door and say funny things for certain reusable tm choices
- skip musical tutorial, because some players have problems
- disable dig outside of battle when season patch included, as a temporary bandaid fix

## both

- add now-possible locations
- after everything else: check docs for up-to-date information, update tests, update location names in ut                             

# Not urgent

- dig with seasons patch crashes the game, not fixable?
- look through scripts and remove space checking for specific items
- fill evo method ids
- more inclusion rules
- complete levelup movesets
- advertise on ds romhacking servers
- post MonochromeScriptAssembler to ds romhacking servers
- make simple script compiler, use for starting season, season npc vanish, tmhm hunt npc vanish, and other future stuff
- change rules dict to being filled on the way
- organize imports for type hints behind TYPE_CHECKING
- pitch webhost and template yaml notes, both individual, but template copying from webhost by default
- Fix locations in pokédex if something written to encounter tables
- route 18 reappearing and undella bay reappearing items get still detected after pickup
- BizHawk 2.11 having issues with modded gen 5 roms

# Single reports, cannot recreate, need to wait for more reports

- not receiving key items?
- scientist nathan no text after battle?
- ranger claude talking french after battle?
- Some hidden items are not checkable immediately?
- grunt in pinwheel forest with vanilla dragon skull not talking anymore after obtaining the dragon skull
- stone grunts not disappearing?
- sequence break problem with npcs not moving, see channel
- incredibly low catch chances? idk how that could be related to the apworld in any way
- plando items having issues? plandoing basic badge into abyssal ruins sometimes raises fillerrors about this item not being placeable
- route 8 bianca items logic, apparently said to be in logic without light/dark stone, but blocked by grunts wanting the stone
