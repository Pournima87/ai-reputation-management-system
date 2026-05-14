# 🚀 AI Reputation Management System  
### OnShore Labs — Product Engineer Intern Assignment  

<p align="center">

AI-powered Online Reputation Management platform for restaurants & hotels that aggregates customer reviews, performs AI sentiment analysis, generates business insights, and provides actionable recommendations.

</p>

---

# 🌟 Project Overview

Restaurants and hotels receive customer feedback across multiple platforms such as:

- Google Reviews
- Zomato
- Swiggy
- TripAdvisor
- Reddit & Social Media

Managing and analyzing these reviews manually is difficult and time-consuming.

This project provides a **centralized AI-powered dashboard** that helps businesses:

✅ Monitor customer sentiment  
✅ Analyze reviews from multiple platforms  
✅ Detect complaints & compliments  
✅ Generate AI-based responses  
✅ Discover operational improvement opportunities  
✅ Export filtered business reports  

The application is designed as a **scalable MVP** for a real-world **Online Reputation Management System**.

---

# ✨ Features

---

## 📊 1. Multi-Business Reputation Dashboard

- Business-wise filtering
- City-wise filtering
- Website/platform-wise filtering
- Dynamic dashboard updates
- KPI analytics
- Interactive visualizations

---

## 🔗 2. Review Aggregation

The system simulates review aggregation from multiple platforms:

- Google Reviews
- Zomato
- Swiggy
- TripAdvisor

The project uses:

- Mock connectors
- Seeded datasets
- Scalable connector architecture

---

## 🤖 3. AI Sentiment Analysis

Each review is analyzed for:

### ✅ Sentiment Detection
- Positive
- Neutral
- Negative

### 😊 Emotion Detection
- Happy
- Neutral
- Frustrated
- Disappointed

### 🧠 Topic Extraction
- Food Quality
- Service
- Ambience
- Pricing
- General

### 🚨 Priority Detection
- High
- Medium
- Low

---

## 📌 4. AI Reputation Insights

The platform generates:

- Overall reputation summary
- Positive review summary
- Negative review summary
- Neutral review summary
- Common customer complaints
- Common customer compliments
- AI actionable recommendations

---

## 💬 5. AI Review Response Generator

Users can:

- Select review priority
- Select individual reviews
- Generate AI-powered professional responses

Generated responses are:

✅ Professional  
✅ Empathetic  
✅ Brand-safe  
✅ Human-like  

---

## 📈 6. Advanced NLP Analytics

The analytics dashboard includes:

- Emotion distribution
- Topic distribution
- Complaint vs compliment analysis
- Source-wise insights
- Review priority segmentation

---

## 📥 7. Exportable Business Reports

Users can download dynamically filtered business datasets as CSV reports.

### Example Reports
- Spice Garden Report
- Royal Dine Report
- Bombay Canteen Report

This demonstrates real-world business intelligence workflows.

---

# 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| AI / NLP | OpenAI API (via OpenRouter) |
| Styling | Custom CSS |

---

# 📂 Project Structure

```bash
AI-REPUTATION-MANAGER/
│
├── app.py
├── requirements.txt
├── .env.example
│
│
├── components/
│   └── sidebar.py
│
├── tabs/
│   ├── dashboard.py
│   ├── ai_insights.py
│   ├── review_management.py
│   └── advanced_analytics.py
│
├── utils/
│   ├── data_loader.py
│   ├── emotion_detector.py
│   ├── priority.py
│   └── topic_extractor.py
│
├── styles/
│   └── main.css
│
└── data/
    └── Restaurant_Reviews.tsv
```

---

# 🏗️ Architecture Explanation

The project follows a **modular architecture approach**.

---

## 🧩 Components Layer

Handles reusable UI components such as:

- Sidebar filters
- Reusable UI blocks

---

## 📑 Tabs Layer

Contains independent dashboard modules:

- Dashboard
- AI Insights
- Review Management
- Advanced Analytics

---

## ⚙️ Utils Layer

Handles:

- NLP processing
- Topic extraction
- Emotion detection
- Priority scoring
- Data loading

---

## 🔌 Connectors Layer

Implements modular mock connectors for different review platforms.

This architecture allows future scalability for:

- Real API integrations
- Live scraping pipelines
- Background jobs
- Multi-platform expansion

Without affecting the core dashboard logic.

---

# ⚡ Setup Instructions

---

## 1️⃣ Clone Repository

```bash
git clone <your-github-repository-url>
```

---

## 2️⃣ Open Project Folder

```bash
cd ai-reputation-management-system
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Create Environment File

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## 7️⃣ Run Application

```bash
streamlit run app.py
```

---

# 📊 Mock Data Notes

This project uses:

- Seeded review datasets
- Simulated review sources
- Mock connector architecture

No aggressive or unsafe scraping has been implemented.

The system respects:

✅ Platform terms of service  
✅ Publicly available data only  
✅ No login-protected scraping  
✅ No spam automation  
✅ No personal data misuse  

---

# ✅ Completed Features

- Multi-business dashboard
- Dynamic filtering
- AI sentiment analysis
- Topic extraction
- Emotion detection
- Priority scoring
- AI-generated summaries
- AI-generated review replies
- Advanced analytics dashboard
- Source-wise filtering
- Exportable filtered reports
- Modular connector architecture
- Custom UI styling
- GitHub-ready structure

---

# 🚀 Future Improvements

- Real API integrations
- Live review fetching
- Authentication system
- Multi-user dashboards
- PDF report exports
- Review trend forecasting
- AI chatbot assistant
- Database integration
- Deployment scaling
- Real-time monitoring

---

# 🎥 Demo Video

https://github.com/user-attachments/assets/4fec4c5d-cc2e-4825-8347-1261a973adfb

---

# 🌐 Live Demo

> Add Deployment Link Here

---

# 🔐 Environment Variables

Example `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# ☁️ Deployment

The application can be deployed using:

- Streamlit Cloud
- Render
- Railway

---

# 👨‍💻 Author

### Pournima More

Computer Science Student • Full Stack Developer • AI Enthusiast

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback.
