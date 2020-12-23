################################################################################
## Form generated from reading UI file 'randomizer_window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scroll_for_main = QScrollArea(self.centralwidget)
        self.scroll_for_main.setObjectName("scroll_for_main")
        self.scroll_for_main.setFrameShape(QFrame.NoFrame)
        self.scroll_for_main.setWidgetResizable(True)
        self.content_for_main_scroll = QWidget()
        self.content_for_main_scroll.setObjectName("content_for_main_scroll")
        self.content_for_main_scroll.setGeometry(QRect(0, 0, 944, 753))
        self.verticalLayout_4 = QVBoxLayout(self.content_for_main_scroll)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tab_for_main = QTabWidget(self.content_for_main_scroll)
        self.tab_for_main.setObjectName("tab_for_main")
        self.tab_for_main.setEnabled(True)
        self.tab_for_settings = QWidget()
        self.tab_for_settings.setObjectName("tab_for_settings")
        self.verticalLayout_2 = QVBoxLayout(self.tab_for_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grid_for_paths = QGridLayout()
        self.grid_for_paths.setObjectName("grid_for_paths")
        self.seed = QLineEdit(self.tab_for_settings)
        self.seed.setObjectName("seed")

        self.grid_for_paths.addWidget(self.seed, 2, 1, 1, 1)

        self.label_for_clean = QLabel(self.tab_for_settings)
        self.label_for_clean.setObjectName("label_for_clean")

        self.grid_for_paths.addWidget(self.label_for_clean, 0, 0, 1, 1)

        self.clean_iso_path = QLineEdit(self.tab_for_settings)
        self.clean_iso_path.setObjectName("clean_iso_path")

        self.grid_for_paths.addWidget(self.clean_iso_path, 0, 1, 1, 1)

        self.label_for_output = QLabel(self.tab_for_settings)
        self.label_for_output.setObjectName("label_for_output")

        self.grid_for_paths.addWidget(self.label_for_output, 1, 0, 1, 1)

        self.output_folder = QLineEdit(self.tab_for_settings)
        self.output_folder.setObjectName("output_folder")

        self.grid_for_paths.addWidget(self.output_folder, 1, 1, 1, 1)

        self.output_folder_browse_button = QPushButton(self.tab_for_settings)
        self.output_folder_browse_button.setObjectName("output_folder_browse_button")

        self.grid_for_paths.addWidget(self.output_folder_browse_button, 1, 2, 1, 1)

        self.label_for_seed = QLabel(self.tab_for_settings)
        self.label_for_seed.setObjectName("label_for_seed")

        self.grid_for_paths.addWidget(self.label_for_seed, 2, 0, 1, 1)

        self.generate_seed_button = QPushButton(self.tab_for_settings)
        self.generate_seed_button.setObjectName("generate_seed_button")

        self.grid_for_paths.addWidget(self.generate_seed_button, 2, 2, 1, 1)

        self.clean_iso_path_browse_button = QPushButton(self.tab_for_settings)
        self.clean_iso_path_browse_button.setObjectName("clean_iso_path_browse_button")

        self.grid_for_paths.addWidget(self.clean_iso_path_browse_button, 0, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.grid_for_paths)

        self.grid_for_logic = QGridLayout()
        self.grid_for_logic.setObjectName("grid_for_logic")
        self.logic_mod = QComboBox(self.tab_for_settings)
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.setObjectName("logic_mod")
        self.logic_mod.setMinimumSize(QSize(70, 0))
        self.logic_mod.setDuplicatesEnabled(False)
        self.logic_mod.setFrame(True)

        self.grid_for_logic.addWidget(self.logic_mod, 0, 3, 1, 1)

        self.logic_spacer = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_logic.addItem(self.logic_spacer, 0, 4, 1, 1)

        self.right_spacer = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_logic.addItem(self.right_spacer, 0, 5, 1, 1)

        self.label_for_logic = QLabel(self.tab_for_settings)
        self.label_for_logic.setObjectName("label_for_logic")
        self.label_for_logic.setEnabled(True)
        self.label_for_logic.setMaximumSize(QSize(489, 16777215))

        self.grid_for_logic.addWidget(self.label_for_logic, 0, 2, 1, 1)

        self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_logic.addItem(self.left_spacer, 0, 1, 1, 1)

        self.logic_desc = QLabel(self.tab_for_settings)
        self.logic_desc.setObjectName("logic_desc")

        self.grid_for_logic.addWidget(self.logic_desc, 1, 2, 1, 3)


        self.verticalLayout_2.addLayout(self.grid_for_logic)

        self.group_for_locations = QGroupBox(self.tab_for_settings)
        self.group_for_locations.setObjectName("group_for_locations")
        self.gridLayout_2 = QGridLayout(self.group_for_locations)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progression_battlesquid = QCheckBox(self.group_for_locations)
        self.progression_battlesquid.setObjectName("progression_battlesquid")

        self.gridLayout_2.addWidget(self.progression_battlesquid, 6, 2, 1, 1)

        self.progression_minigames = QCheckBox(self.group_for_locations)
        self.progression_minigames.setObjectName("progression_minigames")

        self.gridLayout_2.addWidget(self.progression_minigames, 6, 0, 1, 1)

        self.progression_big_octos_gunboats = QCheckBox(self.group_for_locations)
        self.progression_big_octos_gunboats.setObjectName("progression_big_octos_gunboats")

        self.gridLayout_2.addWidget(self.progression_big_octos_gunboats, 7, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.progression_expensive_purchases = QCheckBox(self.group_for_locations)
        self.progression_expensive_purchases.setObjectName("progression_expensive_purchases")
        self.progression_expensive_purchases.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_expensive_purchases, 6, 4, 1, 1)

        self.progression_great_fairies = QCheckBox(self.group_for_locations)
        self.progression_great_fairies.setObjectName("progression_great_fairies")
        self.progression_great_fairies.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_great_fairies, 1, 0, 1, 1)

        self.progression_combat_secret_caves = QCheckBox(self.group_for_locations)
        self.progression_combat_secret_caves.setObjectName("progression_combat_secret_caves")

        self.gridLayout_2.addWidget(self.progression_combat_secret_caves, 0, 4, 1, 1)

        self.progression_savage_labyrinth = QCheckBox(self.group_for_locations)
        self.progression_savage_labyrinth.setObjectName("progression_savage_labyrinth")

        self.gridLayout_2.addWidget(self.progression_savage_labyrinth, 0, 6, 1, 1)

        self.progression_misc = QCheckBox(self.group_for_locations)
        self.progression_misc.setObjectName("progression_misc")
        self.progression_misc.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_misc, 1, 4, 1, 1)

        self.progression_puzzle_secret_caves = QCheckBox(self.group_for_locations)
        self.progression_puzzle_secret_caves.setObjectName("progression_puzzle_secret_caves")
        self.progression_puzzle_secret_caves.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_puzzle_secret_caves, 0, 2, 1, 1)

        self.progression_eye_reef_chests = QCheckBox(self.group_for_locations)
        self.progression_eye_reef_chests.setObjectName("progression_eye_reef_chests")

        self.gridLayout_2.addWidget(self.progression_eye_reef_chests, 7, 6, 1, 1)

        self.progression_mail = QCheckBox(self.group_for_locations)
        self.progression_mail.setObjectName("progression_mail")

        self.gridLayout_2.addWidget(self.progression_mail, 4, 6, 1, 1)

        self.progression_tingle_chests = QCheckBox(self.group_for_locations)
        self.progression_tingle_chests.setObjectName("progression_tingle_chests")

        self.gridLayout_2.addWidget(self.progression_tingle_chests, 1, 6, 1, 1)

        self.progression_island_puzzles = QCheckBox(self.group_for_locations)
        self.progression_island_puzzles.setObjectName("progression_island_puzzles")

        self.gridLayout_2.addWidget(self.progression_island_puzzles, 6, 6, 1, 1)

        self.progression_platforms_rafts = QCheckBox(self.group_for_locations)
        self.progression_platforms_rafts.setObjectName("progression_platforms_rafts")

        self.gridLayout_2.addWidget(self.progression_platforms_rafts, 7, 0, 1, 1)

        self.progression_long_sidequests = QCheckBox(self.group_for_locations)
        self.progression_long_sidequests.setObjectName("progression_long_sidequests")

        self.gridLayout_2.addWidget(self.progression_long_sidequests, 4, 2, 1, 1)

        self.progression_dungeons = QCheckBox(self.group_for_locations)
        self.progression_dungeons.setObjectName("progression_dungeons")
        self.progression_dungeons.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_dungeons, 0, 0, 1, 1)

        self.progression_short_sidequests = QCheckBox(self.group_for_locations)
        self.progression_short_sidequests.setObjectName("progression_short_sidequests")

        self.gridLayout_2.addWidget(self.progression_short_sidequests, 4, 0, 1, 1)

        self.progression_treasure_charts = QCheckBox(self.group_for_locations)
        self.progression_treasure_charts.setObjectName("progression_treasure_charts")

        self.gridLayout_2.addWidget(self.progression_treasure_charts, 9, 2, 1, 1)

        self.progression_spoils_trading = QCheckBox(self.group_for_locations)
        self.progression_spoils_trading.setObjectName("progression_spoils_trading")

        self.gridLayout_2.addWidget(self.progression_spoils_trading, 4, 4, 1, 1)

        self.progression_triforce_charts = QCheckBox(self.group_for_locations)
        self.progression_triforce_charts.setObjectName("progression_triforce_charts")

        self.gridLayout_2.addWidget(self.progression_triforce_charts, 9, 0, 1, 1)

        self.progression_submarines = QCheckBox(self.group_for_locations)
        self.progression_submarines.setObjectName("progression_submarines")
        self.progression_submarines.setChecked(False)

        self.gridLayout_2.addWidget(self.progression_submarines, 7, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 0, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 5, 1, 1)

        self.progression_free_gifts = QCheckBox(self.group_for_locations)
        self.progression_free_gifts.setObjectName("progression_free_gifts")
        self.progression_free_gifts.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_free_gifts, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.group_for_locations)

        self.group_for_settings_secondary = QGroupBox(self.tab_for_settings)
        self.group_for_settings_secondary.setObjectName("group_for_settings_secondary")
        self.gridLayout_3 = QGridLayout(self.group_for_settings_secondary)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.layout_for_race_mode = QHBoxLayout()
        self.layout_for_race_mode.setObjectName("layout_for_race_mode")
        self.label_for_race_mode = QLabel(self.group_for_settings_secondary)
        self.label_for_race_mode.setObjectName("label_for_race_mode")

        self.layout_for_race_mode.addWidget(self.label_for_race_mode)

        self.spacer_for_race_mode = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_race_mode.addItem(self.spacer_for_race_mode)

        self.race_mode = QComboBox(self.group_for_settings_secondary)
        self.race_mode.addItem("")
        self.race_mode.addItem("")
        self.race_mode.addItem("")
        self.race_mode.setObjectName("race_mode")

        self.layout_for_race_mode.addWidget(self.race_mode)


        self.gridLayout_3.addLayout(self.layout_for_race_mode, 2, 2, 1, 1)

        self.layout_for_num_dungeon_race_mode = QHBoxLayout()
        self.layout_for_num_dungeon_race_mode.setObjectName("layout_for_num_dungeon_race_mode")
        self.label_for_num_dungeon_race_mode = QLabel(self.group_for_settings_secondary)
        self.label_for_num_dungeon_race_mode.setObjectName("label_for_num_dungeon_race_mode")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_for_num_dungeon_race_mode.sizePolicy().hasHeightForWidth())
        self.label_for_num_dungeon_race_mode.setSizePolicy(sizePolicy)

        self.layout_for_num_dungeon_race_mode.addWidget(self.label_for_num_dungeon_race_mode)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_num_dungeon_race_mode.addItem(self.horizontalSpacer_6)

        self.num_dungeon_race_mode = QComboBox(self.group_for_settings_secondary)
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.setObjectName("num_dungeon_race_mode")
        self.num_dungeon_race_mode.setMaximumSize(QSize(84, 16777215))

        self.layout_for_num_dungeon_race_mode.addWidget(self.num_dungeon_race_mode)

        self.widget_9 = QWidget(self.group_for_settings_secondary)
        self.widget_9.setObjectName("widget_9")

        self.layout_for_num_dungeon_race_mode.addWidget(self.widget_9)


        self.gridLayout_3.addLayout(self.layout_for_num_dungeon_race_mode, 2, 4, 1, 1)

        self.layout_for_starting_triforce_shards = QHBoxLayout()
        self.layout_for_starting_triforce_shards.setObjectName("layout_for_starting_triforce_shards")
        self.label_for_num_starting_triforce_shards = QLabel(self.group_for_settings_secondary)
        self.label_for_num_starting_triforce_shards.setObjectName("label_for_num_starting_triforce_shards")
        sizePolicy.setHeightForWidth(self.label_for_num_starting_triforce_shards.sizePolicy().hasHeightForWidth())
        self.label_for_num_starting_triforce_shards.setSizePolicy(sizePolicy)

        self.layout_for_starting_triforce_shards.addWidget(self.label_for_num_starting_triforce_shards)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_starting_triforce_shards.addItem(self.horizontalSpacer_5)

        self.num_starting_triforce_shards = QComboBox(self.group_for_settings_secondary)
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.setObjectName("num_starting_triforce_shards")
        self.num_starting_triforce_shards.setMaximumSize(QSize(84, 16777215))

        self.layout_for_starting_triforce_shards.addWidget(self.num_starting_triforce_shards)

        self.widget = QWidget(self.group_for_settings_secondary)
        self.widget.setObjectName("widget")

        self.layout_for_starting_triforce_shards.addWidget(self.widget)


        self.gridLayout_3.addLayout(self.layout_for_starting_triforce_shards, 1, 4, 1, 1)

        self.compass_map_pool_with_keys = QCheckBox(self.group_for_settings_secondary)
        self.compass_map_pool_with_keys.setObjectName("compass_map_pool_with_keys")

        self.gridLayout_3.addWidget(self.compass_map_pool_with_keys, 2, 0, 1, 1)

        self.layout_for_sword = QHBoxLayout()
        self.layout_for_sword.setObjectName("layout_for_sword")
        self.label_for_sword_mode = QLabel(self.group_for_settings_secondary)
        self.label_for_sword_mode.setObjectName("label_for_sword_mode")

        self.layout_for_sword.addWidget(self.label_for_sword_mode)

        self.spacer_for_sword_mode = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_sword.addItem(self.spacer_for_sword_mode)

        self.sword_mode = QComboBox(self.group_for_settings_secondary)
        self.sword_mode.addItem("")
        self.sword_mode.addItem("")
        self.sword_mode.addItem("")
        self.sword_mode.setObjectName("sword_mode")

        self.layout_for_sword.addWidget(self.sword_mode)


        self.gridLayout_3.addLayout(self.layout_for_sword, 0, 0, 1, 1)

        self.layout_for_randomize_entrances = QHBoxLayout()
        self.layout_for_randomize_entrances.setObjectName("layout_for_randomize_entrances")
        self.label_for_randomize_entrances = QLabel(self.group_for_settings_secondary)
        self.label_for_randomize_entrances.setObjectName("label_for_randomize_entrances")

        self.layout_for_randomize_entrances.addWidget(self.label_for_randomize_entrances)

        self.spacer_for_randomize_entrances = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_randomize_entrances.addItem(self.spacer_for_randomize_entrances)

        self.randomize_entrances = QComboBox(self.group_for_settings_secondary)
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.setObjectName("randomize_entrances")

        self.layout_for_randomize_entrances.addWidget(self.randomize_entrances)

        self.widget_2 = QWidget(self.group_for_settings_secondary)
        self.widget_2.setObjectName("widget_2")

        self.layout_for_randomize_entrances.addWidget(self.widget_2)


        self.gridLayout_3.addLayout(self.layout_for_randomize_entrances, 0, 2, 1, 3)

        self.add_shortcut_warps_between_dungeons = QCheckBox(self.group_for_settings_secondary)
        self.add_shortcut_warps_between_dungeons.setObjectName("add_shortcut_warps_between_dungeons")

        self.gridLayout_3.addWidget(self.add_shortcut_warps_between_dungeons, 1, 2, 1, 1)

        self.keylunacy = QCheckBox(self.group_for_settings_secondary)
        self.keylunacy.setObjectName("keylunacy")

        self.gridLayout_3.addWidget(self.keylunacy, 1, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 1, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_17, 1, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.group_for_settings_secondary)

        self.group_for_convenience = QGroupBox(self.tab_for_settings)
        self.group_for_convenience.setObjectName("group_for_convenience")
        self.gridLayout_4 = QGridLayout(self.group_for_convenience)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_13, 0, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_15, 0, 5, 1, 1)

        self.instant_text_boxes = QCheckBox(self.group_for_convenience)
        self.instant_text_boxes.setObjectName("instant_text_boxes")
        self.instant_text_boxes.setChecked(True)

        self.gridLayout_4.addWidget(self.instant_text_boxes, 0, 4, 1, 1)

        self.swift_sail = QCheckBox(self.group_for_convenience)
        self.swift_sail.setObjectName("swift_sail")
        self.swift_sail.setChecked(True)

        self.gridLayout_4.addWidget(self.swift_sail, 0, 0, 1, 1)

        self.randomize_starting_island = QCheckBox(self.group_for_convenience)
        self.randomize_starting_island.setObjectName("randomize_starting_island")

        self.gridLayout_4.addWidget(self.randomize_starting_island, 1, 0, 1, 1)

        self.reveal_full_sea_chart = QCheckBox(self.group_for_convenience)
        self.reveal_full_sea_chart.setObjectName("reveal_full_sea_chart")
        self.reveal_full_sea_chart.setChecked(True)

        self.gridLayout_4.addWidget(self.reveal_full_sea_chart, 0, 2, 1, 1)

        self.randomize_charts = QCheckBox(self.group_for_convenience)
        self.randomize_charts.setObjectName("randomize_charts")

        self.gridLayout_4.addWidget(self.randomize_charts, 1, 2, 1, 1)

        self.skip_rematch_bosses = QCheckBox(self.group_for_convenience)
        self.skip_rematch_bosses.setObjectName("skip_rematch_bosses")
        self.skip_rematch_bosses.setChecked(True)

        self.gridLayout_4.addWidget(self.skip_rematch_bosses, 0, 6, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_14, 0, 3, 1, 1)

        self.remove_title_and_ending_videos = QCheckBox(self.group_for_convenience)
        self.remove_title_and_ending_videos.setObjectName("remove_title_and_ending_videos")
        self.remove_title_and_ending_videos.setChecked(True)

        self.gridLayout_4.addWidget(self.remove_title_and_ending_videos, 1, 4, 1, 1)

        self.layout_for_convenience_option = QHBoxLayout()
        self.layout_for_convenience_option.setObjectName("layout_for_convenience_option")
        self.convenience_option_label = QLabel(self.group_for_convenience)
        self.convenience_option_label.setObjectName("convenience_option_label")

        self.layout_for_convenience_option.addWidget(self.convenience_option_label)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_convenience_option.addItem(self.horizontalSpacer_21)

        self.convenience_option = QComboBox(self.group_for_convenience)
        self.convenience_option.addItem("")
        self.convenience_option.addItem("")
        self.convenience_option.addItem("")
        self.convenience_option.addItem("")
        self.convenience_option.setObjectName("convenience_option")

        self.layout_for_convenience_option.addWidget(self.convenience_option)


        self.gridLayout_4.addLayout(self.layout_for_convenience_option, 1, 6, 1, 1)


        self.verticalLayout_2.addWidget(self.group_for_convenience)

        self.group_for_advanced = QGroupBox(self.tab_for_settings)
        self.group_for_advanced.setObjectName("group_for_advanced")
        self.gridLayout_6 = QGridLayout(self.group_for_advanced)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.randomize_music = QCheckBox(self.group_for_advanced)
        self.randomize_music.setObjectName("randomize_music")
        self.randomize_music.setEnabled(True)

        self.gridLayout_6.addWidget(self.randomize_music, 1, 2, 1, 1)

        self.disable_tingle_chests_with_tingle_bombs = QCheckBox(self.group_for_advanced)
        self.disable_tingle_chests_with_tingle_bombs.setObjectName("disable_tingle_chests_with_tingle_bombs")
        self.disable_tingle_chests_with_tingle_bombs.setEnabled(False)
        self.disable_tingle_chests_with_tingle_bombs.setChecked(True)

        self.gridLayout_6.addWidget(self.disable_tingle_chests_with_tingle_bombs, 1, 6, 1, 1)

        self.do_not_generate_spoiler_log = QCheckBox(self.group_for_advanced)
        self.do_not_generate_spoiler_log.setObjectName("do_not_generate_spoiler_log")
        self.do_not_generate_spoiler_log.setChecked(True)

        self.gridLayout_6.addWidget(self.do_not_generate_spoiler_log, 0, 0, 1, 1)

        self.randomize_enemy_palettes = QCheckBox(self.group_for_advanced)
        self.randomize_enemy_palettes.setObjectName("randomize_enemy_palettes")
        self.randomize_enemy_palettes.setEnabled(True)

        self.gridLayout_6.addWidget(self.randomize_enemy_palettes, 0, 4, 1, 1)

        self.randomize_enemies = QCheckBox(self.group_for_advanced)
        self.randomize_enemies.setObjectName("randomize_enemies")
        self.randomize_enemies.setEnabled(False)

        self.gridLayout_6.addWidget(self.randomize_enemies, 1, 4, 1, 1)

        self.invert_camera_x_axis = QCheckBox(self.group_for_advanced)
        self.invert_camera_x_axis.setObjectName("invert_camera_x_axis")

        self.gridLayout_6.addWidget(self.invert_camera_x_axis, 0, 6, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 0, 3, 1, 1)

        self.remove_music = QCheckBox(self.group_for_advanced)
        self.remove_music.setObjectName("remove_music")

        self.gridLayout_6.addWidget(self.remove_music, 0, 2, 1, 1)

        self.widget_3 = QWidget(self.group_for_advanced)
        self.widget_3.setObjectName("widget_3")

        self.gridLayout_6.addWidget(self.widget_3, 0, 8, 1, 1)

        self.widget_4 = QWidget(self.group_for_advanced)
        self.widget_4.setObjectName("widget_4")

        self.gridLayout_6.addWidget(self.widget_4, 0, 9, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_12, 0, 5, 1, 1)


        self.verticalLayout_2.addWidget(self.group_for_advanced)

        self.tab_for_main.addTab(self.tab_for_settings, "")
        self.tab_for_starting_items = QWidget()
        self.tab_for_starting_items.setObjectName("tab_for_starting_items")
        self.tab_for_starting_items.setEnabled(True)
        self.verticalLayout_10 = QVBoxLayout(self.tab_for_starting_items)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.layout_for_starting_items = QHBoxLayout()
        self.layout_for_starting_items.setObjectName("layout_for_starting_items")
        self.layout_for_randomized_gear = QVBoxLayout()
        self.layout_for_randomized_gear.setObjectName("layout_for_randomized_gear")
        self.label_for_randomized_gear = QLabel(self.tab_for_starting_items)
        self.label_for_randomized_gear.setObjectName("label_for_randomized_gear")

        self.layout_for_randomized_gear.addWidget(self.label_for_randomized_gear)

        self.randomized_gear = QListView(self.tab_for_starting_items)
        self.randomized_gear.setObjectName("randomized_gear")
        self.randomized_gear.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.randomized_gear.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.layout_for_randomized_gear.addWidget(self.randomized_gear)


        self.layout_for_starting_items.addLayout(self.layout_for_randomized_gear)

        self.layout_for_gear_options = QVBoxLayout()
        self.layout_for_gear_options.setObjectName("layout_for_gear_options")
        self.spacer_for_options_gear_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_gear_options.addItem(self.spacer_for_options_gear_top)

        self.remove_gear = QPushButton(self.tab_for_starting_items)
        self.remove_gear.setObjectName("remove_gear")
        self.remove_gear.setMinimumSize(QSize(0, 80))

        self.layout_for_gear_options.addWidget(self.remove_gear)

        self.add_gear = QPushButton(self.tab_for_starting_items)
        self.add_gear.setObjectName("add_gear")
        self.add_gear.setMinimumSize(QSize(0, 80))

        self.layout_for_gear_options.addWidget(self.add_gear)

        self.spacer_for_options_gear_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_gear_options.addItem(self.spacer_for_options_gear_bottom)


        self.layout_for_starting_items.addLayout(self.layout_for_gear_options)

        self.layout_for_starting_gear = QVBoxLayout()
        self.layout_for_starting_gear.setObjectName("layout_for_starting_gear")
        self.label_for_starting_gear = QLabel(self.tab_for_starting_items)
        self.label_for_starting_gear.setObjectName("label_for_starting_gear")

        self.layout_for_starting_gear.addWidget(self.label_for_starting_gear)

        self.starting_gear = QListView(self.tab_for_starting_items)
        self.starting_gear.setObjectName("starting_gear")
        self.starting_gear.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.starting_gear.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.layout_for_starting_gear.addWidget(self.starting_gear)


        self.layout_for_starting_items.addLayout(self.layout_for_starting_gear)


        self.verticalLayout_10.addLayout(self.layout_for_starting_items)

        self.layout_for_starting_health = QHBoxLayout()
        self.layout_for_starting_health.setObjectName("layout_for_starting_health")
        self.label_for_base_health = QLabel(self.tab_for_starting_items)
        self.label_for_base_health.setObjectName("label_for_base_health")

        self.layout_for_starting_health.addWidget(self.label_for_base_health)

        self.starting_bh = QSpinBox(self.tab_for_starting_items)
        self.starting_bh.setObjectName("starting_bh")
        self.starting_bh.setMinimum(1)
        self.starting_bh.setMaximum(3)
        self.starting_bh.setValue(3)

        self.layout_for_starting_health.addWidget(self.starting_bh)

        self.label_for_heart_container = QLabel(self.tab_for_starting_items)
        self.label_for_heart_container.setObjectName("label_for_heart_container")

        self.layout_for_starting_health.addWidget(self.label_for_heart_container)

        self.starting_hcs = QSpinBox(self.tab_for_starting_items)
        self.starting_hcs.setObjectName("starting_hcs")
        self.starting_hcs.setEnabled(True)
        self.starting_hcs.setBaseSize(QSize(0, 0))
        self.starting_hcs.setLayoutDirection(Qt.LeftToRight)
        self.starting_hcs.setMaximum(6)
        self.starting_hcs.setValue(0)
        self.starting_hcs.setDisplayIntegerBase(10)

        self.layout_for_starting_health.addWidget(self.starting_hcs)

        self.label_for_heart_piece = QLabel(self.tab_for_starting_items)
        self.label_for_heart_piece.setObjectName("label_for_heart_piece")

        self.layout_for_starting_health.addWidget(self.label_for_heart_piece)

        self.starting_pohs = QSpinBox(self.tab_for_starting_items)
        self.starting_pohs.setObjectName("starting_pohs")
        self.starting_pohs.setMaximum(44)
        self.starting_pohs.setValue(0)
        self.starting_pohs.setDisplayIntegerBase(10)

        self.layout_for_starting_health.addWidget(self.starting_pohs)

        self.current_health = QLabel(self.tab_for_starting_items)
        self.current_health.setObjectName("current_health")

        self.layout_for_starting_health.addWidget(self.current_health)

        self.spacer_for_health_end = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_starting_health.addItem(self.spacer_for_health_end)

        self.no_heart_in_pool = QCheckBox(self.tab_for_starting_items)
        self.no_heart_in_pool.setObjectName("no_heart_in_pool")

        self.layout_for_starting_health.addWidget(self.no_heart_in_pool)


        self.verticalLayout_10.addLayout(self.layout_for_starting_health)

        self.tab_for_main.addTab(self.tab_for_starting_items, "")
        self.tab_for_model_customization = QWidget()
        self.tab_for_model_customization.setObjectName("tab_for_model_customization")
        self.verticalLayout_3 = QVBoxLayout(self.tab_for_model_customization)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.grid_for_model_general_options = QGridLayout()
        self.grid_for_model_general_options.setObjectName("grid_for_model_general_options")
        self.layout_for_custom_player_model = QHBoxLayout()
        self.layout_for_custom_player_model.setObjectName("layout_for_custom_player_model")
        self.label_for_custom_player_model = QLabel(self.tab_for_model_customization)
        self.label_for_custom_player_model.setObjectName("label_for_custom_player_model")

        self.layout_for_custom_player_model.addWidget(self.label_for_custom_player_model)

        self.custom_player_model = QComboBox(self.tab_for_model_customization)
        self.custom_player_model.setObjectName("custom_player_model")

        self.layout_for_custom_player_model.addWidget(self.custom_player_model)


        self.grid_for_model_general_options.addLayout(self.layout_for_custom_player_model, 0, 0, 1, 1)

        self.layout_for_custom_preset = QHBoxLayout()
        self.layout_for_custom_preset.setObjectName("layout_for_custom_preset")
        self.label_for_custom_color_preset = QLabel(self.tab_for_model_customization)
        self.label_for_custom_color_preset.setObjectName("label_for_custom_color_preset")

        self.layout_for_custom_preset.addWidget(self.label_for_custom_color_preset)

        self.custom_color_preset = QComboBox(self.tab_for_model_customization)
        self.custom_color_preset.setObjectName("custom_color_preset")

        self.layout_for_custom_preset.addWidget(self.custom_color_preset)


        self.grid_for_model_general_options.addLayout(self.layout_for_custom_preset, 1, 0, 1, 1)

        self.layout_for_sail_color = QHBoxLayout()
        self.layout_for_sail_color.setObjectName("layout_for_sail_color")
        self.label_for_sail_color = QLabel(self.tab_for_model_customization)
        self.label_for_sail_color.setObjectName("label_for_sail_color")

        self.layout_for_sail_color.addWidget(self.label_for_sail_color)

        self.sail_color = QComboBox(self.tab_for_model_customization)
        self.sail_color.addItem("")
        self.sail_color.addItem("")
        self.sail_color.addItem("")
        self.sail_color.setObjectName("sail_color")

        self.layout_for_sail_color.addWidget(self.sail_color)


        self.grid_for_model_general_options.addLayout(self.layout_for_sail_color, 3, 0, 1, 1)

        self.disable_custom_player_items = QCheckBox(self.tab_for_model_customization)
        self.disable_custom_player_items.setObjectName("disable_custom_player_items")

        self.grid_for_model_general_options.addWidget(self.disable_custom_player_items, 0, 3, 1, 1)

        self.disable_custom_player_voice = QCheckBox(self.tab_for_model_customization)
        self.disable_custom_player_voice.setObjectName("disable_custom_player_voice")

        self.grid_for_model_general_options.addWidget(self.disable_custom_player_voice, 1, 3, 1, 1)

        self.player_in_casual_clothes = QCheckBox(self.tab_for_model_customization)
        self.player_in_casual_clothes.setObjectName("player_in_casual_clothes")

        self.grid_for_model_general_options.addWidget(self.player_in_casual_clothes, 0, 2, 1, 1)

        self.layout_for_randomize_color_options = QHBoxLayout()
        self.layout_for_randomize_color_options.setObjectName("layout_for_randomize_color_options")
        self.randomize_all_custom_colors_together = QPushButton(self.tab_for_model_customization)
        self.randomize_all_custom_colors_together.setObjectName("randomize_all_custom_colors_together")

        self.layout_for_randomize_color_options.addWidget(self.randomize_all_custom_colors_together)

        self.randomize_all_custom_colors_separately = QPushButton(self.tab_for_model_customization)
        self.randomize_all_custom_colors_separately.setObjectName("randomize_all_custom_colors_separately")

        self.layout_for_randomize_color_options.addWidget(self.randomize_all_custom_colors_separately)


        self.grid_for_model_general_options.addLayout(self.layout_for_randomize_color_options, 2, 0, 1, 1)

        self.disable_custom_boat = QCheckBox(self.tab_for_model_customization)
        self.disable_custom_boat.setObjectName("disable_custom_boat")

        self.grid_for_model_general_options.addWidget(self.disable_custom_boat, 2, 3, 1, 1)

        self.custom_model_comment = QLabel(self.tab_for_model_customization)
        self.custom_model_comment.setObjectName("custom_model_comment")
        self.custom_model_comment.setMaximumSize(QSize(810, 16777215))
        self.custom_model_comment.setWordWrap(True)

        self.grid_for_model_general_options.addWidget(self.custom_model_comment, 1, 2, 2, 1)

        self.layout_for_custom_bck_entry = QHBoxLayout()
        self.layout_for_custom_bck_entry.setObjectName("layout_for_custom_bck_entry")
        self.label_for_custom_bck_entry = QLabel(self.tab_for_model_customization)
        self.label_for_custom_bck_entry.setObjectName("label_for_custom_bck_entry")
        self.label_for_custom_bck_entry.setEnabled(False)

        self.layout_for_custom_bck_entry.addWidget(self.label_for_custom_bck_entry)

        self.custom_bck_entry = QComboBox(self.tab_for_model_customization)
        self.custom_bck_entry.addItem("")
        self.custom_bck_entry.addItem("")
        self.custom_bck_entry.addItem("")
        self.custom_bck_entry.addItem("")
        self.custom_bck_entry.setObjectName("custom_bck_entry")
        self.custom_bck_entry.setEnabled(False)

        self.layout_for_custom_bck_entry.addWidget(self.custom_bck_entry)


        self.grid_for_model_general_options.addLayout(self.layout_for_custom_bck_entry, 3, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.grid_for_model_general_options)

        self.layout_for_color_visualizer = QHBoxLayout()
        self.layout_for_color_visualizer.setObjectName("layout_for_color_visualizer")
        self.layout_for_color_layout = QVBoxLayout()
        self.layout_for_color_layout.setObjectName("layout_for_color_layout")
        self.custom_colors_layout = QVBoxLayout()
        self.custom_colors_layout.setObjectName("custom_colors_layout")

        self.layout_for_color_layout.addLayout(self.custom_colors_layout)

        self.spacer_for_colors_layout = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_color_layout.addItem(self.spacer_for_colors_layout)


        self.layout_for_color_visualizer.addLayout(self.layout_for_color_layout)

        self.layout_for_model_preview = QVBoxLayout()
        self.layout_for_model_preview.setObjectName("layout_for_model_preview")
        self.custom_model_preview_label = QLabel(self.tab_for_model_customization)
        self.custom_model_preview_label.setObjectName("custom_model_preview_label")

        self.layout_for_model_preview.addWidget(self.custom_model_preview_label)

        self.spacer_for_model_preview = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_model_preview.addItem(self.spacer_for_model_preview)


        self.layout_for_color_visualizer.addLayout(self.layout_for_model_preview)


        self.verticalLayout_3.addLayout(self.layout_for_color_visualizer)

        self.tab_for_main.addTab(self.tab_for_model_customization, "")

        self.verticalLayout_4.addWidget(self.tab_for_main)

        self.scroll_for_main.setWidget(self.content_for_main_scroll)

        self.verticalLayout.addWidget(self.scroll_for_main)

        self.option_description = QLabel(self.centralwidget)
        self.option_description.setObjectName("option_description")
        self.option_description.setMinimumSize(QSize(0, 32))
        self.option_description.setWordWrap(True)

        self.verticalLayout.addWidget(self.option_description)

        self.layout_for_permalink = QHBoxLayout()
        self.layout_for_permalink.setObjectName("layout_for_permalink")
        self.label_for_permalink = QLabel(self.centralwidget)
        self.label_for_permalink.setObjectName("label_for_permalink")

        self.layout_for_permalink.addWidget(self.label_for_permalink)

        self.permalink = QLineEdit(self.centralwidget)
        self.permalink.setObjectName("permalink")

        self.layout_for_permalink.addWidget(self.permalink)


        self.verticalLayout.addLayout(self.layout_for_permalink)

        self.update_checker_label = QLabel(self.centralwidget)
        self.update_checker_label.setObjectName("update_checker_label")
        self.update_checker_label.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.update_checker_label)

        self.layout_for_finalize = QHBoxLayout()
        self.layout_for_finalize.setObjectName("layout_for_finalize")
        self.about_button = QPushButton(self.centralwidget)
        self.about_button.setObjectName("about_button")

        self.layout_for_finalize.addWidget(self.about_button)

        self.horizontal_brake_for_about = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_finalize.addItem(self.horizontal_brake_for_about)

        self.reset_settings_to_default = QPushButton(self.centralwidget)
        self.reset_settings_to_default.setObjectName("reset_settings_to_default")
        self.reset_settings_to_default.setMinimumSize(QSize(180, 0))

        self.layout_for_finalize.addWidget(self.reset_settings_to_default)

        self.horizontal_brake_for_reset = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_finalize.addItem(self.horizontal_brake_for_reset)

        self.randomize_button = QPushButton(self.centralwidget)
        self.randomize_button.setObjectName("randomize_button")

        self.layout_for_finalize.addWidget(self.randomize_button)


        self.verticalLayout.addLayout(self.layout_for_finalize)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_for_main.setCurrentIndex(0)
        self.logic_mod.setCurrentIndex(1)
        self.race_mode.setCurrentIndex(0)
        self.custom_bck_entry.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Wind Waker Randomizer", None))
        self.label_for_clean.setText(QCoreApplication.translate("MainWindow", "Clean WW ISO", None))
        self.label_for_output.setText(QCoreApplication.translate("MainWindow", "Output Folder", None))
        self.output_folder_browse_button.setText(QCoreApplication.translate("MainWindow", "Browse", None))
        self.label_for_seed.setText(QCoreApplication.translate("MainWindow", "Seed (optional)", None))
        self.generate_seed_button.setText(QCoreApplication.translate("MainWindow", "New seed", None))
        self.clean_iso_path_browse_button.setText(QCoreApplication.translate("MainWindow", "Browse", None))
        self.logic_mod.setItemText(0, QCoreApplication.translate("MainWindow", "Glitchless \u2013 Beginner", None))
        self.logic_mod.setItemText(1, QCoreApplication.translate("MainWindow", "Glitchless \u2013 Standard", None))
        self.logic_mod.setItemText(2, QCoreApplication.translate("MainWindow", "Glitched \u2013 Trivial", None))
        self.logic_mod.setItemText(3, QCoreApplication.translate("MainWindow", "Glitched \u2013 Moderate", None))
        self.logic_mod.setItemText(4, QCoreApplication.translate("MainWindow", "Glitched \u2013 Lunatic", None))
        self.logic_mod.setItemText(5, QCoreApplication.translate("MainWindow", "Glitched \u2013 No Logic", None))

        self.logic_mod.setCurrentText(QCoreApplication.translate("MainWindow", "Glitchless \u2013 Standard", None))
        self.label_for_logic.setText(QCoreApplication.translate("MainWindow", "Logic Type", None))
        self.logic_desc.setText("")
        self.group_for_locations.setTitle(QCoreApplication.translate("MainWindow", "Where Should Progress Items Appear?", None))
        self.progression_battlesquid.setText(QCoreApplication.translate("MainWindow", "Battlesquid Minigame", None))
        self.progression_minigames.setText(QCoreApplication.translate("MainWindow", "Minigames", None))
        self.progression_big_octos_gunboats.setText(QCoreApplication.translate("MainWindow", "Big Octos and Gunboats", None))
        self.progression_expensive_purchases.setText(QCoreApplication.translate("MainWindow", "Expensive Purchases", None))
        self.progression_great_fairies.setText(QCoreApplication.translate("MainWindow", "Great Fairies", None))
        self.progression_combat_secret_caves.setText(QCoreApplication.translate("MainWindow", "Combat Secret Caves", None))
        self.progression_savage_labyrinth.setText(QCoreApplication.translate("MainWindow", "Savage Labyrinth", None))
        self.progression_misc.setText(QCoreApplication.translate("MainWindow", "Miscellaneous", None))
        self.progression_puzzle_secret_caves.setText(QCoreApplication.translate("MainWindow", "Puzzle Secret Caves", None))
        self.progression_eye_reef_chests.setText(QCoreApplication.translate("MainWindow", "Eye Reef Chests", None))
        self.progression_mail.setText(QCoreApplication.translate("MainWindow", "Mail", None))
        self.progression_tingle_chests.setText(QCoreApplication.translate("MainWindow", "Tingle Chests", None))
        self.progression_island_puzzles.setText(QCoreApplication.translate("MainWindow", "Island Puzzles", None))
        self.progression_platforms_rafts.setText(QCoreApplication.translate("MainWindow", "Lookout Platforms and Rafts", None))
        self.progression_long_sidequests.setText(QCoreApplication.translate("MainWindow", "Long Sidequests", None))
        self.progression_dungeons.setText(QCoreApplication.translate("MainWindow", "Dungeons", None))
        self.progression_short_sidequests.setText(QCoreApplication.translate("MainWindow", "Short Sidequests", None))
        self.progression_treasure_charts.setText(QCoreApplication.translate("MainWindow", "Sunken Treasure (From Treasure Charts)", None))
        self.progression_spoils_trading.setText(QCoreApplication.translate("MainWindow", "Spoils Trading", None))
        self.progression_triforce_charts.setText(QCoreApplication.translate("MainWindow", "Sunken Treasure (From Triforce Charts)", None))
        self.progression_submarines.setText(QCoreApplication.translate("MainWindow", "Submarines", None))
        self.progression_free_gifts.setText(QCoreApplication.translate("MainWindow", "Free Gifts", None))
        self.group_for_settings_secondary.setTitle(QCoreApplication.translate("MainWindow", "Dungeon Randomization Options", None))
        self.label_for_race_mode.setText(QCoreApplication.translate("MainWindow", "Dungeon Mode", None))
        self.race_mode.setItemText(0, QCoreApplication.translate("MainWindow", "Default", None))
        self.race_mode.setItemText(1, QCoreApplication.translate("MainWindow", "Mixed", None))
        self.race_mode.setItemText(2, QCoreApplication.translate("MainWindow", "Race", None))

        self.label_for_num_dungeon_race_mode.setText(QCoreApplication.translate("MainWindow", "Dungeon Number", None))
        self.num_dungeon_race_mode.setItemText(0, QCoreApplication.translate("MainWindow", "1", None))
        self.num_dungeon_race_mode.setItemText(1, QCoreApplication.translate("MainWindow", "2", None))
        self.num_dungeon_race_mode.setItemText(2, QCoreApplication.translate("MainWindow", "3", None))
        self.num_dungeon_race_mode.setItemText(3, QCoreApplication.translate("MainWindow", "4", None))
        self.num_dungeon_race_mode.setItemText(4, QCoreApplication.translate("MainWindow", "5", None))
        self.num_dungeon_race_mode.setItemText(5, QCoreApplication.translate("MainWindow", "6", None))
        self.num_dungeon_race_mode.setItemText(6, QCoreApplication.translate("MainWindow", "Random", None))

        self.num_dungeon_race_mode.setCurrentText(QCoreApplication.translate("MainWindow", "1", None))
        self.label_for_num_starting_triforce_shards.setText(QCoreApplication.translate("MainWindow", "Starting Triforce Shards", None))
        self.num_starting_triforce_shards.setItemText(0, QCoreApplication.translate("MainWindow", "0", None))
        self.num_starting_triforce_shards.setItemText(1, QCoreApplication.translate("MainWindow", "1", None))
        self.num_starting_triforce_shards.setItemText(2, QCoreApplication.translate("MainWindow", "2", None))
        self.num_starting_triforce_shards.setItemText(3, QCoreApplication.translate("MainWindow", "3", None))
        self.num_starting_triforce_shards.setItemText(4, QCoreApplication.translate("MainWindow", "4", None))
        self.num_starting_triforce_shards.setItemText(5, QCoreApplication.translate("MainWindow", "5", None))
        self.num_starting_triforce_shards.setItemText(6, QCoreApplication.translate("MainWindow", "6", None))
        self.num_starting_triforce_shards.setItemText(7, QCoreApplication.translate("MainWindow", "7", None))
        self.num_starting_triforce_shards.setItemText(8, QCoreApplication.translate("MainWindow", "8", None))
        self.num_starting_triforce_shards.setItemText(9, QCoreApplication.translate("MainWindow", "Random", None))
        self.num_starting_triforce_shards.setItemText(10, QCoreApplication.translate("MainWindow", "Mirror Dungeon Number", None))

        self.num_starting_triforce_shards.setCurrentText(QCoreApplication.translate("MainWindow", "0", None))
        self.compass_map_pool_with_keys.setText(QCoreApplication.translate("MainWindow", "Pool Dungeon Items with Keys", None))
        self.label_for_sword_mode.setText(QCoreApplication.translate("MainWindow", "Sword Mode", None))
        self.sword_mode.setItemText(0, QCoreApplication.translate("MainWindow", "Start with Hero's Sword", None))
        self.sword_mode.setItemText(1, QCoreApplication.translate("MainWindow", "No Starting Sword", None))
        self.sword_mode.setItemText(2, QCoreApplication.translate("MainWindow", "Swordless", None))

        self.label_for_randomize_entrances.setText(QCoreApplication.translate("MainWindow", "Randomize Entrances", None))
        self.randomize_entrances.setItemText(0, QCoreApplication.translate("MainWindow", "Disabled", None))
        self.randomize_entrances.setItemText(1, QCoreApplication.translate("MainWindow", "Dungeons", None))
        self.randomize_entrances.setItemText(2, QCoreApplication.translate("MainWindow", "Secret Caves", None))
        self.randomize_entrances.setItemText(3, QCoreApplication.translate("MainWindow", "Dungeons & Secret Caves (Separately)", None))
        self.randomize_entrances.setItemText(4, QCoreApplication.translate("MainWindow", "Dungeons & Secret Caves (Together)", None))

        self.add_shortcut_warps_between_dungeons.setText(QCoreApplication.translate("MainWindow", "Add Shortcuts Between Dungeons", None))
        self.keylunacy.setText(QCoreApplication.translate("MainWindow", "Key-Lunacy", None))
        self.group_for_convenience.setTitle(QCoreApplication.translate("MainWindow", "Additional Options", None))
        self.instant_text_boxes.setText(QCoreApplication.translate("MainWindow", "Instant Text Boxes", None))
        self.swift_sail.setText(QCoreApplication.translate("MainWindow", "Use Swift Sail", None))
        self.randomize_starting_island.setText(QCoreApplication.translate("MainWindow", "Randomize Starting Island", None))
        self.reveal_full_sea_chart.setText(QCoreApplication.translate("MainWindow", "Reveal Full Sea Chart", None))
        self.randomize_charts.setText(QCoreApplication.translate("MainWindow", "Randomize Charts", None))
        self.skip_rematch_bosses.setText(QCoreApplication.translate("MainWindow", "Skip Boss Rematches", None))
        self.remove_title_and_ending_videos.setText(QCoreApplication.translate("MainWindow", "Remove Title and Ending Videos", None))
        self.convenience_option_label.setText(QCoreApplication.translate("MainWindow", "Item Pool", None))
        self.convenience_option.setItemText(0, QCoreApplication.translate("MainWindow", "Default", None))
        self.convenience_option.setItemText(1, QCoreApplication.translate("MainWindow", "Convenient", None))
        self.convenience_option.setItemText(2, QCoreApplication.translate("MainWindow", "Plentiful", None))
        self.convenience_option.setItemText(3, QCoreApplication.translate("MainWindow", "Plentiful and Convenient", None))

        self.group_for_advanced.setTitle(QCoreApplication.translate("MainWindow", "Advanced Options", None))
        self.randomize_music.setText(QCoreApplication.translate("MainWindow", "Randomize Music", None))
        self.disable_tingle_chests_with_tingle_bombs.setText(QCoreApplication.translate("MainWindow", "Tingle Bombs Don't Open Tingle Chests", None))
        self.do_not_generate_spoiler_log.setText(QCoreApplication.translate("MainWindow", "Do Not Generate Spoiler Log", None))
        self.randomize_enemy_palettes.setText(QCoreApplication.translate("MainWindow", "Randomize Enemy Palettes", None))
        self.randomize_enemies.setText(QCoreApplication.translate("MainWindow", "Randomize Enemy Locations", None))
        self.invert_camera_x_axis.setText(QCoreApplication.translate("MainWindow", "Invert Camera X-Axis", None))
        self.remove_music.setText(QCoreApplication.translate("MainWindow", "Remove Music", None))
        self.tab_for_main.setTabText(self.tab_for_main.indexOf(self.tab_for_settings), QCoreApplication.translate("MainWindow", "Randomizer Settings", None))
        self.label_for_randomized_gear.setText(QCoreApplication.translate("MainWindow", "Randomized Gear", None))
        self.remove_gear.setText(QCoreApplication.translate("MainWindow", "<-", None))
        self.add_gear.setText(QCoreApplication.translate("MainWindow", "->", None))
        self.label_for_starting_gear.setText(QCoreApplication.translate("MainWindow", "Starting Gear", None))
        self.label_for_base_health.setText(QCoreApplication.translate("MainWindow", "Base Health", None))
        self.label_for_heart_container.setText(QCoreApplication.translate("MainWindow", "Heart Containers", None))
        self.label_for_heart_piece.setText(QCoreApplication.translate("MainWindow", "Heart Pieces", None))
        self.current_health.setText(QCoreApplication.translate("MainWindow", "Current Starting Health: 3 hearts", None))
        self.no_heart_in_pool.setText(QCoreApplication.translate("MainWindow", "No Additional Health in Pool", None))
        self.tab_for_main.setTabText(self.tab_for_main.indexOf(self.tab_for_starting_items), QCoreApplication.translate("MainWindow", "Starting Items", None))
        self.label_for_custom_player_model.setText(QCoreApplication.translate("MainWindow", "Player Model", None))
        self.label_for_custom_color_preset.setText(QCoreApplication.translate("MainWindow", "Color Preset", None))
        self.label_for_sail_color.setText(QCoreApplication.translate("MainWindow", "Sail", None))
        self.sail_color.setItemText(0, QCoreApplication.translate("MainWindow", "Sail of Red Lions", None))
        self.sail_color.setItemText(1, QCoreApplication.translate("MainWindow", "Swift Sail", None))
        self.sail_color.setItemText(2, QCoreApplication.translate("MainWindow", "Sail of Lions' Pride", None))

        self.disable_custom_player_items.setText(QCoreApplication.translate("MainWindow", "Disable Custom Items", None))
        self.disable_custom_player_voice.setText(QCoreApplication.translate("MainWindow", "Disable Custom Voice", None))
        self.player_in_casual_clothes.setText(QCoreApplication.translate("MainWindow", "Casual Clothes", None))
        self.randomize_all_custom_colors_together.setText(QCoreApplication.translate("MainWindow", "Randomize Colors Orderly", None))
        self.randomize_all_custom_colors_separately.setText(QCoreApplication.translate("MainWindow", "Randomize Colors Chaotically", None))
        self.disable_custom_boat.setText(QCoreApplication.translate("MainWindow", "Disable Custom Boat", None))
        self.custom_model_comment.setText("")
        self.label_for_custom_bck_entry.setText(QCoreApplication.translate("MainWindow", "Animation Deviation", None))
        self.custom_bck_entry.setItemText(0, QCoreApplication.translate("MainWindow", "No Changes", None))
        self.custom_bck_entry.setItemText(1, QCoreApplication.translate("MainWindow", "Not Gameplay", None))
        self.custom_bck_entry.setItemText(2, QCoreApplication.translate("MainWindow", "Basic Gameplay", None))
        self.custom_bck_entry.setItemText(3, QCoreApplication.translate("MainWindow", "All", None))

        self.custom_model_preview_label.setText("")
        self.tab_for_main.setTabText(self.tab_for_main.indexOf(self.tab_for_model_customization), QCoreApplication.translate("MainWindow", "Player Customization", None))
        self.option_description.setText("")
        self.label_for_permalink.setText(QCoreApplication.translate("MainWindow", "Permalink (copy paste to share your settings):", None))
        self.update_checker_label.setText(QCoreApplication.translate("MainWindow", "Checking for updates to the randomizer...", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.reset_settings_to_default.setText(QCoreApplication.translate("MainWindow", "Reset All Settings to Default", None))
        self.randomize_button.setText(QCoreApplication.translate("MainWindow", "Randomize", None))
    # retranslateUi

