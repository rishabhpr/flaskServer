import csv
from typing import List, Dict, Optional
import os

class PlayerService:
    def __init__(self, csv_file: str) -> None:
        self.csv_file: str = csv_file
        self.players: Dict[str, Dict] = {}
        
        # Read CSV file and store data
        with open(csv_file, mode='r', encoding='utf-8') as file:
            self.headers = next(csv.reader(file))  # Store headers
            file.seek(0)  # Reset file pointer
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
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
    
    def add_player(self, player_data: Dict) -> Optional[Dict]:
        """Add a new player to the dataset"""
        # Check if player ID already exists
        player_id = player_data.get('playerID')
        if not player_id:
            return None
        if player_id in self.players:
            return None
            
        # Ensure all fields from CSV are present
        new_player = {header: player_data.get(header, '') for header in self.headers}
        
        # Add to memory
        self.players[player_id] = new_player
        
        # Append to CSV file
        with open(self.csv_file, mode='a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writerow(new_player)
            
        return new_player