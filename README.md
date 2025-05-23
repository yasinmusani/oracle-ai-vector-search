# Oracle AI Vector Search Starter

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

- Oracle Database 23ai
- Python 3.11+
- Flask (API backend)
- Streamlit (Frontend UI)
- Hugging Face Transformers (`sentence-transformers/all-MiniLM-L6-v2`)
- oracledb (Oracle Python driver)
- numpy, pandas

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
python app/populate_embeddings.py
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

Refer to [`sample_data.csv`](sample_data.csv) for sample products. Insert them into your Oracle DB using a bulk `INSERT` statement and generate embeddings for the `VECTOR` column.

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

---
"""

readme_path = Path("/mnt/data/README.md")
readme_path.write_text(readme_content.strip())
readme_path.name
