from flask import Flask, render_template, request,send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve parameters from the request
    image_url = request.args.get('image_url', '')
    top_text = request.args.get('top_text', )  # Default value is 'Top Text'
    bottom_text = request.args.get('bottom_text',)  # Default value is 'Bottom Text'
    rect_color = request.args.get('rect_color', '#000000')  # Default rect color

    # Pass the parameters to the template
    return render_template('index.html', image_url=image_url, top_text=top_text, bottom_text=bottom_text, rect_color=rect_color)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('vadivel', filename)