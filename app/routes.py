from flask import current_app, jsonify, request

def get_players():
    players = current_app.player_service.get_all_players()
    return jsonify(players)

def get_player(player_id):
    player = current_app.player_service.get_player_by_id(player_id)
    if player is None:
        return jsonify({'error': 'Player not found'}), 404
    return jsonify(player)

def add_player():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    player_data = request.get_json()
    
    # Validate required fields
    if 'playerID' not in player_data:
        return jsonify({'error': 'playerID is required'}), 400
    
    new_player = current_app.player_service.add_player(player_data)
    if new_player is None:
        return jsonify({'error': 'Player ID already exists or invalid data'}), 400
        
    return jsonify(new_player), 201

def init_app(app):
    app.add_url_rule('/api/players', 'get_players', get_players)
    app.add_url_rule('/api/players/<player_id>', 'get_player', get_player)
    app.add_url_rule('/api/players', 'add_player', add_player, methods=['POST'])