# Important stuff


# 0.4.0

## APWorld

- make dexsanity hints correctly replace grass with cave etc.
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
    - Evolve when possible
    - Force fully evolved 
      - Level threshold adjustable
    - Type themed
    - Themed gym trainers (also make gym leaders and elite 4 always have themed teams)
    - Prevent early Wonder Guard and fixed HP attacks
    - Rivals keep starter
  - Adjust Levels
    - Trainer team (weaker pokémon used in postgame area battles for similar base stats)
- Randomization Blacklist
  - Wild pokémon
    - Will still put every species that is required to be randomized and base stage into at least one slot
    - Ignores Encounter Plando
  - Trainer pokémon
- Funny dialogue
  - Funny mode, including actually funny things
  - Efficient mode, making a lot of text shorter
- Text Plando
  - Text extractor in client

## Rom

- fix gym leaders not being present in their gyms
- fast travel npc in chargestone cave from south to north if battled N at north exit
- maybe juniper seen count locations can check for national seen? look at cedric in mistralton city and both other dex seen locations
- make mom stop the player at the door and say funny things for certain reusable tm choices
- skip musical tutorial, because some players have problems
- disable dig outside of battle when season patch included, as a temporary bandaid fix
- cold storage sage first sequence after ghetsis makes second sequence not possible since spawn flag is permanently set
- wingull giving TM without grams

## Both

- add now-possible locations
- a way to check whether map or fly menu is opened
- Running shoes as an item, making mom cutscene on route 2 a check
- Bianca route 8 trigger right before door, how should I fix it?
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
