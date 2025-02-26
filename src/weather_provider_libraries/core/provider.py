#!/usr/bin/env python


class WeatherProvider:
    """..."""

    def __init__(self) -> None:
        """..."""
        self.id: str = ""
        self.name: str = ""

    def get_weather(self, city: str) -> dict[str, str]:
        """..."""
        raise NotImplementedError()

    def get_name(self) -> str:
        """..."""
        return self.name
