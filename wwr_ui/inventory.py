# Can't use logic's PROGRESS_ITEMS because there's some items that we can't start with, and also because progressive items require special handling.
REGULAR_ITEMS = [
    "Telescope",
    "Magic Armor",
    "Hero's Charm",
    "Tingle Tuner",
    "Grappling Hook",
    "Power Bracelets",
    "Iron Boots",
    "Boomerang",
    "Hookshot",
    "Bombs",
    "Skull Hammer",
    "Deku Leaf",
    "Mirror Shield",
    "Hurricane Spin",
    "Din's Pearl",
    "Farore's Pearl",
    "Nayru's Pearl",
    "Command Melody",
    "Earth God's Lyric",
    "Wind God's Aria",
    "Spoils Bag",
    "Bait Bag",
    "Delivery Bag",
    "Note to Mom",
    "Maggie's Letter",
    "Moblin's Letter",
    "Cabana Deed",
    "Ghost Ship Chart",
    "Empty Bottle",
    "Magic Meter Upgrade",
    "Wind Waker",
    "Wind's Requiem",
    "Ballad of Gales",
    "Song of Passing",
    "Boat's Sail",
]
REGULAR_ITEMS.sort()

PROGRESSIVE_ITEMS = (
    ["Progressive Bow"] * 3
    + ["Progressive Quiver"] * 2
    + ["Progressive Bomb Bag"] * 2
    + ["Progressive Wallet"] * 2
    + ["Progressive Picto Box"] * 2
    + ["Progressive Sword"] * 3
)
PROGRESSIVE_ITEMS.sort()

DUNGEON_NONPROGRESS_ITEMS = (
    ["DRC Dungeon Map", "DRC Compass"]
    + ["FW Dungeon Map", "FW Compass"]
    + ["TotG Dungeon Map", "TotG Compass"]
    + ["FF Dungeon Map", "FF Compass"]
    + ["ET Dungeon Map", "ET Compass"]
    + ["WT Dungeon Map", "WT Compass"]
)

STNDRD_ITEMS = REGULAR_ITEMS + DUNGEON_NONPROGRESS_ITEMS
STNDRD_ITEMS.sort()
INVENTORY_ITEMS = PROGRESSIVE_ITEMS + STNDRD_ITEMS
INVENTORY_ITEMS.sort()

DEFAULT_STARTING_ITEMS = [
    "Wind Waker",
    "Wind's Requiem",
    "Ballad of Gales",
    "Song of Passing",
    "Boat's Sail",
    "DRC Dungeon Map",
    "FW Dungeon Map",
    "TotG Dungeon Map",
    "FF Dungeon Map",
    "ET Dungeon Map",
    "WT Dungeon Map",
]
DEFAULT_STARTING_ITEMS.sort()

QUEST_ITEMS = [
    "Din's Pearl",
    "Farore's Pearl",
    "Nayru's Pearl",
    "Command Melody",
    "Earth God's Lyric",
    "Wind God's Aria",
]

KEY_ITEMS = [
    "Bait Bag",
    "Bombs",
    "Boomerang",
    "Progressive Bow",
    "Deku Leaf",
    "Delivery Bag",
    "Cabana Deed",
    "Maggie's Letter",
    "Moblin's Letter",
    "Note to Mom",
    "Empty Bottle",
    "Ghost Ship Chart",
    "Grappling Hook",
    "Hookshot",
    "Iron Boots",
    "Magic Meter Upgrade",
    "Mirror Shield",
    "Progressive Picto Box",
    "Power Bracelets",
    "Skull Hammer",
    "Spoils Bag",
    "Progressive Sword",
    "Progressive Wallet",
]
# KEY_ITEMS.sort()

NONKEY_ITEMS = [
    "Progressive Bomb Bag",
    "Hero's Charm",
    "Hurricane Spin",
    "Magic Armor",
    "Progressive Quiver",
    "Telescope",
    "Tingle Tuner",
]
NONKEY_ITEMS.sort()

SORT_KEY = KEY_ITEMS + QUEST_ITEMS + DUNGEON_NONPROGRESS_ITEMS + NONKEY_ITEMS
# INVENTORY_ITEMS.sort(key=lambda x:SORT_KEY.index(x))
