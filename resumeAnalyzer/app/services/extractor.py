# app/services/extractor.py
import spacy

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

def extract_details(text):
    skills = []
    activities = []
    
    # Predefined list of technical skills
    predefined_skills = [
        'Python', 'Java', 'C', 'C#', 'MERN', 'SQL', 'React', 'Node.js', 'HTML', 'CSS', 'JavaScript', 'Git', 'Django', 'Flask', 'Machine Learning', 'TensorFlow', 'PyTorch'
    ]
    
    # Extract skills by matching predefined technical skills
    doc = nlp(text)
    for token in doc:
        if token.text in predefined_skills and token.text not in skills:
            skills.append(token.text)

    # Extract activities from phrases involving events, hackathons, workshops, etc.
    activity_keywords = ['participated', 'winner', 'selected', 'finalist', 'event', 'workshop', 'hackathon', 'competition', 'conference', 'course']
    for sent in doc.sents:
        if any(keyword in sent.text.lower() for keyword in activity_keywords):
            activities.append(sent.text.strip())

    # Return extracted skills and activities
    return {
        'Skills': skills,
        'Activities': activities
    }
