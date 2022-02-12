## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```


## Päänäkymä

![](./kuvat/kayttoliittyma.png)

- Tallennettavan miditiedoston tahtilajin voi valita.
- Markov syvyys tarkoittaa sitä kuinka pitkiä sekvenssejä tallennetaan triehen ja vastaavasti kuinka pitkä on sekvenssi jonka perusteella haetaan seuraavaa arvoa. Data tallennetaan triehen  syvyys + 1 pitkinä osajonoina.
- Käytä alkuperäistä rytmiä mahdollistaa valita tehdäänkä rytmi markovin ketjujen avulla vai käyttäänkö rytmi tiedoston rytmi sellaisenaan.
- Melodiatiedosto on se jonka perusteella tehdään tonaalinen materiaali
- Rytmitiedosto on rytmin perustana joko sellaisenaan tai markovin ketjujen materiaalina

- kansiossa data on joitan midifilejä joita voi käyttää materiaalina. Kansiossa moniääniset on neliäänisiä koraaleja joita voi kokeilla mutta niiden osalta toiminnot ovat keskeneräisiä.



## Testus

- Sovellusta voi tastata seuraavilla komennoilla:

```bash
poetry run invoke test
```

```bash
poetry run invoke coverage
```

```bash
poetry run invoke report
```

```bash
poetry run invoke lint
```

