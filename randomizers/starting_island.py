import tweaks
from class_ms import YamlOrderedDictLoader

import os
from paths import DATA_PATH
import yaml
from collections import OrderedDict

def randomize_starting_island(self):
  possible_starting_islands = list(range(1, 49+1))

  # Don't allow Forsaken Fortress to be the starting island.
  # It wouldn't really cause problems, but it would be weird because you normally need bombs to get in, and you would need to use Ballad of Gales to get out.
  possible_starting_islands.remove(1)

  starting_island_room_index = self.rng.choice(possible_starting_islands)

  if not self.dry_run:
    tweaks.set_new_game_starting_room_index(self, starting_island_room_index)
    tweaks.change_ship_starting_island(self, starting_island_room_index)

  self.starting_island_index = starting_island_room_index
  #print(str(starting_island_room_index))
  return starting_island_room_index

def get_starting_island(self,starting_island_room_index):

  with open(os.path.join(DATA_PATH, "island_data.txt")) as f:
    island_data = yaml.load(f, YamlOrderedDictLoader)

  starting_island_name = island_data[starting_island_room_index]["Long Name"]
  island_macro = f"Can Travel to {starting_island_name}"

  req_string = "Nothing"
  self.set_macro(island_macro, req_string)
  #print(str(starting_island_room_index))
