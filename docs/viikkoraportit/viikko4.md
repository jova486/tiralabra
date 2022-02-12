# Viikkoraportti 4


### Mitä olen tehnyt tällä viikolla?

Midifilet teettävät työtä edelleen. Yksiäänisen ja moniäänisen avaamisen ja tallentamisen automatisointi tuotti bugeja joiden korjaamiseen meni aikaa. Dokumentointia on aloitettu ja testi kattavuutta parannettu.
Käyttöliittymään on lisätty mahdollisuus valita tahtilaji ja markovin ketjun haluttu syvyys. Melodialle ja rytmille voi valita omat tiedostonsa.

### Miten ohjelma on edistynyt?

Ohjelma ei ole edistynyt toivotulla tavalla, paitsi bugikorjausten niin myös epäonnistuneiden kehitysideoiden takia. Ehkä vähän huonosta suunittelusta johtuen en saanut musiikin rakennetta tuottavaa toimintoa aikaiseksi. Se jäänee ensi viikkoon. Qt:n haltuunotto on edistynyt ja uskon että saan sillä tehtyä ihan siistin käyttöliittymän.

### Mitä opin tällä viikolla / tänään?

Opin ennenkaikkea että huono suunittelu johtaa helposti umpikujaan kun ohjelmaa haluaa laajentaa. Pyqt5 on ollut mielenkiintoinen tuttavuus ja uskon että sille tulee olemaan paljon käyttöä tulevaisuudessa.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia? Vastaa tähän kohtaan rehellisesti, koska saat tarvittaessa apua tämän kohdan perusteella.

Trien ja markovin ketjujen osalta mielestäni ei ole paljoa tehtävää. Ne toimivat kuten suuniteltu. Midifilejen avaamiseen täytyy miettiä hyvä strategia. Mikäli pidättäydyn siinä että sovelma käyttää vain valittua dataa ei paljoa tarvitse tehdä. Jos taas haluan että minkä vaan midifilen voi avata materiaaliksi on tehtävää aika paljon. Täytyy miettiä jätänkö moniäänisyyden kokonaan pois. Periaatteessa sen voi kai jättää mukaan vaikka en ehtisi enää kehittää sitä pidemmälle. Nyt tuntuu siltä että menetelmä on parhaimmillaan löytäessään yllättäviä yhdistelmiä erityyppisestä materiaalista. En usko että kannattaa liikaa käyttää aikaa siihen että saisi musiikillisesti mielekkään tuloksen ulos.
Kysymyksiä:
1. Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista) Tämä lienee sama kuin määrittelydokumentissa? Ainakin Trien osalta kyseessä on O(n) aikavaativuus. Mielestäni myös markovin ketjun osalta. Tilavaativuus lienee vain Trien osalta? En oikeastaan tiedä miten se määritellään. Triehän on erinomainen tietorakenne koska se tallentaa sekvenssejä osin päällekkäin.
2. Huomasin että arvostelukriteereissä oli mainittu Dokumentoiva koodi? Tämä kai tarkoittaa sitä että metodit ja muuttujat on nimetty siten että niistä selviää niiden tehtävä? Oma koodini on nyt aika kaukana siitä. Olisiko koodi syytä korjata tässä mielessä?

### Mitä teen seuraavaksi?

Teen jonkinlaisen metodin jolla voi luoda struktuuria ulostuloon. Pyrin kehittämään moniäänisyyden tuottamista.

**Työaika:** noin 9 tuntia

