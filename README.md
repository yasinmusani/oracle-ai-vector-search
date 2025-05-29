# Oracle AI Vector Search Starter

**Disclaimer:** This project is a personal initiative created for educational purposes and is not affiliated with or endorsed by my employer.


![Oracle AI Vector Search](OracleAIVectorSearchStarter_Cover.png)

A sample project demonstrating Oracle Database 23ai's **AI vector search capabilities** using **Hugging Face embeddings** and a user-friendly **Streamlit interface**. Includes both API and UI to explore semantic product search.

---

## 🔧 Features

- 🔌 Connects to Oracle Database 23ai
- 🤗 Uses Hugging Face Transformers to generate embeddings
- 📦 Stores vector data in Oracle `VECTOR` column type
- 🔍 Performs semantic vector search using `VECTOR_DISTANCE`
- 🌐 Flask API for programmatic access
- 🖥️ Streamlit UI for user-friendly search interface

---

## 🛠 Tech Stack

This project utilizes the following technologies, each licensed by their respective vendors:

- **Oracle Database 23ai**: Licensed product of Oracle Corporation. This project does not include or distribute any Oracle software or proprietary content.
- **Python 3.11+**: Open-source programming language licensed under the [Python Software Foundation License](https://docs.python.org/3/license.html).
- **Flask**: A lightweight WSGI web application framework licensed under the [BSD-3-Clause License](https://flask.palletsprojects.com/en/2.0.x/license/).
- **Streamlit**: An open-source app framework for Machine Learning and Data Science licensed under the [Apache 2.0 License](https://github.com/streamlit/streamlit/blob/develop/LICENSE).
- **Hugging Face Transformers**: A library for state-of-the-art NLP licensed under the [Apache 2.0 License](https://github.com/huggingface/transformers/blob/main/LICENSE).
- **oracledb**: Oracle Python driver licensed under the [Oracle License](https://www.oracle.com/database/technologies/appdev/python.html).
- **numpy**: A fundamental package for scientific computing with Python licensed under the [BSD License](https://numpy.org/doc/stable/license.html).
- **pandas**: A fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool licensed under the [BSD-3-Clause License](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html#license).

> **Disclaimer:** This project is intended for educational purposes only and is not affiliated with or endorsed by Oracle Corporation or any other vendor mentioned.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yasinmusani/oracle-ai-vector-search.git
cd oracle-ai-vector-search
```

### 2. Create and Activate Python Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download or Provide Hugging Face Model

Place the Hugging Face model (e.g. `all-MiniLM-L6-v2`) locally under:

```
models/all-MiniLM-L6-v2/
```

You can download it using:

```python
from transformers import AutoModel, AutoTokenizer
AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
```

Then move the `.cache` content into `models/`.

---

### 5. Configure Oracle DB Credentials

Update your `.env` file or hardcode in `db_utils.py`:

```
DB_USER=hr
DB_PASSWORD=oracle
DB_DSN=localhost/freepdb1
```

---

### 6. Populate Vector Embeddings

```bash
python app/vectorize_update.py
```

---

### 7. Run Flask API

```bash
python app/main.py
```

- Endpoint: `http://localhost:5000/search`
- Sample Request:

```json
{
  "query": "smartphone"
}
```

---

### 8. Run Streamlit App

```bash
streamlit run app/ui.py
```

- Visit: `http://localhost:8501`

---

## 🧪 Sample Data

Refer to [`sample_products.csv`](sample_products.csv) for sample products. Insert them into your Oracle DB using a bulk `INSERT` statement and generate embeddings for the `VECTOR` column.

---

## 📬 Example Output

**Request**:

```json
{ "query": "Watch" }
```

**Response**:

```json
{
  "results": [
    ["Smartwatch", "Fitness tracking with heart rate monitor", 0.8155],
    ["Smartphone", "Latest model with AI camera features", 0.8299],
    ["eBook Reader", "6-inch glare-free display", 0.8787],
    ["Gaming Keyboard", "Mechanical keyboard with RGB lighting", 0.9783],
    ["Noise Cancelling Headphones", "Over-ear headphones with ANC", 0.9808]
  ]
}
```
