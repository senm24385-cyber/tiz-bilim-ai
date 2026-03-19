import random

# User memory system
memory = {}

def detect_level(score):
    if score < 30:
        return "beginner"
    elif score < 70:
        return "intermediate"
    return "advanced"

def simplify(text):
    return f"Has ýönekeý düşündiriş: {text}"

def teacher_response(user_id, message, score, weak_topics):

    user = memory.get(user_id, {
        "score": score,
        "weak_topics": weak_topics,
        "attention": 5,
        "last_topic": ""
    })

    level = detect_level(user["score"])

    # 🧠 Explanation Agent
    if level == "beginner":
        explanation = f"{message} — muny örän ýönekeý düşündireýin."
    elif level == "intermediate":
        explanation = f"{message} — indi muny biraz çuň düşündireýin."
    else:
        explanation = f"{message} — professional derejede düşündiriş."

    # 🌍 Example Agent (2 real-life examples)
    examples = [
        "Mysal 1: bazarda söwda edýän wagtyň hasaplama.",
        "Mysal 2: dostlaryň bilen pul paýlaşanyňda ulanýan logika."
    ]

    # ❤️ Emotion Agent
    if "düşünmedim" in message.lower():
        explanation = simplify(explanation)
        emotion = "Bolýar, başga ýol bilen düşündireýin."
        user["weak_topics"].append(message)
    else:
        emotion = random.choice([
            "Gowy barýaň 👍",
            "Ajaýyp, dowam et!",
            "Sen muny başarýaň 💪"
        ])

    # ⚙️ Difficulty Adapter
    if user["score"] < 50:
        question = "Sorag: Ýönekeý mysal bilen düşündirip bilersiňmi?"
    else:
        question = "Sorag: Muny başga ýagdaýda ulanyp bilersiňmi?"

    # 🎯 Motivation Agent
    motivation = "Sen her gün gowulaşýaň."

    # 🧩 Planner Agent
    next_step = "Indi indiki ädime geçeli."

    response = f"""
Düşündiriş:
{explanation}

{examples[0]}
{examples[1]}

{emotion}
{motivation}

{question}
{next_step}
"""

    # 📊 Update learning score
    user["score"] = min(100, user["score"] + 2)

    memory[user_id] = user

    return {
        "response": response,
        "learning_score": user["score"],
        "weak_topics": user["weak_topics"]
    }
