import geoip2.database

def enrich_with_geo(ip_address, db_path='GeoLite2-City.mmdb'):
    try:
        reader = geoip2.database.Reader(db_path)
        response = reader.city(ip_address)
        return {
            "country": response.country.name,
            "city": response.city.name,
            "latitude": response.location.latitude,
            "longitude": response.location.longitude,
            "isp": response.traits.isp
        }
    except Exception as e:
        return {"error": str(e)}
