
# Farmer's Friend

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Deployment](#deployment)
- [Usage](#usage)
- [Authors](#authors)

<br>

## Introduction


This project is the backend implementation of the Farmer's Friend application. The application is a web application that allows farmers to keep track of their crops and livestock. 


## Getting Started

The Code is written in Python 3.10.0 and deployed on the AWS cloud. The serverless framework is used to deploy the application. The application is deployed on AWS Lambda. The database used here is mySQL and mongoDB. 


### Prerequisites

- Python 3.10.0
- Serverless Framework ( AWS Lambda )
- mySQL
- mongoDB
- Code-Build
- API Gateway
- Docker



### Installation
 
1. Clone the repo
   ```sh
   git clone https://github.com/nitish-pandey/Project-BackEnd-Public.git
    ```

2. Create a virtual environment
   ```sh
   python3 -m venv venv
   ```

3. Activate the virtual environment
   ```sh
    source venv/bin/activate
    ```
4. Install the required packages
    ```sh
     pip install -r requirements.txt
     ```

5. SET Up Environment Variables in the .env file
    ```sh
    # Add the following variables to the .env file
    export DB_HOST = <DB_HOST>
    export DB_USER = <DB_USER>
    export DB_PASSWORD = <DB_PASSWORD>
    export DB_NAME = <DB_NAME>
    ... etc.    
    ```
6. Run the application
    ```sh
    python3 app.py
    ```
7. Run the Python app
    ```sh
    python app.py
    ```





### Deployment

The application is deployed on AWS Lambda using the serverless framework. The serverless framework is used to deploy the application. The application is deployed on AWS Lambda. The database used here is mySQL and mongoDB.

The Buildspec file contains the commands to deploy the application on AWS Lambda. The buildspec file is used by the AWS CodeBuild to deploy the application on AWS Lambda. 


# Docker

The application is also deployed on Docker. The [Dockerfile](dockerfile) contains the commands to deploy the application on Docker. 

The [compose file](compose.yml) contains the commands to deploy the application on Docker. The compose file is used by the Docker to deploy the application on Docker.




## Usage

LocalHost API endpoints link: https://127.0.0.1:5000/

Paths are defined in the [paths.py](paths.py) file.



## Authors

Nitish Pandey <br>
[Instagram](https://www.instagram.com/nitishpandey___/) <br>
[WebSite](https://nitishpandey.com.np/)

