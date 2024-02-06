from flask import Flask, render_template, request, redirect, url_for
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

app = Flask(__name__)

# Load the locally stored model and tokenizer
model_name = "vuk/bart-finetuned-samsum"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a summarization pipeline
summarizer = pipeline('summarization', model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template for the input form

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        text = request.form['text']
        result = summarizer(text)
        summary = result[0]['summary_text']
        # Pass the original text and summary to the summary.html template
        return render_template('summary.html', original_text=text, summary=summary)
    else:
        # Handle invalid request method
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
