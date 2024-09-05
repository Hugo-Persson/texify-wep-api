from flask import Flask, request, jsonify
from PIL import Image
from texify.inference import batch_inference
from texify.model.model import load_model
from texify.model.processor import load_processor
import io

app = Flask(__name__)
model = None
processor = None

def get_processor():
    global processor
    if processor is None:
        processor = load_processor()
    return processor

def get_model():
    global model
    if model is None:
        model = load_model()
    return model

@app.route('/predict', methods=['POST'])
def predict():
    print('Request received')
    try:
        # Get the image file from the request
        print(request.files)
        image_file = request.files['image'].stream
        print(request.files)
        if not image_file:
            return jsonify({'error': 'No image provided'}), 400

        image = Image.open(image_file)
        print("Image opened successfully")
        model = get_model()
        processor = get_processor()
        results = batch_inference([image], model, processor)
        # Create a JSON response
        response = {
            'success': True,
            'message': 'Image processed successfully',
            'results': results
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
