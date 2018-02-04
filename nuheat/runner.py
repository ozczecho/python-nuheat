from nuheat import NuHeat

# Initalize an API session with your login credentials
api = NuHeat("https://www.mythermostat.info/api", "<email>", "<pwd>")
api.authenticate()

thermostat = api.get_thermostat("<serial>")

current = thermostat.celsius
target = thermostat.target_celsius

heating = thermostat.heating
online = thermostat.online
serial = thermostat.serial_number