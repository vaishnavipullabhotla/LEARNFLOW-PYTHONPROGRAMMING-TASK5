import pyshorteners
import pyperclip

urls = {}  # Dictionary to store short URL mappings

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    return short_url

def main():
    while True:
        operation = input("Type of operation to be done (s: shorten, l: lengthen, e: exit): ").strip().lower()
        
        if operation == 's':
            long_url = input("Enter the URL to shorten: ").strip()
            short_url = shorten_url(long_url)
            urls[short_url] = long_url
            pyperclip.copy(short_url)  # Copy short URL to clipboard
            print(f"Shortened URL: {short_url}")

        elif operation == 'l':
            short_url = input("Enter the shortened URL: ").strip()
            long_url = urls.get(short_url)
            if long_url:
                pyperclip.copy(long_url)  # Copy long URL to clipboard
                print(f"Original URL: {long_url}")
            else:
                print("URL not found.")

        elif operation == 'e':
            break

        else:
            print("Invalid operation. Please enter 's', 'l', or 'e'.")

if __name__ == '__main__':
    main()
