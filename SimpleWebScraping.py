import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Definisi kelas Scraper
class Scraper:
    def __init__(self, keywords, pages):
        self.keywords = keywords # Menyimpan kata kunci pencarian
        self.pages = pages # Jumlah halaman (int)

    def fetch(self, base_url): # Mengatur parameter dan mengirim permintaan GET ke URL
        self.base_url = base_url
        self.params = {
            'query': self.keywords,
            'sortby': 'relevance',
            'page': 1
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
        try:
            # Mengirim permintaan GET dan mengembalikan respons
            return requests.get(self.base_url, params=self.params, headers=self.headers)
        except requests.exceptions.RequestException as e:
            print(f"Error saat mengambil data: {e}")
            return None

    def get_articles(self): # Mengambil artikel dari halaman web
        article_list = [] # List untuk menyimpan artikel
        total_articles = 0 # Menghitung total artikel
        # Loop untuk setiap halaman dari 1
        for page_num in range(1, int(self.pages) + 1):
            self.params['page'] = page_num # Mengupdate nomor halaman
            response = requests.get(self.base_url, params=self.params, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser') # Parsing HTML

            articles = soup.find_all('article') # Mencari semua elemen artikel

            if not articles:
                print(f"Artikel tidak ditemukan pada halaman {page_num}.")
                continue

            # Loop untuk setiap artikel yang ditemukan
            for article in articles:
                title_element = article.find("h3") or article.find("h2")
                title_link = title_element.find('a')['href'] if title_element else None

                if title_link:
                    article_page = requests.get(title_link, headers=self.headers)
                    article_soup = BeautifulSoup(article_page.text, 'html.parser')

                    # Mencari konten artikel
                    content_element = article_soup.find("div", class_="media__desc") or article_soup.find("p")
                    content = content_element.get_text(strip=True) if content_element else "Tidak ada konten"

                    # Mencari tanggal artikel
                    date_element = article_soup.find("div", class_="detail__date")
                    date = date_element.get_text(strip=True) if date_element else "Tidak ada tanggal"

                    # Menyimpan informasi artikel dalam dictionary
                    article_list.append({
                        "title": title_element.get_text(strip=True),
                        "content": content,
                        "date": date
                    })

            total_articles += len(articles)
            print(f"Halaman {page_num}/{self.pages} selesai, {len(articles)} artikel diambil. Total: {total_articles} artikel.")

        self.articles = article_list # Menyimpan semua artikel yang diambil
        print(f"[~] Total Artikel: {len(self.articles)}") # Menampilkan total artikel
        return self.articles # Mengembalikan daftar artikel

    def show_results(self, row=5): # Menampilkan hasil artikel yang diambil
        for i, article in enumerate(self.articles[:row], 1):
            print(f"Article {i}:")
            print(f"Title: {article['title']}")
            print(f"Content: {article['content']}")
            print(f"Date: {article['date']}\n")

    def save_file(self, file_format="csv"): # Menyimpan hasil artikel ke file
        time_scrape = datetime.now().strftime("%Y%m%d%H%M%S")
        df = pd.DataFrame(self.articles)

        file_name = f"Hasil_{self.keywords}_{time_scrape}"
        if file_format == "csv":
            file_name += ".csv"
            df.to_csv(file_name, index=False)
            print(f"Hasil disimpan di '{file_name}'")
        elif file_format == "excel":
            file_name += ".xlsx"
            df.to_excel(file_name, index=False)
            print(f"Hasil disimpan di '{file_name}'")
        else:
            print("Format file tidak didukung. Gunakan 'csv' atau 'excel'.")

if __name__ == '__main__':
    keywords = input("Masukkan kata kunci: ")
    pages = int(input("Jumlah halaman: "))
    base_url = "https://www.detik.com/search/searchall"

    scrape = Scraper(keywords, pages) # Membuat objek Scraper
    response = scrape.fetch(base_url) # Mengambil respons dari URL dasar

    if response and response.status_code == 200:
        articles = scrape.get_articles()
        scrape.show_results(row=5)

        ask = input("Simpan File? (y/n)").lower()
        if ask == "y":
            file_format = input("Format File (csv/excel): ").lower()
            scrape.save_file(file_format=file_format) # Panggil metode yang benar
        else:
            scrape.show_results()
    else:
        print("Terjadi kesalahan saat mengambil data")
