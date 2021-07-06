from POC.Location import Location
import urllib.request
from POC.ExcelImporter import ExcelImporter


class LocationMeasurer:
    distance_matrix_api_address = 'https://maps.googleapis.com/maps/api/distancematrix/'
    msg_format = None
    api_key = None
    origins = None
    destination = None
    departure_time = 1625641740
    traffic_model = 'optimistic'

    def __init__(self, api_key: str, origins: list, destination: Location, msg_format='json'):
        self.api_key = api_key
        self.origins = origins
        self.destination = destination
        self.msg_format = msg_format

    def start(self):
        api_query_string = \
            f'{self.distance_matrix_api_address}{self._msg_format}{self._origins()}&{self._destinations()}&' \
            f'{self._departure_time()}&{self._traffic_model()}&{self._credentials()} '
        print(api_query_string)
        with urllib.request.urlopen(api_query_string) as res:
            print(res.read().decode('utf-8'))

    def _origins(self):
        origins = 'origins='
        for location in self.origins:
            origins += location[0].get_location_string() + '|'
        origins = origins[:-1]
        return origins

    def _destinations(self):
        return 'destinations= ' + self.destination.get_location_string()

    def _departure_time(self):
        return f'departure_time={self.departure_time}'

    def _traffic_model(self):
        return f'traffic_model={self.traffic_model}'

    def _msg_format(self):
        return f'{self.msg_format}?'

    def _credentials(self):
        return f'key={self.api_key}'


if __name__ == '__main__':
    addresses = ExcelImporter().read_file()
    street_name = list(addresses['Straat'])
    house_number = list(addresses['Huisnummer'])
    city = list(addresses['Plaats'])
    id = list(addresses['Medwerker_id'])

    addresses = []
    for i in range(len(street_name)):
        addresses.append((Location(street_name=street_name[i], house_number=house_number[i], city=city[i]), id[i]))

    destination = Location(street_name='Zernikedreef', house_number=11, city='Leiden')
    app = LocationMeasurer('', addresses, destination)

    app.start()
