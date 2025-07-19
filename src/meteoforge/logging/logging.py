#  SPDX-FileCopyrightText: 2024-2025 Copyright Contributors to the MeteoForge project
#  SPDX-License-Identifier: MPL-2.0

import logging
import logging.config
import os

import yaml


def setup_logging(config_path: str | None = None):
    """Set up project logging using the 'logging_config.yaml' config file."""
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), "logging_config.yaml")
    if os.path.exists(config_path):
        with open(config_path, encoding="utf-8") as file:
            config = yaml.safe_load(file)
            logging.config.dictConfig(config)
    else:
        raise FileNotFoundError(f"Logging configuration file not found: {config_path}")


setup_logging()

logger = logging.getLogger("meteoforge")
logger.info("MeteoForge logging initialized.")
logger.info("Logging level set to %s", logger.getEffectiveLevel())
