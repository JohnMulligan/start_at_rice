# Start@Rice 2022 Data Viz Class

This repository contains the materials that will be used for the October 9 data visualization course in the Start@Rice program.

We will be using the example of COVID-19 excess mortality data to discuss the uses (and abuses) of exploratory data analysis, and to quickly build up a simple app that can be used to visually navigate the CDC's relevant, curated, public datasets in this area.

All reference materials (inluding the PowerPoint) are available on the Start@Rice canvas page: https://canvas.rice.edu/courses/44851/modules

Some reference materials are available in the reference_materials subfolder of this repository.

You *don't* need to know how to "code" to take this course, and you *won't* "learn to code" in one day!

What you will be introduced to:

1. some basic programming moves that
	1. can be adapted to a number of use-cases and
	1. will familiarize you to the process publishing interactive data viz applications.
1. why people publish these sorts of apps
1. methods for critically thinking about
	1. interactivity
	1. data visualization

## Software and documentation

In order to actively participate in this lesson, you have to install some basic software

### Required software installations

These are all free and you can install in class or beforehand.

* Text Editor (pick one)
	* BBEdit: https://www.barebones.com/products/bbedit/
	* Visual Studio: https://visualstudio.microsoft.com/downloads/
* Git: https://git-scm.com/downloads
	* For Windows users, git bash will make all of this much, much easier!
* Python
	* Pip: https://pip.pypa.io/en/stable/
	* Virtual Environments: https://docs.python.org/3/tutorial/venv.html
* Plotly:
	* Dash: https://dash.plotly.com/installation

### Cloud Deployment

I have set up 10 AWS deployment pipelines and micro apps for you. Credentials will be handed out in class.

* AWS deployment documentation, for your reference
	* Deploy directly with ElasticBeanstalk: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
	* Deploy via a repository using CodeCommit: https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-simple-codecommit.html

I deploy my apps to Heroku as I find it to be more straightforward, but they are deprecating their free tier, and so I will not be using this in the class. You can see how this sort of code looks in my other repositories.

* Containerized R deployment to Heroku: https://github.com/JohnMulligan/covid_dashR/
* Simple Python deployment to Heroku: https://github.com/JohnMulligan/covid_dashPy

* Heroku deployment documentation
	* CLI installation: https://devcenter.heroku.com/articles/git
	* Git deployment https://devcenter.heroku.com/articles/git
	
--------------------

# The app

# Adaptation of CDC's All-Cause Excess Mortality Dashboard

This repo uses CDC data on excess mortality (generated to estimate the impacts of COVID-19) as an exercise in quickly building and deploying interactive data visualizations to the web, because these are the cornerstone of exploratory data analysis.

csv from: https://data.cdc.gov/api/views/xkkf-xrst/rows.csv?accessType=DOWNLOAD&bom=true&format=true%20target=

## Core technologies

The following frameworks and services are used in what is outlined below:

* Free, curated data from the CDC
* Python
* Pandas
* Plotly (Dash)
* AWS CodeCommit --> CodeDeploy --> ElasticBeanstalk

## Setting up your environment (Python)

In order to run through this exercise, you will need Python 3 installed, and specific packages for it. It's best to set up a virtual environment so that you can record the specifics of your installation, in order for a web server to rebuild that later on.

1. Open a terminal

*navigate to this folder*, and initialize a Python virtual environment.

	python3 -m venv venv

This command invokes the python module "venv"
	
2. Initialize the virtual environment

Its source files live in the folder you created with the above command (the second "venv")

	source venv/bin/activate
	
3. Install the packages

These are listed in requirements.txt

	pip3 install -r requirements.txt

4. You're good to go! Try running an app.

	python app.py

## Running the applications in this repo

These applications are single-page apps rendered in React on top of Flask. Plotly is truly excellent when you want to quickly make a dataset visually interactive. The curve is a steep one as you ask for more functionality, FYI.

There are two apps in this repo. Each can be run simply by invoking the file in python (from within the virtual environment), like:
	
	python scatter.py
	
	python application.py
	

### What do the apps do?

1. scatter.py: this application shows
	1. For the weeks since January 1, 2020:
	1. The number of people who
		1. were expected to die in Texas, week by week
		1. actually died in excess of that number
	1. These numbers are stacked up to show the excess mortality
	1. For weeks where the death rate was exceptionally high (above the 95% CI upper bound as determined by a Farrington outbreak detection algorithm), an "x" has been tagged to the top of the week
1. application.py: this application shows
	1. for the weeks since January 1, 2020:
	1. A multi-select geographic heatmap ("choropleth")
		1. of the United States
		1. showing the percentage of weeks that rose above the 95% CI upper bound predicted mortality for that state based on historical data
	1. The number of people who
		1. Were expected to die in any state or combination of states
		1. As selected in the choropleth
		1. And, if only one state or the entire US is selected, it flags the exceptionally high weeks with an "x"

## Deploying to AWS

I've set up 10 AWS code deployment pipelines and app servers for the class. This app can be pushed as is to AWS, with a bit of configuration.

In class we'll be going through these steps in detail, but I outline them below for your reference.

Download the SSH keys that I've provided for you, and put these in ~/.ssh. This will give you access to the AWS Codecommit repository I set up for you.

Update your git config with the below information:

	Host git-codecommit.*.amazonaws.com
	User USERNAME
	IdentityFile ~/.ssh/PRIVATEKEYFILENAME

Add the keys to your keychain: ```ssh-add ~/.ssh/PRIVATEKEYFILENAME```

Pull your repository down from AWS: ```	git clone ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/START_AT_RICE_LEARNER_ID```

Look at the app, make some changes, save those, and push back up. We'll look at the code deployment live together.

	git add .
	git commit -m "my changes"
	git push