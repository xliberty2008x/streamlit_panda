# Prompt-driven Analysis with PandasAI and OpenAI's GPT-3

This project is a web application built with Streamlit that allows you to perform prompt-driven analysis on CSV data using PandasAI and OpenAI's GPT-3.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- [Streamlit](https://streamlit.io/) installed: You can install it using `pip install streamlit`
- [Pandas](https://pandas.pydata.org/) installed: You can install it using `pip install pandas`
- [PandasAI](https://pypi.org/project/pandasai/) installed: You can install it using `pip install pandasai`
- [dotenv](https://pypi.org/project/python-dotenv/) installed: You can install it using `pip install python-dotenv`
- An OpenAI API key. You can sign up for one on the [OpenAI website](https://beta.openai.com/signup/).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-project
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Set your OpenAI API key as an environment variable by creating a `.env` file in the project directory and adding the following line:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

7. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

The app should be accessible in your web browser at the specified URL.

## Usage

1. Upload a CSV file for analysis.
2. Enter a prompt in the provided text area.
3. Click the "Generate" button to analyze the data based on your prompt.
4. View the generated response.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [PandasAI](https://pypi.org/project/pandasai/)
- [OpenAI](https://openai.com/)

