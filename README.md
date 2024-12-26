
# **Market Research & Use Case Generator**

Welcome to the **Market Research & Use Case Generator**! This tool allows users to input a company's URL, extract its content, generate actionable AI/ML use cases from the content, and fetch relevant datasets from **Kaggle**. Powered by third-party APIs like **Tavily**, **Google Gemini**, and **Kaggle**, this system helps you identify AI opportunities and access valuable datasets for analysis.

---

## **Table of Contents**

1. [Overview](#overview)
2. [Features](#features)
3. [System Architecture](#system-architecture)
4. [Modules](#modules)
5. [Getting Started](#getting-started)
6. [Technologies Used](#technologies-used)
7. [How to Use](#how-to-use)
8. [Output](#output)
9. [Contributing](#contributing)
10. [License](#license)

---

## **Overview**

The **Market Research & Use Case Generator** is designed to extract valuable insights from any company’s website. By analyzing the company’s content, the system generates relevant AI/ML use cases and identifies datasets related to those use cases. You can download these results in `.csv` and `.txt` formats.

### **Key Features**
- **URL Input**: Simply input a company's URL, and the system will handle the rest.
- **Content Extraction**: Automatically extracts content from the given URL using the **Tavily API**.
- **Use Case Generation**: Generates actionable AI/ML use cases and keywords using **Google Gemini**.
- **Dataset Fetching**: Fetches relevant datasets from **Kaggle** based on generated keywords.
- **Downloadable Results**: Get structured results in `.csv` and `.txt` formats for easy access.

---

## **System Architecture**

The **Market Research & Use Case Generator** follows a modular architecture, comprising several interconnected components:

1. **User Interface (UI)**: Built with **Streamlit**, the UI allows users to input URLs and interact with the application.
2. **API Integrations**:
    - **Tavily API**: Extracts content from the provided URL.
    - **Google Gemini API**: Analyzes content and generates AI/ML use cases.
    - **Kaggle API**: Retrieves relevant datasets for generated keywords.
3. **Data Processing**: Aggregates use cases and datasets into a final output.
4. **Output Handling**: Allows users to download results in `.csv` and `.txt` formats.

### **Architecture Diagram**
```plaintext
+----------------------------+
|      Streamlit UI           |
|                            |
|  1. Input URL               |
|  2. Trigger Analysis        |
+----------------------------+
            |
            v
+----------------------------+     +-------------------------------+     +----------------------------+
|     Tavily API             |---->|   Google Gemini API           |---->|    Kaggle API              |
|   Extracts Content         |     |  Generates Use Cases          |     |  Fetches Datasets          |
|   from the URL             |     |  and Keywords                |     |  based on Keywords         |
+----------------------------+     +-------------------------------+     +----------------------------+
            |                                                      |
            v                                                      v
+----------------------------------------------------------------------------+
|       Data Aggregation                                                     |
|  Aggregates Use Cases & Datasets                                           |
|  Structures Data for Output                                                |
+----------------------------------------------------------------------------+
            |
            v
+----------------------------+
| Output Handling            |
|  1. Save to .csv and .txt  |
|  2. Display Results        |
+----------------------------+
```

---

## **Data Storage Files**

The following files are created by the system to store the output:

| **File Name**       | **Data Type** | **Description**                                                  |
|----------------------|---------------|------------------------------------------------------------------|
| `usecases_txt.txt`  | Plain Text    | Contains AI-generated use cases derived from extracted content.  |
| `datasets.csv`      | CSV           | Contains Kaggle datasets fetched based on generated keywords.    |


---

## **Modules**

### **1. User Interface (UI)**
- **Streamlit** web interface for input and interaction.
- User inputs a company URL, triggers the analysis, and views results.

### **2. Tavily API Integration**
- Extracts content from the provided company URL.
- The raw content is sent for further processing.

### **3. Google Gemini API Integration**
- Generates AI/ML use cases and keywords based on the extracted content.

### **4. Kaggle API Integration**
- Fetches relevant datasets based on generated keywords.

### **5. Data Aggregation**
- Combines use cases and datasets into structured files for output.

---

## **Getting Started**

To get started with the **Market Research & Use Case Generator**, follow these steps:

### **Prerequisites**

- Python 3.8 or higher
- API keys for **Tavily**, **Google Gemini**, and **Kaggle**

### **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/JANNATHA-MANISH/GENAI-Multi-Agent-Phidata
   cd market-research-use-case-generator
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   - Create a `.env` file and add your API keys for **Tavily**, **Google Gemini**, and **Kaggle**.

   Example `.env` file:

   ```env
   TAVILY_API_KEY=your-tavily-api-key
   GEMINI_API_KEY=your-gemini-api-key
   KAGGLE_API_KEY=your-kaggle-api-key
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

---

## **Technologies Used**

- **Streamlit** – For building the interactive web interface.
- **Tavily API** – For extracting content from websites.
- **Google Gemini API** – For generating AI/ML use cases.
- **Kaggle API** – For fetching relevant datasets.
- **Python 3.x** – The primary programming language.
- **Pandas** – For data manipulation and structuring.
- **dotenv** – For environment variable management.

---

## **How to Use**

1. **Input a URL**: Enter the URL of a company’s website in the provided text field.
2. **Trigger Analysis**: Click the "Start Analysis" button to begin the process.
3. **View Results**: Once the process is complete, view the generated use cases and related datasets.
4. **Download Files**: Download the results as `.csv` and `.txt` files for further analysis.

---

## **Output**

After running the analysis, the following output will be available:

- **Use Cases**: A list of AI/ML use cases related to the company’s website, with detailed descriptions and potential applications.
- **Datasets**: A list of datasets related to the generated use cases, fetched from Kaggle.

### **Example Output Files**
- **use_cases.txt**:
   ```txt
   Use Case Title: Predictive Maintenance for Commercial Vehicles
   Objective/Use Case: To reduce downtime and maintenance costs for Tata Motors'......
   AI Application:  Machine Learning .
   Cross-Functional Benefit:  Reduced maintenance costs in the operations department....
   ```

- **datasets.csv**:
   | Dataset Name            | Dataset Link                        | Source       | Keywords                        |
   |-------------------------|-------------------------------------|--------------|---------------------------------|
   | Predictive Maintenance   | https://www.kaggle.com/datasets/xyz | Kaggle       | predictive maintenance, IoT     |
   | IoT Sensor Data         | https://www.kaggle.com/datasets/abc | Kaggle       | IoT, sensor data, maintenance   |

---

## **Execution Instructions**

### 1. Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/market-research-use-case-generator.git
cd market-research-use-case-generator
```

---

### 2. Set Up the Environment

(Optional but recommended) Create a virtual environment for the project:

```bash
python -m venv menv
```

Activate the virtual environment:
- **On Windows**:
  ```bash
  menv\Scripts\activate
  ```
- **On macOS/Linux**:
  ```bash
  source menv/bin/activate
  ```

---

### 3. Install Dependencies

Install all necessary dependencies by running:

```bash
pip install -r requirements.txt
```

---

### 4. Configure API Keys

To interact with the APIs, you need to configure your API keys. Create a `.streamlit/secrets.toml` file in the root directory and add your keys:

```toml
[default]
TAVILY_KEY = "your_tavily_api_key"
GEMINI_KEY = "your_google_api_key"
```

Be sure to replace `"your_tavily_api_key"` and `"your_google_api_key"` with your actual keys.

---

### 5. Run the Streamlit App

Finally, to launch the app:

```bash
streamlit run market_research_agent.py
```

Once the app is running, enter your company URL and click **"Run Analysis"** to start generating use cases and fetching datasets.

---

## **Requirements**

This project requires Python 3.9 or higher, along with the following dependencies:

```plaintext
phidat
pandas
kaggle
streamlit
tavily-python
```

To install the dependencies:

```bash
pip install -r requirements.txt
```

---

## **DOCUMENTATION :**
---
https://drive.google.com/file/d/1uDMRBJfOdL4V-ElIY1H3XEIdzkkoVLWa/view?usp=sharing

## **DEMO VIDEO :**
---
https://drive.google.com/file/d/16lrw72mziKges8VysBQLw4l6lOuqMlCP/view?usp=sharing

---
