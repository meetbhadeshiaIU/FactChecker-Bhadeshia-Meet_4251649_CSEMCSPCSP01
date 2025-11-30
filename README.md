# Prompt based AI website to fact check news with the help of NLP

## Overview
In an era where digital information spreads at unprecedented speed, the rise of fake news has become a critical global concern. Misinformation can manipulate public opinion, influence voting behavior, incite communal tensions, and destabilize societies. With multiple news outlets often presenting biased or conflicting perspectives, identifying accurate and unbiased information has become increasingly challenging for the general public.

This project proposes the development of a prompt-based fact-checking website designed to help users quickly evaluate the credibility of news content. By leveraging natural language processing, reliable data sources, and automated verification techniques, the platform analyzes user-submitted text and identifies potential misinformation. The system highlights inconsistencies, provides context from trusted sources, and offers an objective assessment of the news item’s authenticity.

The goal of this project is to empower individuals with a practical tool that encourages informed decision-making and promotes media literacy. By helping users distinguish truth from misinformation, the platform contributes to a safer, more transparent, and more resilient information ecosystem.

## Key Features
* **Chat-Based Interface**: Intuitive chat system for seamless user interaction
* **Real-Time Fact-Checking**: Instantly analyzes user-submitted news or statements
* **Contextual Insights**: Highlights inconsistencies and provides trusted source references
* **AI-Powered Verification**: Uses advanced NLP to assess credibility and flag misinformation
* **Responsive Frontend**: Lightweight, fast, and user-friendly web experience

## System Architecture
### 1. Frontend (Client Layer)

**Technologies**: Vanilla JavaScript, HTML, CSS

* Provides an intuitive chat-style interface where users enter news, claims, or statements.

* Sends user queries to the backend using HTTP (REST API).

* Receives responses from the backend and displays:

    * Verdict (True / False / Unclear)

    * Explanation

    * Supporting evidence

* Lightweight and independent — can run on any modern browser.

### 2. Backend (Server Layer)

**Technology**: Python

* Acts as the central logic controller of the system.

* Handles incoming HTTP requests from the frontend.

* Passes the user-submitted text to the AI/NLP model for evaluation.

* Fetches external evidence from:

    * Public APIs

    * Open datasets

    * News sources

* Processes results and sends a structured JSON response back to the frontend.

### 3. AI Fact-Checking Model (NLP Layer)

**Role**: Analyze user input, extract claims, evaluate credibility

* Uses Natural Language Processing (NLP) to:

    * Understand the semantic meaning of user input

    * Perform claim extraction or text classification

    * Compare claims against retrieved evidence

    * Generate a final judgement with reasoning

* Designed to be modular → can be swapped or upgraded without changing the rest of the system.

### 4. External Evidence Sources (Retrieval Layer)

* Public APIs, open news datasets, or verified online sources supply factual context.

* The backend queries these sources to support or refute user claims.

* Ensures the system remains up-to-date and grounded in real-world data.

### 5. Communication Layer (REST API)

* Frontend and backend communicate through HTTP requests.

* A standard JSON-based REST API ensures:

    * Consistent request/response structure

    * Platform independence

    * Clear separation of concerns

* This decoupling allows the UI and backend to evolve independently.

## Folder Structure
```

├── data/
├── docs/            
├── src/
|    ├── ai model/                 # its backend + ai model                             
|    |   ├── venv/                 # for ubuntu users, virtual env
|    |   ├── main.py                
|    |   ├── model.py              # model file     
|    |   └── requirements.txt      # all python required libraries
|    ├── backend/
|    └── frontend/
|        ├── index.html            # main frontend file
|        └── styles.css
├── tests/
├── .gitignore
└── README.md
```

## Installation and Setup
### Prerequisites
```
sentence-transformers             # our model's library
fastapi                           # api library                             
uvicorn                           # for continuously running our server
```

### Quick Start
1. **Clone the repository**
1. **Install dependencies**: ```pip install -r src/requirements.txt```
1. **Run the backend** from root: python src/ai\ model/main.py
1. **Start the frontend** from src/frontend/index.html

## **About the Model: `all-mpnet-base-v2`**

`all-mpnet-base-v2` is a **Sentence Transformer** model created by **Microsoft** and fine-tuned by the SentenceTransformers team. It is one of the highest-performing general-purpose semantic similarity models.

## **Key Points**
- Built on **MPNet (Masked and Permuted Pre-training for Language Understanding)** architecture.  
- Produces **high-quality sentence embeddings** ideal for tasks like:  
  - Semantic similarity  
  - Text matching  
  - Clustering  
  - Information retrieval  
- Embedding size: **768 dimensions**  
- Average speed: **fast**, optimized for CPU and GPU usage.  
- Known for **state-of-the-art performance** on STS (Semantic Textual Similarity) benchmarks.

## **Minimum System Requirements**

This model is **lightweight** and runs on almost any modern machine.

### **Minimum Requirements (CPU Only)**
- **RAM:** 4 GB (8 GB recommended for larger batches)  
- **CPU:** Any modern dual-core processor  
- **Storage:** ~500 MB (model + dependencies)  
- **OS:** Windows, macOS, or Linux  
- **Python:** 3.8 or higher  

> Running on CPU is fully possible, just slower for large workloads.

### **Recommended Requirements (For Faster Performance)**
To achieve fast embedding generation:

- **RAM:** 8–16 GB  
- **GPU:**  
  - NVIDIA GPU with **4 GB VRAM** or more  
  - CUDA 11+  
- **Installation:** `torch` with CUDA support  

> With a GPU, embedding generation becomes **10–50x faster**.

## Goals
### **Functional Requirements**

#### **1. Ability to Classify a News Text as Fake**

The system must be capable of analyzing an input news article or statement and determining whether it exhibits characteristics commonly associated with misinformation.  
This involves:

- **Processing natural-language text**
- **Identifying linguistic patterns, claims, or features linked to fabricated or misleading content**
- Producing a clear output label such as **“Fake,” “False,” or “Likely Misinformation”**

#### **2. Ability to Classify a News Text as Correct**

The system should also recognize and label content that aligns with verified facts.  
This includes:

- **Comparing statements with known information or trusted sources** (directly or through trained model representation)
- **Identifying consistency, coherence, and factual alignment**
- Producing an output label such as **“Correct,” “True,” or “Verified”**

#### **3. Ability to Ask Questions Through Prompts**

Users should be able to interact with the model using natural-language prompts.  
This functionality should allow:

- Asking questions such as **“Is this news real?”** or **“Can you verify this claim?”**
- **Submitting custom text for analysis**
- Receiving **clear and actionable responses** from the system

### **Non-Functional Requirements**

#### **1. User Interface (UI) Quality**

The application should provide an intuitive and accessible user interface that supports easy interaction.  
Important considerations include:

- A **clean and straightforward layout** for entering news text and viewing classification results  
- **Visual indicators** (e.g., colors, icons, badges) for easier interpretation of results  

### **Safety Requirements**

#### **1. Avoiding Misclassification of Real News as Fake**

It is important that the system minimizes **false positives**—cases where genuine news is incorrectly labeled as misinformation.  
Misclassifying real news may:

- **Undermine trust** in credible sources  
- **Mislead users** and create unnecessary doubt  
- **Reduce confidence** in the system’s reliability  

Therefore:

- The classification model should be **trained and evaluated** to reduce such errors  
- **Explanations or confidence scores** may be provided to help users understand uncertainty  


## Phase status
Finalisation Phase

### **Conception Phase**

The project began with the development of a clear idea: **detecting fake news using semantic Natural Language Processing (NLP)**.  
In this phase, the focus was on understanding the problem, designing a viable approach, and defining what the system should ultimately achieve.

### **Implementation Phase**

Once the conceptual groundwork was established, the development process moved into the implementation phase.  
This phase involved building the application, testing different NLP models, and integrating the chosen model into the system.

#### **1. Initial Development Work**

The implementation began with setting up the core structure of the application.  
A decision was made to build the **frontend using Vanilla JavaScript and CSS**, as these technologies are lightweight, fast, and sufficient for the project's functional needs. The focus was on simplicity and responsiveness.

#### **2. Evaluating Semantic Similarity Models**

A significant part of the implementation revolved around selecting the most effective semantic similarity model.  
This included:

- Testing multiple pretrained NLP models.  
- Comparing their performance in understanding and matching the meaning of two text inputs.  
- Evaluating accuracy, computational efficiency, and suitability for fake news detection.

#### **3. Integrating the Selected Model**

After careful evaluation, a semantic similarity model was chosen based on its strong performance.  
It was then:

- Integrated into the backend logic.  
- Used to compute a **similarity score** between the user-provided news text and reference factual content.

#### **4. Classification Logic**

The system determines the authenticity of the news as follows:

- If the similarity score is **high**, the news is classified as **correct** because it closely matches factual information.  
- If the similarity score is **low**, the system labels the news as **fake** due to weak or inconsistent semantic alignment.  

This rule-based classification, driven by the model’s output, forms the core decision-making mechanism of the project.

## Risks
| Type | Description | Likelihood | Impact | Mitigation
|-----------|-----------|-----------|-----------|-----------|
| Resource  | Resource being copyrighted | High | High | Use publically available api  |
| Technical | Ai model giving False news | Low | High | Finetune the model more |

