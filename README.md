# House Prices Prediction

This repository contains code for predicting house prices, a simple linear regression model is used. The project is to practice using git and docker.

## To run
### Clone the repository
`git clone https://github.com/lailahamdy/advanced-house-prices.git`

`cd advanced-house-prices`

### Install dependencies
`pip install -r requirements.txt`

### Run the script
`python finalscript.py`

## To build and run the image
`docker build -t house-prices-prediction .`

`docker run -it -p 8888:8888 house-prices-pred`
 
## To pull and run the image from Docker Hub
`docker pull lailahamdy/house-prices-prediction:latest`

`docker run lailahamdy/house-prices-prediction:latest`
