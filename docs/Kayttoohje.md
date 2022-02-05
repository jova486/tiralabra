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

- Sovellus aukeaa päänäkymään jossa voi avata midi filen ja valita tallennettava filen nimen.
- Testausta varten on midi filejä data kansiossa.
- Sovellus ei testaa filejen sopivuutta ja kaatuu mikäli jotain muuta avataan.

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

