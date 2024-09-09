# GraphRAG with Hugging Face

This repository enables you to use GraphRAG with any models from Hugging Face, as well as your own models.

## Installation and Setup

To set up this repository and utilize GraphRAG with local models from Ollama, follow these steps:

### 1. Create and Activate a New Conda Environment

Ensure that Python version 3.10 is being used to prevent any compatibility issues.

```bash
conda create -n graphrag-ollama-local python=3.10
conda activate graphrag-ollama-local
```

### 2. Install Ollama

Install Ollama by visiting their official website or by running the following commands:

```bash
curl -fsSL https://ollama.com/install.sh | sh  # Ollama for Linux
pip install ollama
```

### 3. Download Required Models via Ollama

Select from available models such as Mistral, Gemma2, or Qwen2 for the LLM, and any embedding model provided by Ollama:

```bash
ollama pull llama3  # LLM model
ollama pull nomic-embed-text  # Embedding model
```

### 4. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/TheAiSingularity/graphrag-local-ollama.git
```

### 5. Install the GraphRAG Package

This step is crucial. Ensure the package is installed with the following command:

```bash
pip install -e .
```

### 6. Create the Input Directory

Create a directory where the experiment data and results will be stored:

```bash
mkdir -p ./ragtest/input
```

### 7. Copy Sample Data to the Input Directory

Copy the sample data from the `input/` folder to `./ragtest/input`. You can also add your own `.txt` files here:

```bash
cp input/* ./ragtest/input
```

### 8. Initialize the `./ragtest` Directory

Initialize the `./ragtest` directory to generate the required files:

```bash
python -m graphrag.index --init --root ./ragtest
```

### 9. Move the `settings.yaml` File

Copy the pre-configured `settings.yaml` file to the `./ragtest` directory:

```bash
cp settings.yaml ./ragtest
```

You can modify this file to experiment with different models. For LLM models, use options like `llama3`, `mistral`, or `phi3`. For embedding models, choose options like `mxbai-embed-large` or `nomic-embed-text`. The full list of models provided by Ollama is available on their website, which can be deployed locally. 

To add your own custom model, refer to the guide [`Testing a New Model`](#testing-a-new-model).

Default API base URLs:

- LLM: `http://localhost:11434/v1`
- Embeddings: `http://localhost:11434/api`

### 10. Run Indexing to Create a Graph

Run the indexing process to generate a graph:

```bash
python -m graphrag.index --root ./ragtest
```

### 11. Run a Query (Global Method Only)

Execute a query using the global method:

```bash
python -m graphrag.query --root ./ragtest --method global "What are some common applications and challenges of using MRI in medical imaging?"
```

## Testing a New Model

To test a new model, follow these steps:

1. Change the model name.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Convert the Hugging Face model to GGUF format:

```bash
python convert_hf_to_gguf.py -h
```

4. Use the following command to convert the custom model:

```bash
python3 llama.cpp/convert_hf_to_gguf.py custom_model --outfile custom_model.gguf --outtype q8_0
```

### Importing from GGUF

Ollama supports importing GGUF models in the `Modelfile`:

1. Create a file named `Modelfile`, with a `FROM` instruction pointing to the local file path of the model you want to import:

```bash
FROM ./custom_model.gguf
```

2. Create the model in Ollama:

```bash
ollama create custom_model -f Modelfile
```

3. Run the model:

```bash
ollama run custom_model 
```
You can also just use `ollama list` to check if the model is correctly added.

4. Update `settings.yaml` to include `custom_model` and copy it to the `./ragtest` directory:

```bash
cp settings.yaml ./ragtest
```

5. Run the indexing process:

```bash
python -m graphrag.index --root ./ragtest
```


Note : Some custom models will make your graphrag crash if they do not follow the openai prompt style (change in `settings.yaml`), embedding (change in `settings.yaml`), or output a bad JSON format. So make sure to make the appropriate changes to adapt the graph rag to your own model.


## Citations

- Original GraphRAG repository by Microsoft: [GraphRAG](https://github.com/microsoft/graphrag)
- Ollama: [Ollama](https://ollama.com/)

Inspired by : [graph-rag-ollama](https://github.com/TheAiSingularity/graphrag-local-ollama)