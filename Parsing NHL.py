from bs4 import BeautifulSoup
import requests
import csv
import time


def site(url) -> None:
    max_pages = 5
    current_page = 1

    with open('scraped_data1.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Team', 'Wins', 'Year', 'Losses'])

        while current_page <= max_pages:
            print(f'{url}?page_num={current_page}')

            raw_html = requests.get(f'{url}?page_num={current_page}')
            soup = BeautifulSoup(raw_html.text, 'html.parser')

            for entry in soup.find_all('tr', {'class': 'team'}):
                team = entry.find('td', {'class': 'name'}).text.strip()
                wins = entry.find('td', {'class': 'wins'}).text.strip()
                year = entry.find('td', {'class': 'year'}).text.strip()
                losses = entry.find('td', {'class': 'losses'}).text.strip()


                writer.writerow([team, wins, year, losses])

                print(f'Team: {team} | Wins: {wins} | Year: {year} | Losses: {losses}')

            time.sleep(15)
            current_page += 1
            print('\n\n')


def main() -> int:
    URL = 'https://www.scrapethissite.com/pages/forms/'
    site(URL)
    return 0


if __name__ == '__main__':
    exit(main())
