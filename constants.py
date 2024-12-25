SYSTEM_PROMPT = """
You are an AI assistant specializing in market research, AI/ML use case generation, and web data extraction.
Your role is to analyze industries, extract relevant information from the web, identify trends, and propose actionable AI/ML solutions.
Return your response in Markdown format.
"""

INTRO_PROMPT = """
 Write an introductory paragraph for Generative AI & ML use cases for {company_name} in this format:
        
        GenAI & ML Use Cases for {company_name}
        newline(/n)
        As one of the leading players in the [industry] sector, {company_name} can leverage Generative AI, Large Language Models (LLMs), and Machine Learning to enhance operational efficiency, improve product quality, and expand service offerings. By utilizing AI Planet’s GenAI Stack and collaborating with a team of AI experts, {company_name} can unlock transformative AI-driven solutions that drive innovation, streamline processes, and deliver superior results across operations. With the support of cutting-edge AI technologies, {company_name} can gain a competitive edge in the market and achieve sustainable growth.     
           
         dont mention the url"""

ADDITIONAL_RESOURCES_PROMPT = """
Based on this company description: {company_description}, perform the following:

1. Recommend agents to refer to reports and insights on AI and digital transformation from industry-specific sources like McKinsey, Deloitte, or Nexocode. Include a list of valuable reports or insights related to AI and digital transformation for the company’s industry.
2. Conduct a search for industry-specific use cases. For example, "how is the retail industry leveraging AI and ML" or "AI applications in automotive manufacturing." Provide examples and trends in how companies in the relevant industry are implementing AI/ML technologies.

Ensure that the content is specific to the company’s industry and its operational needs.
"""

USE_CASE_PROMPT = """
Based on this company description: {company_description}, generate at least 4 Generative AI & ML based on company industry department use cases in this format:

Use Case Title: [Title]
Objective/Use Case: [Objective]
AI Application: [Specific AI technology used]
Cross-Functional Benefit: [Impacts on operations, finance, supply chain, etc.]

Ensure that each use case is unique and relevant to the company's operations and industry only.
"""

KEYWORDS_PROMPT = """
Based on the following AI/ML use cases:

{use_cases}

For the use cases above,

Generate a list of relevant keywords that can be used to search datasets on platforms like Kaggle or Hugging Face. These keywords should be in the following format:

**Use Case Title:** 
**Description:** 
**Keywords:** 

The keywords should include technologies, methods, applications, and relevant industry terms. Ensure that the formatting matches the example provided:  
- Use **bold** for "Use Case Title", "Description", and "Keywords" labels only (not the content).
- The **title** should be capitalized correctly and maintain consistent formatting.
- Ensure that **keywords** are separated by commas, with no extra punctuation or line breaks.
- Provide only one unbroken paragraph for each entry.

Do not provide the information in any other format.
"""
