from flask import current_app, jsonify

def get_players():
    players = current_app.player_service.get_all_players()
    return jsonify(players)

def get_player(player_id):
    player = current_app.player_service.get_player_by_id(player_id)
    if player is None:
        return jsonify({'error': 'Player not found'}), 404
    return jsonify(player)

def init_app(app):
    app.add_url_rule('/api/players', 'get_players', get_players)
    app.add_url_rule('/api/players/<player_id>', 'get_player', get_player)