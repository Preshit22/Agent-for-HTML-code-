# Agent-for-HTML-code-
This project involves building a web application that converts screenshots into HTML and Tailwind CSS code. The application consists of a FastAPI backend and a Streamlit frontend. Users can upload an image through the Streamlit interface, which then sends the image to the FastAPI server. 

# Features
- Image Upload: Upload screenshots in PNG, JPG, or JPEG formats.
- HTML & Tailwind CSS Generation: Converts uploaded screenshots to HTML and Tailwind CSS code using OpenAI's model.
- Real-Time Preview: Displays the generated HTML code and renders the output in the Streamlit interface.
- Image Generation: Automatically generates images referenced in the HTML using AI.

# Installation
**Prerequisites** 
- Python 3.8+
- Git
- Virtual environment tool (e.g., venv, virtualenv)
 
**Clone the Repository**
    git clone https://github.com/Preshit22/Agent-for-HTML-code-
    cd <repository_directory>

**Set Up the Backend**
- Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

- Install the required packages:
    pip install -r requirements.txt

- Create a .env file in the root directory and add your OpenAI API key:

    OPENAI_API_KEY=your_openai_api_key
  
- Start the FastAPI server:
    uvicorn main:app --reload

**Set Up the Frontend**
- Open a new terminal window and navigate to the project directory.
- Activate the virtual environment:
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

- Run the Streamlit app:
    streamlit run app.py

# Usage
- Open the Streamlit app in your browser.
- Upload an image using the file uploader.
- Click the "Generate Code" button.
- View the generated HTML and Tailwind CSS code.
- See the rendered output of the generated HTML code.
- 
# Project Structure
    .
    ├── main.py                     # FastAPI entry point
    ├── app.py                      # Streamlit entry point
    ├── routes
    │   └── generate_code.py        # Endpoint for image processing and code generation
    ├── prompts
    │   ├── __init__.py             # Prompt assembly functions
    │   └── screenshot_system_prompts.py  # System prompts for HTML and Tailwind CSS generation
    ├── image_generation.py         # Functions for handling image processing
    ├── llm.py                      # Functions for interacting with OpenAI's model
    ├── config.py                   # Configuration file for API keys and other settings
    ├── requirements.txt            # Python dependencies
    └── README.md                   # Project README file


# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgements
- OpenAI for providing the API and models.
- FastAPI for the backend framework.
- Streamlit for the frontend framework.
