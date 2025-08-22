import requests
from bs4 import BeautifulSoup
import csv

def scrape_ftse250_wikipedia():
    url = "https://en.wikipedia.org/wiki/FTSE_250_Index"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscamos la sección "Constituents" (constituentes)
    # Find the "Constituents" section header
    header = soup.find(id="Constituents")
    if not header:
        print("No se encontró la sección de Constituyentes / 'Constituents' section not found")
        return

    # La tabla está justo después de ese encabezado
    # The table is located just after this header
    table = header.find_next('table', {'class': 'wikitable'})
    if not table:
        print("No se encontró la tabla de constituyentes / Constituents table not found")
        return

    # Extraemos todas las filas excepto la primera (que es el encabezado)
    # Extract all rows except the header row
    rows = table.find_all('tr')[1:]

    # Abrimos un archivo CSV para escribir los datos
    # Open a CSV file to write the data
    with open('ftse250_companies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Escribimos la cabecera
        # Write the CSV header
        writer.writerow(['Company Name', 'Ticker Symbol', 'Industry Classification'])

        for row in rows:
            # Extraemos las columnas de cada fila
            # Extract columns from each row
            cols = row.find_all(['th', 'td'])
            if len(cols) >= 3:
                company_name = cols[0].get_text(strip=True)
                ticker = cols[1].get_text(strip=True)
                industry = cols[2].get_text(strip=True)
                # Escribimos la fila en el CSV
                # Write the row to the CSV
                writer.writerow([company_name, ticker, industry])

    print("Datos guardados en 'ftse250_companies.csv' / Data saved to 'ftse250_companies.csv'")

if __name__ == "__main__":
    scrape_ftse250_wikipedia()
