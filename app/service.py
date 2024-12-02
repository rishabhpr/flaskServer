import csv
from typing import List, Dict, Optional

class PlayerService:
    def __init__(self, csv_file: str) -> None:
        # Store players in a dictionary for quick lookup
        self.players: Dict[str, Dict] = {}
        
        # Read CSV file and store data
        with open(csv_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Clean empty strings to None
                player_dict = {
                    key: (None if value == '' else value) 
                    for key, value in row.items()
                }
                self.players[row['playerID']] = player_dict
    
    def get_all_players(self) -> List[Dict]:
        """Return list of all players"""
        return list(self.players.values())
    
    def get_player_by_id(self, player_id: str) -> Optional[Dict]:
        """Return player by ID or None if not found"""
        return self.players.get(player_id)