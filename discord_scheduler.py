
import requests
import datetime
import pytz

# Configuration
DISCORD_WEBHOOK = "https://discordapp.com/api/webhooks/1358046429616148480/c4RFindu8sWCSfqcLBeH4Zw-8iHCCHe7yrN7ci_OV1EhFD82RVPAC-B6eBZPozi3YtjF"
TIMEZONE = pytz.timezone("Europe/Paris")

def send_discord_message(content):
    requests.post(DISCORD_WEBHOOK, json={"content": content})

def send_weekly_forecast():
    message = '''
📊 **Weekly Forecast : Semaine du 7 au 11 avril 2025**

🧭 Préparation du Forecast Hebdomadaire  
📆 Dimanche 6 avril – Avant l’ouverture du marché US

1. HTF BIAS  
- Weekly Bias : 🟢 / 🔴 / ⚪  
- Daily Bias (Lun–Mer) :  
  - Lundi :  
  - Mardi :  
  - Mercredi :  

2. Structure Générale  
- IPDA Weekly High :  
- IPDA Weekly Low :  
- EQ Weekly :  
- PO3 Phase : Accum / Manip / Expansion

3. Niveaux Clés à Surveiller  
- Monday Opening Gap :  
- FVG Daily :  
- OB Weekly :  
- Premium / Discount Zone :  

4. Liquidity Targets Probables  
- Buy Side :  
- Sell Side :  
- Zones à balayer ? SMT possible ?

5. News Majeures / Bank Holidays  
- CPI / FOMC / NFP :  
- ⚠️ À éviter : (ex. CPI mardi = pas de London)

6. Synthèse  
- Direction préférée :  
- Sessions prioritaires : London / NY AM / NY PM  
- Sessions à éviter :  
- Score de confiance global : ⭐️⭐️⭐️⭐️☆
'''
    send_discord_message(message)

def send_trading_plan():
    message = '''
📄 **Trading Plan Hebdo**

1. Jours à Trader / Éviter :

| Jour      | Session     | News ?         | Trader ? |
|-----------|-------------|----------------|----------|
| Lundi     | London / NY |                | ✅ / ❌ |
| Mardi     | NY AM Only  | CPI 🇺🇸         | ❌      |
| Mercredi  | ❌          | FOMC 🇺🇸         | ❌      |
| Jeudi     | NY AM       |                | ✅      |
| Vendredi  | NY AM       |                | ✅      |

2. Objectifs Hebdo
- 🎯 Setup à chasser : RTH Gap + MSS  
- ⚠️ À éviter : NY PM mardi, London mercredi  
- 🛑 Conditions invalidantes : pas de MSS, trop proche news

3. Règles Prop Firm
- Max 2 trades / jour (risk 1R + 0.5R)  
- 2 jours SL consécutifs = 1 jour OFF  
- Objectif : +3% sur 1 compte

4. Discipline & Conscience
- État mental : ⭐️⭐️⭐️⭐️☆  
- Discipline cible : >90%  
- Temps dispo : Full / PM Only / OFF mercredi
'''
    send_discord_message(message)

def send_daily_calendar():
    today = datetime.datetime.now(TIMEZONE).strftime("%A %d %B %Y")
    message = f'''
📆 **Disponibilité du Jour – {today}**

🔔 Es-tu dispo pour trader aujourd’hui ?

🔘 Oui, je suis dispo  
🔘 Non, journée OFF / indispo

🕐 Si oui, sur quelles sessions ?
- London (3:00 – 6:00 NY / 9:00 – 12:00 Paris)  
- NY AM (8:30 – 11:30 NY / 14:30 – 17:30 Paris)  
- NY PM (13:30 – 15:30 NY / 19:30 – 21:30 Paris)

📌 Si OFF, l’IA passe en mode Observation
'''
    send_discord_message(message)

def send_weekly_rex():
    message = '''
🔁 **REX de la Semaine – Analyse Réalité vs Plan**

1. Résumé de la Semaine
- Jours actifs vs OFF :  
- Sessions tradées :  
- Respect du plan : ✅ / ❌  
- News bien évitées ? ✅ / ❌

2. Performances
- Gain net : $...  
- Prop Firms progression  
- Objectif hebdo atteint ? ✅ / ❌  
- Nombre total de trades :  
- Discipline Score : %

3. Psychologie
- Moments de tilt ?  
- Respect du risk plan ?  
- Fatigue mentale ?

4. Setup & Qualité
- Setup le + efficace :  
- Meilleur trade :  
- Trade à éviter :  
- Erreurs à corriger :

5. Recommandations IA
- Ajustements ?  
- Sessions à éviter ?  
- Règles mentales à renforcer ?
'''
    send_discord_message(message)

def run_all():
    now = datetime.datetime.now(TIMEZONE)
    if now.weekday() == 6 and now.hour == 18:  # Sunday 18h
        send_weekly_forecast()
        send_trading_plan()
    elif now.weekday() in range(0, 5) and now.hour == 9:  # Monday to Friday at 9h
        send_daily_calendar()
    elif now.weekday() == 5 and now.hour == 18:  # Saturday 18h
        send_weekly_rex()

if __name__ == "__main__":
    run_all()


def send_session_active():
    message = '''
🧠 **Session Active – Analyse Contextuelle**

1. Actualisation :
- BIAS Daily : 🟢 / 🔴 / ⚪
- Session : London / NY ?
- Prix vs 00:00 NY : 🔼 / 🔽 / ⚫
- Asia : Accum / Range / Trend ?
- London : Sweep / Expansion ?
- Structure actuelle : MSS / OB / FVG ?
- Zone actuelle : Premium / Discount ?

2. Observations :
- MSS confirmé ?
- OB valide ?
- SMT détecté ?
- Niveau HTF atteint ?

3. IA suggère :
- 3 scénarios
- Setup potentiels
- Score de probabilité
'''
    send_discord_message(message)

def send_setup_detected():
    message = '''
🎯 **Setup Detected – Validation**

Choisis la setup détectée :
- MSS + OB
- RTH Gap + Sweep
- SMT + FVG
- Breaker Block

Checklist IA :
- MSS confirmé ?
- OB englobante ?
- RTH Gap comblé ?
- SMT entre NQ / ES ?
- News proches ?

Score Probabilité IA : %...  
Validation finale à faire par toi 👤
'''
    send_discord_message(message)

def send_setup_confirmed():
    message = '''
📌 **Setup Confirmée – TP / SL / Risk**

1. TP/SL :
- SL : sous OB / Breaker
- TP1 : zone liquidité
- TP2 : HTF OB / FVG

2. Risk :
- Calcul lot size
- Réduction si SL avant
- BE possible après TP1

3. Choix :
- TP1 lock ? TP2 extension ?
- SL dynamique selon structure
'''
    send_discord_message(message)

def send_end_of_trade():
    message = '''
🧾 **Fin de Trade – Feedback**

1. Résultat :
- Setup :  
- Résultat : TP / SL / BE  
- RR initial / réalisé  
- Durée trade

2. Émotion :
- Avant : calme / stress  
- Pendant : doute / focus  
- Après : satisfait / tilt ?

3. Technique :
- Setup bien validé ?
- Le prix a continué ou reversé ?
- Sweep ou PDA HTF atteint ?
- Entrée améliorable ?

➡️ Ajouté dans le journal
'''
    send_discord_message(message)

def send_propfirm_update():
    message = '''
💼 **Prop Firm Tracker – MAJ**

1. Compte :
- Plateforme : MFFU / APEX...
- Compte : 50K / 100K
- Mode : Eval / Live

2. Solde :
- Avant : $...
- Après trade : +$ / -$
- Solde actuel : $...
- Jours validés : x/10
- Drawdown : ...%

3. Stats :
- Winrate : ...%
- Nombre de trades cette semaine : ...
- Jours tradés sur le mois (style MFFU)

📌 Auto-ajustement du risk si nécessaire
'''
    send_discord_message(message)

def send_tilt_prevention():
    message = '''
🧠 **Tilt & Discipline Check**

⚠️ Tu viens de gagner un trade ?
➡️ Risque de tilt en hausse

Stats :
- Objectif hebdo atteint ? ✅ / ❌
- Gain net : $...
- Discipline Score : ...%
- Trade restant aujourd’hui : 0 / 1

Recommandations IA :
- Pause ?
- Mode Observation ?
- Setup A++ uniquement ?
- Focus sur journalisation

🎯 Reviens plus tard si nécessaire
'''
    send_discord_message(message)

def run_all_extended():
    now = datetime.datetime.now(TIMEZONE)
    if now.weekday() == 6 and now.hour == 18:  # Sunday 18h
        send_weekly_forecast()
        send_trading_plan()
    elif now.weekday() in range(0, 5) and now.hour == 9:  # Weekdays 9h
        send_daily_calendar()
    elif now.weekday() == 5 and now.hour == 18:  # Saturday 18h
        send_weekly_rex()

    # For manual triggering of others if needed
    # Uncomment to send test messages anytime
    # send_session_active()
    # send_setup_detected()
    # send_setup_confirmed()
    # send_end_of_trade()
    # send_propfirm_update()
    # send_tilt_prevention()

if __name__ == "__main__":
    run_all_extended()
