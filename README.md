## Chainlit demo

The goal is to test a prompt creation workflow using [Chainlit](https://github.com/Chainlit/chainlit).

The demo consist of a note taking application aiming to categorize using openai api.

### Setup

- clone the repository
- install dependencies:

```shell
pip install -r requirements.txt
```

- start the flask application:

```shell
python app.py
```

- start chainlit:

```shell
chainlit run chainlit.py -w
```

### How to use?

You can use chainlit to dynamically build the proper query.
The latest commit contains a working solution
The previous commit contains the base prompt that will be your starting point.
