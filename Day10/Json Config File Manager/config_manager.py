import json
from pathlib import Path

# json.load() → Read JSON file and convert it into a Python dictionary.
# json.dump() → Write a Python dictionary into a JSON file.

DEFAULTS = {
    "theme": "light",
    "language": "en",
    "font_size": 14,
    "auto_save": True
}


class ConfigManager:

    def __init__(self, path="config.json"):
        self.path = Path(path)
        self.config = self._load()

    def _load(self):
        """Load configuration from file or create it with defaults."""
        if not self.path.exists():
            self._save(DEFAULTS)
            return DEFAULTS.copy()

        with open(self.path, "r") as f:
            return json.load(f)

    def _save(self, data):
        """Save configuration to JSON file."""
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def get(self, key, default=None):
        """Return the value for the given key."""
        return self.config.get(key, default)

    def set(self, key, value):
        """Add or update a configuration value and save immediately."""
        self.config[key] = value
        self._save(self.config)

    def delete(self, key) -> bool:
        """
        Delete a configuration key.
        Returns True if the key existed, otherwise False.
        """
        if key in self.config:
            del self.config[key]
            self._save(self.config)
            return True
        return False

    def reset(self):
        """Restore configuration to default values."""
        self.config = DEFAULTS.copy()
        self._save(self.config)


def main():
    config = ConfigManager()

    print("Initial Config:")
    print(config.config)

    print("\nTheme:")
    print(config.get("theme"))

    print("\nUpdating Theme...")
    config.set("theme", "dark")
    print(config.config)

    print("\nAdding New Key...")
    config.set("notifications", True)
    print(config.config)

    print("\nDeleting language...")
    print("Deleted:", config.delete("language"))
    print(config.config)

    print("\nDeleting invalid key...")
    print("Deleted:", config.delete("xyz"))

    print("\nResetting...")
    config.reset()
    print(config.config)


if __name__ == "__main__":
    main()