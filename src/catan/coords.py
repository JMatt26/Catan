from __future__ import annotations
from dataclasses import dataclass

# Create a lightweight, memory-efficient, and immutable data container with fixed attributes
@dataclass(frozen=True, slots=True)
class Hex:
    q: int
    r: int
    # axial neighbors
    def neighbors(self) -> list["Hex"]:
        return [
            Hex(self.q + 1, self.r    ),
            Hex(self.q + 1, self.r - 1),
            Hex(self.q    , self.r - 1),
            Hex(self.q - 1, self.r    ),
            Hex(self.q - 1, self.r + 1),
            Hex(self.q    , self.r + 1),
        ]


@dataclass(frozen=True, slots=True)
class Vertex:
    # A vertex can be represented as (hex, corner_index 0..5)
    # corner 0 corresponds to edge between directions (0,5) in axial; clockwise thereafter
    h: Hex
    corner: int  # 0..5


@dataclass(frozen=True, slots=True)
class Edge:
    # An edge can be represented as (hex, edge_index 0..5), where edge i is between corners i and (i+1)%6
    h: Hex
    edge: int  # 0..5
