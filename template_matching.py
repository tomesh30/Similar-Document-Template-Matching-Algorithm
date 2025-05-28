import cv2
import numpy as np
import os

def find_template_in_image(image_path, template_path, output_path=None, show_steps=False):
    """
    Find a template in an image using template matching and draw a bounding box around it.
    
    Args:
        image_path (str): Path to the input image
        template_path (str): Path to the template image
        output_path (str, optional): Path to save the output image. If None, won't save.
        show_steps (bool): Whether to display intermediate processing steps
    
    Returns:
        tuple: (top_left_x, top_left_y, width, height) of the bounding box, or None if not found
    """
    # Validate file paths
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return None
    if not os.path.exists(template_path):
        print(f"Error: Template file not found at {template_path}")
        return None

    # Load images
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read image at {image_path}")
            return None
            
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Error: Could not read template at {template_path}")
            return None
    except Exception as e:
        print(f"Error loading images: {str(e)}")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    if show_steps:
        cv2.imshow('Input Image', image)
        cv2.imshow('Template', template)
        cv2.waitKey(0)

    # Perform template matching
    try:
        result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    except Exception as e:
        print(f"Error in template matching: {str(e)}")
        return None

    # Get the best match location
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # You can adjust this threshold based on your needs
    confidence_threshold = 0.8
    if max_val < confidence_threshold:
        print(f"Template not found with sufficient confidence (max confidence: {max_val:.2f})")
        return None

    # Get template dimensions
    h, w = template.shape
    
    # Create bounding box (using actual template size)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    # Draw rectangle on the image
    output_image = image.copy()
    cv2.rectangle(output_image, top_left, bottom_right, (0, 0, 255), 2)
    
    # Add confidence text
    cv2.putText(output_image, f'Confidence: {max_val:.2f}', 
                (top_left[0], top_left[1] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    
    if show_steps:
        cv2.imshow('Matching Result', output_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # Save output if requested
    if output_path:
        try:
            cv2.imwrite(output_path, output_image)
            print(f"Result saved to {output_path}")
        except Exception as e:
            print(f"Error saving output image: {str(e)}")
    
    return (*top_left, w, h)

# Example usage
if __name__ == "__main__":
    # Replace these paths with your actual image paths
    image_path = r"C:\Users\ASMIT BISEN\OneDrive\Desktop\Prac_Codes_Python\PYTHON\projects\mbill.png"  # The image where you want to find the object
    template_path = r"C:\Users\ASMIT BISEN\OneDrive\Desktop\Prac_Codes_Python\PYTHON\projects\seal.jpg"   # The template image you're searching for
    output_path = r"C:\Users\ASMIT BISEN\OneDrive\Desktop\Prac_Codes_Python\PYTHON\projects"       # Where to save the result (optional)
    
    # Call the function
    result = find_template_in_image(image_path, template_path, output_path, show_steps=True)
    
    if result:
        x, y, w, h = result
        print(f"Found template at position (x={x}, y={y}) with size (w={w}, h={h})")
    else:
        print("Template not found in the image")