def generate_questions_skills(skills):
    questions = []
    # Question templates for skills
    skill_questions = {
        "Python": "Can you explain how you manage memory in Python?",
        "React": "Have you worked with React hooks? Can you give an example?",
        "SQL": "How do you optimize SQL queries for better performance?",
        "Machine Learning": "Can you explain the difference between supervised and unsupervised learning?",
        "Git": "How do you resolve merge conflicts in Git?",
        "Java":"What is the difference between JDK, JRE, and JVM in Java?",
        "C":"How do you handle buffer overflows in C?",
    }

    for skill in skills:
        if skill in skill_questions:
            questions.append(skill_questions[skill])

    return questions

def generate_activity_questions(activities):
    activity_questions = []

    for activity in activities:
        if "hackathon" in activity.lower():
            activity_questions.append("Can you describe your role in the hackathon and the challenges you faced?")
        elif "workshop" in activity.lower():
            activity_questions.append("What were the key takeaways from the workshop?")
        elif "competition" in activity.lower():
            activity_questions.append("What strategies did you use to succeed in the competition?")
        elif "contest" in activity.lower():
            activity_questions.append("Can you describe an event where you collaborated with a diverse team?")
        elif "event" in activity.lower():
            activity_questions.append("How do you ensure quality work while working under pressure in a contest?")

    return activity_questions

def generate_questions(skills, activities):
    skill_based_questions = generate_questions_skills(skills)
    activity_based_questions = generate_activity_questions(activities)

    return skill_based_questions + activity_based_questions

