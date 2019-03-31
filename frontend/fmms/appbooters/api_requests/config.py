import configparser
import os

BASE_URL = dict(base_url='http://127.0.0.1:8000/api/v2/')

# USERCONFIG = configparser.ConfigParser()


class UserConfigurations(configparser.ConfigParser):
    def __init__(self, filen='user.cfg'):
        super().__init__()
        self.path = self.default_path()
        self.filen = filen

    def default_path(self):
        return os.path.dirname(__file__)

    def read_default(self):
        try:
            return self.read(os.path.join(self.path,self.filen))
        except configparser.Error as e:
            raise e

    def save_config(self):
        """
        Save a config file
        """
        try:
            with open(os.path.join(self.path,self.filen), "w") as config_file:
                self.write(config_file)
        except configparser.Error as e:
            raise e

    def create_config(self, file_path,options={}):
        """
        Create a config file
        """
        if options:
            self.add_section("Settings")
            self.set("Settings", "font", "Courier")
            self.set("Settings", "font_size", "10")
            self.set("Settings", "font_style", "Normal")
            self.set("Settings", "font_info",
                       "You are using %(font)s at %(font_size)s pt")

        try:
            with open(file_path, "w") as config_file:
                self.write(config_file)
        except configparser.Error as e:
            raise e

    def get_config(self, path=None, fnam=None):
        """
        Returns the config object
        """
        if path and fnam:
            self.path=path.strip()
            self.filen=fnam.strip()

        elif path:
            self.path=path.strip()

        elif fnam:
            self.filen=fnam.strip()

        fpath= os.path.join(self.path,self.filen)

        try:
            if not os.path.exists(fpath):
                self.create_config(fpath)
            return self.read(fpath)
        except configparser.Error as e:
            raise e

    def get_setting(self, section, setting,path=None, fnam=None):
        """
        Print out a setting
        """
        sfile = self.get_config(path, fnam)
        value = sfile.get(section, setting)
        print("{section} {setting} is {value}".format(
            section=section, setting=setting, value=value))
        return value

    def update_setting(self, section, setting, value, path=None, fnam=None):
        """
        Update a setting
        """
        config = self.get_config(path,fnam)
        config.set(section, setting, value)
        try:
            with open(path, "w") as config_file:
                config.write(config_file)
        except configparser.Error as e:
            raise e

    def delete_setting(self, section, setting, path=None, fnam=None):
        """
        Delete a setting
        """
        config = self.get_config(path, fnam)
        config.remove_option(section, setting)
        try:
            with open(path, "w") as config_file:
                config.write(config_file)
        except configparser.Error as e:
            raise e
