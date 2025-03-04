import sqlite3
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk, messagebox
from urllib.parse import urlparse


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('web_search.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS websites 
                          (id INTEGER PRIMARY KEY, url TEXT UNIQUE)''')
        self.conn.commit()

    def add_url(self, url):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO websites (url) VALUES (?)", (url,))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_urls(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT url FROM websites")
        return [row[0] for row in cursor.fetchall()]

    def clear_db(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM websites")
        self.conn.commit()

    def __del__(self):
        self.conn.close()


class WebParser:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def search_on_page(self, url, search_term):
        try:
            response = requests.get(url, headers=self.headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text().lower()
            count = text.count(search_term.lower())
            return {'url': url, 'count': count}
        except Exception as e:
            return {'url': url, 'count': 0}

    def search_multiple(self, urls, search_term):
        results = []
        for url in urls:
            result = self.search_on_page(url, search_term)
            results.append(result)
        return sorted(results, key=lambda x: x['count'], reverse=True)


class UserInterface:
    def __init__(self, db, parser):
        self.db = db
        self.parser = parser
        self.window = Tk()
        self.window.title("Web Search")

        self.url_entry = Entry(self.window, width=50)
        self.url_entry.grid(row=0, column=0, padx=10, pady=10)
        Button(self.window, text="Додати URL", command=self.add_url).grid(row=0, column=1, padx=10, pady=10)

        self.search_entry = Entry(self.window, width=50)
        self.search_entry.grid(row=1, column=0, padx=10, pady=10)
        Button(self.window, text="Пошук", command=self.search).grid(row=1, column=1, padx=10, pady=10)

        self.results_tree = ttk.Treeview(self.window, columns=("URL", "Кількість"), show='headings')
        self.results_tree.heading("URL", text="URL")
        self.results_tree.heading("Кількість", text="Кількість збігів")
        self.results_tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        Button(self.window, text="Очистити базу", command=self.clear_db).grid(row=3, column=0, columnspan=2, pady=10)

    def add_url(self):
        url = self.url_entry.get().strip()
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        if self.db.add_url(url):
            messagebox.showinfo("Успіх", "URL додано до бази")
            self.url_entry.delete(0, END)
        else:
            messagebox.showerror("Помилка", "URL вже існує або некоректний")

    def search(self):
        search_term = self.search_entry.get().strip()
        if not search_term:
            messagebox.showwarning("Попередження", "Введіть пошуковий запит")
            return

        urls = self.db.get_urls()
        if not urls:
            messagebox.showwarning("Попередження", "Додайте URL до бази даних")
            return

        self.results_tree.delete(*self.results_tree.get_children())
        results = self.parser.search_multiple(urls, search_term)

        for result in results:
            self.results_tree.insert('', END, values=(result['url'], result['count']))

    def clear_db(self):
        if messagebox.askyesno("Підтвердження", "Очистити базу даних?"):
            self.db.clear_db()
            self.results_tree.delete(*self.results_tree.get_children())
            messagebox.showinfo("Успіх", "База даних очищена")

    def run(self):
        self.window.mainloop()


def run():
    db = Database()
    parser = WebParser()
    ui = UserInterface(db, parser)
    ui.run()


if __name__ == "__main__":
    run()