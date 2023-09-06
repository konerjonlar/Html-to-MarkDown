# HTML'den Markdown'a Dönüştürücü
# HTML to Markdown Converter

Bu araç, html-code.txt dosyasındaki HTML kodlarını markdown formatına dönüştüren bir araçtır. Dönüştürülen veriler html-to-markdown.txt dosyasına kaydedilir.

This is a tool that converts HTML codes in the html-code.txt file to markdown format. The converted data is saved in the html-to-markdown.txt file.

## Klonlama / Clone 

Git kurulumu: 

Git installation: 

- [Windows/ Linux/ Mac](https://www.atlassian.com/git/tutorials/install-git)
  
Projeyi klonlayacağımız klasörde terminali açın. Ardından aşağıdaki komutu terminale girin.

Open terminal in the folder where we will clone the project. Then enter the following command in terminal.

```bash
git clone https://github.com/konerjonlar/Html-to-MarkDown
```

Bulunduğunuz dizie **Html-to-MarkDown** dosyası eklenmiş olmalı. 

The **Html-to-MarkDown** file must have been added to the directory you are in. 

## Kurulum / Setup

Proje klasörü içerisine cd(change directory) komutu ile geçiş yapalım. 

Let's switch to the project folder with the cd (change directory) command. 

```bash
cd Html-to-MarkDown
``` 

Öncelikle sanal bir ortam oluşturun ve etkinleştirin:

First create and activate a virtual environment:

```bash
python -m venv venv
```
Diğer başka kullanımda da sanal ortam gizli klasör olarak projeye dahil edilebilir. Klasör isminin temelde önemi olmasa da Python'da topluluk izinden gitmek önemli bir husustur. 

In another use, the virtual environment can be included in the project as a hidden folder. While the folder name is not fundamentally important, following the community footsteps is an important consideration in Python. 

```bash
python -m venv v ".env"
```

Etkinleştirme:
Activation:

[Linux/Mac](https://www.sinanerdinc.com/python-virtualenv-kullanimi) 

```bash
source venv/bin/activate 
```

[Windows](https://medium.com/@sonsuz_dongu_youtube/windows-ortam%C4%B1na-python-ve-virtualenv-kurma-209f0257a564) 

```bash
venv\Scripts\activate
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
