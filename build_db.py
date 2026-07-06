import sqlite3
import pandas as pd
from pathlib import Path

import os

if os.path.exists("/Users/agustindei/Documents/NLP/Projet_sorbonne/AnalyseCorpus/article_citations/seneca_prosopography_v1/seneca.db"):
    os.remove("/Users/agustindei/Documents/NLP/Projet_sorbonne/AnalyseCorpus/article_citations/seneca_prosopography_v1/seneca.db")

#DB_PATH = Path("db/seneca_prosopography.db")
#DATA = Path("data")

#DB_PATH.parent.mkdir(exist_ok=True)

db_path = "/Users/agustindei/Documents/NLP/Projet_sorbonne/AnalyseCorpus/article_citations/seneca_prosopography_v1/seneca.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# tell SQLite to enforce foreign key constraints for the current database connection.

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("DROP TABLE IF EXISTS occurrences;")
cursor.execute("DROP TABLE IF EXISTS variants;")
cursor.execute("DROP TABLE IF EXISTS persons;")


# persons table

cursor.execute("""
CREATE TABLE persons (
    person_id TEXT PRIMARY KEY,
    canonical_name TEXT NOT NULL,
    language TEXT
);
""")


# variants table

cursor.execute("""
CREATE TABLE name_variants (
    variant_id TEXT PRIMARY KEY,
    person_id TEXT NOT NULL,
    canonical_name TEXT NOT NULL,
    variant TEXT NOT NULL,
    variant_type TEXT NOT NULL,
    FOREIGN KEY (person_id) REFERENCES persons(person_id) ON DELETE CASCADE     
               );
               """)


# occurrences table

cursor.execute("""
CREATE TABLE occurrences (
    occurrence_id TEXT PRIMARY KEY,
    person_id TEXT,
    canonical_name TEXT NOT NULL,
    book_name TEXT NOT NULL,
    book_n INTEGER NOT NULL,
    chapter_n INTEGER NOT NULL,
    chapter_head TEXT,
    label TEXT NOT NULL,
    pars TEXT,
    paragraph  TEXT,
    FOREIGN KEY (person_id) REFERENCES persons(person_id) ON DELETE CASCADE
);
""")

# load data from CSV files into the database tables

persons = pd.read_csv('/Users/agustindei/Documents/NLP/Projet_sorbonne/AnalyseCorpus/article_citations/db_sql/data/persons_2.csv')
variants = pd.read_csv('/Users/agustindei/Documents/NLP/Projet_sorbonne/AnalyseCorpus/article_citations/db_sql/data/variants_2.csv')
occurrences = pd.read_csv('/Users/agustindei/Documents/NLP/Projet_sorbonne/AnalyseCorpus/article_citations/db_sql/data/occurrences_full.csv')

persons["language"] = persons["language"].fillna("unknown")
# insert data

persons.to_sql("persons", conn, if_exists="append", index=False)
variants.to_sql("name_variants", conn, if_exists="append", index=False)
occurrences.to_sql("occurrences", conn, if_exists="append", index=False)


pd.read_sql("""
SELECT name
FROM sqlite_master
WHERE type='table';
""", conn)

conn.commit()
conn.close()