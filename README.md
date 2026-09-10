# 🚢 Greenfleet — AI-Powered Maritime Fleet Optimization

> **Smart • Sustainable • Efficient Maritime Transportation**

Greenfleet is an AI-powered maritime fleet management and voyage optimization platform designed to help shipping companies reduce fuel consumption, lower carbon emissions, and improve overall fleet efficiency.

The platform combines **AI/ML-based fuel prediction**, **voyage optimization**, and **fleet monitoring** to provide data-driven recommendations for greener maritime transportation.

---

## 🌱 Problem Statement

Maritime transportation consumes large amounts of fuel and contributes significantly to global greenhouse gas emissions.

Fleet operators need to balance:

* Fuel consumption
* Vessel speed
* Cargo capacity
* Voyage efficiency
* Operational cost
* Environmental impact

Greenfleet addresses this challenge by using intelligent optimization techniques to recommend more fuel-efficient and environmentally friendly operating conditions.

---

## 💡 Our Solution

Greenfleet provides a centralized dashboard where users can enter vessel and fuel information and receive optimized recommendations.

The system analyzes vessel parameters and generates:

* Recommended vessel configuration
* Suitable fuel type
* Recommended operating speed
* Estimated fuel consumption
* Estimated emissions
* Optimization score

This allows fleet operators to make better operational decisions while reducing unnecessary fuel usage and emissions.

---

## ✨ Key Features

### 🚢 Fleet Management

Manage vessel information including:

* Vessel type
* Cargo capacity
* Number of vessels
* Fuel type
* Operational parameters

### 🤖 AI/ML Fuel Prediction

The system uses a trained machine-learning model to estimate fuel requirements based on vessel and operational parameters.

### ⚙️ Voyage Optimization

Greenfleet evaluates available vessel and fuel combinations and recommends an efficient configuration.

### 🌱 Emission Reduction

Estimated emissions help operators compare alternatives and select greener options.

### 📊 Interactive Dashboard

The web dashboard provides an easy-to-understand interface for viewing fleet information and optimization results.

### 📈 Reports

The reporting section summarizes fleet performance and optimization results.

---

## 🧠 System Workflow

```text
             ┌─────────────────────┐
             │   User Input         │
             │ Vessel & Fuel Data   │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   Fleet Database    │
             │   vessels.csv       │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ AI/ML Prediction    │
             │ Fuel Consumption    │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Optimization Engine │
             │ Speed / Fuel / Load │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Greenfleet Results  │
             │ Fuel • Emissions    │
             │ Speed • Score       │
             └─────────────────────┘
```

---

## 🏗️ Project Structure

```text
Greenfleet/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
│
├── data/
│   └── vessels.csv
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── optimization/
│   └── optimizer.py
│
├── prediction/
│   ├── fuel_model.pkl
│   └── fuel_prediction.py
│
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask
* Flask-CORS

### AI / ML

* Python
* Machine Learning
* Trained fuel prediction model

### Data & Optimization

* CSV-based vessel dataset
* Optimization algorithms
* Fuel consumption estimation
* Emission estimation

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/S1i2d3d4h5i/Greenfleet.git
```

### 2. Open the project

```bash
cd Greenfleet
```

### 3. Install Python dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Start the backend

```bash
python backend/app.py
```

The Flask backend should start on the configured local port.

### 5. Open the frontend

Open:

```text
frontend/index.html
```

in your browser.

---

## 🚀 How It Works

### Step 1 — Enter Vessel Details

The user provides information such as:

```text
Vessel Type
Fuel Type
Number of Vessels
Cargo Capacity
```

### Step 2 — Prediction

The AI/ML model estimates the expected fuel requirement.

### Step 3 — Optimization

The optimization engine evaluates the available parameters and generates a recommended configuration.

### Step 4 — Results

The dashboard displays:

```text
Recommended Speed
Estimated Fuel
Estimated Emissions
Optimization Score
```

### Step 5 — Decision Making

The fleet operator can use the results to select a more efficient and environmentally responsible operating strategy.

---

## 🌍 Environmental Impact

Greenfleet aims to support sustainable maritime transportation by helping operators:

* Reduce unnecessary fuel consumption
* Reduce greenhouse-gas emissions
* Improve vessel efficiency
* Compare different fuel options
* Make data-driven operational decisions

---

## 📊 Future Scope

Future versions of Greenfleet can include:

* Real-time vessel tracking
* Weather-aware route optimization
* Live fuel-price integration
* AIS data integration
* Advanced deep-learning models
* Carbon-credit estimation
* Multi-vessel fleet optimization
* Cloud deployment
* Mobile application
* Real-time emission monitoring
* Predictive maintenance

---

## 🏆 Smart India Hackathon

Greenfleet is developed as a prototype for **Smart India Hackathon (SIH)**, focusing on the use of AI, data, and optimization techniques to address challenges in sustainable maritime transportation.

---

## 👥 Team

**Greenfleet Team**

Developed as an academic and innovation project.

---

## 📄 License

This project is intended for educational, research, and prototype-development purposes.
