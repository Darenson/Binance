# Running Crypto Flask App through Docker & Kuberetes and AWS
<img width="1218" alt="Screen Shot 2021-06-04 at 4 55 29 PM" src="https://user-images.githubusercontent.com/78613742/120873336-9013ad00-c556-11eb-99d9-e5d47e0f5933.png">


### What the project does and how it was made?
This project has been built using Python3 to develop Real-Time Candlestick Charts and a Crypto Trading Bot using Binance API and Websockets via Flask based web application. Once the Flask App was developed:
* Created a customized Docker container from the current version of Python that deploys a python application
* Pushed Docker image to Amazon ECR 
* Created ECS Cluster Task and Service
* Pull image down and run it on a cloud platform cloud shell: Google Cloud Shell or AWS
Cloud9.
* Deploy an application to managed Kubernetes cluster via AWS EKS




To build this project perform the following steps:

Clone the GitHub repository
Install the library requirements from the requirements.txt file
Run the command python app.py on the terminal. Make sure that you are executing this command from the directory of the file.
To view the live site visit 

* Create a customized Docker container from the current version of Python that deploys a
python application
* Push image to DockerHub or Amazon ECR or Google Container Registry
* Pull image down and run it on a cloud platform cloud shell: Google Cloud Shell or AWS
Cloud9.
* Deploy an application to managed Kubernetes cluster
