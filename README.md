<H3><u>Theme</u> : Climate Change & Environmental Sustainability </H3>
<h2> <u>Topic:</u> <i>Urban Heat Islands: The Rising Temperature Crisis in Indian Cities</i></h2>
<h3> <u>Tagline </u>: Predicting Urban Heat Islands using AI and Satellite Data </h3>

<h3><b>Impact</b></h3>
<p>"With an accuracy of 99.5%, our model can help optimize green cover distribution, reduce heat-related illnesses, and guide urban cooling strategies."</p>

<H3><b>Problem Statement</b></H3>
<p>"Indian cities are experiencing rising temperatures due to increased urbanization. This project aims to predict whether an area will become a UHI in the future based on weather, air quality, and urbanization data, Help city planners make informed decisions about urban heat risks."</p>

<h3><b>Objective & Goals</b></h3>
<p>The project aims to leverage AI-driven climate analytics to predict Urban Heat Islands (UHIs) and provide insights for sustainable urban planning. By analyzing historical weather patterns, air quality indices, and urbanization factors, the model forecasts which areas are at high risk of extreme heat events in the future.</p>
<ul>
  <li>Predict UHIs using Machine Learning models.</li>
  <li>Provide real-time predictions for users based on input location data.</li>
  <li>Help city planners make informed decisions about urban heat risks.</li>
</ul>

<h3> <b> Key Features in the Model</b></h3>
<ul>
<li>Temperature Anomalies (Difference between max & min temp)</li>
<li>Air Quality Index (AQI) (PM2.5, NO2, SO2)</li>
<li>Seasonal Data (Extracted Year, Month, and Season)</li>
<li>Urbanization Levels (Population density, land use)</li>
</ul>
<ol>
  <li>Predict Future Urban Heat Islands (UHIs)</li>
  <ul>
    <li>Build an ML-powered system that predicts whether an area will turn into an Urban Heat Island.</li>
    <li>Use climate data, urbanization trends, and air quality metrics to enhance prediction accuracy.</li>
  </ul>
  <li>Real-World Usability with Location-Based Insights</li>
  <ul>
    <li>Allow users to input geographical coordinates (latitude, longitude) to get heat risk predictions.</li>
    <li>Provide an interactive and accessible way for researchers, policymakers, and citizens to assess heat risk.</li>
  </ul>
  <li>Data-Driven Urban Planning & Policy Recommendations</li>
  <ul>
    <li>Offer actionable insights for city planners and environmental organizations.</li>
    <li>Help reduce the urban heat effect by suggesting green cover, water bodies, and ventilation corridors.</li>
  </ul>
  <li>Innovation with Scalable & Deployable ML Models</li>
  <ul>
    <li>Develop a highly accurate machine learning model using Random Forest & XGBoost.</li>
    <li> Plan for future deployment as a web or mobile application for wider accessibility.</li>
  </ul>
</ol>

<h2> Why This Matter ?</h2>
<p>This project goes beyond just predictions—it provides real-time, data-driven recommendations that can shape climate resilience strategies. By making this information accessible, we contribute to a sustainable, heat-resilient future for urban India! </p>

<h3><u>Datasets Used</u></h3>
<ul>
  <li>India climate data</li>
  <li>India Air Quality</li>
  <li>Urban Air Pollution</li>
  <li>India State wise and District wise Weather Data</li>
  <li>Inida State wise Temperaature</li>
</ul>
<p><b>Note:</b>You can find Datasets in folder <i>Raw_Data</i> named as archives</p>
<h3>Architecture & Workflow </h3>
<h2>[Data Collection] → [Raw Data] → [Data Cleaning] → [EDA] → [Feature Engineering] → [Advance featyure Engineering] → [Model Training] → [Tunning] → [Prediction] </h2>

<h3>Machine Learning Model</h3>
<ul>
  <li>Random Forest (Select through auto sklearn)</li>
  <li>Evaluation Metrics:</li>
  <ol>
    <li>MAE: 0.0945</li>
    <li>RMSE: 0.2379</li>
    <li><b>R² Score: 99.5% </b></li>
  </ol>
</ul>
<h2>Prediction:</h2>
<p> This is the interface of our GUI a user can simply put value in it and findout whether it comes under UIH or not</p>




<h3> Download Requirement.txt for module installation</h3>
<h3> run the model : <b> streamlit run gui.py  </b></h3>

<h2>Summary</h2>
<ul>
  <li>Use reuirements.txt for module installation </li> 
  <li>In Raw_Data folder all the raw data collected from diff source is there <b>Data collection</b></li>
  <li>Our next Step was Data cleaning to handle missing values by mean, mode, median and many more </li>
  <li>After Handling values we merge all the Data and store it in one csv file Name: engineered_features which is in folder : preprocessed data</li>
  <li>Now Feature Eng. came into process to find trend in our data. we find the tren by using various charts and graphs after that we take it advacned one  </li>
  <li>1after finding the trend we done the feature scalling , normalization to overcome the problem of Overfitting </li>
  <li>We store our final data in csv file : consolidated_features</li>
  <li>Model evaluation : by autosklearn we find the best alg which is suitable for it </li>
  <li>our second last step is tunning our model</li>
  <li>last but not list Prediction our score is 99.5 which is pretty good </li>
</ul





