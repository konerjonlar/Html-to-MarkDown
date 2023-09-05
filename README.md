# HTML'den Markdown'a Dönüştürücü
# HTML to Markdown Converter

Bu araç, html-code.txt dosyasındaki HTML kodlarını markdown formatına dönüştüren bir araçtır. Dönüştürülen veriler html-to-markdown.txt dosyasına kaydedilir.

This is a tool that converts HTML codes in the html-code.txt file to markdown format. The converted data is saved in the html-to-markdown.txt file.

## Kurulum / Setup

Öncelikle sanal bir ortam oluşturun ve etkinleştirin:

First create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
``` 

Gerekli Python bağımlılıklarını yüklemek için aşağıdaki komutu kullanın:

Use the following command to install the required Python dependencies:

```bash
pip install -r requirements.txt
```

## Kullanım / Use

Dönüşüm işlemini başlatmadan önce için html kodlarınızı html-code.txt dosyasına ekleyin.

Add your html codes to the html-code.txt file before starting the conversion process.

Dosyayı kaydettikten sonra aşağıdaki komutu çalıştırın:

After saving the file run the following command:

```bash
python html-to-markdown.py

```
### Örnek / Example

HTML dosyası (html-code.txt) içeriği:

HTML file (html-code.txt) content:

```html
<html>
  <body>
    <h1>Hello, World!</h1>
    <p>This is a simple HTML to Markdown conversion example.</p>
  </body>
</html>
```

```bash
python html-to-markdown.py
```

Markdown dosyası (html-to-markdown.md) çıktısı:

Markdown file (html-to-markdown.md) content:

```markdown
# Hello, World!

This is a simple HTML to Markdown conversion example.
```
