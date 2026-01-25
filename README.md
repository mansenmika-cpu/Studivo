🎓 Studivo: AI-Powered Academic Assistant
Studivo is an all-in-one educational platform designed to streamline study management and provide personalized AI tutoring. By combining resource organization with the power of Gemini-2.5-flash, Studivo helps students master their subjects through interactive dialogue and multimodal learning.

⚙️ Installation & Local Setup
Follow these steps to get a local copy of Studivo up and running on your machine.

1. Clone the Repository
Open your terminal or command prompt and run:

Bash

git clone https://github.com/mansenmika-cpu/Studivo.git
cd Studivo

2. Set Up a Virtual Environment (Recommended)
This keeps your project dependencies organized and separate from your system Python:

Bash

# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Required Packages
Install all necessary libraries defined in the project requirements:

Bash

pip install -r requirements.txt

Note: This will install streamlit, pandas, google-generativeai, and other essential tools for the AI and UI.

4. Configure Your API Secrets
The app requires an API key to communicate with the Gemini-2.5-flash model.

Create a folder named .streamlit in the root directory.

Create a file named secrets.toml inside that folder.

Add your key exactly like this:

Ini, TOML

GEMINI_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"

5. Initialize the Database
Ensure the modules.csv file is in the root directory. If it doesn't exist, the app will create a new one when you add your first module.

6. Launch the App
Run the main entry file to start the Streamlit server:

Bash

streamlit run start.py
