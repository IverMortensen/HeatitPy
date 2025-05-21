"""A client library for accessing Heatit WiFi Panel"""

from importlib.metadata import version, PackageNotFoundError
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)

try:
    # must match the [tool.poetry].name in pyproject.toml
    __version__ = version("heatitpy")
except PackageNotFoundError:
    # fallback if someone is running from source without installing
    __version__ = "0.0.0"
