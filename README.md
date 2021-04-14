# PDF-Form-Filling
PDF Form Filling with unicode characters such as Arabic. 

## Behind the scene

Filling PDF Form with arabic characters is such a pain. It took around a week to explore Github, and I found there are 2 main libraries that being used.

1. PDFTK
2. iTextPDF

#### PDFTK

A library based on Java. There are many wrapper on every programming languages, such as PHP, Go, Javascript, etc. This is the simple way to fill PDF Form automatically. If you are not bother with unicode characters, then this is the main way to go. 

#### iTextPDF

Also based on Java. The current version is PAID. But you could found an old version with JAR extension. This is able to do form filling with unicode characters, but not very stable due the version I was using. 

## Which to use

The current answer for this question is, [PDFRW (https://github.com/pmaupin/pdfrw)](https://github.com/pmaupin/pdfrw). It is based on Python. If you are coming from PHP, Python is not scary as its looks. It's quite fun, and this is your time to learn Python.

## Weaknes?

There is two weaknesess when you are using PDFRW, the PDF Result should be open with Adobe Acrobat Reader. The other PDF Viewer such as browser version or Preview from macOS could not handle the value all the time. So you might find some fields are empty, some are not.

The second one, all the fields inside the PDF Form should be using default font that all computer should have. Arial and Helvetica could be use.

## Preparing

You should have Python 3.x installed and these libraries:

1. PDFRW
```text
# pip install pdfrw
```
## How to use

Put the `formfilling.py` on your working directory. You may check example.py to start over.

```python
from formfilling import FormFilling

field_data = """
field_key_name This is the value
fieldname_ar ندما يريد العالم أن ‪يتكلّم ‬
"""
form = FormFilling()
output = form.generate(field_data, "./pdf_template.pdf", "./output")
print(output)
```


