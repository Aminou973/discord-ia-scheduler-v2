
import discord_scheduler
import time

while True:
    discord_scheduler.run_all_extended()
    time.sleep(3600)  # exécute toutes les heures
