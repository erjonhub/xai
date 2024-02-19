from data_manager import get_data
from openai import OpenAI
from config import chatgpt_key
import pandas as pd

index, questions_df, answers_df, model = get_data()


def answer_question(new_question, n=5, index=index, questions=questions_df, answers=answers_df, model=model):
    # Encode the question to get its embedding, ensuring it's in the correct shape
    question_embedding = model.encode([new_question]).reshape(1, -1)
    # Search the index for the n closest questions
    D, I = index.search(question_embedding, n)
    
    # Get the IDs of the similar questions
    question_ids = questions.iloc[I[0]].index
    
    # Prepare lists to hold the similar questions and their answers
    similar_questions = []
    similar_answers = pd.DataFrame()
    
    # Loop through each similar question ID to get the question text and its answers
    for q_id in question_ids:
        similar_questions.append(questions.loc[q_id].Body)  # Assuming there's a QuestionText column
        q_answers = answers[answers['ParentId'] == q_id]
        similar_answers = pd.concat([similar_answers, q_answers], ignore_index=True)

    
    content = f"I have a question that I need answered based solely on the information contained in the following 5 answers. Please do not use any external knowledge or pre-existing information you might have. Just use the details provided in these answers to formulate the best possible response. If the answer is not in the provided information, answer that you dont have enough information to provide an answer. Be coincise.\n\n\n"


    for i, answer in enumerate(similar_answers['Body']): # Assumes a list of answers
        content += f"Start of Answer {i+1}: {answer}\n End of Answer {i+1}\n\n\n"      
    content += f"Question: {new_question}"
    client = OpenAI(api_key=chatgpt_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
        temperature=0.0,
        max_tokens=150,
    )

    answer_content = chat_completion.choices[0].message.content

    return new_question, similar_questions, similar_answers, answer_content