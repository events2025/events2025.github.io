---
title: 🟣 Notable Papers and Methods
nav_order: 7
layout: home
---

<h1 style="color: purple;">Notable Papers and Methods</h1>
<br>

<div style="max-width: 100%;">
  <!-- START -->
<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/in_data_we_trust_a_comparison_of_ucdp_ged_and_acled_conflict_events_datasets.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">In data we trust? A comparison of UCDP GED and ACLED conflict events datasets</p>
        <p style="margin: 0;">This paper examines the strengths and weaknesses of two prominent conflict event datasets, the UCDP Georeferenced Event Dataset (UCDP GED) and the Armed Conflict Location and Event Dataset (ACLED), which have facilitated microlevel analyses of civil war dynamics. It discusses differences in scope, definitions, and data collection processes, highlighting issues like UCDP GED’s focus on fatalities and ACLED’s inclusion of non-fatal and non-violent events. The paper uses georeferenced, disaggregated event data, primarily from Africa, detailing specific cases to evaluate coding quality and methodological challenges in both datasets.</p>
        <p style="margin: 0;"><a href="https://journals.sagepub.com/doi/10.1177/0010836711434463"><i class="fa-regular fa-file-pdf"></i>https://journals.sagepub.com/doi/10.1177/0010836711434463</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/neural_jump-diffusion_temporal_point_processes.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Neural Jump-Diffusion Temporal Point Processes</p>
        <p style="margin: 0;">The paper introduces a framework that models temporal point processes (TPPs) using neural jump-diffusion stochastic differential equations (SDEs).  Motivation: Traditional TPP models often rely on predefined functional forms, which can limit their flexibility in capturing complex event dynamics. To address this limitation, the authors propose reformulating the intensity processes of TPPs as solutions to neural jump-diffusion SDEs. This approach aims to improve the model's capacity to represent intricate temporal patterns without being constrained by specific functional assumptions. Method Description: The proposed framework, termed Neural Jump-Diffusion Temporal Point Process (NJDTPP), models the intensity function of a TPP using a neural jump-diffusion SDE (NJDSDE). In this setup, the SDE's drift, diffusion, and jump coefficients are parameterized by neural networks, allowing the model to learn complex dependencies from data. This design offers theoretical guarantees regarding the existence and uniqueness of solutions to the NJDSDE. Datasets Used: The authors evaluate NJDTPP on both synthetic and real-world datasets: Synthetic Datasets: Poisson Process, Hawkes Process, Self-Correcting Process Real-World Datasets: Retweet Data, Earthquake Records, Taxi Rides, Taobao User Behavior, StackOverflow Activity, MIMIC-II Clinical Database</p>
        <p style="margin: 0;"><a href="https://openreview.net/forum?id=d1P6GtRzuV"><i class="fa-regular fa-file-pdf"></i>https://openreview.net/forum?id=d1P6GtRzuV</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/beyond_hawkes:_neural_multi-event_forecasting_on_spatio-temporal_point_processes.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Beyond Hawkes: Neural Multi-event Forecasting on Spatio-Temporal Point Processes</p>
        <p style="margin: 0;">This paper proposes a new neural architecture for simultaneous multi-event forecasting of spatio-temporal point processes. The research utilized a variety of synthetic and real-world datasets: South California Earthquakes: Earthquake events from 2008 to 2016 in South California with magnitudes of at least 2.5. The data includes time, location in 3 dimensions, magnitude, and consecutive events' time intervals as event markers. Link of the data: https://scedc.caltech.edu/data/datasets.html Citibike: Rental events from a bike-sharing service in New York City. The data includes the starting time of the biking, location in 2 dimensions, the biker's birth year, and consecutive rentals' time intervals as event markers. Link of the data: https://citibikenyc.com/system-data. COVID-19: Daily COVID-19 cases in different states of the United States. The data includes the day of catching COVID-19, location in 2 dimensions, the number of cases on that day, and consecutive events' time intervals as event markers. Pinwheel: A synthetic dataset where Hawkes time instances were simulated using the thinning algorithm and assigned to a cluster-based pinwheel distribution. The data includes time instances and spatial points sampled from the formed distribution. </p>
        <p style="margin: 0;"><a href="https://arxiv.org/abs/2211.02922"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/abs/2211.02922</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/beyond_point_prediction:_score_matching-based_pseudolikelihood_estimation_of_neural_marked_spatio-temporal_point_process.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Beyond Point Prediction: Score Matching-based Pseudolikelihood Estimation of Neural Marked Spatio-Temporal Point Process</p>
        <p style="margin: 0;">propose SMASH to address the challenges of learning STPPs, which involve complex spatio-temporal dynamics and the need for accurate confidence interval predictions. SMASH bypasses the intractable integral computation in log-likelihood estimation by using a score-matching objective. This approach allows for the prediction of confidence intervals and regions for event times and locations through score-based sampling. The research utilized several real-world datasets to validate their approach: Earthquake Dataset: Contains the location and time of all earthquakes in Japan from 1990 to 2020 with a magnitude of at least 2.0. The data is partitioned into three categories: small,medium, and large based on their magnitude. Data Link: https://scedc.caltech.edu/data/datasets.html. Crime Dataset: Comprises reported crimes from 2015 to 2020 provided by the Atlanta Police Department. Events are classified into four types according to the crime type. Data Link: https://www.atlantapd.org Football Dataset: Records football event data retrieved from the WyScout Open Access Dataset. Each event signifies an action made by the player, associated with the type of action. </p>
        <p style="margin: 0;"><a href="https://openreview.net/forum?id=CpI37NA7MO"><i class="fa-regular fa-file-pdf"></i>https://openreview.net/forum?id=CpI37NA7MO</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/context-aware_spatiotemporal_event_prediction_via_convolutional_wawkes_processes.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Context-aware Spatiotemporal Event Prediction via Convolutional Hawkes Processes</p>
        <p style="margin: 0;">They proposed a method called ConvHawkes (Convolutional Hawkes Process) that leverages image data (e.g., satellite images, weather maps) to capture the heterogeneity in external factors and determine their effect on the triggering process of events. They extend the neural network model by combining it with continuous kernel convolution and parameterize the Hawkes process intensity based on this extended model. The goal is to accurately predict spatiotemporal events by utilizing the rich external features contained in georeferenced images. The research utilized several real-world datasets to validate their approach: Conflict Dataset: Provided by the Armed Conflict Location and Event Dataset (ACLED), this dataset consists of roughly 17,000 armed conflicts in Africa from April 1, 2018, to March 31, 2020. Each event is recorded with time and location (latitude and longitude coordinates). Data Link: https://acleddata.com/data-export-tool/ Protest Dataset: Also provided by ACLED, this dataset contains over 34,000 demonstration events in the Middle East from April 1, 2018, to March 31, 2020. Each record includes the time and location of the protest.  Data Link: https://acleddata.com/data-export-tool/ Disease Dataset: A collection of reported incidents of animal disease outbreaks in Europe, provided by EMPRES-i. It contains 21,529 records, each showing the time, latitude, and longitude of the outbreak. Data Link: http://empres-i.fao.org/eipws3g/</p>
        <p style="margin: 0;"><a href="https://link.springer.com/article/10.1007/s10994-022-06136-5"><i class="fa-regular fa-file-pdf"></i>https://link.springer.com/article/10.1007/s10994-022-06136-5</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/deep_mixture_point_processes:_spatio-temporal_event_prediction_with_rich_contextual_information.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Deep Mixture Point Processes: Spatio-temporal Event Prediction with Rich Contextual Information .</p>
        <p style="margin: 0;">This paper proposes a novel method called Deep Mixture Point Processes (DMPP) for predicting spatiotemporal events by incorporating rich contextual information such as weather, social activities, geographical characteristics, and traffic. The authors propose DMPP, a point process model that leverages heterogeneous and high-dimensional context available in image and text data. The intensity of the point process model is designed as a mixture of kernels, where the mixture weights are modeled by a deep neural network. This allows the model to automatically learn the complex nonlinear effects of contextual factors on event occurrence and makes analytical integration over the intensity tractable. The research utilized several real-world datasets to validate their approach: NYC Collision Data: This dataset contains approximately 32,000 motor vehicle collisions in New York City. Each collision is recorded with the time and location (latitude and longitude coordinates). Data Link: https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data  Chicago Crime Data: This dataset is a collection of reported incidents of crime in Chicago, containing approximately 13,000 records. Each record includes the time and location (latitude and longitude) of the crime. Data Link: Crimes - https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data NYC Taxi Data: This dataset consists of approximately 30 million taxi pick-up records in New York City, collected by the NYC Taxi and Limousine Commission (TLC). Each record contains the pick-up time and location (latitude and longitude coordinates). Data Link: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page . </p>
        <p style="margin: 0;"><a href="https://dl.acm.org/doi/abs/10.1145/3292500.3330937"><i class="fa-regular fa-file-pdf"></i>https://dl.acm.org/doi/abs/10.1145/3292500.3330937</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>
<!-- STOP -->
</div>
