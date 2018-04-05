from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定国家名返回pygal中对应的两字母国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

