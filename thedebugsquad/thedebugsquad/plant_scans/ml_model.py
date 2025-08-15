import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import json
import matplotlib.pyplot as plt
from PIL import Image

def load_labels(labels_path):
    """Load class labels from a JSON file"""
    try:
        if not os.path.exists(labels_path):
            print(f"Labels file not found: {labels_path}")
            return []
            
        with open(labels_path, 'r') as f:
            labels_data = json.load(f)
            class_names = labels_data.get('labels', [])
        return class_names
    except Exception as e:
        print(f"Error loading labels file: {e}")
        return []

def preprocess_image(image_path, target_size=(224, 224)):
    """Load and preprocess an image for prediction"""
    try:
        img = load_img(image_path, target_size=target_size)
        img_array = img_to_array(img)
        img_array = img_array / 255.0  # Normalize to [0,1]
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        return img_array, img
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None, None

def predict_image(model, img_array, class_names):
    """Make a prediction on a preprocessed image"""
    try:
        predictions = model.predict(img_array, verbose=0)
        predicted_class_index = np.argmax(predictions[0])
        confidence = predictions[0][predicted_class_index]
        
        # Get top 5 predictions (or fewer if there are fewer classes)
        num_classes = min(5, len(predictions[0]))
        top_indices = np.argsort(predictions[0])[-num_classes:][::-1]
        top_predictions = []
        
        for idx in top_indices:
            class_name = class_names[idx] if idx < len(class_names) else f"Unknown (Class {idx})"
            confidence_value = predictions[0][idx]
            top_predictions.append((class_name, idx, confidence_value))
        
        return predicted_class_index, confidence, top_predictions
    except Exception as e:
        print(f"Error during prediction: {e}")
        return 0, 0.0, []

def display_prediction(img, predicted_class_index, confidence, top_predictions, class_names, save_path=None):
    """Display the image with prediction results"""
    try:
        # Check if we have valid predictions
        if not top_predictions:
            print("No valid predictions to display")
            return
            
        # Create figure
        plt.figure(figsize=(12, 6))
        
        # Display image
        plt.subplot(1, 2, 1)
        plt.imshow(img)
        plt.title("Input Image")
        plt.axis('off')
        
        # Display prediction results
        plt.subplot(1, 2, 2)
        if top_predictions:
            plt.barh([p[0] for p in top_predictions], [p[2] for p in top_predictions])
            plt.xlabel("Confidence")
            plt.title(f"Top {len(top_predictions)} Predictions")
            plt.xlim(0, 1)
        else:
            plt.text(0.5, 0.5, "No predictions available", ha='center', va='center')
        plt.tight_layout()
        
        # Save or show
        if save_path:
            plt.savefig(save_path)
            print(f"Prediction visualization saved to {save_path}")
        else:
            plt.show()
        
        # Print results
        predicted_class_name = class_names[predicted_class_index] if predicted_class_index < len(class_names) else f"Unknown (Class {predicted_class_index})"
        print(f"\nPrediction Results:")
        print(f"Predicted Class: {predicted_class_name}")
        print(f"Confidence: {confidence:.4f} ({confidence*100:.2f}%)")
        
        print(f"\nTop {len(top_predictions)} Predictions:")
        for i, (class_name, class_idx, conf) in enumerate(top_predictions):
            print(f"{i+1}. {class_name} (Class {class_idx}): {conf:.4f} ({conf*100:.2f}%)")
    except Exception as e:
        print(f"Error displaying prediction: {e}")
        # Still try to show the image if possible
        try:
            plt.figure()
            plt.imshow(img)
            plt.title("Input Image (Error in prediction display)")
            plt.axis('off')
            plt.show()
        except:
            pass

def main():
    try:
        print("\n===== Plant Disease Classification =====")
        print("This program will analyze an image to detect plant diseases.")
        print("Default model: plant_disease_model.keras")
        print("Default labels: labels.json")
        print("=========================================\n")
        
        # Get image path from user input
        image_path = input("Enter the path to the image file: ")
        
        # Set default values for other parameters
        model_path = '/Users/nehalajmal/Documents/pythoncodes/plant_disease_evaluator_clean/plant_disease_model.keras'
        labels_path = '/Users/nehalajmal/Documents/pythoncodes/plant_disease_evaluator_clean/labels.json'
        
        # Ask if user wants to save the visualization
        save_option = input("Do you want to save the visualization? (y/n, default: n): ").strip().lower()
        if save_option == 'y' or save_option == 'yes':
            save_path = input("Enter the path to save the visualization (e.g., result.png): ")
        else:
            save_path = None  # Don't save by default
        
        # Check if image file exists
        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            return
        
        # Check if model file exists
        if not os.path.exists(model_path):
            print(f"Model file not found: {model_path}")
            return
        
        # Load the model
        print(f"Loading model from {model_path}...")
        try:
            model = load_model(model_path)
        except Exception as e:
            print(f"Error loading model: {e}")
            return
        
        # Load class labels
        class_names = load_labels(labels_path)
        print(f"Loaded {len(class_names)} class names")
        
        # Preprocess the image
        print(f"Processing image: {image_path}")
        try:
            # Get input shape from model
            input_shape = model.input_shape[1:3] if hasattr(model, 'input_shape') else (224, 224)
            img_array, img = preprocess_image(image_path, target_size=input_shape)
        except Exception as e:
            print(f"Error determining model input shape: {e}")
            # Fallback to default size
            img_array, img = preprocess_image(image_path)
        
        if img_array is None:
            print("Failed to preprocess image. Exiting.")
            return
        
        # Make prediction
        print("Making prediction...")
        predicted_class_index, confidence, top_predictions = predict_image(model, img_array, class_names)
        
        # Display results
        display_prediction(img, predicted_class_index, confidence, top_predictions, class_names, save_path)
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()