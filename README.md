# Community Questions

## Introduction

This is a demo ML classifier that runs in a Docker container and exposes an API enpoint for predictions.

## API in Docker

### Getting Started

1. Clone the repository.

```bash
git clone https://github.com/bjornorri/moonraker.git
```

2. Navigate to the project directory.

```bash
cd moonraker
```

3. Build the docker container image.

```bash
docker build -t moonraker .
```

4. Start the docker container .

```bash
docker run moonraker
```

5. Locate the Docker container's IP address.

```bash
docker ps # Get container id
docker inspect CONTAINER_ID # Get IP address
```

6. Access the prediction API at `http://IP_ADDRESS/predict?VisitsLastYear=123&QuestionTextLength=456`. Example:

```bash
curl "http://172.17.0.3/predict?VisitsLastYear=123&QuestionTextLength=456"
```

### Request and response format

Provide the following parameters as query parameters. These are used as input features for the model.

| Name               |    Type |
| ------------------ | ------: |
| VisitsLastYear     | integer |
| QuestionTextLength | integer |

Example response:

```json
{ "prediction": false }
```

## Jupyter Notebook

To see how the model was created, view the provided Jupyter notebook.

### Getting Started

1. Clone the repository.

```bash
git clone https://github.com/bjornorri/moonraker.git
```

2. Navigate to the project directory.

```bash
cd moonraker
```

3. (Optional) Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

5. Run the Jupyter server. This should launch your browser.

```bash
jupyter notebook
```

6. Open `community_questions.ipynb`.

## Advanced model

If I create a more advanced model (optional task), I will do it on another branch in this repository.
