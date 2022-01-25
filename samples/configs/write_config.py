from configparser import ConfigParser

# Initialize the Parser.
config = ConfigParser()

# Add the Section.
config.add_section("graph_api")

# Set the Values.
config.set("graph_api", "client_id", "cc4eb15e-6d48-4c45-8e16-23bfec6182f6")
config.set("graph_api", "client_secret", "_rq7Q~nn0fBT0E-Ke10wl0GPjqbS2DkJJLsUJ")
config.set("graph_api", "redirect_uri", "https://localhost/graph_login")

# Write the file.
with open(file="samples/configs/config.ini", mode="w+", encoding="utf-8") as f:
    config.write(f)
