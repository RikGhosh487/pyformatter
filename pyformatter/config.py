import logging
import os
import tomllib


def load_config(tool_name: str, logger: logging.Logger) -> dict:
    """Load configuration for the specified tool from pyproject.toml.

    This function reads the configuration for a given tool from the
    pyproject.toml file. It expects the configuration to be structured
    under the `[tool.<tool_name>]` section.

    Args:
        tool_name (str): The name of the tool to load configuration for.
        logger (logging.Logger): Logger instance for logging messages.

    Returns:
        dict: The configuration dictionary for the specified tool.

    Raises:
        TypeError: If `tool_name` is not a string.
    """
    if not isinstance(tool_name, str):
        raise TypeError("tool_name must be a string")

    if not os.path.exists("pyproject.toml"):
        return {}

    with open("pyproject.toml", "rb") as f:
        try:
            config = tomllib.load(f)
        except tomllib.TOMLDecodeError as e:
            logger.warning(f"Failed to decode pyproject.toml: {e}")
            return {}

    return config.get("tool", {}).get(tool_name, {})
