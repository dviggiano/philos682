# Senior Honors Thesis — Supplementary Materials

> **Topic**: Creative Idea Production By Large Language Models: A Philosophical Analysis of the “What” and the “How”

Code and results for experiments conducted for senior honors thesis. Exploring functional exhibitions of creativity in large language models.

## Getting started

First ensure you have [Python 3.12 installed](https://www.python.org/downloads/). Then open up a terminal window.

Clone this repository into a local directory (folder), and navigate to it:

```
git clone https://github.com/dviggiano/philos682.git
cd philos682
```

Create a `.env` file to store API keys from OpenAI and Google:

```
touch .env
```

Open the file with your preferred text editor and include the following:

```
OPENAI_API_KEY=insert your API key here (generate at https://platform.openai.com/docs/overview)
GOOGLE_API_KEY=insert your API key here (generate at https://ai.google.dev/)
```

> You can open the file from the command line using `notepad .env` on Windows or `nano .env` on macOS.

Finally, set up your Python environment (this will allow you to execute code with functions defined by OpenAI and Google to query their LLMs):

### Windows

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### macOS/Linux

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You can now execute the included code to run the experiments on your own.

For example, you can run the combinatorial creativity experiments with `python3 code/c-creativity.py` on macOS or `python code/c-creativity.py` on Windows, so long as you are still in the same directory as the repository and you have activated the virtual environment with `source venv/bin/activate` on macOS or `venv\Scripts\activate` on Windows.