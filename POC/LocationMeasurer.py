from Location import Location


class LocationMeasurer:
    distance_matrix_api_address = 'https://maps.googleapis.com/maps/api/distancematrix/'
    msg_format = None
    api_key = None
    origins = None
    destination = None

    def __init__(self, api_key: str, origins: list, destination: Location, msg_format='json'):
        self.api_key = api_key
        self.origins = origins
        self.destination = destination
        self.format = msg_format

    def start(self):
        api_query_string = \
            f'{self.distance_matrix_api_address}{self.msg_format}{self._origins()}&{self._destinations()}&'

    def _origins(self):
        origins = ''
        for location in self.origins:
            origins += location.get_location_string() + '|'
        origins = origins[:-1]
        return origins

    def _destinations(self):
        return self.destination.get_location_string()

    def _departure_time(self):
        return 'departure_time=1625468400000'

    def _traffic_model(self):
        return 'traffic_model=optimistic'

    def _msg_format(self):
        return f'{self.format}?'

    def _credentials(self):
        return f'&key={self.api_key}'


if __name__ == '__main__':
    app = LocationMeasurer('AIzaSyCUKMACuSeuwJYnfxzfv__gTD1V6YRIPBk', )
    app.start()
