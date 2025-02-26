#!/usr/bin/env python


class WeatherModel:
    """..."""

    def __init__(self, name: str) -> None:
        """..."""
        self.name = name

    def get_weather(self, city: str) -> dict[str, str]:
        """..."""
        raise NotImplementedError()

    def get_name(self) -> str:
        """..."""
        return self.name
