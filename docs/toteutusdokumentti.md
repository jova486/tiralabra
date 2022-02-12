# Toteutusdokumentti


## Käytettävät tietorakenteet ja algoritmit
Midifileistä avattavat sekvenssit tallennetaan trie rakenteeseen halutulla maksimipituudella. Trie tallentaa myös sekvenssien lyhyemmät osajonot. Triestä voi hakea seuraavan sekvenssissä olevan arvon pituuksilla 0-(max-1).
Trien ohella tärkein algoritmi on markov_chain.py filessä oleva get_next joka jolle annetaan parametrina Trie rakenne sekä sekvenssi jota vastaavat yhtä pidemmät sekvenssit haetaan trie rakenteesta. Seuraavalle arvolle lasketaan frekvenssi ja niitä hyödyntäen arvotaan seuraava arvo. Tätä metodia hyödynnetään pidempiä ketjuja rakentavassa doArray metodissa.


## Käytettävät tekniikat

Ohjelmisto on toteutettu käyttäen python ohjelmointikielenä. Käyttöliittymä on toteutettu PyQt5 kirjaston avulla. Midifilejen avaamiseen on käytössä Mido kirjasto ja niiden tallennukseen on käytössä midiutil kirjastoa.


## Ohjelmiston yleinen rakenne

Sovelman rakenteen muodostavat App luokka ui.py tiedostossa ja Servise luokka. App luokka on käyttöliittymäluokka. Servise luokassa on kaikki toiminnallisuus. Midifilen avaamiseen ja tallentamiseen tarvittavat metodit ovat midiIO.py tiedostossa.



## Saavutetut aika- ja tilavaativuudet

Trie tietorakenteella saavutetaan aika- ja tilavaatimuksiltaan [määritelydokumentissa](./maarittelydokumentti.md) annetut rajat. Markovin ketjujen osalta O(n) aika vaatimus toteutuu.

## Työn mahdolliset puutteet ja parannusehdotukset

-   Midifilejen avaaminen vaatisi enemmän vielä miettimistä. Sovelma ei osaa käsitellä taukoja ollenkaan vaan sivuutta tauot tiedostoja avattaessa.


# Lähteet

-   Laaksonen A, 2018, "Kisakoodarin käsikirja", luettu 18.1.2022. Saatavilla: [https://www.cs.helsinki.fi/u/ahslaaks/kkkk.pdf](https://www.cs.helsinki.fi/u/ahslaaks/kkkk.pdf)
