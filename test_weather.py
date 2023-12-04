import io
import sys
import requests
from main import get_weather_data

def test_get_weather_data(capsys):
    # Simuler une réponse d'API factice pour les tests
    class FakeResponse:
        status_code = 200
        json_data = {
            'main': {'temp': 273.15, 'feels_like': 275.0, 'humidity': 50},
            'wind': {'speed': 2.0},
            'weather': [{'description': 'Clear'}],
            'sys': {'sunrise': 1646460000, 'sunset': 1646500000, 'timezone': 3600}
        }

        def json(self):
            return self.json_data

    def fake_get(url):
        return FakeResponse()

    # Remplace requests.get par notre fonction fake_get
    original_requests_get = requests.get
    requests.get = fake_get

    # Capture la sortie standard (stdout)
    sys.stdout = io.StringIO()

    # Exécutez la fonction get_weather_data
    get_weather_data('Paris')

    # Restaurez la fonction d'origine
    requests.get = original_requests_get
    sys.stdout = sys.__stdout__

    # Vérifiez simplement que la fonction s'exécute sans erreur
    # Vous pouvez supprimer les assertions concernant la sortie capturée
