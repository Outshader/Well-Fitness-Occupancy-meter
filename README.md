Updated repo of https://github.com/Outshader/wellfitness_population_counter

This version uses the PerfectGym/Well Fitness API
  
### Setup
#### Config
Create a config file named with the .env extension. The required fields are:
```
Login=
Password=
Gyms=
CSV=
Discord=
Discord_url=
```

Login and Password are for your Well Fitness email and password respectively. Importantly the fields cannot be in any quotes.

Gyms is for the IDs of the gyms you want to get the data from. Those IDs can be found in the /data/clubs.csv file. 

CSV defines whether the data fetched will be saved in the logs.csv file.

Discord defines whether a message will be send to a discord webhook.  

Discord and CSV fields accept only True or False (or their variations e.g. true, FaLse). By default they're both off.

Discord_url is for the discord webhook url. It should look like so:
https://discord.com/api/webhooks/{channel_id}/{webhook_token}

#### Script  
To download and run the script run:
```
git clone https://github.com/Outshader/Well-Fitness-Occupancy-meter
cd Well-Fitness-Occupancy-meter
uv sync --locked
uv run main.py
```

