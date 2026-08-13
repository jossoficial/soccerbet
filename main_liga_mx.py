from src.thestats_real import get_liga_mx_competition, get_liga_mx_matches_real, get_match_stats_real
from src.isports_real import get_liga_mx_league_id, get_today_fixtures_liga_mx
import pandas as pd

print("=== LIGA MX REAL TIME ===")
comp = get_liga_mx_competition()
print(f"Competición real encontrada: {comp['name']} ID: {comp['id']}")

# Trae últimos 50 partidos reales para calcular promedios
historical = get_liga_mx_matches_real(comp['id'], comp['current_season_id'])

# Calcula promedios reales de corners/goles/remates por equipo (sin simular)
team_stats = {}
for m in historical:
    stats = get_match_stats_real(m['id'])
    # stats contiene shots, shots_on_target, corners reales del API
    # Aquí sumas por equipo para sacar media móvil últimos 5
    #...

# Partidos de HOY Liga MX en tiempo real
liga_mx_id = get_liga_mx_league_id()
hoy = get_today_fixtures_liga_mx(liga_mx_id)
print(f"Partidos hoy Liga MX: {len(hoy)}")

# Genera Excel con data real
df = pd.DataFrame(hoy)
df.to_excel("liga_mx_hoy_real.xlsx", index=False)
print("Archivo generado con data 100% real de API")
