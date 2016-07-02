import json
from pygal.maps.world import World
from country_codes import get_country_code
# Load data into a json list
filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Print gdp for each country
cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2014':
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp

wm = World()
wm.title = 'Gross Domestic Product in 2014, by Country'
wm.add('2014', cc_gdp)

wm.render_to_file('world_gdp.svg')
