from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/display')
def display():
    # Get data from request parameters
    image_url = request.args.get('image_url', '')
    text = request.args.get('text', '')
    rect_color = request.args.get('rect_color', '#000000')  # Default to white if not provided
    text_bottom = request.args.get('text', '')
    text_color= request.args.get('rect_color', '#FFFFFF')

    return render_template('index.html', image_url=image_url, text=text,text_bottom=text_bottom, rect_color=rect_color,text_color=text_color)

if __name__ == '__main__':
    app.run(debug=True)
