import pygame
from dataclasses import dataclass
from typing import Optional, Callable
import maps

TILE_SIZE = 1000
LINE_WIDTH = 120
LINE_LENGTH = 420
START_FINISH_TILE = (0, 0)


def build_start_finish_line(tile_position=START_FINISH_TILE,
                            line_length: int = LINE_LENGTH,
                            line_width: int = LINE_WIDTH,
                            orientation: Optional[str] = None) -> pygame.Rect:
    """
    Build a start/finish line rectangle anchored to a map tile.

    The line is centered within the provided tile. If no orientation is
    provided, the tile rotation controls whether the line is vertical or
    horizontal to align with the rendered track piece.
    """
    tile_x, tile_y = tile_position
    tile_rotation = maps.map_1_rot[tile_y][tile_x] % 2
    tile_origin_x = tile_x * TILE_SIZE
    tile_origin_y = tile_y * TILE_SIZE

    is_horizontal = (orientation == "horizontal") or (
        orientation is None and tile_rotation == 1
    )

    if is_horizontal:
        width, height = line_length, line_width
    else:
        width, height = line_width, line_length

    offset_x = tile_origin_x + (TILE_SIZE - width) // 2
    offset_y = tile_origin_y + (TILE_SIZE - height) // 2
    return pygame.Rect(offset_x, offset_y, width, height)


@dataclass
class RaceState:
    max_laps: int = 3
    lap_count: int = 0
    lap_started: bool = False
    race_finished: bool = False

    def reset(self) -> None:
        self.lap_count = 0
        self.lap_started = False
        self.race_finished = False

    def process_crossing(self, car_rect: pygame.Rect, finish_rect: pygame.Rect,
                         on_first_lap_start: Optional[Callable[[], None]] = None) -> None:
        if self.race_finished:
            # Preserve whether the vehicle remains on the line without
            # reprocessing completions.
            self.lap_started = finish_rect.colliderect(car_rect)
            return

        if finish_rect.colliderect(car_rect):
            if not self.lap_started:
                self.lap_count += 1
                self.lap_started = True
                if self.lap_count == 1 and on_first_lap_start is not None:
                    on_first_lap_start()
                if self.lap_count >= self.max_laps:
                    self.race_finished = True
        else:
            self.lap_started = False
