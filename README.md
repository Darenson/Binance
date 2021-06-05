# Running Crypto Flask App through Docker, Kubernetes and AWS
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
To view the live site visit: [http://cryptobinancedemo.us-west-1.elasticbeanstalk.com/](http://cryptobinancedemo.us-west-1.elasticbeanstalk.com/)

### Setup to run the project
1. Flask App
2. Docker

#### Dockerfile
Create a Dockerfile, which is a list of commands that the Docker client calls while creating an image. It's a simple way to automate the image creation process. View sample Dockerfile [here](https://github.com/Darenson/Capstone_BinanceFlask_Docker_Kubernetes/blob/master/Dockerfile)

Now that we have our Dockerfile, we can build our image. The docker build command does the heavy-lifting of creating a Docker image from a Dockerfile.
The docker build command is quite simple - it takes an optional tag name with -t and a location of the directory containing the Dockerfile.
<img width="1165" alt="Screen Shot 2021-06-04 at 5 54 18 PM" src="https://user-images.githubusercontent.com/78613742/120874956-f8b25800-c55d-11eb-8024-bcd288e1f958.png">

The last step in this section is to run the image and see if it actually works (replacing my username with yours).
![Uploading Screen Shot 2021-06-04 at 6.05.07 PM.png…]()


3. Elastic Beanstalk
4. ECR
5. ECS
6. EKS


