#!/usr/bin/env python
from weather_provider_libraries.core.provider import WeatherProvider

"""A Class module for the WeatherProviderManager class."""


class WeatherProviderManager:
    """A Manager for Weather Provider classes that allows uniform access to all attached providers.

    The goal of this class is to provide a way to register and access multiple WeatherProvider classes
    in a uniform way. This allows for easy access to multiple providers without needing to know the
    specifics of each provider.

    Attributes
    ----------
        providers (dict[str, WeatherProvider]):
                A dictionary of WeatherProvider classes, with the key being the name of the provider and the value
                being the provider class.

    """

    def __init__(self) -> None:
        """Class initializer."""
        self.providers: dict[str, WeatherProvider] = {}

    def load_providers(self, providers_to_load: list[str] | None = None) -> None:
        """..."""
        if providers_to_load is None:
            providers_to_load = self._find_possible_providers()

        for provider in providers_to_load:
            self._load_provider(provider)

    @staticmethod
    def _find_possible_providers() -> list[str]:
        """..."""
        list_of_possible_providers: list[str] = []

        # 1. Check for all possible providers via the weather_provider_sources package based on naming conventions
        ...
        # 2. Add matching providers to the list_of_possible_providers

        return list_of_possible_providers

    def _load_provider(self, provider: str) -> None:
        """..."""
        # 1. Import the WeatherProvider module
        ...

        # 2. Instantiate and add the provider to the providers dictionary
        ...
        provider_instance: WeatherProvider = WeatherProvider()
        self.providers[provider_instance.id] = provider_instance
