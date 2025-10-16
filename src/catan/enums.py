from enum import Enum, auto
from typing import Final
from __future__ import annotations

class Resource(Enum):
    WOOD = "wood"
    BRICK = "brick"
    ORE = "ore"
    SHEEP = "sheep"
    WHEAT = "wheat"

ALL_RESOURCES = Final[tuple[Resource, ...]] = (Resource.WOOD, Resource.BRICK, Resource.ORE, Resource.SHEEP, Resource.WHEAT) # Faster and takes less memory than list

class Build(Enum):
    ROAD = "road"
    SETTLEMENT = "settlement"
    CITY = "city"
    DEV_CARD = "dev_card"

class PortType(Enum):
    THREE_TO_ONE = "3:1"
    BRICK = "brick"
    WOOD = "wood"
    ORE = "ore"
    SHEEP = "sheep"
    WHEAT = "wheat"

class ActionType(Enum):
    PLACE_INITIAL_SETTLEMENT = auto()
    PLACE_INITIAL_ROAD = auto()
    ROLL_DICE = auto()
    MOVE_ROBBER = auto()
    STEAL = auto()
    BUILD_ROAD = auto()
    BUILD_SETTLEMENT = auto()
    BUILD_CITY = auto()
    BUY_DEV_CARD = auto() 
    BUY_DEV_CARD = auto()
    PLAY_DEV_CARD = auto()
    TRADE_BANK = auto()
    TRADE_PLAYER = auto()
    END_TURN = auto()