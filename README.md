# parse-headlines

## Objective

Internet has become an increasingly influential source of news for citizens. 

However, since most of them spend a small amount of time on those websites, it
can be assumed that a lot of the information retained comes from the headlines
more than the actual content of the article.

In order to gather data, this repository aims at scraping the headlines
of the main sources of information in France.

## Implementation

Websites:

- [x] [Le Monde](https://www.lemonde.fr/)
- [x] [Le Figaro](https://www.lefigaro.fr/)
- [x] [France TV Info](https://mobile.francetvinfo.fr/)
- [x] [Ouest France](https://www.ouest-france.fr/)
- [x] [20 Minutes](https://www.20minutes.fr/)
- [x] [Le Parisien](https://www.leparisien.fr/)
- [x] [BFM TV](https://www.bfmtv.com/)

Notes:

- The video in "Le Figaro" is not included because it is triggered by Javascript.

The data is output to `data`. Each CSV file is formatted with a timestamp in UTC.

## Challenges

- Parsing webpage to extract articles (using `beautifulsoup`)
- Refactor to limit code duplication with inherited classes
- Ouest France requires JavaScript: replace `requests` with `selenium` and `webdriver_manager`
- Ouest France uses reCAPTCHA -> not solved

## Appendix

### Choosing media

#### Fondation Descartes

[« Comment les Français s’informent-ils sur Internet ? Analyse des comportements d’information et de désinformation en ligne », 2021](https://www.fondationdescartes.org/wp-content/uploads/2021/03/Etude_Information_Internet_FondationDescartes_2021.pdf)

| Media              | % Consulted* |
| ------------------ | -----------: |
| Le Figaro          |          38% |
| Ouest France       |          26% |
| France Info        |          25% |
| 20 Minutes         |          25% |
| Journal des Femmes |          23% |
| Le Parisien        |          22% |
| Le Monde           |          22% |
| Elle               |          21% |
| L’Internaute.com   |          21% |
| BFMTV              |          21% |
| Voici              |          19% |
| Femme Actuelle     |          16% |
| Actu.fr            |          16% |
| Doctissimo         |          14% |
| L’Équipe           |          14% |
| Capital            |          14% |
| Gala               |          13% |
| France Bleu        |          13% |
| 01.net             |          12% |
| RTL                |          12% |
| LCI                |          12% |
| Challenges         |          12% |
| Yahoo! Actualités  |          12% |
| CNews              |          11% |

*During the 30 days of the study, 38% of participants consulted at least one time "Le Figaro"

## ACPM

[Classement des Sites novembre 2021](https://www.acpm.fr/Les-chiffres/Frequentation-Sites-et-Applications/Classement-des-Sites)

| Site             | Visites totales |
| ---------------- | --------------: |
| LeFigaro.fr      |     161 969 906 |
| Orange.fr        |     136 872 873 |
| Ouest-france.fr  |     131 020 339 |
| Tele-Loisirs.fr  |     122 753 509 |
| Bfmtv.com        |     115 123 264 |
| Franceinfo.fr    |     111 545 123 |
| LeMonde.fr       |      95 018 956 |
| L'Equipe.fr      |      93 253 564 |
| 20minutes.fr     |      78 468 892 |
| LeParisien.fr    |      78 125 225 |
| Closermag.fr     |      70 723 423 |
| Actu.fr          |      69 798 438 |
| Voici.fr         |      66 695 986 |
| Femmeactuelle.fr |      59 264 537 |
| Gala.fr          |      55 877 237 |
| Ladepeche.fr     |      46 042 844 |
| Boursorama.com   |      45 921 243 |
| Footmercato.net  |      37 052 497 |
| Sudouest.fr      |      34 834 486 |
| Midilibre.fr     |      33 139 944 |

### Reuters-Oxford University

[Digital News Report 2021](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2021/france)

| Brand                                    | Weekly use | At least 3 days per week |
| ---------------------------------------- | ---------: | -----------------------: |
| 20 minutes online                        |        18% |                       9% |
| Other regional or local newspaper online |        15% |                       8% |
| Le Monde online                          |        14% |                       6% |
| France Info (public broadcaster)         |        13% |                       7% |
| BFM TV online                            |        12% |                       9% |
| TF1 News online                          |        12% |                       7% |
| Le Parisien online                       |        10% |                       5% |
| Le Figaro online                         |        10% |                       4% |
| Brut                                     |        10% |                       4% |
| M6 online                                |        10% |                       5% |
| Le HuffPost                              |         9% |                       3% |
| Yahoo! News                              |         8% |                       3% |
| Médiapart                                |         7% |                       3% |
| Cnews online                             |         7% |                       4% |
| Ouest France online                      |         7% |                       3% |
| MSN News                                 |         7% |                       4% |