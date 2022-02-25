## Testausdokumentti

Ohjelmaa on testattu automatisoiduilla yksikköteillä unittestilla sekä manuaalisesti järjestelmätasolla. Sovellusta on testattu myös erityisillä testimidifileillä jolla on testattu että markovin ketjujen muodostuminen on odotettua. Ne sijaitsevat data/testit kansiossa. Näiden avulla on mahdollista selvittää että markovin ketjut eivät tuota opetusdatassa olemattomia sekvenssejä. Saadun informaation perusteella on markovin ketjun tuottavaa doArray metodia korjattu. Nämä testit on toteutettu järjestelmätasolla. Myös midiI0.py luokan testauksessa on hyödynnetty midifilejä jotka sijaitsevat data kansiossa.



## Sovelluslogiikka

Sovelluslogiikasta vastaavaa `Service`-luokkaa on testattu järjestelmätasolla.


### Testauskattavuus

Sovelluksen testauksen haarautumakattavuus on 97%

![](./kuvat/testikattavuus.png)
