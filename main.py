from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/<subject>')
def get_page(subject):
    return render_template('./' + subject + '.html')


@app.route("/unitwise/<subject>")
def unitwisedbms(subject):
    return render_template('./unitwise/' + subject + '.html')


@app.route('/questions/<subject>')
def get_questions(subject):
    print(subject)
    with open('./json/' + subject + '.json') as file:
        questions_data = json.load(file)
    return jsonify(questions_data)


@app.route('/unitwisequestions/<subject>')
def get_unitwise_questions(subject):
    print(subject)
    with open('./json/unitwise/' + subject + '.json') as file:
        questions_data = json.load(file)
    return jsonify(questions_data)


@app.route("/scrape", methods=['GET'])
def scrape():
    # scraper = WebScraper()
    # scraper.scrape_options()
    return "Scraping done!"


if __name__ == '__main__':
    app.run()
