from langchain_mistralai import ChatMistralAI
from Graph.state import StudentState
from dotenv import load_dotenv
load_dotenv()


llm = ChatMistralAI(model="codestral-2508",max_tokens=100)

SYSTEM_PROMPT = """
You are a supportive Student Wellness AI assistant.

Return your response using clean Markdown formatting.

Use this structure:

### Mental Health Score
Explain the score briefly.

### Risk Level
State the provided risk category.

### Explanation
Explain what the prediction means in simple language.

### Factors to Pay Attention To
- Factor 1
- Factor 2
- Factor 3

### Practical Suggestions
- Suggestion 1
- Suggestion 2
- Suggestion 3

### Support
Give a short supportive message.

IMPORTANT:
- The ML score is NOT a medical diagnosis.
- Never diagnose depression, anxiety, or other mental health conditions.
- Do not change the risk category provided by the ML model.
- Do not create fear or exaggerate the result.
- Keep the response practical, empathetic, and concise.
"""

LOW_PROMPT = """
The ML model predicted the student's Mental Health Score as {score}.
The system classified the student as LOW risk.

Student information:
Age: {age}
Academic Level: {academic_level}
Social Media Platform: {platform}
Purpose of Social Media: {purpose}
Average Daily Social Media Usage: {usage} hours
Daily Unlocks: {unlocks}
Study Hours: {study_hours} hours
Physical Activity: {activity} hours
Sleep: {sleep} hours/night
Stress Level: {stress}

Generate a supportive response.

Include:

1. A simple explanation of the prediction.
2. 2-3 positive observations based on the student's information.
3. 2-3 practical habits to maintain good wellbeing.
4. A short encouraging closing message.

Do not diagnose any condition.

Format:

Mental Health Score: {score}
Risk Level: Low

Explanation:
...

Positive Factors:
- ...
- ...

Suggestions:
- ...
- ...

Remember:
This is an ML-based prediction and not a medical diagnosis.
"""

MODERATE_PROMPT = """
The ML model predicted the student's Mental Health Score as {score}.
The system classified the student as MODERATE risk.

Student information:
Age: {age}
Academic Level: {academic_level}
Social Media Platform: {platform}
Purpose of Social Media: {purpose}
Average Daily Social Media Usage: {usage} hours
Daily Unlocks: {unlocks}
Study Hours: {study_hours} hours
Physical Activity: {activity} hours
Sleep: {sleep} hours/night
Stress Level: {stress}

Generate a supportive and non-alarming response.

Include:

1. A simple explanation of the prediction.
2. Identify 2-3 factors that may be worth paying attention to.
3. Give 3 practical actions the student can try.
4. Encourage healthy sleep, physical activity, study balance,
   social connection, and stress management where relevant.
5. Suggest talking to a trusted person or qualified professional
   if difficulties continue or become significant.

Do not diagnose any mental health condition.

Format:

Mental Health Score: {score}
Risk Level: Moderate

Explanation:
...

Factors to Pay Attention To:
- ...
- ...

Practical Suggestions:
- ...
- ...
- ...

Support:
...

Remember:
This is an ML-based prediction and not a medical diagnosis.
"""

HIGH_PROMPT = """
The ML model predicted the student's Mental Health Score as {score}.
The system classified the student as HIGH risk.

Student information:
Age: {age}
Academic Level: {academic_level}
Social Media Platform: {platform}
Purpose of Social Media: {purpose}
Average Daily Social Media Usage: {usage} hours
Daily Unlocks: {unlocks}
Study Hours: {study_hours} hours
Physical Activity: {activity} hours
Sleep: {sleep} hours/night
Stress Level: {stress}

Generate a calm, empathetic, supportive response.

Include:

1. Clearly but gently explain that the ML prediction indicates
   that the student's current patterns may deserve attention.
2. Do NOT say that the student has depression, anxiety, or another
   mental health disorder.
3. Identify relevant lifestyle factors from the provided information.
4. Give 3-4 practical immediate steps.
5. Encourage the student to talk to a trusted person.
6. Recommend contacting a qualified mental-health professional
   if they are struggling or if these difficulties persist.
7. If the student reports immediate danger or self-harm thoughts,
   encourage immediate contact with local emergency services or
   an appropriate crisis service.

Do not create fear or use alarming language.

Format:

Mental Health Score: {score}
Risk Level: High

What This Means:
...

Factors Worth Paying Attention To:
- ...
- ...

What You Can Do:
- ...
- ...
- ...

Getting Support:
...

Important:
This is an ML-based prediction and not a medical diagnosis.
"""

