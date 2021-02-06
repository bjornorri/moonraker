# Community Questions

## Introduction

This is a demo ML classifier that runs in a Docker container and exposes an API enpoint for predictions.

## Getting Started

1. Clone the repository.

    git clone https://github.com/bjornorri/moonraker.git

2. Navigate to the project directory.

    cd moonraker

3. Build the docker container image.

    docker build -t moonraker .

4. Start the docker container .

    docker run moonraker

5. Locate the Docker container's IP address.

    docker ps # Get container id
    docker inspect CONTAINER_ID # Get IP address

6. Access the prediction API at `http://IP_ADDRESS/predict?VisitsLastYear=123&QuestionTextLength=456`. Example:

    curl "http://172.17.0.3/predict?VisitsLastYear=123&QuestionTextLength=456"

## Request and response format

Provide the following parameters as query parameters. These are used as input features for the model.

| Name               |    Type |
| ------------------ | ------: |
| VisitsLastYear     | integer |
| QuestionTextLength | integer |

Example response:

    {"prediction":false}
