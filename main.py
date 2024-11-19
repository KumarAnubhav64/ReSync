import os
import sys
from sync.file_monitor import start_monitoring
from network.peer_discovery import PeerDiscovery
from sync.sync_manager import SyncManager
from utils.config_loader import ConfigLoader
import typer

app = typer.Typer()

# Load configuration
config = ConfigLoader.load("config.yaml")

# Initialize components
sync_manager = SyncManager(config)
peer_discovery = PeerDiscovery(config)

@app.command()
def start():
    """
    Start the synchronization process.
    """
    try:
        # Retrieve the directory to monitor from the config
        watch_directory = config["sync"]["watch_directory"]

        # Start monitoring the specified directory for changes
        start_monitoring(watch_directory, sync_manager)  # Pass both path and sync_manager

        # Start peer discovery process
        peer_discovery.start()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    app()
