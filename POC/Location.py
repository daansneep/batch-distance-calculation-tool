class Location:
    latitude = None
    longitude = None
    street_name = None
    house_number = None
    addition = None
    city = None
    place_id = None

    def __init__(self, latitude=None, longitude=None, street_name=None, house_number=None, addition=None, city=None,
                 place_id=None):
        self.latitude = latitude
        self.longitude = longitude
        self.street_name = street_name
        self.house_number = house_number
        self.addition = addition
        self.city = city
        self.place_id = place_id

        if not self._is_valid():
            raise ValueError('Object does not have proper parameters to represent a location')

    def get_location_string(self):
        if self.place_id is not None:
            return f'{self.place_id}'
        if self.latitude is not None and self.longitude is not None:
            return f'{self.latitude}%2C{self.longitude}'
        if self.addition is not None:
            return f'{self.house_number}%2B{self.addition}%2B{self._url_encode_street_name()}%2B{self.city}'
        else:
            return f'{self.house_number}%2B{self._url_encode_street_name()}%2B{self.city}'

    def _url_encode_street_name(self):
        return self.street_name.replace(' ', '%20')

    def _is_valid(self):
        if (self.latitude and self.longitude) or (self.street_name and self.house_number and self.city) or self.place_id:
            return True
        else:
            return False
