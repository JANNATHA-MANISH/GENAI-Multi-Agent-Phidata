---

# **Market Research & Use Case Generator**

alt text

---

## **Project Overview**

The **Market Research & Use Case Generator** is a modular Python-based system designed to automate the following tasks:
1. **Content Extraction**: Extracts text content from a given company URL using Tavily Extract.
2. **AI-Powered Use Case Generation**: Uses Phidata's Gemini model to generate AI/ML use cases, introductory paragraphs, and additional resources based on the extracted content.
3. **Dataset Collection**: Fetches relevant datasets from Kaggle based on dynamically generated keywords.

The system leverages **Tavily Extract**, **Phidata's Gemini model**, and the **Kaggle API** to provide a streamlined workflow for market research, AI use case generation, and dataset retrieval.

---

## **Table of Contents**

- [Project Overview](#project-overview)
- [Architecture Diagram](#architecture-diagram)
- [Data Storage Files](#data-storage-files)
- [Sample Input and Output](#sample-input-and-output)
- [Execution Instructions](#execution-instructions)
- [Requirements](#requirements)
- [License](#license)

---

## **Architecture Diagram**

Below is the architecture diagram of the system:

```plaintext
+-----------------------------------+
| Market Research & Use Case Gen   |
| Streamlit App                    |
+-----------------------------------+
              |
              v
+-----------------------------------+
| Tavily Extract                   |
| Extracts content from URL         |
+-----------------------------------+
              |
              v
+-----------------------------------+
| Phidata's Gemini Model           |
| Generates AI/ML use cases,       |
| keywords, and additional insights|
+-----------------------------------+
              |
              v
+-----------------------------------+
| Kaggle API                        |
| Fetches datasets based on         |
| generated keywords                |
+-----------------------------------+
              |
              v
+-----------------------------------+
| Outputs:                          |
| - usecases_txt.txt (Use Cases)    |
| - datasets.csv (Datasets)         |
+-----------------------------------+
```

---

## **Data Storage Files**

The following files are created by the system to store the output:

| **File Name**       | **Data Type** | **Description**                                                  |
|----------------------|---------------|------------------------------------------------------------------|
| `usecases_txt.txt`  | Plain Text    | Contains AI-generated use cases derived from extracted content.  |
| `datasets.csv`      | CSV           | Contains Kaggle datasets fetched based on generated keywords.    |

---

## **Sample Input and Output**

### **Sample Input**
#### Company URL:
```plaintext
https://www.tatamotors.com/
```

### **Sample Output**

#### `usecases_txt.txt`:
```plaintext
Use Case Title: Predictive Maintenance for Commercial Vehicles
Objective/Use Case: Machine learning models to predict failures in commercial vehicle fleets using sensor data.
AI Application: Predictive modeling using time series analysis and anomaly detection.
Cross-Functional Benefit: Reduces downtime, optimizes maintenance schedules, and improves fleet efficiency.

Use Case Title: Customer Sentiment Analysis for Automotive Brands
Objective/Use Case: Analyze customer feedback from social media platforms to improve customer satisfaction.
AI Application: Natural Language Processing (NLP) for sentiment analysis.
Cross-Functional Benefit: Enhances customer experience and identifies pain points in real-time.
```

#### `datasets.csv`:
```csv
Use Case Title,Use Case Description,Keyword,Dataset Name,Dataset Link,Source
Predictive Maintenance for Commercial Vehicles,"Machine learning models to predict failures in commercial vehicle fleets using sensor data.","predictive maintenance","Vehicle Sensor Data","https://www.kaggle.com/dataset-xyz","Kaggle"
Customer Sentiment Analysis for Automotive Brands,"Analyze customer feedback from social media platforms to improve customer satisfaction.","sentiment analysis","Social Media Sentiment Dataset","https://www.kaggle.com/dataset-abc","Kaggle"
```

---

## **Execution Instructions**

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/market-research-use-case-generator.git
cd market-research-use-case-generator
```

---

### 2. Set Up the Environment

Create a virtual environment (optional but recommended):

```bash
python -m venv menv
```

Activate the virtual environment:
- On Windows:
  ```bash
  menv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source menv/bin/activate
  ```

---

### 3. Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

---

### 4. Configure API Keys

Create a `.streamlit/secrets.toml` file in the root directory and add your API keys:

```toml
[default]
TAVILY_KEY = "your_tavily_api_key"
GEMINI_KEY = "your_google_api_key"
```

Replace `"your_tavily_api_key"` and `"your_google_api_key"` with your actual API keys.

---

### 5. Run the Streamlit App

To run the app:

```bash
streamlit run market_research_agent.py
```

Enter your company URL in the input field and click "Run Analysis."

---

## **Requirements**

The following dependencies are required for this project:

- Python 3.9 or later
- Libraries listed in `requirements.txt`:
  ```plaintext
  phidata             
  pandas            
  kaggle             
  streamlit         
  tavily-python    
  ```

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
