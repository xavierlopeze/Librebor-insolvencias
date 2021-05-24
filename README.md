# Librebor-insolvencias

Analysis de datos de LibreBOR para analizar los datos de insolvencias para ver cómo ha afectado el covid19 al tejido empresarial.

## Objetivos:

- Visualizar insolvencias mensual interanual
- Visualizar involvencias por provincias
- Visual insolvencias por sector

## Code
- get_flat_data.py: To convert data from .json to a flat csv file.
- get_monthly_insolvency.py: Get the monthly insolvency visualizations in the img folder
- Full Code.ipynb: Notebook where the code was developed
- Conclusions_insolvencias.ipynb (and html): Notebook with the conclusions of bankruptcies.
- Conclusions_concursos.ipynb (and html): Notebooko with the conclusions of contests.


## Conclusions
Data from bankruptcies (insolvencias) need to be checked for data quality clearly, data from contests (concursos) seems to be more consistent.
Visualizations for monthly and by provinces have been done, getting information by sector is still left to do, it should be obtained from the text.

## Data
Two datasets have been analyzed:
- insolvencias_2021.04.20.json
- concursos_2021.05.10.json (not available on the repo due to memory limitations)