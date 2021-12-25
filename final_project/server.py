from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

# print(translator.english_to_french("Hello"))

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translation_french = translator.english_to_french(textToTranslate)
    return translation_french

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translation_english = translator.french_to_english(textToTranslate)
    return translation_english

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    # app.run(debug=True, port=5555)
    app.run(host="0.0.0.0", port=8080)
