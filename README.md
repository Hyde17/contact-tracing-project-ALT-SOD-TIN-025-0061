# Contact Tracing & Exposure Analysis System

A simple Python-based contact tracing system that tracks infection status, records contact events, and identifies high-risk exposures based on cumulative contact duration.

---

## 📌 Features

- Track people and their infection status
- Record contact events with duration validation
- Automatically register new people during contact logging
- Aggregate exposure duration across multiple contact events
- Identify **high-risk exposures** (≥ 15 minutes total exposure)
- Generate a readable exposure report

---

## 🧠 How It Works

1. Each person has an infection status (`infected` or `not infected`).
2. Contacts are logged as `(person1, person2, duration)`.
3. If an infected person has contact with a non-infected person, the exposure time is accumulated.
4. If total exposure time reaches **15 minutes or more**, the contact is classified as **high risk**.

---

## 🗂️ Data Structures

```python
infection_status = {}  # { person_name: bool }
contacts = []          # [ (person1, person2, duration) ]
