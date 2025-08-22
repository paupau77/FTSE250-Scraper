# FTSE250-Scraper

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-✓-green)
![Requests](https://img.shields.io/badge/Requests-✓-yellow)
![Status](https://img.shields.io/badge/Scraper-Working-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Un script en Python que realiza **web scraping** de la página de Wikipedia del [FTSE 250 Index](https://en.wikipedia.org/wiki/FTSE_250_Index) y genera un archivo CSV con:

- Nombre de la empresa  
- Símbolo bursátil (Ticker)  
- Clasificación industrial  

El resultado se guarda como `ftse250_companies.csv`.

---

## 🚀 Requisitos

- Python 3.x  
- requests  
- beautifulsoup4  

Instalación de dependencias:
```bash
pip install requests beautifulsoup4


---

▶️ Uso

Ejecutar el script:

python AppLondonScrapping.py

Esto generará el archivo ftse250_companies.csv en el mismo directorio.


---

📊 Ejemplo de salida

Company Name	Ticker	Industry

3i Group	III	Investment
Aggreko	AGK	Support services
Balfour Beatty	BBY	Construction



---

📜 Licencia

Este proyecto está bajo la licencia MIT.
¡Siéntete libre de usarlo, modificarlo y compartirlo!

---
