# GDP World Map 
Maked with Python module Pygal.

Data was taken from: (https://datahub.io/core/gdp#data)

The map is interactive and SVG file can be opened in your favorite browser.

![Screenshot](/map.gif)

***
To run the code Pygal and pygal.maps.world needs to be installed.

The year can be changed in GDP_map_py in line 16
```python
if pop_dict['Year'] == 2016:
```

country_codes.py is bad designed, because of I dont't know how to search in 2 dictionaries at the same time. Contact me if u know how to make it better ;)