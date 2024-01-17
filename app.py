from flask import Flask, render_template, request,send_from_directory

app = Flask(__name__)

@app.route('/')
def display():
    # Get data from request parameters
    image_url = request.args.get('image_url', '')
    text = request.args.get('text', '')
    rect_color = request.args.get('rect_color', '#000000')  # Default to white if not provided
    text_bottom = request.args.get('text', '')
    text_color= request.args.get('rect_color', '#FFFFFF')

    return render_template('index.html', image_url=image_url, text=text,text_bottom=text_bottom, rect_color=rect_color,text_color=text_color)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('meme', filename)
