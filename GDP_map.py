import json

import pygal
from pygal.style import RotateStyle, LightColorizedStyle

from country_codes import get_country_code

#list fills with data
filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)

# gdp output for 2016
cc_gdps = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        gdp = int(float(pop_dict['Value']))
        gdp /= 1000000000
        code = get_country_code(country_name)
        if code:
            cc_gdps[code] = gdp

# grouping countries in 3 lvls of gdp
cc_gdps_0, cc_gdps_1, cc_gdps_2, cc_gdps_3, cc_gdps_4 = {}, {}, {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 50:
        cc_gdps_0[cc] = gdp
    if gdp < 100:
        cc_gdps_1[cc] = gdp
    elif gdp < 1000:
        cc_gdps_2[cc] = gdp
    elif gdp < 10000:
        cc_gdps_3[cc] = gdp
    else: 
        cc_gdps_4[cc] = gdp

wm_style = RotateStyle('#999900', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World gdp in 2016, by Country'
wm.add('< 50 billions', cc_gdps_0)
wm.add('< 100 billions', cc_gdps_1)
wm.add('< 1000 billions', cc_gdps_2)
wm.add('> 1000 billions', cc_gdps_3)
wm.add('> 10000 billions', cc_gdps_4)

wm.render_to_file('world_gdp.svg')