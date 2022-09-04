
class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

    def spill(self):
        print(f"Spiller {self._tittel} av {self._artist}")

    def sjekkArtist(self, navn):
        # Lager lister av navn og artist. Splittes ved mellomrom.
        delArtistListe = self._artist.split()
        delNavneListe = navn.split()
        # Sammenligner elementene i delArtistListe og delNavneListe
        for delNavn in delNavneListe:
            if delNavn in delArtistListe:
                # Returnerer True ved første mulige match
                return True
        # Returnerer False dersom ingen matcher
        return False

    def sjekkTittel(self, tittel):
        # Titlene defineres som like uavhengig av små/store bokstaver
        return tittel.lower() == self._tittel.lower()

    def sjekkArtistOgTittel(self, artist, tittel):
        # Påkaller andre metoder i klassen med self.
        # Returnerer True hvis begge uttrykk evaluerer til True, False ellers.
        return self.sjekkArtist(artist) and self.sjekkTittel(tittel)
