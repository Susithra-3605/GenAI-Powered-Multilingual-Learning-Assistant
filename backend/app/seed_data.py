from .db import db

def seed_lessons():
    lessons = [
        {
            "id": "1",
            "title": "Introduction to Numbers",
            "language": "hi",
            "content": "संख्या गिनना सीखें",
            "quiz": ["2 + 2 = ?", "5 - 3 = ?"]
        },
        {
            "id": "2",
            "title": "Basic Tamil Alphabets",
            "language": "ta",
            "content": "அகர முதல எழுத்தெல்லாம்",
            "quiz": ["What comes after அ?", "What is the sound of இ?"]
        }
    ]
    db.lessons.insert_many(lessons)
    print("Seed data inserted.")
