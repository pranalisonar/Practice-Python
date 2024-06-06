from flask import Flask, request, send_file 
from PIL import Image 
app = Flask(name) 
@app.route('/process-image', methods=['POST']) 
def process_image():  
    image_file = request.files['image']  # Load the image using Pillow  
    image = Image.open(image_file)  # Perform desired image processing tasks  # Example: resizing the image to a specific size  
    resized_image = image.resize((800, 600))  # Save the processed image  
    processed_image_path = 'processed_image.jpg'  
    resized_image.save(processed_image_path)  
    return send_file(processed_image_path, mimetype='image/jpeg') # Usage if __name_ == '_main_':  
app.run()