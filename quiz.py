import random
from datasets import load_dataset
import inquirer

# List of available categories
categories = [
    "high_school_european_history",
    "business_ethics",
    "clinical_knowledge",
    "medical_genetics",
    "high_school_us_history",
    "high_school_physics",
    "high_school_world_history",
    "virology",
    "high_school_microeconomics",
    "econometrics",
    "college_computer_science",
    "high_school_biology",
    "abstract_algebra",
    "professional_accounting",
    "philosophy",
    "professional_medicine",
    "nutrition",
    "global_facts",
    "machine_learning",
    "security_studies",
    "public_relations",
    "professional_psychology",
    "prehistory",
    "anatomy",
    "human_sexuality",
    "college_medicine",
    "high_school_government_and_politics",
    "college_chemistry",
    "logical_fallacies",
    "high_school_geography",
    "elementary_mathematics",
    "human_aging",
    "college_mathematics",
    "high_school_psychology",
    "formal_logic",
    "high_school_statistics",
    "international_law",
    "high_school_mathematics",
    "high_school_computer_science",
    "conceptual_physics",
    "miscellaneous",
    "high_school_chemistry",
    "marketing",
    "professional_law",
    "management",
    "college_physics",
    "jurisprudence",
    "world_religions",
    "sociology",
    "us_foreign_policy",
    "high_school_macroeconomics",
    "computer_security",
    "moral_scenarios",
    "moral_disputes",
    "electrical_engineering",
    "astronomy",
    "college_biology",
]

# Prompt the user to select a category
category_prompt = [
    inquirer.List(
        "category",
        message="Select a category:",
        choices=categories,
    )
]
selected_category = inquirer.prompt(category_prompt)["category"]

# Load the MMLU dataset with the selected category
dataset = load_dataset("lukaemon/mmlu", selected_category, trust_remote_code=True)

# Get the test split of the dataset
test_data = dataset["test"]

# Function to prompt the user with a random question
def ask_question():
    # Select a random question from the dataset
    question_index = random.randint(0, len(test_data) - 1)
    question = test_data[question_index]

    # Extract the relevant information from the question
    question_text = question["input"]
    choices = [question["A"], question["B"], question["C"], question["D"]]
    correct_answer = ord(question["target"]) - ord("A")

    # Print the question text
    print("\nQuestion:")
    print(question_text)

    # Create the inquirer prompt for answer choices
    prompt = [
        inquirer.List(
            "answer",
            message="Select your answer:",
            choices=choices,
        )
    ]

    # Prompt the user with the answer choices and get their answer
    user_answer_index = choices.index(inquirer.prompt(prompt)["answer"])

    # Check if the user's answer is correct
    if user_answer_index == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer is: {choices[correct_answer]}")
        return 0

# Run the quiz
num_questions = 20
score = 0

for i in range(num_questions):
    print(f"\nQuestion {i+1} of {num_questions}")
    score += ask_question()

# Calculate the grade
grade = (score / num_questions) * 100

print(f"\nQuiz completed!")
print(f"Your score: {score} out of {num_questions}")
print(f"Grade: {grade:.2f}%")