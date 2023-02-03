# Primer Bot

Primer Bot is a GPT-powered question-and-answer bot that answers questions about [Primer Interface Guidelines](https://github.com/primer/design). The bot works by first creating an embeddings index of the markdown contents of the primer/design repository. Then, when a question is submitted, that index is queried for text chunks that have a high similarity to the user's question. Those text chunks are used to populate a GPT prompt for answer creation and summarization.

This bot was inspired by a [blog post written by Pete Hunt at Dagster](https://dagster.io/blog/chatgpt-langchain).

## Running locally

Install requirements:
```
pip install -r requirements.tx
```

Set your OpenAI API Key:
```
export OPEN_API_KEY=sk-.....
```

Run the application server:
```
waitress-serve --host 0.0.0.0 app:app
```

## Deployment
Deploy this on any Docker platform, such as [Aptible](https://www.aptible.com/).

## OpenAI API key
The bot requires access to OpenAI APIs for generating text embeddings and answer summarization. After you [generate an OpenAI API key](https://beta.openai.com/account/api-keys), configure this app to use it by storing the key in the `OPEN_API_KEY` environment variable.

## Indexing a different repository
You can optionally target a different public repository by providing new values for `OWNER` and `REPO` environment variables.
