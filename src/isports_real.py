import requests
from.config import ISPORTS_BASE, ISPORTS_KEY
import datetime

def get_liga_mx_league_id():
    # 1. Descubre el leagueId real de Liga MX
    url = f"{ISPORTS_BASE}/sport/football/league/basic/list?api_key={ISPORTS_KEY}"
    data = requests.get(url).json()
    for league in data.get('data', []):
        if league.get('name') == 'Mexican Liga MX' or 'Liga MX' in league.get('name',''):
            return league['leagueId'] # ej: 262
    return None

def get_today_fixtures_liga_mx(league_id):
    # 2. Usa endpoint real Schedule & Results con date + leagueId
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    url = f"{ISPORTS_BASE}/sport/football/schedule/basic?api_key={ISPORTS_KEY}&date={today}&leagueId={league_id}"
    r = requests.get(url).json()
    return r.get('data', [])

def get_live_corners_odds(match_id):
    url = f"{ISPORTS_BASE}/sport/football/odds?api_key={ISPORTS_KEY}&matchId={match_id}"
    return requests.get(url).json()
