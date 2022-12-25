from configparser import ConfigParser

conf_file = ConfigParser()
conf_file.read("./Dynamic_Input/config.cfg")

print(conf_file.get("first_section", "password"))
