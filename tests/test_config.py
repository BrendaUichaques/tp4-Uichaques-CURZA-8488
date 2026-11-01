"""Pruebas de validacion de la configuracion de infraestructura (TP4)."""
import os
import unittest

import yaml  # pip install pyyaml

# Ruta al docker-compose.yml, calculada relativa a este archivo
COMPOSE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "docker", "docker-compose.yml"
)


class TestDockerCompose(unittest.TestCase):
    def setUp(self):
        with open(COMPOSE_PATH, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def test_yaml_valido(self):
        """El archivo es YAML sintacticamente correcto y no esta vacio."""
        self.assertIsInstance(self.data, dict)

    def test_servicios_definidos(self):
        """Estan definidos los dos servicios requeridos."""
        services = self.data.get("services", {})
        self.assertIn("web_server", services)
        self.assertIn("log_analyzer", services)


if __name__ == "__main__":
    unittest.main()
