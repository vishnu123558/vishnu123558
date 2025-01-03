# Nutritionist AI - Personal Dietary Assistant

## Description

**Nutritionist AI** is an innovative mobile application designed to provide personalized dietary recommendations and nutritional advice using the advanced capabilities of the Gemini Pro model. The app leverages artificial intelligence to analyze user data, dietary preferences, and health goals, delivering tailored meal plans, nutritional insights, and wellness tips. The primary aim of Nutritionist AI is to promote healthier eating habits and improve overall well-being through intelligent and data-driven recommendations.

## Requirements

Before setting up and running the application, ensure that you meet the following prerequisites:

- **Python** version **3.9+** (Python 3.13 recommended)
- **Streamlit** library (for the user interface)
- **Google Generative AI** for the AI-based content generation
- **dotenv** library for environment variable management
- **Pillow** library for image handling

## Installation

Follow the steps below to install the required dependencies and set up the environment:

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/nutritionist-ai.git
cd nutritionist-ai
```

### Step 2: Create a virtual environment (recommended)
It is recommended that a virtual environment be created to manage dependencies.

```bash
python -m venv .venv
```
### Step 3: Activate the virtual environment
For Windows (PowerShell):

```bash
.\.venv\Scripts\Activate.ps1
```
If you encounter a script execution policy issue, you can run:
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

For MacOS/Linux:
```bash
source .venv/bin/activate
```

### Step 4: Install dependencies
Once the virtual environment is activated, install the required dependencies by running:

```bash
pip install -r requirements.txt

```
### Step 5: Set up environment variables
Click the provided link to access the following webpage.

Link: https://ai.google.dev/gemini-api/docs/api-key
![image](https://github.com/user-attachments/assets/a1496c44-db85-4f2a-b33f-225b1fb6cf22)


After signing in to your account, navigate to the 'Get an API Key' option. Clicking on this option will redirect you to another webpage as shown below.
![image](https://github.com/user-attachments/assets/e4be78cc-b95f-470c-9c93-9541cfb418de)

Next, click on 'Create API Key' and choose the generative language client as the project. Then, select 'Create API key in existing project'.
![image](https://github.com/user-attachments/assets/1f98b0e4-cfa9-4a5d-9eaf-544a67b2d71d)

Copy the newly generated API key as it is required for loading the Gemini Pro pre-trained model.


Add your API KEY in .env file

```bash
GOOGLE_API_KEY=your_api_key_here
```


Running the Application
You can run the application once all dependencies are installed and the environment variables are set up.

Run the Streamlit app
Start the Streamlit app using the following command:

```bash
streamlit run app.py
```

### OUTPUTS
![image](https://github.com/user-attachments/assets/c8f4803f-6a1b-46a2-9fef-575d60045d9b)
![image](https://github.com/user-attachments/assets/f66059c6-a39a-4853-8508-9f972e66e319)


