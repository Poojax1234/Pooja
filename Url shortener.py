import random
import string

class URLShortener:
    def __init__(self):
        self.url_to_short = {}
        self.short_to_url = {}
        self.chars = string.ascii_letters + string.digits
        self.base_url = "http://short.ly/"

    def generate_short_key(self, length=6):
        return ''.join(random.choice(self.chars) for _ in range(length))

    def shorten_url(self, original_url):
        if original_url in self.url_to_short:
            return self.base_url + self.url_to_short[original_url]

        while True:
            short_key = self.generate_short_key()
            if short_key not in self.short_to_url:
                self.short_to_url[short_key] = original_url
                self.url_to_short[original_url] = short_key
                return self.base_url + short_key

    def expand_url(self, short_url):
        short_key = short_url.split("/")[-1]
        if short_key in self.short_to_url:
            return self.short_to_url[short_key]
        else:
            return "URL not found."

if __name__ == "__main__":
    shortener = URLShortener()

    while True:
        print("1. Shorten URL")
        print("2. Expand Short URL")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            original_url = input("Enter the URL to shorten: ")
            short_url = shortener.shorten_url(original_url)
            print(f"Shortened URL: {short_url}")

        elif choice == "2":
            short_url = input("Enter the short URL to expand: ")
            original_url = shortener.expand_url(short_url)
            print(f"Original URL: {original_url}")

        elif choice == "3":
            break