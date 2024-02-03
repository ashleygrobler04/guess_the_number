import json


class JConfig:
    """A simple configuration manager that allows you to make use of json for configuration."""

    def __init__(self, configFile):
        """
        Initialize the JConfig instance.

        Parameters:
        - configFile (str): The path to the configuration file.
        """
        self.configFile = configFile
        self.configDict = {}
        self.initialize()

    def initialize(self):
        """Load the configuration from the file, creating an empty one if the file doesn't exist."""
        try:
            with open(self.configFile, "r") as f:
                self.configDict = json.load(f)
        except FileNotFoundError:
            pass  # The file doesn't exist yet; it will be created when saving.

    def save(self):
        """Save the current configuration to the file."""
        with open(self.configFile, "w") as f:
            json.dump(self.configDict, f, indent=2)

    def configure(self, name, value):
        """
        Configure a value in the configuration.

        Parameters:
        - name (str): The name of the configuration item.
        - value: The value to set for the configuration item.
        """
        self.configDict[name] = value
        self.save()

    def get(self, name):
        """
        Get a configuration item by name.

        Parameters:
        - name (str): The name of the configuration item.

        Returns:
        - ConfigItem: The configuration item with the specified name.
        """
        if name not in self.configDict:
            return ConfigItem("Error", "")
        return ConfigItem(name, self.configDict[name])


class ConfigItem:
    """A single configuration item with a name and a value."""

    def __init__(self, name, value):
        """
        Initialize a ConfigItem.

        Parameters:
        - name (str): The name of the configuration item.
        - value: The value of the configuration item.
        """
        self.name = name
        self.value = value
