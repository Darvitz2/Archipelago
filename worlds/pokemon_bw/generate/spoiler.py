from typing import TextIO, TYPE_CHECKING

if TYPE_CHECKING:
    from .. import PokemonBWWorld


def write_spoiler_encounter(world: "PokemonBWWorld", spoiler_handle: TextIO) -> None:
    from ..data.locations.encounters.region_connections import connections, connection_by_region
    from ..data.pokemon.species import by_id
    from ..data.pokemon.pokedex import by_number

    methods: dict[str, list[str]] = {name: [] for name in connections}
    for name, data in world.wild_encounter.items():
        region = name[:name.rfind(" ")]
        methods[connection_by_region[region]].append(by_id[data.species_id])

    spoiler_handle.write(f"Pokemon locations ({world.player_name}):\n")
    for method, species in methods.items():
        spoiler_handle.write(method+": "+(", ".join(species)))

    for name, data in world.static_encounter.items():
        spoiler_handle.write(name+": "+by_id[data.species_id])
    for name, data in world.trade_encounter.items():
        spoiler_handle.write(name+": "+by_id[data.species_id]+" for "+by_number[data.wanted_dex_number])


def write_spoiler_trainer(world: "PokemonBWWorld", spoiler_handle: TextIO) -> None:
    pass
