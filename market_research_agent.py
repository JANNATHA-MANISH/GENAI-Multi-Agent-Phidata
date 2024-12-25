import streamlit as st
import os
import pandas as pd
from phi.agent import Agent
from phi.model.google import Gemini
from tavily import TavilyClient  
from kaggle.api.kaggle_api_extended import KaggleApi  
from constants import SYSTEM_PROMPT, INTRO_PROMPT, ADDITIONAL_RESOURCES_PROMPT, USE_CASE_PROMPT, KEYWORDS_PROMPT


os.environ['TAVILY_API_KEY'] = st.secrets["TAVILY_KEY"]
os.environ['GOOGLE_API_KEY'] = st.secrets["GEMINI_KEY"]


usecases_output_path = "usecases_txt.txt"
datasets_output_path = "datasets.csv"


def get_tavily_client():
    return TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def get_agent():
    return Agent(
        model=Gemini(id="gemini-1.5-flash"),
        system_prompt=SYSTEM_PROMPT,
        markdown=True,
    )


def extract_content_from_url(url):
    try:
        tavily_client = get_tavily_client()
        response = tavily_client.extract(
            urls=[url],
            include_raw_content=True,
            include_images=False
        )
        if response and "results" in response:
            results = response["results"]
            if results:
                return results[0].get("raw_content", "No text content extracted.")
        return "No text content extracted."
    except Exception as e:
        st.error(f"Error extracting content from {url}: {e}")
        return ""


def fetch_datasets_from_kaggle(keyword):
    try:
        api = KaggleApi()
        api.authenticate()
        search_results = api.dataset_list(search=keyword)
        return [
            {"name": dataset.title,
             "url": f"https://www.kaggle.com/{dataset.ref}",
             "source": "Kaggle"}
            for dataset in search_results[:5]  
        ]
    except Exception as e:
        st.error(f"Error fetching datasets from Kaggle: {e}")
        return []


def parse_use_cases_and_keywords(use_cases_response, keywords_response):
    use_cases = []
    use_case_blocks = use_cases_response.content.split("\n\n")  

    for block in use_case_blocks:
        lines = block.strip().split("\n")
        use_case = {}
        for line in lines:
            if line.startswith("Use Case Title:"):
                use_case["title"] = line.split("Use Case Title:")[1].strip()
            elif line.startswith("Objective/Use Case:"):
                use_case["description"] = line.split("Objective/Use Case:")[1].strip()
            elif line.startswith("AI Application:"):
                use_case["ai_application"] = line.split("AI Application:")[1].strip()
            elif line.startswith("Cross-Functional Benefit:"):
                use_case["cross_functional_benefit"] = line.split("Cross-Functional Benefit:")[1].strip()

        
        if use_case.get("title"):
            for keyword_block in keywords_response.content.split("\n\n"):
                if f"**Use Case Title:** {use_case['title']}" in keyword_block:
                    keywords_line = keyword_block.split("**Keywords:**")[1].strip()
                    use_case["keywords"] = [kw.strip() for kw in keywords_line.split(",")]
                    break

            
            if all(key in use_case for key in ["title", "description", "keywords"]):
                use_cases.append(use_case)

    return use_cases


def process_and_aggregate(use_cases):
    all_resources = []

    
    for use_case in use_cases:
        title = use_case["title"]
        description = use_case["description"]
        keywords = use_case["keywords"]
        st.write(f"Fetching datasets for: {title}")

        for keyword in keywords[:4]:  
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

    st.write("No datasets found.")
    return pd.DataFrame()


st.title("Market Research & Use Case Generator")

company_url = st.text_input("Enter the company URL:")

if st.button("Run Analysis"):
    try:
        agent = get_agent()

        
        st.write(f"Extracting content from URL: {company_url}")
        extracted_content = extract_content_from_url(company_url)


        
        intro_prompt_filled = INTRO_PROMPT.format(company_name=company_url)
        intro_response = agent.run(intro_prompt_filled)
        st.write(f"Introductory Paragraph:\n\n{intro_response.content}")

        
        additional_resources_prompt_filled = ADDITIONAL_RESOURCES_PROMPT.format(company_description=extracted_content)
        additional_resources_response = agent.run(additional_resources_prompt_filled)
  

        
        use_cases_prompt_filled = USE_CASE_PROMPT.format(company_description=extracted_content)
        use_cases_response = agent.run(use_cases_prompt_filled)
        st.write(f"Use Cases:\n{use_cases_response.content}")

        
        keywords_prompt_filled = KEYWORDS_PROMPT.format(use_cases=use_cases_response.content)
        keywords_response = agent.run(keywords_prompt_filled)
        st.write(f"Keywords:\n{keywords_response.content}")

        
        parsed_use_cases = parse_use_cases_and_keywords(use_cases_response, keywords_response)

        
        aggregated_df = process_and_aggregate(parsed_use_cases)

        full_output = f"{intro_response.content}\n\n{use_cases_response.content}"
        
        with open(usecases_output_path, "w") as f:
            f.write(full_output)

        if not aggregated_df.empty:
            aggregated_df.to_csv(datasets_output_path, index=False)
            st.write(f" atasets saved to {datasets_output_path}.")
            st.dataframe(aggregated_df)

    except Exception as e:
        st.error(f"Error: {e}")
