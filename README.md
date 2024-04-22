# Mildew Detection in Cherry Leaves

This project was developed for Farmy & Foods, a company in the agricultural sector that produces and harvests different types of food. Recently, the company has faced a challenge where their cherry plantations have been presenting powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products and the company is concerned about supplying the market with a product of compromised quality.

Powdery mildew is a fungal disease that commonly affects cherry trees. It appears as a white or gray powdery substance on the leaves, stems, and sometimes fruit of the tree. The fungus responsible for powdery mildew thrives in warm, humid conditions and is spread through spores being carried by the wind.

The risk of infection with powdery mildew is relatively high in cherry trees, especially during periods of warm, humid weather. Once infected, the fungus can spread rapidly throughout the tree and cause damage to the leaves, reducing the tree's ability to photosynthesize and eventually impacting fruit production.

To prevent and manage powdery mildew in cherry trees, it is important to regularly inspect the tree for signs of infection and take prompt action to control the spread of the fungus. This may involve using fungicides, pruning affected branches, and practicing good plant hygiene to reduce the risk of infection.

Prior to completion of this project, Farmy & Foods employees would manually inspect leaves to establish if they were infected or healthy. This process would usually take around 30 minutes per tree. 

The main overall intention of the project was to create a Machine Learning System with the capability to instantly detect in an image of a leave was healthy or infected, this would ensure the company could continue to provide a high quality healthy product without the need for time consuming manual inspections.

## Dataset Content

The dataset for this project was provided by the client. It contained a total of 4208 images which were split into 2104 healthy images and 2104 powery mildew infected images of cherry leaves.

The dataset was sourced from Kaggle and can be accessed [here.](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)

## Business Requirements

As previously summerised, our client, Farmy & Foods are facing a challenge as a result of their Cherry Tree Plantation showing signs of powder mildew infection. It currently take employees around 30 minutes to inspect a cherry tree and confirm if it is healthy or infected. The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection. Our goal is to produce a Machine Learning System which is capable of examing images of the cherry tree leaves and confirming if they are healthy or infected.

The two business requirements identified for this project are - 
* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
* The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.

## Hypothesis and validation

### Hypothesis

Plants which are infected with powdery mildew show distinct markings on their leaves which indicate infection. The markings on an infected leaf are usually light powdery stripes and spots.

### How to Validate

In order to be able to validate this hypothesis firstly we must research powdery mildew infection, understand why and how it occurs and thereafter be able to recognise the signs and symptoms. Then, I must use the dataset provided by the client in order to create an image study which will allow us to investigate the images of leaves and use this to build a Machine Learning System capable of recognising if an image of a cherry leaf is either healthy or infected with powdery mildew.

### Validation

By displaying images of infected and healthy leaves we can visually compare them in order to establish differences in the leaves. This is done by creating an image montage to conduct the comparison of infected and healthy leaves. From analysis of the montage it can be seen that infected leaves show distinct white markings that the healthy leaves don't.

## The rationale to map the business requirements to the Data Visualizations and ML tasks

From each of the business requirements identified a number of user stories were created which subsequently became machine learning tasks.

### Business Requirement 1
* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

#### User Stories

- As a client, I need a user-friendly dashboard to easily navigate in order to access and view study and image displays.
- As a client, I want to see the average image and variability of healthy and powdery mildew-infected leaves in the dataset to understand their differences.
- As a client, I want to compare the average images of healthy and infected leaves to see if there are noticeable distinctions.
- As a client, I would like to view a montage of images showing healthy and infected leaves in the dataset to visually compare the two.

These user stories were implemented by -

- The client dashboard was created using Streamlit with 6 pages and a easy to use menu for navigation.
- TensorFlow was used to load dataset images into an array in the Data Visualization notebook, enabling the display of average and variability for all images on the Cherry Leaf Visualizer Page in Dashboard.
- Users can visualize the difference between healthy leaves and infected leaves on the Cherry Leaf Visualizer page of the Dashboard.
- Users can create an image montage of healthy or infected cherry leaf images on the Cherry Leaf Visualizer page.

### Business Requirement 2
* The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.

#### User Stories

- As a client, I want a Machine Learning Model capable of predicting if a given image of a Cherry Leaf is Healthy or infected with Powdery Mildew with an accuracy of at least 97%.
- As a client, I was to be able to easily access the performance metrics so I can understand the accuracy of the Machine Learning Model.
- As a client, I want to be able to upload an image, or multiple images of Cherry Leaves to be quickly analysed so I can confirm which need treated as a result of being infected.
- As a client, I want to be able to download a copy of the prediction report.

These user stories were implemented by -

- A Machine Learning Model capable of predicting if a leaf is infected or not was created and when tested provided an accuaracy level of 98.1%, exceeding the clients expectations.
- The performance metrics for the Model are displayed in the ML_Performance page.
- In the mildew infection detector page users can upload an image, or multiple images at the same time, for prediction. This allows for a quick analysis to be conducted and provides the client with confirmation if the leaves are healthy or infected.
- Users can download a copy of a prediction report which they can save for their own use.


## Dashboard Design (Streamlit App User Interface)

## The process of Cross-industry standard process for data mining

## Bugs

## Deployment
The project code is stored on GitHub and deployed with [Heroku](https://www.heroku.com/). 
The steps needed to deploy this projects are as follows:

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 

## Cloning this repository

In order to work on this repository you will first need to clone it.

**Instructions to clone the repository**:

1 - While in the GitHub repository, click on the green code button.

2 - Copy the link.

3 - In your IDE or local coding environment use the link to open the repository. 

For example: in CodeAnywhere
- Click on 'Add new workspace'
- You will then be given the option to 'Create from your project repository' and a box in which to paste the link
- CodeAnywhere will now open a new workspace containing the repository.
- You should now be set up ready to work on the repository.

## Forking a branch

In order to protect the main branch while you work on something new, essential when working as part of a team or when you want to experiment with a new feature, you will need to fork a branch.

**Instructions to fork the repository**:

1 - While in the GitHub repository, click on the branch symbol and text indicating the number of branches.

2 - This will load details on current branches. Click on the green 'New branch' button.

3 - Enter a name for the new branch and then click the green 'create new branch' button.

4 - Your new branch should now have appeared on the screen.

5 - Clicking on the new branch and then following the steps for cloning will allow you to open up and work on this branch.

## Technologies used

### Platforms


### Languages
- [Python](https://www.python.org/)
- [Markdown](https://en.wikipedia.org/wiki/Markdown)
  
### Main Data Analysis and Machine Learning Libraries

## Credits 

### Content
- The dataset for the cherry leaves was obtained from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) and created by [Code Institute](https://www.kaggle.com/codeinstitute)

### Media

### Code

### Acknowledgements

* My Code Institute Mentor, Mo Shammi for his continuous feedback, help, guidance and expertise throughout this project.
* My fellow users of the Code Institute Slack Channel for their support, feedback and help. 
