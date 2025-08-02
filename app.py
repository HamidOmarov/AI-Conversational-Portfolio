import gradio as gr
import os
import re

def load_knowledge_files():
    knowledge_base = ""
    for filename in os.listdir('.'):
        if filename.endswith(".txt"):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    knowledge_base += f.read() + "\n\n"
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return knowledge_base

knowledge = load_knowledge_files()
knowledge_chunks = [chunk.strip() for chunk in knowledge.split('\n\n') if chunk.strip()]

def hybrid_search(question):
    question_lower = question.lower()
    bonus_scores = {
        'barda': 100, 'ağdam': 100, 'karvansaray': 100, 'zafar': 100, 'yengicə': 100,
        'chenot': 90, 'sharadil': 90, 'chinar': 90, 'gashalti': 90,
        'pmdp': 20, 'socar': 20, 'mkt-ik': 20
    }
    stop_words = {'a', 'an', 'the', 'is', 'in', 'on', 'of', 'for', 'about', 'to', 'me', 'my', 'his', 'him', 'tell', 'more', 'and', 'was', 'did'}
    words_from_question = re.findall(r'\b\w+\b', question_lower)
    question_keywords = [word for word in words_from_question if word not in stop_words and len(word) > 1]

    if not question_keywords: return []
    chunk_scores = {}
    for chunk in knowledge_chunks:
        current_score = 0
        chunk_lower = chunk.lower()
        for keyword in question_keywords:
            if keyword in chunk_lower:
                current_score += 2
        for keyword, score in bonus_scores.items():
            if keyword in chunk_lower:
                current_score += score
        if current_score > 0: chunk_scores[chunk] = current_score

    if not chunk_scores: return []
    sorted_matches = sorted(chunk_scores.items(), key=lambda item: item[1], reverse=True)
    return [match[0] for match in sorted_matches[:3]]

def answer_question(question):
    matches = hybrid_search(question)
    if matches:
        response = "Based on my knowledge base, here is the most relevant information I found:\n\n"
        for i, match in enumerate(matches, 1):
            response += f"**Result {i}:**\n---\n{match}\n\n"
        return response
    return "I couldn't find a specific answer in my knowledge base. Please rephrase your question."

iface = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(lines=3, placeholder="Ask about Hamid's skills, projects, or experience..."),
    outputs=gr.Markdown(label="Assistant's Response"),
    title="Hamid Omarov's Interactive AI Assistant",
    description="This is an AI trained on Hamid's professional documents.",
    allow_flagging="never"
)
iface.launch()