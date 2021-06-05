# Running Crypto Flask App through Docker & Kuberetes and AWS
<img width="1218" alt="Screen Shot 2021-06-04 at 4 55 29 PM" src="https://user-images.githubusercontent.com/78613742/120873336-9013ad00-c556-11eb-99d9-e5d47e0f5933.png">


### What the project does and how it was made?
This project was built using Python3 to develop Real-Time Candlestick Charts and a Crypto Trading Bot using Binance API and Websockets via Flask based web application. Once the Flask App was developed:
* I created a customized Docker container of the flask application
* Pushed the Docker image to Amazon ECR and Elastic Beanstalk
* Created an AWS ECS and Cluster Task
* Pull image down and run it on a cloud platform cloud shell: AWS Cloud9
* Deployed the application to managed Kubernetes cluster via AWS EKS

### Prerequisites:
* Python3
* [Binance API Key](https://www.binance.com/en) (signup for free)
* [AWS Account](https://aws.amazon.com/free/)
* [Docker](https://docs.docker.com/)



### To build this project perform the following steps:

Clone the GitHub repository
Install the library requirements from the requirements.txt file
Run the command python app.py on the terminal. Make sure that you are executing this command from the directory of the file.
To view the live site visit: 

### Setup to run the project


