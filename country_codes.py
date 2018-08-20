from pygal.maps.world import COUNTRIES

error_countries = {
    'bo' : 'Bolivia',
    'cd' : 'Congo, Dem. Rep.',
    'cg' : 'Congo, Rep.',
    'eg' : 'Egypt, Arab Rep.',
    'gm' : 'Gambia, The',
    'hk' : 'Hong Kong SAR, China',
    'ir' : 'Iran, Islamic Rep.',
    'kp' : 'Korea, Dem. Rep.',
    'kr' : 'Korea, Rep.',
    'kg' : 'Kyrgyz Republic',
    'la' : 'Lao PDR',
    'ly' : 'Libya',
    'mo' : 'Macao SAR, China',
    'mk' : 'Macedonia, FYR',
    'md' : 'Moldova',
    'sk' : 'Slovak Republic',
    'tz' : 'Tanzania',
    've' : 'Venezuela, RB',
    'vn' : 'Vietnam',
    'ye' : 'Yemen, Rep.',
}

def get_country_code(country_name):
    """Returns 2-digit Pygal code for country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        else:
            for code, name in error_countries.items():
                if name == country_name:
                    return code
    return None

#print(get_country_code('Russian Federation'))