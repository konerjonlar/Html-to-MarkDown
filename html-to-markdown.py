
from bs4 import BeautifulSoup
import markdownify

with open("html-code.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()

# HTML metnini parse et
soup = BeautifulSoup(icerik, 'html.parser')

# Markdown formatına dönüştür
markdown_text = markdownify.markdownify(str(soup))

# Dosyayı aç ve çıktıyı dosyaya yaz
with open("html-to-markdown.md", "w", encoding="utf-8") as dosya:
    dosya.write(markdown_text)

