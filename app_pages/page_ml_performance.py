import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'
    
    st.write(
        f"Here we can see how the dataset was divided to fit and train "
        f"the model. We can also see how the model performs.")

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")

    st.info(
        f"For the label distribution outlined above the dataset was divided as follows - \n"
        f"* Train - healthy - 1472 images.\n"
        f"* Train - powdery_mildew - 1472 images.\n"
        f"* Validation - healthy - 210 images.\n"
        f"* Validation - powdery_mildew - 210 images.\n"
        f"* Test - healthy - 422 images.\n"
        f"* Test - powdery_mildew - 422 images.")


    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.success(
        f"This shows the model operates with an accuracy of 98.1% which \n"
        f"exceeds the accuracy percentage agreed with the client."        )