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

To view the live site visit: [http://cryptobinancedemo.us-west-1.elasticbeanstalk.com/](http://cryptobinancedemo.us-west-1.elasticbeanstalk.com/)

### Setup to run the project
1. Flask App

Clone the GitHub repository.
Install the library requirements from the `requirements.txt` file. Change your `config.py` file with the appropriate API_KEY and API_SECRET.  Run the command python 
```bash
python3 app.py
``` 
or 
```python
flask run
``` 
on the terminal. Make sure that you are executing this command from the directory of the file.

2. Docker

#### Dockerfile
Create a Dockerfile, which is a list of commands that the Docker client calls while creating an image. It's a simple way to automate the image creation process. View sample Dockerfile [here](https://github.com/Darenson/Capstone_BinanceFlask_Docker_Kubernetes/blob/master/Dockerfile)

Now that we have our Dockerfile, we can build our image. The docker build command does the heavy-lifting of creating a Docker image from a Dockerfile.
The docker build command is quite simple - it takes an optional tag name with -t and a location of the directory containing the Dockerfile.
<img width="1165" alt="Screen Shot 2021-06-04 at 5 54 18 PM" src="https://user-images.githubusercontent.com/78613742/120874956-f8b25800-c55d-11eb-8024-bcd288e1f958.png">

The last step in this section is to run the image and see if it actually works (replacing my username with yours).

<img width="1159" alt="Screen Shot 2021-06-04 at 6 05 07 PM" src="https://user-images.githubusercontent.com/78613742/120875198-8478b400-c55f-11eb-91e1-114bef3e6225.png">

The command we just ran used port 5000 for the server inside the container and exposed this externally on port 8888. Head over to the URL with port 8888, where your app should be live.

3. Elastic Beanstalk

Now we need to upload our application code. But since our application is packaged in a Docker container, we just need to tell EB about our container. Open the 
`Dockerrun.aws.json` located [here](https://github.com/Darenson/Capstone_BinanceFlask_Docker_Kubernetes/blob/master/Dockerrun.aws.json) and edit the Name of the image to your image's name. When you are done, click on the radio button for "Upload your Code", choose this file, and click on "Upload".
Now click on "Create environment". The final screen that you see will have a few spinners indicating that your environment is being set up. 
(Note: the warning sign doesn't seem to impact the app from running)


<img width="1045" alt="Screen Shot 2021-06-04 at 6 19 23 PM" src="https://user-images.githubusercontent.com/78613742/120875603-83e11d00-c561-11eb-9609-63987f19b175.png">




4. ECR

### Login to ECR
`aws ecr get-login-password --region REGIONHERE!!!! | docker login --username AWS --password-stdin ACCOUNTIDHERE!!!!.dkr.ecr.REGIONHERE!!!.amazonaws.com`

<img width="1166" alt="Screen Shot 2021-06-04 at 6 26 18 PM" src="https://user-images.githubusercontent.com/78613742/120875781-7710f900-c562-11eb-8582-fca5ca7df692.png">


### Tag the version
`docker tag test:latest YOURACCOUNT.dkr.ecr.YOURREGION-1.amazonaws.com/YOURREPO:YOURTAG`

<img width="1262" alt="Screen Shot 2021-06-04 at 6 31 14 PM" src="https://user-images.githubusercontent.com/78613742/120876024-5bf2b900-c563-11eb-8dd6-d394a971f32c.png">


### Upload
`docker push YOURACCOUNT.dkr.ecr.YOURREGION.amazonaws.com/YOURREPO:YOURTAG`

<img width="1163" alt="Screen Shot 2021-06-04 at 6 23 32 PM" src="https://user-images.githubusercontent.com/78613742/120875729-33b68a80-c562-11eb-8fa5-eac761105047.png">


6. ECS
7. EKS


