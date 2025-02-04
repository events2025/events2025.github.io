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
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">In Data We Trust? A Comparison of UCDP GED and ACLED Conflict Events Datasets</p>
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
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Beyond Hawkes: Neural Multi-Event Forecasting on Spatio-Temporal Point Processes</p>
        <p style="margin: 0;">This paper proposes a new neural architecture for simultaneous multi-event forecasting of spatio-temporal point processes. The research utilized a variety of synthetic and real-world datasets:\\n South California Earthquakes: Earthquake events from 2008 to 2016 in South California with magnitudes of at least 2.5. The data includes time, location in 3 dimensions, magnitude, and consecutive events' time intervals as event markers. Link of the data: https://scedc.caltech.edu/data/datasets.html\\n Citibike: Rental events from a bike-sharing service in New York City. The data includes the starting time of the biking, location in 2 dimensions, the biker's birth year, and consecutive rentals' time intervals as event markers. Link of the data: https://citibikenyc.com/system-data\\n COVID-19: Daily COVID-19 cases in different states of the United States. The data includes the day of catching COVID-19, location in 2 dimensions, the number of cases on that day, and consecutive events' time intervals as event markers.\\nPinwheel: A synthetic dataset where Hawkes time instances were simulated using the thinning algorithm and assigned to a cluster-based pinwheel distribution. The data includes time instances and spatial points sampled from the formed distribution.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/abs/2211.02922"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/abs/2211.02922</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Beyond Point Prediction: Score Matching-Based Pseudolikelihood Estimation of Neural Marked Spatio-Temporal Point Process</p>
        <p style="margin: 0;">propose SMASH to address the challenges of learning STPPs, which involve complex spatio-temporal dynamics and the need for accurate confidence interval predictions. SMASH bypasses the intractable integral computation in log-likelihood estimation by using a score-matching objective. This approach allows for the prediction of confidence intervals and regions for event times and locations through score-based sampling. The research utilized several real-world datasets to validate their approach: Earthquake Dataset: Contains the location and time of all earthquakes in Japan from 1990 to 2020 with a magnitude of at least 2.0. The data is partitioned into three categories: small,medium, and large based on their magnitude. Data Link: https://scedc.caltech.edu/data/datasets.html. Crime Dataset: Comprises reported crimes from 2015 to 2020 provided by the Atlanta Police Department. Events are classified into four types according to the crime type. Data Link: https://www.atlantapd.org Football Dataset: Records football event data retrieved from the WyScout Open Access Dataset. Each event signifies an action made by the player, associated with the type of action. </p>
        <p style="margin: 0;"><a href="https://openreview.net/forum?id=CpI37NA7MO"><i class="fa-regular fa-file-pdf"></i>https://openreview.net/forum?id=CpI37NA7MO</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Context-Aware Spatiotemporal Event Prediction Via Convolutional Hawkes Processes</p>
        <p style="margin: 0;">They proposed a method called ConvHawkes (Convolutional Hawkes Process) that leverages image data (e.g., satellite images, weather maps) to capture the heterogeneity in external factors and determine their effect on the triggering process of events. They extend the neural network model by combining it with continuous kernel convolution and parameterize the Hawkes process intensity based on this extended model. The goal is to accurately predict spatiotemporal events by utilizing the rich external features contained in georeferenced images. The research utilized several real-world datasets to validate their approach: Conflict Dataset: Provided by the Armed Conflict Location and Event Dataset (ACLED), this dataset consists of roughly 17,000 armed conflicts in Africa from April 1, 2018, to March 31, 2020. Each event is recorded with time and location (latitude and longitude coordinates). Data Link: https://acleddata.com/data-export-tool/ Protest Dataset: Also provided by ACLED, this dataset contains over 34,000 demonstration events in the Middle East from April 1, 2018, to March 31, 2020. Each record includes the time and location of the protest.  Data Link: https://acleddata.com/data-export-tool/ Disease Dataset: A collection of reported incidents of animal disease outbreaks in Europe, provided by EMPRES-i. It contains 21,529 records, each showing the time, latitude, and longitude of the outbreak. Data Link: http://empres-i.fao.org/eipws3g/</p>
        <p style="margin: 0;"><a href="https://link.springer.com/article/10.1007/s10994-022-06136-5"><i class="fa-regular fa-file-pdf"></i>https://link.springer.com/article/10.1007/s10994-022-06136-5</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Deep Mixture Point Processes: Spatio-Temporal Event Prediction With Rich Contextual Information</p>
        <p style="margin: 0;">This paper proposes a novel method called Deep Mixture Point Processes (DMPP) for predicting spatiotemporal events by incorporating rich contextual information such as weather, social activities, geographical characteristics, and traffic. The authors propose DMPP, a point process model that leverages heterogeneous and high-dimensional context available in image and text data. The intensity of the point process model is designed as a mixture of kernels, where the mixture weights are modeled by a deep neural network. This allows the model to automatically learn the complex nonlinear effects of contextual factors on event occurrence and makes analytical integration over the intensity tractable. The research utilized several real-world datasets to validate their approach: NYC Collision Data: This dataset contains approximately 32,000 motor vehicle collisions in New York City. Each collision is recorded with the time and location (latitude and longitude coordinates). Data Link: https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data  Chicago Crime Data: This dataset is a collection of reported incidents of crime in Chicago, containing approximately 13,000 records. Each record includes the time and location (latitude and longitude) of the crime. Data Link: Crimes - https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data NYC Taxi Data: This dataset consists of approximately 30 million taxi pick-up records in New York City, collected by the NYC Taxi and Limousine Commission (TLC). Each record contains the pick-up time and location (latitude and longitude coordinates). Data Link: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page . </p>
        <p style="margin: 0;"><a href="https://dl.acm.org/doi/abs/10.1145/3292500.3330937"><i class="fa-regular fa-file-pdf"></i>https://dl.acm.org/doi/abs/10.1145/3292500.3330937</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Imitation Learning of Neural Spatio-Temporal Point Processes</p>
        <p style="margin: 0;">This paper presents a novel Neural Embedding Spatio-Temporal (NEST) point process model for spatio-temporal discrete event data and develops an efficient imitation learning-based approach for model fitting The authors propose the NEST model to capture complex spatio-temporal dependencies between discrete events using a mixture of heterogeneous Gaussian diffusion kernels. The parameters of these kernels are parameterized by neural networks. The imitation learning approach for model fitting is more robust than the maximum likelihood estimate, directly measuring the divergence between empirical distributions of training data and model-generated data. The research utilized both synthetic and real-world datasets: Synthetic Data: The synthetic datasets were generated to validate the model's capability in capturing spatial information from discrete event data. These datasets included sequences of events with varying spatial and temporal dependencies. Real-World Data: Atlanta 911 Calls-for-Service Data: This dataset includes 7,831 reported robbery events in Atlanta from the end of 2015 to 2017. Each event is recorded with the time and geolocation (latitude and longitude). Data Link: https://www.kaggle.com/datasets/sachinpatil1280/911-emergency-calls This data-link is a similar data but not exactly the one in the paper. Northern California Seismic Data: This dataset contains 16,401 seismic records with magnitudes larger than 3.0 from 1978 to 2018 in Northern California. The data includes the time and geolocation of each seismic event. Data Link: https://ncedc.org/ </p>
        <p style="margin: 0;"><a href="https://ieeexplore.ieee.org/abstract/document/9336246"><i class="fa-regular fa-file-pdf"></i>https://ieeexplore.ieee.org/abstract/document/9336246</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Integration-Free Training for Spatio-Temporal Multimodal Covariate Deep Kernel Point Processes</p>
        <p style="margin: 0;">This paper proposes a novel deep spatio-temporal point process model called Deep Kernel Mixture Point Processes (DKMPP) that incorporates multimodal covariate information. The authors propose DKMPP, an enhanced version of Deep Mixture Point Processes (DMPP), which uses a more flexible deep kernel to model complex relationships between events and covariate data. To address the intractable training procedure of DKMPP due to the non-integrable deep kernel, they utilize an integration-free method based on score matching and further improve efficiency by adopting a scalable denoising score matching method. The research utilized several real-world datasets to validate their approach: Crimes in Vancouver: This dataset is composed of more than 530 thousand crime records, including all categories of crimes committed in Vancouver. Each crime record contains the time and location (latitude and longitude) of the crime. Data Link: https://www.kaggle.com/datasets/wosaku/crime-in-vancouver NYC Vehicle Collisions: The New York City vehicle collision dataset contains about 1.05 million vehicle collision records. Each collision record includes the time and location (latitude and longitude). Data Link: https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data  NYC Complaint Data: This dataset contains over 228 thousand complaint records in New York City. Each record includes the date, time, and location (latitude and longitude) of the complaint. Data Link: https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Current-Year-To-Date-/5uac-w243/about_data</p>
        <p style="margin: 0;"><a href="https://proceedings.neurips.cc/paper_files/paper/2023/hash/4eb2c0adafbe71269f3a772c130f9e53-Abstract-Conference.html"><i class="fa-regular fa-file-pdf"></i>https://proceedings.neurips.cc/paper_files/paper/2023/hash/4eb2c0adafbe71269f3a772c130f9e53-Abstract-Conference.html</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Modeling Randomly Observed Spatiotemporal Dynamical Systems</p>
        <p style="margin: 0;">This paper proposes a novel method for modeling spatiotemporal dynamical systems observed at random times and locations. The authors propose a new spatiotemporal method that effectively handles randomly sampled data. Their model integrates techniques from amortized variational inference, neural differential equations, neural point processes, and implicit neural representations to predict both the dynamics of the system and the probabilistic locations and timings of future observations. This approach aims to improve predictive accuracy and computational efficiency for modeling complex dynamical systems observed under realistic, unconstrained conditions. The research utilized several synthetic datasets generated by three commonly-used PDE systems: Burgers' System: This dataset models nonlinear 1D wave propagation. The system is simulated on a time interval [0,2] and on a spatial domain [0,1] with periodic boundary conditions. The dataset contains 10,000 trajectories, each evaluated on a uniform temporal grid with 101 time points and a uniform spatial grid with 256 nodes.  Data Link: https://github.com/esa/torchquad  Shallow Water System: This dataset models 2D wave propagation under gravity. The system is simulated on a time interval [0,1] and on a spatial domain [−2.5,2.5]². The dataset contains 1,000 trajectories, each evaluated on a uniform temporal grid with 101 time points and a uniform 128-by-128 spatial grid. Data Link: https://github.com/esa/torchquad  Navier-Stokes System with Transport: This dataset models the spread of a pollutant in a liquid over a 2D domain. The system is simulated on a time interval [0,1] and on a spatial domain [0,1]² with periodic boundary conditions. The dataset contains 1,000 trajectories, each evaluated at randomly selected spatial locations and time points. Data Link: https://github.com/esa/torchquad</p>
        <p style="margin: 0;"><a href="https://arxiv.org/abs/2406.00368"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/abs/2406.00368</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Neural Point Process for Learning Spatiotemporal Event Dynamics</p>
        <p style="margin: 0;">This paper proposes a novel deep dynamics model called Deep Spatiotemporal Point Process (DeepSTPP) for learning and forecasting spatiotemporal event dynamics. The authors propose DeepSTPP, a deep dynamics model that integrates spatiotemporal point processes with deep learning. The model is designed to forecast irregularly sampled events over space and time by using a nonparametric space-time intensity function governed by a latent process. The intensity function enjoys closed-form integration for the density, and the latent process captures the uncertainty of the event sequence. The model uses amortized variational inference to infer the latent process with deep networks.  The research utilized both synthetic and real-world datasets:  Synthetic Data: The synthetic datasets were generated using Ogata's thinning algorithm and included:  Spatiotemporal Hawkes Process (STHP): This dataset models self-exciting processes where past events influence future events. It includes parameters like background event density and event influence decay over time.  Spatiotemporal Self-Correcting Process (STSC): This dataset models processes where the intensity increases between events and decreases sharply after an event. It includes parameters like background event density and negative event influence.  Real-World Data: Earthquakes Japan: This dataset contains information on the times and locations of all earthquakes in Japan between 1990 and 2020 with magnitudes of at least 2.5.  Data Link: https://earthquake.usgs.gov/earthquakes/search/  COVID-19 New Jersey: This dataset includes COVID-19 cases in New Jersey at the county level, published by The New York Times. Data Link: https://github.com/nytimes/covid-19-data  </p>
        <p style="margin: 0;"><a href="https://proceedings.mlr.press/v168/zhou22a.html"><i class="fa-regular fa-file-pdf"></i>https://proceedings.mlr.press/v168/zhou22a.html</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Neural Spatiotemporal Point Processes</p>
        <p style="margin: 0;">This paper proposes a new class of parameterizations for spatiotemporal point processes using Neural ODEs (Ordinary Differential Equations) to model discrete events in continuous time and space. The authors propose a method that leverages Neural ODEs to create flexible, high-fidelity models of spatiotemporal point processes. They introduce two novel neural architectures: Jump Continuous-time Normalizing Flows (Jump CNF) and Attentive Continuous-time Normalizing Flows (Attentive CNF). These architectures allow the model to learn complex distributions for both spatial and temporal domains and condition non-trivially on the observed event history. The research utilized several synthetic and real-world datasets: Pinwheel Dataset: A synthetic dataset with multimodal and non-Gaussian spatial distributions designed to test the ability to capture drastic changes due to event history. The dataset consists of 10 clusters forming a pinwheel structure, with events sampled from a multivariate Hawkes process. Data Link: This is a synthetic dataset and is not publicly available for direct download. Earthquakes Japan: This dataset contains the location and time of all earthquakes in Japan from 1990 to 2020 with magnitudes of at least 2.5. The data was gathered from the U.S. Geological Survey. Data Link: https://earthquake.usgs.gov/earthquakes/search/ COVID-19 Cases in New Jersey: This dataset includes daily COVID-19 cases in New Jersey, aggregated at the county level, from March to July 2020. The data was released publicly by The New York Times. Data Link: https://github.com/nytimes/covid-19-data BOLD5000: This dataset consists of fMRI scans of participants given visual stimuli. Brain responses were converted into spatiotemporal events following a z-score thresholding approach. Data Link: It was released on github but is no longer available now </p>
        <p style="margin: 0;"><a href="https://arxiv.org/abs/2011.04583"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/abs/2011.04583</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Neural Spectral Marked Point Processes</p>
        <p style="margin: 0;">This paper introduces a novel neural network-based non-stationary influence kernel for handling complex discrete event data. The authors propose a Neural Spectral Marked Point Process (NSMPP) model that uses a spectral decomposition of the influence kernel with a finite-rank truncation. This approach allows the model to capture non-stationary processes and high-dimensional marks, going beyond traditional stationary point processes like the Hawkes process. The model leverages neural networks to represent the kernel function, enabling it to handle complex spatiotemporal dependencies and provide theoretical performance guarantees. The research utilized both synthetic and real-world datasets: Synthetic Data: The synthetic datasets were generated to validate the model's capability in capturing non-stationary and high-dimensional kernel structures. These datasets included sequences of events with varying spatial and temporal dependencies. Real-World Data: Seismic Data: This dataset includes seismic records from Northern California with magnitudes larger than 3.0 from 1978 to 2018. The data contains the time and geolocation of each seismic event. Data Link: https://ncedc.org/ Police Data: This dataset consists of 911 calls-for-service data in Atlanta from 2015 to 2017, focusing on reported robbery events. Each record includes the time and geolocation of the robbery. Data Link: I couldn’t get the direct data link but it is from the Atlanta open data portal https://gis.atlantaga.gov/?page=OPEN-DATA-HUB  </p>
        <p style="margin: 0;"><a href="https://arxiv.org/abs/2106.10773"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/abs/2106.10773</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Recurrent Marked Temporal Point Processes: Embedding Event History to Vector</p>
        <p style="margin: 0;">This paper proposes a novel method called Recurrent Marked Temporal Point Process (RMTPP) for modeling event data with covariates using recurrent neural networks. The authors propose RMTPP to simultaneously model the event timings and the markers. The key idea is to view the intensity function of a temporal point process as a nonlinear function of the history and use a recurrent neural network (RNN) to automatically learn a representation of influences from the event history. This approach aims to improve the predictive performance for both the event type and timing compared to traditional parametric models. The research utilized both synthetic and real-world datasets: Synthetic Data: The synthetic datasets were generated to validate the model's capability in capturing temporal dynamics from discrete event data. These datasets included sequences of events with varying temporal dependencies. Real-World Data: NYC Taxi Dataset: This dataset contains 173 million trip records of individual taxis in New York City for 12 months in 2013. Each record includes the time and location (latitude and longitude) of passenger pickups and drop-offs. Data Link: https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data  Financial Transaction Dataset: This dataset includes high-frequency transaction records from the New York Stock Exchange (NYSE) for a single stock in one day. Each record contains the time (in milliseconds) and the action (buy or sell). Data Link: Not publicly available for download. MIMIC-II Medical Dataset: This dataset is a collection of de-identified clinical visit records of Intensive Care Unit (ICU) patients over seven years. Each event records the time when a patient had a visit to the hospital and the diagnosis of the major disease. Data Link: https://mimic.mit.edu/ Stack Overflow Dataset: This dataset includes badge awards for users on the Stack Overflow website. Each event records the time and type of badge awarded to a user. Data Link: https://archive.org/details/stackexchange</p>
        <p style="margin: 0;"><a href="https://dl.acm.org/doi/abs/10.1145/2939672.2939875"><i class="fa-regular fa-file-pdf"></i>https://dl.acm.org/doi/abs/10.1145/2939672.2939875</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Spatio-Temporal Diffusion Point Processes</p>
        <p style="margin: 0;">This paper proposes a novel parameterization framework for Spatio-temporal Point Processes (STPPs) using diffusion models to learn complex spatio-temporal joint distributions. The authors propose a new framework called Spatio-temporal Diffusion Point Processes (DSTPP). This framework leverages diffusion models to decompose the learning of the target joint distribution into multiple steps, each described by a Gaussian distribution. The model introduces a spatio-temporal co-attention module to capture the interdependence between event time and space adaptively. This approach aims to break the restrictions on spatio-temporal dependencies in existing solutions and enable flexible and accurate modeling of STPPs.  The research utilized both synthetic and real-world datasets: Earthquakes in Japan: This dataset includes earthquakes with a magnitude of at least 2.5 from 1990 to 2020, recorded by the U.S. Geological Survey. Data Link: https://earthquake.usgs.gov/earthquakes/search/  COVID-19 Spread in New Jersey: This dataset records daily infected cases of COVID-19 in New Jersey, aggregated at the county level, and publicly released by The New York Times. Data Link: https://github.com/nytimes/covid-19-data Citibike: This dataset contains bike-sharing data in New York City, where the start of each trip is considered an event. Data Link: https://citibikenyc.com/system-data Hawkes Gaussian Mixture Model (GMM): This synthetic dataset uses a Gaussian Mixture Model to generate spatial locations, with events sampled from a multivariate Hawkes process. Data Link: https://github.com/facebookresearch/neural_stpp/blob/main/toy_datasets.py  Atlanta Crime Data: This dataset records robbery crime events in Atlanta, provided by the Atlanta Police Department. Data Link: Data link is not available and is available on City of Atlanta Open Data Portal</p>
        <p style="margin: 0;"><a href="https://dl.acm.org/doi/abs/10.1145/3580305.3599511"><i class="fa-regular fa-file-pdf"></i>https://dl.acm.org/doi/abs/10.1145/3580305.3599511</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Spatio-Temporal Point Processes with Deep Non-stationary Kernels</p>
        <p style="margin: 0;">This paper proposes a novel deep non-stationary influence kernel for modeling spatio-temporal point processes (STPPs). The authors propose a new deep non-stationary influence kernel (DNSK) that can model non-stationary spatio-temporal point processes. The main idea is to approximate the influence kernel with a novel and general low-rank decomposition, enabling efficient representation through deep neural networks. They introduce a log-barrier penalty to maintain the non-negativity constraint of the conditional intensity function, ensuring the model is statistically meaningful and numerically stable. The proposed method aims to improve computational efficiency and predictive performance compared to existing models. The research utilized both synthetic and real-world datasets: Synthetic Data: The synthetic datasets were generated using thinning algorithms and included: 1D Exponential Kernel: This dataset models events with an exponentially decaying influence over time. 1D Non-stationary Kernel: This dataset models events with a non-stationary influence over time. 1D Infinite Rank Kernel: This dataset models events with a complex, infinite-rank influence kernel. 2D Exponential Kernel: This dataset models events with an exponentially decaying influence over space and time. 3D Non-stationary Inhibition Kernel: This dataset models events with a non-stationary inhibition influence over space and time. 3D Non-stationary Mixture Kernel: This dataset models events with a mixture of non-stationary influences over space and time. Real-World Data: Southern California Earthquake Data: This dataset contains time and location information of earthquakes in Southern California from 1999 to 2019 with magnitudes larger than 2.5. Data Lin: https://scedc.caltech.edu/data/datasets.html  Atlanta Robbery & Burglary Data: This dataset includes reported robbery and burglary events in Atlanta from 2013 to 2019, with time and location information. Data Link: Data is available on City of Atlanta Open Data Portal. Atlanta Textual Crime Data: This dataset records crime incidents in Atlanta from 2016 to 2017, including time, location, and textual descriptions of the crimes. Data Link: This dataset is proprietary and not publicly available for direct download.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/abs/2211.11179"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/abs/2211.11179</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Tensor Kernel Recovery for Discrete Spatio-Temporal Hawkes Processes</p>
        <p style="margin: 0;">This paper introduces a new discrete spatio-temporal Hawkes process model by formulating the general influence of the Hawkes process as a tensor kernel. The authors propose a discrete spatio-temporal Hawkes process model with a tensor kernel to capture the interactions between events over space and time. They formulate the estimation of the tensor kernel as a convex optimization problem using the Fourier transformed nuclear norm. The model aims to provide theoretical performance guarantees and demonstrate computational efficiency through numerical simulations on synthetic and real-world data. The research utilized both synthetic and real-world datasets: Synthetic Data: The synthetic datasets were generated to validate the model's capability in capturing spatial and temporal dependencies from discrete event data. These datasets included sequences of events with varying spatial and temporal dependencies. Real-World Data: Atlanta Burglary Data: This dataset includes 47,245 burglary incidents in Atlanta from January 1, 2015, to February 28, 2017. The events are recorded with time and geolocation (latitude and longitude). Data Link: Data is available on City of Atlanta Open Data Portal.</p>
        <p style="margin: 0;"><a href="https://ieeexplore.ieee.org/abstract/document/10002294"><i class="fa-regular fa-file-pdf"></i>https://ieeexplore.ieee.org/abstract/document/10002294</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/default_image.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Unlocking Point Processes Through Point Set Diffusion</p>
        <p style="margin: 0;">This paper introduces a novel approach called Point Set Diffusion for modeling point processes on general metric spaces. The authors propose Point Set Diffusion, a diffusion-based latent variable model that can represent arbitrary point processes without relying on the intensity function. This method directly learns to stochastically interpolate between noise and data point sets, enabling efficient, parallel sampling and flexible generation for complex conditional tasks defined on the metric space. The approach aims to overcome the limitations of existing models that rely on the characteristic intensity function, which often introduces trade-offs between efficiency and flexibility. The research utilized both synthetic and real-world datasets: Japan Earthquakes: This dataset includes the location and time of all earthquakes in Japan from 1990 to 2020 with magnitudes of at least 2.5. The data was gathered from the U.S. Geological Survey. Data Link: https://earthquake.usgs.gov/earthquakes/search/  New Jersey COVID-19 Cases: This dataset records daily COVID-19 cases in New Jersey, aggregated at the county level, and publicly released by The New York Times. Data Link: https://github.com/nytimes/covid-19-data  Citibike Pickups: This dataset contains bike-sharing data in New York City, where the start of each trip is considered an event. Data Link: https://citibikenyc.com/system-data  Pinwheel: A synthetic dataset based on a multivariate Hawkes process, designed to test the ability to capture drastic changes due to event history. Data Link: This is a synthetic dataset and is not publicly available for direct download.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/abs/2410.22493"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/abs/2410.22493</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>
<!-- STOP -->
</div>
