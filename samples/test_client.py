from pprint import pprint
from configparser import ConfigParser
from ms_graph.client import MicrosoftGraphClient

scopes = [
    "Calendars.ReadWrite",
    "Files.ReadWrite.All",
    "User.ReadWrite.All",
    "Notes.ReadWrite.All",
    "Directory.ReadWrite.All",
    "User.Read.All",
    "Directory.Read.All",
    "Directory.ReadWrite.All"
]

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read("samples/configs/config.ini")

# Get the specified credentials.
client_id = config.get("graph_api", "client_id")
client_secret = config.get("graph_api", "client_secret")
redirect_uri = config.get("graph_api", "redirect_uri")

# Initialize the Client.
graph_client = MicrosoftGraphClient(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scopes,
    credentials="config/ms_graph_state.jsonc"
)

# Login to the Client.
graph_client.login()