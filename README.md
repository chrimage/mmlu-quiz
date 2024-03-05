# MMLU Quiz

Welcome to the MMLU Quiz, a Python application that challenges you to test your knowledge and intelligence against state-of-the-art language models. This quiz is based on the Massive Multitask Language Understanding (MMLU) dataset, which consists of multiple-choice questions covering a wide range of categories, including history, science, mathematics, and more.

The MMLU dataset has become a benchmark for evaluating the performance and capabilities of advanced language models. One of the most prominent models, GPT-4, developed by OpenAI, has achieved an impressive score of 86.5% on this test. Now, it's your turn to see how you measure up!

With the MMLU Quiz, you can choose from a variety of categories and answer a series of randomly selected questions. The quiz provides immediate feedback on the correctness of your answers and presents you with a final score and grade at the end.

Whether you're a trivia enthusiast, a curious learner, or someone interested in comparing your knowledge to that of cutting-edge AI models, the MMLU Quiz offers an engaging and challenging experience. Put your skills to the test and see how you stack up against the likes of GPT-4!

## Features

- Choose from a variety of categories to quiz yourself on.
- Answer 20 randomly selected questions from the chosen category.
- Receive immediate feedback on the correctness of your answers.
- Get a final score and grade at the end of the quiz.

## Requirements

- Python 3.6 or higher
- `datasets` library (install via `pip install datasets`)
- `inquirer` library (install via `pip install inquirer`)

## Usage

1. Clone the repository:
```
git clone https://github.com/chrimage/mmlu-quiz.git
```

2. Navigate to the project directory:
```
cd mmlu-quiz
```

3. Install the required libraries:
```
pip install -r requirements.txt
```

4. Run the quiz script:
```
python quiz.py
```

5. Select a category from the provided list using the arrow keys and press Enter.

6. Answer each question by selecting one of the multiple-choice options using the arrow keys and pressing Enter.

7. After answering all 20 questions, you will see your final score and grade.

## Dataset

The MMLU Quiz uses the Massive Multitask Language Understanding (MMLU) dataset, which consists of multiple-choice questions covering a wide range of domains. The dataset is loaded using the Hugging Face `datasets` library.

For more information about the MMLU dataset, please refer to the original paper:

- Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, Jacob Steinhardt. "Measuring Massive Multitask Language Understanding." Proceedings of the International Conference on Learning Representations (ICLR), 2021. [[Paper]](https://arxiv.org/abs/2009.03300)

## Contributing

Contributions to the MMLU Quiz project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The MMLU Quiz project was inspired by the Massive Multitask Language Understanding research.
- Thanks to the creators of the MMLU dataset for making it publicly available.