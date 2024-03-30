# **PCOS Diagnosis Website**


- ![Blog_090319_What-is-PCOS](https://github.com/Ard313/WebsitePCOS/assets/122507060/1bbd3309-4685-4959-a4c2-4e8f7b6bc4d0)


**Overview:**
This project aims to provide a platform for proactive identification of Polycystic Ovary Syndrome (PCOS) in women. PCOS is a common hormonal disorder among women of reproductive age, and early detection can significantly improve healthcare outcomes. The website utilizes machine learning algorithms to predict PCOS occurrence based on reported symptoms, facilitating early diagnosis and intervention.

**Features:**
- ![Picture2](https://github.com/Ard313/WebsitePCOS/assets/122507060/60d24e1f-5981-4c5d-b129-16b0dd22af45)

1. **Questionnaire**: Users can fill out a questionnaire providing information on age and various symptoms associated with PCOS, such as unusual hair growth and pimples.
2. **Diagnosis Prediction**: Upon submission of the questionnaire, the machine learning model predicts the likelihood of PCOS occurrence based on the provided symptoms.
3. **Result Analysis**: Users receive instant feedback on their PCOS prediction along with relevant insights and suggestions for further action.
4. **Data Visualization**: Data visualization techniques are employed to illustrate associations between symptoms and PCOS occurrence.
5. **User-Friendly Interface**: The website offers an intuitive and easy-to-use interface for seamless navigation and interaction.

**Methodology:**

- <img width="622" alt="Screenshot 2024-03-30 213734" src="https://github.com/Ard313/WebsitePCOS/assets/122507060/72c6f225-df2b-4df1-a6fa-6a8d67f8c71b">



- **Data Collection**: A questionnaire was designed to collect symptom-related data from women aged 15 and above. Additionally, a dataset from Kaggle was integrated for analysis.
- **Data Analysis and Visualization**: Python and Excel were used for data analysis and visualization to identify patterns and correlations within the dataset.
- <img width="670" alt="Screenshot 2024-03-30 215432" src="https://github.com/Ard313/WebsitePCOS/assets/122507060/eca718b7-889c-424c-ba38-728612ecd094">
- <img width="658" alt="Screenshot 2024-03-30 215733" src="https://github.com/Ard313/WebsitePCOS/assets/122507060/9e7bbe84-563a-4a33-b9b3-247226cdb034">
- **Data Preprocessing**: Null values were addressed, unnecessary attributes were removed, and data normalization was performed using a min-max scaler.
- **Model Selection and Training**: Various classifier algorithms were trained and tested on a split of 75% training and 25% test data. Hyperparameter tuning was conducted to optimize model performance.
- **Result Analysis**: The performance of nine classifiers was compared, with KNN achieving the highest accuracy of 91%. Performance metrics like accuracy score, recall, and training time were used for evaluation.
  
- <img width="617" alt="Screenshot 2024-03-30 214544" src="https://github.com/Ard313/WebsitePCOS/assets/122507060/6146211f-eadb-408c-bb07-8d68792f600c">


**Deployment:**
- The trained machine learning model was serialized into a pkl file.
- Flask framework was used to deploy the model locally.
- ![Picture1](https://github.com/Ard313/WebsitePCOS/assets/122507060/40114a04-b18b-4b74-b821-5e5369f233ad)


**Repository Structure:**
- **app.py**: Flask application script for website deployment.
- **model.pkl**: Serialized machine learning model for PCOS prediction.
- **templates/**: HTML templates for website pages.
- **static/**: Static files such as CSS and JavaScript.
- **data/**: Dataset files used for model training and testing.

**Getting Started:**
1. Clone the repository.
2. Install dependencies.
3. Run the Flask application.
4. Access the website locally via the provided URL.


**Acknowledgments:**
- Thanks to Kaggle for providing the dataset used in this project.

**Disclaimer:**
- This website is intended for informational purposes only and should not be used as a substitute for professional medical advice. Users are encouraged to consult healthcare professionals for accurate diagnosis and treatment recommendations.

