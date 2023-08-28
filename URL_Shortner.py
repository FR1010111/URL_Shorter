import random
import string

class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

    def shorten_url(self, original_url):
        if original_url in self.url_to_code:
            return self.url_to_code[original_url]

        short_code = self.generate_short_code()
        self.url_to_code[original_url] = short_code
        self.code_to_url[short_code] = original_url
        return short_code
    
    def expand_url(self, short_code):
        return self.code_to_url.get(short_code, "URL not found")

if __name__ == "__main__":
    url_shortener = URLShortener()

    while True:
        choice = input("Enter 's' to shorten a URL, 'e' to expand a URL, or 'q' to quit: ").lower()

        if choice == 's':
            original_url = input("Enter the original URL: ")
            short_code = url_shortener.shorten_url(original_url)
            print(f"Shortened URL: http://short.url/{short_code}")
        
        elif choice == 'e':
            short_code = input("Enter the short code: ")
            original_url = url_shortener.expand_url(short_code)
            print(f"Original URL: {original_url}")
        
        elif choice == 'q':
            break


#FR1010111