# OCR Forms System

מערכת לעיבוד טפסים אוטומטי עם תמיכה בעברית.

## התקנה

### דרישות מקדימות

- Docker & Docker Compose V2
- Node.js 18+
- Python 3.11+
- Tesseract OCR

### הוראות התקנה

1. התקנת תלויות:
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

2. הפעלה:
```bash
docker compose up --build
```

הממשק זמין ב:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## תכונות

- עיבוד OCR לטפסים בעברית
- ממשק משתמש רספונסיבי
- תמיכה במגוון פורמטים
- היסטוריית עיבודים
- ייצוא תוצאות
