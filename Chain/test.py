student_answer = """
   Python is a high-level programming language.
   It is widely used in web development, data science,
   and artificial intelligence.
"""

### Step 1
def clean_answer(answer):
    return answer.strip()

cleaned_answer=clean_answer(student_answer)
#print(clean_answer(student_answer))

#step 2:Count the words
def count_words(answer):
    return len(answer.split())
word_count=count_words(cleaned_answer)

#Step 3:Generate the feedback
def generate_feedback(answer,word_count):
    return f"""
    The answer contains {word_count} words.
    The student correctly explained python and mentioned some important applicatin areas.    
        """
        
feedback=generate_feedback(cleaned_answer,word_count)   
#Step 4:Format the feedback
def format_feedback(feedback):
    return feedback.strip().upper()

