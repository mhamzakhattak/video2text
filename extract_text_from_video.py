### Video text extractor

import cv2
import pytesseract

def extract_text_from_video(video_path, output_file):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Initialize the OCR engine (change according to file path)
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    frame_count = 0

    extracted_text = ''

    while video.isOpened():
        # Read the current frame
        ret, frame = video.read()

        # Check if the frame was read successfully
        if not ret:
            break

        # Preprocess the frame (e.g., resize, denoise, enhance quality)
        processed_frame = preprocess_frame(frame)

        # Perform OCR on the processed frame
        text = perform_ocr(processed_frame)

        # Append the extracted text to the result
        extracted_text += text

        frame_count += 1

    # Release the video capture object
    video.release()

    # Remove spaces from the extracted text
    extracted_text = extracted_text.replace(' ', '')

    # Convert the text to ASCII
    ascii_text = extracted_text.encode('ascii', 'ignore').decode('ascii')

    # Write the ASCII text to the output file
    with open(output_file, 'w') as f:
        f.write(ascii_text)

def preprocess_frame(frame):
    # Implement any necessary preprocessing techniques on the frame
    # This may include resizing, denoising, contrast enhancement, etc.
    # Return the preprocessed frame
    return frame

def perform_ocr(frame):
    # Perform OCR on the frame using Tesseract OCR engine
    # You may need to adjust configuration options based on your specific requirements
    extracted_text = pytesseract.image_to_string(frame)

    # Return the extracted text
    return extracted_text

# Path to the video file
video_path = '/input/path'
# Path to the output text file
output_file = '/output/path'

# Call the function to extract text and save to file
extract_text_from_video(video_path, output_file)
