from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        musikk = open(filnavn)
        # Splitter linjene i musikkfilen samt oppretter sangobjekt per linje
        for linje in musikk:
            tittelOgArtist = linje.strip().split(";")
            tittel = tittelOgArtist[0]
            artist = tittelOgArtist[1]
            sang = Sang(artist, tittel)
            self._sanger.append(sang)

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        # Sletter Sang-objektet som sang-parameteren refererer til
        self._sanger.remove(sang)

    def spillSang(self, sang):
        # Kaller på spill-metoden til Sang-objektet sang-parameteren refererer til
        sang.spill()

    def spillAlle(self):
        for Sang in self._sanger:
            Sang.spill()

    def finnSang(self, tittel):
        for Sang in self._sanger:
            if Sang.sjekkTittel(tittel):
                # Returnerer første sang som oppfyller tittelkriteriet
                return Sang
        # None vil kun returneres dersom ingen sanger er funnet i sanglista
        return None

    def hentArtistUtvalg(self, artistnavn):
        sangUtvalg = []
        for Sang in self._sanger:
            if Sang.sjekkArtist(artistnavn):
                sangUtvalg.append(Sang)
        return sangUtvalg
