# 🛒 BigMart Sales Prediction

A machine learning web application that predicts the sales of BigMart products based on product and outlet characteristics. The project uses a trained regression model and provides an interactive interface for real-time sales prediction.

---

## 📌 Overview

BigMart retailers require accurate sales forecasting to optimize inventory management, pricing strategies, and business planning. This project leverages Machine Learning to estimate product sales using historical product and outlet information.

The application enables users to input product details and instantly receive predicted sales through a simple web interface.

---

## 🚀 Features

- Interactive web application
- Real-time sales prediction
- Pre-trained Machine Learning model
- User-friendly interface
- Fast prediction response
- Docker support for deployment

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Web Framework | Streamlit |
| Model Serialization | Pickle |
| Deployment | Docker |

---

## 📂 Project Structure

```
BIGMART/
│
├── app/
│   ├── app.py
│   ├── BigMart_Sales_Model.pkl
│   ├── requirements.txt
│   ├── Dockerfile
│   └── BigMart_Sales_Prediction.ipynb
│
├── README.md
├── .gitignore
└── how_to_run.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/BIGMART.git
```

### 2. Navigate to the project

```bash
cd BIGMART/app
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📊 Machine Learning Workflow

- Data Collection
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Model Serialization (.pkl)
- Web Application Integration
- Real-Time Prediction

---

## 📥 Input Features

The application accepts product and outlet information such as:

- Item Weight
- Item Fat Content
- Item Visibility
- Item Type
- Item MRP
- Outlet Identifier
- Outlet Size
- Outlet Location Type
- Outlet Type
- Outlet Establishment Year

---

## 📈 Output

The model predicts:

**Estimated Product Sales**

---

## 📷 Application Preview

Add screenshots inside a folder named `images/`.

Example:

```
images/
    home.png
    prediction.png
```

Then include them as:

```markdown
![Home](images/home.png)

![Prediction](images/prediction.png)
```

---

## 🔮 Future Improvements

- Model retraining with larger datasets
- Multiple regression model comparison
- Cloud deployment
- Prediction history
- Batch prediction using CSV upload
- Performance analytics dashboard

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Visarapu Rohith**

- B.Tech – Computer Science & Engineering (AI & ML)
- Interested in Software Development, Machine Learning, and Artificial Intelligence.

---

### ⭐ If you found this project useful, consider giving it a Star.
