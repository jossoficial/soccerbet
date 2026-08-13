import requests
from.config import THESTATS_BASE, THESTATS_KEY

headers = {"x-api-key": THESTATS_KEY}

def get_liga_mx_competition():
    # 1. Busca la competencia real de Liga MX
    r = requests.get(f"{THESTATS_BASE}/competitions", params={"country": "Mexico"}, headers=headers).json()
    # Filtra por nombre real, no ID quemado
    for comp in r.get('data', []):
        if 'Liga MX' in comp['name']:
            return comp # contiene id y current_season_id
    return None

def get_liga_mx_matches_real(competition_id, season_id):
    # 2. Trae fixtures reales de la temporada actual
    r = requests.get(f"{THESTATS_BASE}/matches",
        params={"competition_id": competition_id, "season_id": season_id, "per_page": 100},
        headers=headers).json()
    return r.get('data', [])

def get_match_stats_real(match_id):
    # 3. Stats reales: corners, shots, sot, xG
    r = requests.get(f"{THESTATS_BASE}/matches/{match_id}/stats", headers=headers).json()
    return r.get('data', {})
