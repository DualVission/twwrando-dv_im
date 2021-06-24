from collections import OrderedDict

HARD_REQUIRED_ITEMS = [
  "Telescope",
  "Wind Waker",
  "Grappling Hook",
  "Boomerang",
  "Hookshot",

  "Triforce Shard 1",
  "Triforce Shard 2",
  "Triforce Shard 3",
  "Triforce Shard 4",
  "Triforce Shard 5",
  "Triforce Shard 6",
  "Triforce Shard 7",
  "Triforce Shard 8",

  "Wind's Requiem",
  "Ballad of Gales",

  "Boat's Sail"
]+ \
  ["Progressive Sword"]*4 + \
  ["Progressive Shield"]*2 + \
  ["Progressive Bow"]*3

SOFT_REQUIRED_ITEMS = [
  "Tingle Tuner",

  "Spoils Bag",
  "Power Bracelets",
  "Iron Boots",
  "Bait Bag",
  "Delivery Bag",
  "Bombs",
  "Skull Hammer",
  "Deku Leaf",

  "Nayru's Pearl",
  "Din's Pearl",
  "Farore's Pearl",

  "Command Melody",
  "Earth God's Lyric",
  "Wind God's Aria",
  "Song of Passing",

  "Note to Mom",
  "Maggie's Letter",
  "Moblin's Letter",
  "Cabana Deed",

  "Dragon Tingle Statue",
  "Forbidden Tingle Statue",
  "Goddess Tingle Statue",
  "Earth Tingle Statue",
  "Wind Tingle Statue",

  "Progressive Bomb Bag",
  "Progressive Quiver",
  "Hurricane Spin",

  "Magic Meter Upgrade",
  "Ghost Ship Chart",
] + \
  ["Progressive Wallet"]*2 + \
  ["Progressive Picto Box"]*2 + \
  ["Empty Bottle"]*4

PROGRESS_ITEMS = HARD_REQUIRED_ITEMS + SOFT_REQUIRED_ITEMS

NONPROGRESS_ITEMS = [
  "Magic Armor",
  "Hero's Charm",

  "Fill-Up Coupon",

  "Submarine Chart",
  "Beedle's Chart",
  "Platform Chart",
  "Light Ring Chart",
  "Secret Cave Chart",
  "Great Fairy Chart",
  "Octo Chart",
  "Tingle's Chart",

]
HEALTH_ITEMS = ["Piece of Heart"]*44 + \
  ["Heart Container"]*6

CONSUMABLE_ITEMS = \
   1 * ["Green Rupee"] + \
   2 * ["Blue Rupee"] + \
   3 * ["Yellow Rupee"] + \
   5 * ["Red Rupee"] + \
  10 * ["Purple Rupee"] + \
  15 * ["Orange Rupee"] + \
  15 * ["Silver Rupee"] + \
   1 * ["Rainbow Rupee"] + \
  \
   9 * ["Joy Pendant"] + \
   9 * ["Skull Necklace"] + \
   1 * ["Boko Baba Seed"] + \
   9 * ["Golden Feather"] + \
   3 * ["Knight's Crest"] + \
   1 * ["Red Chu Jelly"] + \
   1 * ["Green Chu Jelly"] + \
  \
   1 * ["All-Purpose Bait"] + \
   4 * ["Hyoi Pear"]
# (Note: Blue Chu Jelly is not included as it is specially coded and would cause issues if randomly placed as a field item.)

CONVENIENCE_ITEMS = [
  "Progressive Bomb Bag",
  "Progressive Quiver",
]

XTRA_ITEMS = [
  "Progressive Sword",
  "Progressive Bow",
  "Progressive Wallet",
  "Progressive Picto Box",
  "Hookshot",
  "Rainbow Rupee",
  "Progressive Bomb Bag",
  "Progressive Quiver",
  "Magic Meter Upgrade",
]

# Once all the items that have a fixed number per seed are used up, this list is used.
# Unlike the other lists, this one does not have items removed from it as they are placed.
# The number of each item in this list is instead its weighting relative to the other items in the list.
DUPLICATABLE_CONSUMABLE_ITEMS = \
   3 * ["Yellow Rupee"] + \
   7 * ["Red Rupee"] + \
  10 * ["Purple Rupee"] + \
  15 * ["Orange Rupee"] + \
  \
   3 * ["Joy Pendant"]

FARMABLE_ITEMS = \
   3 * ["Yellow Rupee"] + \
   4 * ["Red Rupee"] + \
   7 * ["Purple Rupee"] + \
   3 * ["Orange Rupee"] + \
   1 * ["Silver Rupee"] + \
  \
   5 * ["Joy Pendant"] + \
   2 * ["Golden Feather"] + \
   2 * ["Green Chu Jelly"] + \
   2 * ["Skull Necklace"]

DUNGEON_PROGRESS_ITEMS = []
POSSIBLE_DUNGEON_PROGRESS_ITEMS = OrderedDict()
POSSIBLE_DUNGEON_PROGRESS_ITEMS["Dragon Roost Cavern"] = ["DRC Big Key"]  *1 + ["DRC Small Key"] *4
POSSIBLE_DUNGEON_PROGRESS_ITEMS["Forbidden Woods"]     = ["FW Big Key"]   *1 + ["FW Small Key"] *1
POSSIBLE_DUNGEON_PROGRESS_ITEMS["Tower of the Gods"]   = ["TotG Big Key"] *1 + ["TotG Small Key"] *2
POSSIBLE_DUNGEON_PROGRESS_ITEMS["Forsaken Fortress"]   = ["FF Big Key"]   *0 + ["FF Small Key"] *0
POSSIBLE_DUNGEON_PROGRESS_ITEMS["Earth Temple"]        = ["ET Big Key"]   *1 + ["ET Small Key"] *3
POSSIBLE_DUNGEON_PROGRESS_ITEMS["Wind Temple"]         = ["WT Big Key"]   *1 + ["WT Small Key"] *2

POSSIBLE_DUNGEON_PROGRESS_ITEMS_LIST = []
for dungeons in POSSIBLE_DUNGEON_PROGRESS_ITEMS:
  POSSIBLE_DUNGEON_PROGRESS_ITEMS_LIST+=POSSIBLE_DUNGEON_PROGRESS_ITEMS[dungeons]

DUNGEON_NONPROGRESS_ITEMS = \
  ["DRC Dungeon Map", "DRC Compass"] + \
  ["FW Dungeon Map", "FW Compass"] + \
  ["TotG Dungeon Map", "TotG Compass"] + \
  ["FF Dungeon Map", "FF Compass"] + \
  ["ET Dungeon Map", "ET Compass"] + \
  ["WT Dungeon Map", "WT Compass"]
