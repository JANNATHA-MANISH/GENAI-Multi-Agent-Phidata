## **Low-Level Design (LLD)**
# **Market Research & Use Case Generator**

## **Overview**

The **Market Research & Use Case Generator** is a system designed to analyze a company's web presence, extract relevant content, generate AI/ML use cases, and fetch datasets related to these use cases. It integrates with third-party APIs, including **Tavily** for content extraction, **Google Gemini** for natural language processing, and **Kaggle** for fetching datasets. The application saves and displays aggregated results in structured formats like `.txt` and `.csv`.

---

## **Key Modules & Components**

### **1. User Interface (UI)**

- **Streamlit Interface**: The web-based UI allows users to input a company URL and interact with the system to generate and display use cases, datasets, and additional insights.

### **2. APIs**

- **Tavily API**: For extracting content from a provided company URL.
- **Google Gemini API (via `phi.agent.Agent`)**: For generating use cases, keywords, and AI applications based on the extracted content.
- **Kaggle API**: For fetching datasets based on keywords generated from the extracted content.

### **3. Data Processing**

- **Content Extraction**: Extract relevant content from the provided company URL using the Tavily API.
- **Use Case Generation**: Generate detailed use cases, AI applications, and keywords using Google Gemini.
- **Dataset Aggregation**: Fetch relevant datasets from Kaggle based on the generated keywords and aggregate them for further analysis.

### **4. File Outputs**

- **Generated Content Files**: Save use cases as `.txt` files and datasets as `.csv` files for further use or analysis.

---

## **Functions & Methods**

### **1. Core Functions**

#### **1.1. `get_tavily_client()`**

This function initializes the Tavily API client.

- **Input**: None
- **Output**: `TavilyClient` object

```python
def get_tavily_client():
    return TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
```

#### **1.2. `get_agent()`**

Initializes the Gemini model agent for generating content and use cases.

- **Input**: None
- **Output**: Gemini Agent object

```python
def get_agent():
    return Agent(
        model=Gemini(id="gemini-1.5-flash"),
        system_prompt=SYSTEM_PROMPT,
        markdown=True,
    )
```

#### **1.3. `extract_content_from_url(url)`**

Extracts raw content from the provided URL using the Tavily API.

- **Input**: `url` (string)
- **Output**: Extracted content (string)

```python
def extract_content_from_url(url):
    try:
        tavily_client = get_tavily_client()
        response = tavily_client.extract(
            urls=[url],
            include_raw_content=True,
            include_images=False
        )
        return response["results"][0]["raw_content"] if response else "No content extracted."
    except Exception as e:
        st.error(f"Error extracting content: {e}")
        return ""
```

#### **1.4. `fetch_datasets_from_kaggle(keyword)`**

Fetches Kaggle datasets based on the provided keyword.

- **Input**: `keyword` (string)
- **Output**: List of datasets (list of dictionaries)

```python
def fetch_datasets_from_kaggle(keyword):
    try:
        api = KaggleApi()
        api.authenticate()
        search_results = api.dataset_list(search=keyword)
        return [
            {"name": dataset.title, "url": f"https://www.kaggle.com/{dataset.ref}", "source": "Kaggle"}
            for dataset in search_results[:5]
        ]
    except Exception as e:
        st.error(f"Error fetching datasets: {e}")
        return []
```

#### **1.5. `parse_use_cases_and_keywords(use_cases_response, keywords_response)`**

Parses the Gemini-generated use cases and keywords into a structured list.

- **Input**: `use_cases_response` and `keywords_response` (Gemini API responses)
- **Output**: Structured list of use cases

```python
def parse_use_cases_and_keywords(use_cases_response, keywords_response):
    use_cases = []
    use_case_blocks = use_cases_response.content.split("\n\n")
    
    for block in use_case_blocks:
        use_case = {}
        for line in block.strip().split("\n"):
            if line.startswith("Use Case Title:"):
                use_case["title"] = line.split(":")[1].strip()
            elif line.startswith("Objective/Use Case:"):
                use_case["description"] = line.split(":")[1].strip()
            elif line.startswith("AI Application:"):
                use_case["ai_application"] = line.split(":")[1].strip()
            elif line.startswith("Cross-Functional Benefit:"):
                use_case["cross_functional_benefit"] = line.split(":")[1].strip()

        for keyword_block in keywords_response.content.split("\n\n"):
            if f"**Use Case Title:** {use_case['title']}" in keyword_block:
                keywords_line = keyword_block.split("**Keywords:**")[1].strip()
                use_case["keywords"] = [kw.strip() for kw in keywords_line.split(",")]
                break

        if all(key in use_case for key in ["title", "description", "keywords"]):
            use_cases.append(use_case)
    
    return use_cases
```

#### **1.6. `process_and_aggregate(use_cases)`**

Aggregates the use cases and fetches Kaggle datasets based on the keywords for each use case.

- **Input**: List of parsed use cases
- **Output**: Aggregated DataFrame containing use case titles, descriptions, datasets, and sources

```python
def process_and_aggregate(use_cases):
    all_resources = []
    
    for use_case in use_cases:
        title = use_case["title"]
        description = use_case["description"]
        keywords = use_case["keywords"]
        
        for keyword in keywords[:4]:  # Limit to top 4 keywords
            kaggle_datasets = fetch_datasets_from_kaggle(keyword)
            for dataset in kaggle_datasets:
                all_resources.append({
                    "Use Case Title": title,
                    "Use Case Description": description,
                    "Keyword": keyword,
                    "Dataset Name": dataset["name"],
                    "Dataset Link": dataset["url"],
                    "Source": dataset["source"]
                })

    df = pd.DataFrame(all_resources)
    
    if not df.empty:
        aggregated_df = df.groupby(['Use Case Title', 'Use Case Description']).agg({
            'Keyword': lambda x: ', '.join(sorted(x.unique())),
            'Dataset Name': lambda x: ', '.join(sorted(x.unique())),
            'Dataset Link': lambda x: ', '.join(sorted(x.unique())),
            'Source': lambda x: ', '.join(sorted(x.unique()))
        }).reset_index()

        return aggregated_df
    return pd.DataFrame()
```

---

## **Process Flow**

The process flow of the system is as follows:

1. **User Inputs URL**: The user provides a company URL via the Streamlit UI.
2. **Content Extraction**: The system extracts the raw content from the URL using Tavily API.
3. **Use Case Generation**: The extracted content is processed by the Gemini model to generate use cases.
4. **Keyword Extraction**: Keywords are generated from the use cases for fetching relevant datasets.
5. **Dataset Fetching**: Datasets related to the keywords are fetched from Kaggle.
6. **Data Aggregation & Output**: The results are aggregated and saved to `.csv` and `.txt` files for easy access.

---

## **Data Flow Diagram**

Below is the data flow between various components in the system:

```
+---------------------------------------------------------------+
|                        Streamlit UI                           |
|---------------------------------------------------------------|
|    [User Inputs URL] -> [Press Run Analysis]                   |
+---------------------------------------------------------------+
            |                            |
            v                            v
+---------------------------------------------------------------+
|  Extract Content from URL (Tavily)                             |
|---------------------------------------------------------------|
|       [Company URL] -> [Tavily API] -> [Extract Raw Content]   |
+---------------------------------------------------------------+
            |                            |
            v                            v
+---------------------------------------------------------------+
|  Generate Introductory Paragraph (Gemini)                     |
|---------------------------------------------------------------|
|        [Extracted Content] -> [Gemini] -> [Intro Paragraph]    |
+---------------------------------------------------------------+
            |                            |
            v                            v
+---------------------------------------------------------------+
|  Generate Use Cases (Gemini)                                   |
|---------------------------------------------------------------|
|        [Extracted Content] -> [Gemini] -> [Use Cases]          |
+---------------------------------------------------------------+
            |                            |
            v                            v
+---------------------------------------------------------------+
|  Generate Keywords (Gemini)                                    |
|---------------------------------------------------------------|
|        [Use Cases] -> [Gemini] -> [Keywords]                   |
+---------------------------------------------------------------+
            |                            |
            v                            v
+---------------------------------------------------------------+
|  Fetch Datasets from Kaggle (Based on Keywords)                |
|---------------------------------------------------------------|
|        [Keywords] -> [Kaggle API] -> [Fetch Datasets]          |
+---------------------------------------------------------------+
            |                            |
            v                            v
+---------------------------------------------------------------+
|  Aggregate Results & Save to Files                             |
|---------------------------------------------------------------|
|   [Aggregated Data] -> [Save to CSV and TXT] -> [Display Data] |
+---------------------------------------------------------------+
```

---

## **Error Handling**

- **Tavily

 API**: If the API fails to extract content, a user-friendly error message will be displayed in the UI.
- **Google Gemini API**: Handles missing or malformed responses gracefully.
- **Kaggle API**: Manages API limits and authentication errors with appropriate error messages.

---

## **Conclusion**

This README outlines the detailed design for the **Market Research & Use Case Generator** application. The system architecture, API interactions, methods, and error handling are described in-depth to ensure a smooth, user-friendly experience. By following this design, the application efficiently aggregates and displays relevant datasets and use cases, allowing users to gain insights into AI/ML opportunities based on company-specific content.

