# Seneca the Elder *Controversiae* and *Suasoriae* Database

## Overview

The **Seneca the Elder *Controversiae* and *Suasoriae* Database** is an open relational database of named declamators occurring in the *Controversiae* and *Suasoriae* of Seneca the Elder. It was developed to support research in Ancient rhetoric and declamation, Latin and Greek literature, and Digital & Computational Humanities studies by providing a curated authority list of historical persons cited by Seneca the Elder together with their orthographic and inflectional variants and their occurrences in the corpus.

The Database is structured according to Seneca's citation methods that are distinguishable in the two macro-sections covering the whole anthology: *Sententiae*, the *Diuisiones* and the *Colores*. Since these last two sections share the similar citation patterns they are regrouped in one categorie as *Diuisiones et Colores*. 

The database serves as a resource for the study of Seneca the Elder's declamatory anthology by enabling users to query the text according to multiple criteria, including the cited declaimer, name variants, book, chapter, textual section, and the pars (i.e. the argumentative position adopted in favour of or against the case). For the *Sententiae* section, it is also possible to query the corpus by the speaker. The text was extracted from Seneca, L. A. (1922). *Annaei Senecae oratorum et rhetorum sententiae, diuisiones, colores* (A. Kiessling, ed.). Leipzig: B. G. Teubner.

The text, in particularly the declamators names text, was orthographically normalised by converting v to u and j to i, while preserving the remaining orthographic features of the source edition.

The database combines manual philological curation with automatic extraction methods. It is designed to be extensible and to facilitate quantitative, network-based, and prosopographical analyses.

---

# Contents

The database currently contains three relational tables.

## 1. `persons`

One record for each historical individual.

| Field            | Description                              |
| ---------------- | ---------------------------------------- |
| `person_id`      | Stable identifier (e.g. P0001)           |
| `canonical_name` | Preferred canonical form of the name     |
| `language`       | Language in which the declamator is cited|

Example:

| person_id | canonical_name  | language |
| --------- | --------------- |----------|
| P0002     | Adaeus          | greek    |

---

## 2. `name_variants`

Authority list of orthographic, inflectional, and contextual variants associated with each individual.

| Field            | Description                                                           |
| ---------------- | --------------------------------------------------------------------- |
| `variant_id`     | Stable identifier                                                     |
| `person_id`      | Foreign key to `persons`                                              |
| `canonical_name` | Canonical name                                                        |
| `variant`        | Variant occurring in the corpus                                       |
| `variant_type`   | Type of variant (canonical, variant) |

Examples of variants include:

* orthographic variation
* inflected forms
* reversed word order
* abbreviated references

---

## 3. `occurrences`

One record for each occurrence of a person in the corpus.

| Field            | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| `occurrence_id`  | Stable identifier                                             |
| `person_id`      | Foreign key to `persons`                                      |
| `canonical_name` | Canonical name                                                |
| `book_name`      | Work (e.g. *Controversiae*)                                   |
| `book_n`         | Book number                                                   |
| `chapter_n`      | Chapter number                                                |
| `chapter_head`   | Chapter heading                                               |
| `label`          | Textual section (*Sententiae*, *DivisionesEtColores*) |
| `pars`           | Internal subdivision where applicable                         |
| `paragraph`      | Paragraph containing the occurrence                           |

---

# Database Structure

```
persons
---------
person_id (PK)
canonical_name
language

name_variants
----------------------------
variant_id (PK)
person_id (FK)
canonical_name
variant
variant_type

occurrences
----------------------------
occurrence_id (PK)
person_id (FK)
canonical_name
book_name
book_n
chapter_n
chapter_head
label
pars
paragraph
```

---

# Methodology

Named entities were identified using a hybrid extraction pipeline combining:

* exact matching against a manually curated authority list;
* exact phrase matching for multi-token names;
* Jaro–Winkler similarity for orthographic variation;
* iterative manual validation and correction.

The authority list was progressively expanded by incorporating attested orthographic, inflectional, and contextual variants encountered during corpus analysis.

---

# Data Sources

Primary source:

* Seneca the Elder, *Controversiae* and *Suasoriae*.

---

# Repository Structure

```
├──seneca.db
├── README.md
└── LICENSE
```

---

# Usage

The SQLite database can be queried directly using any SQLite-compatible software.

Example:

```sql
SELECT canonical_name
FROM persons;
```

Retrieve all occurrences of a person:

```sql
SELECT *
FROM occurrences
WHERE person_id = 'P0001';
```

Count occurrences by individual:

```sql
SELECT canonical_name,
       COUNT(*) AS occurrences
FROM occurrences
GROUP BY canonical_name
ORDER BY occurrences DESC;
```

---

# Versioning

Each public release represents a stable snapshot of the database.

Future releases may include:

* additional names (non declamators cited by Seneca);
* corrections (if necessary);
* additional metadata;
* links to external prosopographical resources.

---

# Citation

If you use this database, please cite:

> *Seneca the Elder Prosopographical Database (SEPD)*, Version X.X.

When available, please also cite the associated Zenodo DOI.

---

# License

Data: CC BY 4.0

Code: MIT License

---

# Acknowledgements

This database was developed as part of ongoing research funded by the Émergence project, at Sorbonne University and Rouen Normandie University (France), "SenecAI: Artificial Intelligence for the Stylistic and Authorial Analysis of Seneca the Elder’s Declamatory Anthology".