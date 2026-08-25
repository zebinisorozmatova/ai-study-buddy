🤖 AI Study Buddy

AI Study Buddy is an AI-powered learning assistant that analyzes students' mistakes and generates personalized exercises based on their knowledge level.

✨ Features

- 🤖 AI-powered answer analysis
- 🧠 Detects weak and strong topics
- 📚 Generates personalized exercises
- 💡 Explains mistakes in simple language
- 📈 Tracks learning progress
- 🎯 Automatically adjusts exercise difficulty
- 🔄 Creates new exercises based on previous mistakes

🛠️ Tech Stack

- Frontend: React / Next.js
- Backend: Python + FastAPI
- AI: OpenAI API
- Database: PostgreSQL
- Authentication: JWT
- Deployment: Vercel + Render

⚙️ How It Works

Student
   ↓
Answers a question
   ↓
AI analyzes the answer
   ↓
Identifies mistakes
   ↓
Updates knowledge profile
   ↓
Generates a personalized exercise
   ↓
Student solves the new exercise
   ↓
Progress is updated

🚀 MVP

The first version focuses on three core features:

1. Answer a question
2. Analyze the answer using AI
3. Generate the next personalized exercise

📂 Project Structure

ai-study-buddy/
├── frontend/
├── backend/
│   ├── api/
│   ├── models/
│   ├── services/
│   └── main.py
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

🔐 Environment Variables

Create a ".env" file and add:

OPENAI_API_KEY=your_api_key
DATABASE_URL=your_database_url
JWT_SECRET=your_secret_key

«Never commit your ".env" file or API keys to GitHub.»

📌 Roadmap

- [x] Project setup
- [ ] User authentication
- [ ] AI answer analysis
- [ ] Personalized exercise generation
- [ ] Progress tracking
- [ ] Student dashboard
- [ ] Difficulty adaptation
- [ ] Deployment

🤝 Contributing

Contributions, ideas, and improvements are welcome. Feel free to open an issue or submit a pull request.

📄 License

This project is licensed under the MIT License.
