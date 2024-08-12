import sys
import webbrowser

urls = {
    "fashion": ["https://in.louisvuitton.com/eng-in/homepage", "https://www.gucci.com/", "https://www.prada.com/"],
    "study": ["https://www.w3schools.com/", "https://chat.openai.com/"],
    "tutorial": ["https://www.youtube.com", "https://www.udemy.com"]
}

def open_websites(urls):
    for url in urls:
        webbrowser.open(url)

if __name__ == "__main__":
    set_name = sys.argv[1]
    urls = urls[set_name]
    open_websites(urls)