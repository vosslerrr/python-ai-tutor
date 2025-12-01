def concept_explainer(topic):
    return (
        f"Explain the following Python concept clearly and simply:\n"
        f"{topic}\n\n"
        "Respond using this format:\n\n"
        
        "### Concept Explanation\n"
        "- Explain in 3–5 beginner-friendly sentences.\n\n"
        
        "### Code Example\n"
        "```python\n"
        "# Provide a clean, readable example related to the concept\n"
        "```\n\n"
        
        "### Practice Exercise\n"
        "- Create a short exercise without giving the answer.\n"
    )


def code_example_generator(topic):
    return (
        f"Provide a clear Python code example for:\n{topic}\n\n"
        "Use this format:\n\n"
        
        "### Code Example\n"
        "```python\n"
        "# Write a complete example\n"
        "```\n\n"
        
        "### Explanation\n"
        "- Explain the example in plain English.\n\n"
        
        "### Mini Exercise\n"
        "- Give the student a follow-up task.\n"
    )


def code_debugger(code):
    return (
        "Find the bugs in this Python code and rewrite it correctly:\n\n"
        f"```python\n{code}\n```\n\n"
        "Respond using this format:\n\n"
        
        "### Error Explanation\n"
        "- Explain what is wrong.\n\n"
        
        "### Corrected Code\n"
        "```python\n"
        "# Fix the code here\n"
        "```\n\n"
        
        "### Why This Fix Works\n"
        "- Explain the correction.\n"
    )


def exercise_creator(topic):
    return (
        f"Create a beginner Python exercise about:\n{topic}\n\n"
        "Use this format:\n\n"
        
        "### Exercise\n"
        "- Write a short, clear problem statement.\n\n"
        
        "### Requirements\n"
        "- List 2–3 requirements.\n\n"
        
        "### Hint\n"
        "- Give a small hint.\n"
    )


def answer_evaluator(question, student_answer, expected):
    return (
        "Evaluate the following student's Python answer.\n\n"
        
        f"### Question\n{question}\n\n"
        
        f"### Student Answer\n{student_answer}\n\n"
        
        f"### Expected Solution\n{expected}\n\n"
        
        "Respond using this format:\n\n"
        
        "### Summary\n"
        "- Briefly summarize correctness.\n\n"
        
        "### What They Did Well\n"
        "- List strengths.\n\n"
        
        "### Mistakes\n"
        "- List incorrect or missing parts.\n\n"
        
        "### How to Improve\n"
        "- Offer guidance.\n\n"
        
        "### Score\n"
        "- Score out of 10.\n\n"
        
        "### Encouragement\n"
        "- Friendly motivation.\n"
    )
