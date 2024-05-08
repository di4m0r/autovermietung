class Fahrzeug:
    def __init__(self, farbe, hersteller, kilometerstand, maximale_geschwindigkeit):
        self._farbe = farbe
        self._hersteller = hersteller
        self._kilometerstand = kilometerstand
        self._maximale_geschwindigkeit = maximale_geschwindigkeit

    # Getter für Farbe, Hersteller und Kilometerstand
    def get_farbe(self):
        return self._farbe

    def get_hersteller(self):
        return self._hersteller

    def get_kilometerstand(self):
        return self._kilometerstand

    # Setter für Kilometerstand und Geschwindigkeit
    def set_kilometerstand(self, km):
        if km > self._kilometerstand:
            self._kilometerstand = km

    def set_maximale_geschwindigkeit(self, geschwindigkeit):
        self._maximale_geschwindigkeit = geschwindigkeit