# Viikkoraportti 3

### Mitä olen tehnyt tällä viikolla?

Täällä viikolla olen saanut aikaan testejä markovin ketkujen osalta. Testaus on tosin vielä alussa ja jouduin tekemään ylimääräisen metodin doArray_strict jonka avulla voi testata doArray metodin tekemiä sekvenssejä. doArray on vaikea testata koska aina on mahdollista että ketjuun syntyy tilanne josta ei pääse eteenpäin. Tämä on ratkaistu siten että peruutetaan takaisin lyhyempiin yhdistelmiin tarvittaessa alkuun asti. Näin voidaan taata että riittävän pitkä sekvenssi voidaan tuottaa. Tämä testataan toisella testillä.
Testikattavuus on nyt parantunut. Olen jakanut koodia uudelleen ja nyt Service luokka vastaa ohjelmalogiikasta. Tällä hetkellä on kaksi eri metodia moniäänisellä (4 ääniselle) ja yksiääniselle tuotokselle. Erittäin paljon aikaa ja pähkäilyä on kulunut midi IO:n parantamisessa. Tavoitteena on saada riittävän kattava (joskaan ei yleispätevä) midi IO sovelman tarpeisiin.
Olen myös aloittanut graafisen käyttöliittymän suunittelun ja alustava toteutus on aloitettu Qt:llä.
Tällä hetkellä voi valita avattavan ja tallennettavan filen sekä valita käyttääkö sovelma midifilen tekoon alkuperäistä rytmihahmoa vai generoiko se rytmit uudelleen.

### Miten ohjelma on edistynyt?

Käyttöliittymä aloitettu. Muuten tällä viikolla on mennyt aika paljon aikaa asioiden uudelleen koodaamiseen.

### Mitä opin tällä viikolla / tänään?

Tällä viikolla on tullut selväksi että opetusdatan pitää olla täällä metodilla hyvin homogeenistä. Tämä on aiheuttanut ongelmia. Kaikkineen tuntuu siltä että ei kannata liikaa käyttää energiaa siihen että markovin ketjuilla saisi yksinään kovin ihmeellistä musiikkia aikaiseksi.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia? Vastaa tähän kohtaan rehellisesti, koska saat tarvittaessa apua tämän kohdan perusteella.

Trien ja markovin ketjujen osalta asiat tuntuvat selvältä. Suurin pohtimisen aihe on mitä näillä tekisin. Mietinnässä on ollut millä tavoin rakennetta voisi tehdä. Olen miettinyt että joitan musiikillisia perusrakenteita voisi tehdä ja käyttäjä voisi esim. rakentaa kirjoittamalla vaikka ABABCA tms. Ajattelin että vois valita jokaiselle fraasille oman filen jonka materiaalista se tehdään. Ja voisi myös ottaa rytmin toisesta ja intervallirakenteen toisesta. Mutta katsotaan mitä ehtii. Toivoisin erityisesti ohjeita mitä olisi vielä tarpeen tehdä.

### Mitä teen seuraavaksi?

 Huomasin tosin että ohjeissa mainittiin että tietorakenteet pitäisi tehdä itse. Trie käyttää pythonin dictionary tietorakennetta, tämä lienee syytä vaihtaa vastaavaan itse tehtyyn. Sitten parannan testikattavuutta, lisään ominaisuuksia ja rakennan käyttöliittymään kaikkien parametrien säätömahdollisuudet. Koodin kommentointi ja laadun parantaminen on saatava vauhtiin.

**Työaika:** noin 11 tuntia
