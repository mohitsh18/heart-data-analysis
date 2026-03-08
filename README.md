# Heart Disease Data Analysis

A Flask web application for analyzing heart disease patient data with interactive dashboards and data visualizations.

## Features

- Interactive Tableau-style dashboards
- Demographic analysis (age, gender, ethnicity)
- Lifestyle factors analysis (smoking, alcohol, physical activity)
- Medical insights (BMI, diabetes, stroke correlations)
- Data storytelling with visualizations
- Risk factor identification

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **Data Processing:** Pandas
- **Deployment:** Gunicorn

## Project Structure

```
heart-data-analysis/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── config.py                # Database configuration
├── Procfile                 # Deployment config (Heroku)
├── app.py                   # Flask application
├── load.data.py             # MySQL data loader script
├── data/
│   └── Heart_new2.csv       # Dataset
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── background.jpg
│       ├── contact.png
│       ├── hero.png
│       └── hero1.png
└── templates/
    ├── base.html
    ├── index.html
    ├── about.html
    ├── dashboard.html
    └── story.html
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd heart-data-analysis
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup

1. Install MySQL Server
2. Create database:
```sql
CREATE DATABASE heart_disease_db;
```

3. Update database credentials in `load.data.py` if needed:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="heart_disease_db"
)
```

4. Load data into database:
```bash
python load.data.py
```

### 5. Run the Application
```bash
# Development
python app.py

# Production (with gunicorn)
gunicorn app:app
```

### 6. Access the Application
Open your browser and navigate to: `http://localhost:5000`

## Pages

- **Home** (`/`) - Landing page with features overview
- **About** (`/about`) - About the project
- **Dashboard** (`/dashboard`) - Interactive data dashboards
- **Story** (`/story`) - Data stories and visualizations

## Deployment

### Heroku
The app is configured for Heroku deployment with `Procfile` and `requirements.txt`.

```bash
heroku create
git push heroku main
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

