
🚀 Cyno-Flow: AI-Powered Campaign Engine


Cyno-Flow is a rapid autonomous marketing suite designed to turn product ideas into high-converting copy in seconds. Built for the Cymonic.ai Hackathon, this tool leverages the power of Large Language Models to bridge the gap between product conception and market launch.
+1

📑 Table of Contents


The Problem

The Solution

Key Features

Tech Stack

Setup Instructions

❓ The Problem


Small business owners and startup founders often face "blank page syndrome" when trying to market their products. Creating consistent, high-quality content across LinkedIn, Twitter, and Email is time-consuming and expensive, often delaying actual product launches by weeks.

💡 The Solution


Cyno-Flow addresses this by providing an instant "Marketing Department in a Box." By entering a simple product description, users receive a coordinated three-channel campaign. The application is built with a robust error-handling architecture, ensuring that even during third-party API instability, the user experience remains seamless through smart fallback generators.
+1

✨ Key Features

Multi-Channel Generation: Instant copy for LinkedIn, Twitter hooks, and professional Email outreach.


Clean UX: A dark-themed, minimalist Streamlit interface designed for focus.

One-Click Export: Download your entire generated strategy as a .txt file for immediate use.

Fault-Tolerant Logic: Integrated fallback mechanisms to provide demo content if API limits are reached.

🛠️ Tech Stack

Language: Python 3.11 


Frontend Framework: Streamlit 


AI Model: Google Gemini 1.5 Flash (via REST API) 

Environment Management: Python-Dotenv


Version Control: Git & GitHub 

⚙️ Setup Instructions


Follow these steps to run Cyno-Flow on your local machine:

1. Clone the Repository


Bash
git clone https://github.com/gowrinandana21/Cyno-Flow.git
cd Cyno-Flow
3. Install Dependencies
Ensure you have Python installed, then run:

Bash
pip install streamlit requests python-dotenv google-generativeai
3. Configure Environment Variables
Create a .env file in the root directory and add your Gemini API Key:

Plaintext
GEMINI_API_KEY=your_api_key_here
4. Run the Application
Start the Streamlit server:

Bash
streamlit run app.py


🎥 Video Demo


A full walkthrough of the application, including the user flow and key features, can be found here:
## 🔗 Project Links
**GitHub Repository:** [https://github.com/gowrinandana21/Cyno-Flow](https://github.com/gowrinandana21/Cyno-Flow) 
**Video Demo:** https://www.loom.com/share/8ed8fed9b1fa4fc69548c91f49191429


Developed by: Gowri Nandana


Project for: Cymonic.ai Hackathon 2026
