API_URL = "https://www.mythermostat.info/api"

AUTH_URL = "/authenticate/user"
THERMOSTAT_URL = "/thermostat"

REQUEST_HEADERS = {
    "content-type": "application/x-www-form-urlencoded",
    "accept": "application/json",
    "dnt": "1",
    "origin": "https://www.mythermostat.info/api"
}

# NuHeat Schedule Modes
SCHEDULE_RUN = 1
SCHEDULE_TEMPORARY_HOLD = 2  # hold the target temperature until the next scheduled program
SCHEDULE_HOLD = 3  # hold the target temperature until it is manually changed
