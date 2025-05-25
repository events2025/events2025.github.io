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
      <img src="/assets/images/thumb/conflict-logo.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
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
      <img src="/assets/images/thumb/neuraltpp.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
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
      <img src="/assets/images/thumb/neural_spatiotemporal_point_processes_trends_and_challenges.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Neural Spatiotemporal Point Processes: Trends and Challenges</p>
        <p style="margin: 0;">This paper, published in February 2025, discusses STPPs, probabilistic models for events occurring in continuous space and time; they categorize existing approaches, unify key design choices, explain the challenges of working with this data modality, identify open challenges, and gaps in the literature. They describe the applications possible in various datasets, such as natural disasters, crimes, and traffic.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/pdf/2502.09341v1"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/pdf/2502.09341v1</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/neural_temporal_point_processes_a_review.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Neural Temporal Point Processes: A Review</p>
        <p style="margin: 0;">This paper, published in August 2021, discusses neural TPPs for merging and combining deep learning with temporal point process models. They focus on design choices for this topic, applications, and datasets such as earthquake occurrences; they discuss the open challenges such as the lack of standardized experimental setups and high-quality benchmark datasets, which makes a problematic challenge for the comparison of different neural TPP architectures.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/pdf/2104.03528"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/pdf/2104.03528</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/an_empirical_study_extensive_deep_temporal_point_process.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">An Empirical Study: Extensive Deep Temporal Point Process</p>
        <p style="margin: 0;">This paper, published in December 2024 discusses neural TPPs, this paper mainly focuses on the temporal point process using deep learning with deep empirical study on the subject.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/pdf/2110.09823"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/pdf/2110.09823</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/spatio_temporal_point_process_statistics_a_review.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Spatio-temporal point process statistics: A review</p>
        <p style="margin: 0;">This paper, published in November 2016, provides a review describing statistical models and methods for spatio-temporal data. They define characteristics and statistics to uniquely characterize certain spatio-temporal point processes.</p>
        <p style="margin: 0;"><a href="https://surl.li/ofjlkm"><i class="fa-regular fa-file-pdf"></i>https://surl.li/ofjlkm</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/a_review-of_self_exciting_spatio_temporalpoint_processes_and_their_applications.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">A Review of Self-Exciting Spatio-Temporal Point Processes and Their Applications</p>
        <p style="margin: 0;">This paper, published in August 2018, the basic theory, survey-related estimation, and inference techniques, highlights several key applications and suggests directions for future research. and highlights self-exciting models when spatio-temporal point processes can be divided into clusters of events triggered by common causes.</p>
        <p style="margin: 0;"><a href="https://surl.li/oekoqa"><i class="fa-regular fa-file-pdf"></i>https://surl.li/oekoqa</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/statistical_deep_learning_for_spatial_and_spatiotemporal_data.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Statistical Deep Learning for Spatial and Spatiotemporal Data</p>
        <p style="margin: 0;">This paper, published in 2023, provides a review of traditional and machine learning spatial and spatial-temporal data with a focus on a variety of hybrid models that integrate statistical models with deep learning models and gives an overview of computational technologies that have proven useful.</p>
        <p style="margin: 0;"><a href="https://surl.li/tkiigr"><i class="fa-regular fa-file-pdf"></i>https://surl.li/tkiigr</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/spatio_temporal_hawkes_point_processes_a_review.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Spatio-Temporal Hawkes Point Processes: A Review</p>
        <p style="margin: 0;">This paper, published in September 2024, provides background on major aspects of Hawkes processes with a focus on simulation methods and estimation techniques among an overview of stochastic processes and the challenges of Hawkes processes.</p>
        <p style="margin: 0;"><a href="https://link.springer.com/article/10.1007/s13253-024-00653-7"><i class="fa-regular fa-file-pdf"></i>https://link.springer.com/article/10.1007/s13253-024-00653-7</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/behaviour_based_dependency_networks.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Behaviour-Based Dependency Networks Between Places Shape Urban Economic Resilience</p>
        <p style="margin: 0;">This paper, published December 2024, explains that during disruptions like pandemics, business closures affect not just the businesses themselves but also people's movements, which then impact other businesses. The study uses data from five US cities to measure how businesses depend on each other. It finds that behavior-based relationships improve predictions of business resilience by about 40% compared to distance-based models. Ignoring these relationships can lead to underestimating the spread of disruptions. The research highlights the need to understand human mobility patterns to boost urban economic resilience.</p>
        <p style="margin: 0;"><a href="https://www.nature.com/articles/s41562-024-02072-7"><i class="fa-regular fa-file-pdf"></i>https://www.nature.com/articles/s41562-024-02072-7</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/child_marriage_paper.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Child Marriage in Conflict Settings: A Geospatial Analysis</p>
        <p style="margin: 0;">This paper, published in July 2024, highlights the impact of conflict events on the incidence of child marriage. They used georeferenced data on armed conflict and population-level microdata for marriages of more than 2 million women across 56 countries to estimate the impact of the occurrence and severity of conflict events in or before the year of marriage on the incidence of child marriage.</p>
        <p style="margin: 0;"><a href="https://link.springer.com/article/10.1007/s43545-024-00940-7"><i class="fa-regular fa-file-pdf"></i>https://link.springer.com/article/10.1007/s43545-024-00940-7</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/conflict_and_forest_loss in_colombia.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Toward Causal Inference for Spatio-Temporal Data: Conflict and Forest Loss in Colombia</p>
        <p style="margin: 0;">This paper, published in Jan 2022, discusses how armed conflict influences tropical forest loss. In this study, they propose a class of causal models for spatio-temporal stochastic processes, which allows one to formally define and quantify the causal effects.</p>
        <p style="margin: 0;"><a href="https://www.tandfonline.com/doi/full/10.1080/01621459.2021.2013241#abstract"><i class="fa-regular fa-file-pdf"></i>https://www.tandfonline.com/doi/full/10.1080/01621459.2021.2013241#abstract</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/multi_modality_spatio_temporal forecasting.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Multi-Modality Spatio-Temporal Forecasting via Self-Supervised Learning</p>
        <p style="margin: 0;">This paper, published in May 2024, proposes a novel MoST learning framework via self-supervised learning, namely MoSSL, which aims to uncover latent patterns from temporal, spatial, and modality perspectives while quantifying dynamic heterogeneity. Experiment results on two real-world MoST datasets verify the superiority of this approach compared with the state-of-the-art baselines.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/pdf/2405.03255"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/pdf/2405.03255</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/spatio-remporal_field_neural_networks_for_air_quality.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Spatio-Temporal Field Neural Networks for Air Quality Inference</p>
        <p style="margin: 0;">This paper, published in June 2024, highlights the limitation of graph neural networks and makes a first effort to combine two different spatiotemporal perspectives.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/pdf/2403.02354"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/pdf/2403.02354</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/weather_impact_on_social_medial.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Worse Weather Amplifies Social Media Activity</p>
        <p style="margin: 0;">This paper, published in February 2025, highlights if environmental factors alter rates of online social activity. The study was performed in the U.S.A. using Facebook and X (Twitter) data with over 3.5 billion posts. They found that extreme temperatures and added precipitation each independently amplified social media activity, effects that persisted within individuals. Compounded weather extremes produced markedly larger increases in social media activity.</p>
        <p style="margin: 0;"><a href="https://journals.sagepub.com/doi/10.1177/09567976241306099"><i class="fa-regular fa-file-pdf"></i>https://journals.sagepub.com/doi/10.1177/09567976241306099</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/classical_stratification_for_disease_spreading.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">A Mathematical, Classical Stratification Modeling Approach to Disentangling the Impact of Weather on Infectious Diseases: A Case Study Using Spatio-Temporally Disaggregated Campylobacter Surveillance Data for England and Wales</p>
        <p style="margin: 0;">This paper, published in Jan 2024, disentangling the impact of the weather on transmission of infectious diseases is crucial for health protection, preparedness, and prevention while using campylobacteriosis, a bacterial food disease, as a case study where they developed a novel conditional incidence method based on classical stratification. The predicted incidence of campylobacteriosis increased by 1 case per million people for every 5° (Celsius) increase in temperature within the range of 8°-15°.</p>
        <p style="margin: 0;"><a href="https://pubmed.ncbi.nlm.nih.gov/38236828/"><i class="fa-regular fa-file-pdf"></i>https://pubmed.ncbi.nlm.nih.gov/38236828/</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/comparative_eval_of_point_process_forecasts.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Comparative Evaluation of Point Process Forecasts</p>
        <p style="margin: 0;">This paper, published in July 2023, performs a comparative study. It adapts the concept of consistent scoring functions and proper scoring rules, which are statistically principled tools for the comparative evaluation of predictive performance, to the point process setting and places both new and existing methodology in their framework for a case study on a simulation operational earthquake forecast for Italy.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/pdf/2103.11884"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/pdf/2103.11884</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/DKMPP.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Integration-free Training for Spatio-temporal Multimodal Covariate Deep Kernel Point Processes</p>
        <p style="margin: 0;">This paper, published in November 2023, proposes a novel deep spatio-temporal point process model, Deep Kernel Mixture Point Processes (DKMPP), that incorporates multimodal covariate information, utilizes an integration-free method based on score matching, and improves efficiency by adopting a scalable denoising score matching method.</p>
        <p style="margin: 0;"><a href="https://openreview.net/pdf?id=Yvpenkym8A"><i class="fa-regular fa-file-pdf"></i>https://openreview.net/pdf?id=Yvpenkym8A</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/maya_okawa_multi_modal_model_paper.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Deep Mixture Point Processes: Spatio-temporal Event Prediction with Rich Contextual Information</p>
        <p style="margin: 0;">This paper, published in June 2021, proposes DMPP (Deep Mixture Point Processes), a point process model for predicting spatio-temporal events with the use of rich contextual information; it incorporates heterogeneous and high-dimensional context available in image and text data. They design the intensity of their point process model as a mixture of kernels, where the mixture weights are modeled by a deep neural network. This allows to automatically learn the complex nonlinear effects of the contextual factors on event occurrence.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/pdf/1906.08952"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/pdf/1906.08952</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/DeepSTPP.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Neural Point Process for Learning Spatiotemporal Event Dynamics</p>
        <p style="margin: 0;">This paper, published in 2023, proposes Deep Spatiotemporal Point Process (DeepSTPP), a deep dynamics model that integrates spatiotemporal point processes. This method can accurately forecast irregularly sampled events over space and time. The key construction is the nonparametric space-time intensity function, governed by a latent process. They used synthetic and real-world data.</p>
        <p style="margin: 0;"><a href="https://proceedings.mlr.press/v168/zhou22a/zhou22a.pdf"><i class="fa-regular fa-file-pdf"></i>https://proceedings.mlr.press/v168/zhou22a/zhou22a.pdf</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/goodness_of_fit_test_paper_500_500.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Goodness-Of-Fit Tests for Spatial Point Processes: A Review</p>
        <p style="margin: 0;">This paper, published in 2025, the state-of-the-art for goodness-of-fit testing for spatial point processes is summarized. Test statistics based on classical functional summary statistics and recent contributions from topological data analysis are considered.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/pdf/2501.03732v1"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/pdf/2501.03732v1</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/Agricultural insecticides.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Agricultural Insecticides Threaten Surface Waters at the Global Scale</p>
        <p style="margin: 0;">This study reveals that agricultural insecticides are contaminating surface waters worldwide at levels that pose significant risks to aquatic biodiversity. The research highlights that current regulatory thresholds are often exceeded, leading to substantial declines in aquatic invertebrate populations.</p>
        <p style="margin: 0;"><a href="https://www.pnas.org/doi/10.1073/pnas.1500232112"><i class="fa-regular fa-file-pdf"></i>https://www.pnas.org/doi/10.1073/pnas.1500232112</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/flood events.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Large Floods Drive Changes in Cause-Specific Mortality in the United States</p>
        <p style="margin: 0;">Analyzing 35.6 million U.S. death records from 2001 to 2018, this study finds that large floods are associated with increased mortality from cardiovascular and infectious diseases, as well as injuries. The research underscores the need for effective public health responses to flooding events.</p>
        <p style="margin: 0;"><a href="https://www.nature.com/articles/s41591-024-03358-z"><i class="fa-regular fa-file-pdf"></i>https://www.nature.com/articles/s41591-024-03358-z</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/Hot_classroom.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Exposure to Heat and Student Cognitive Functioning</p>
        <p style="margin: 0;">This paper examines the impact of heat exposure on student cognitive performance, revealing that higher temperatures negatively affect test scores, particularly among minority and low-income students. The findings suggest that climate change could exacerbate educational inequalities.</p>
        <p style="margin: 0;"><a href="https://yabogv.github.io/research/heat_executive_function/"><i class="fa-regular fa-file-pdf"></i>https://yabogv.github.io/research/heat_executive_function/</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/prior vae.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">PriorVAE: Encoding Spatial Priors with VAEs for Small-Area Estimation</p>
        <p style="margin: 0;">PriorVAE introduces a novel approach to spatial modeling by using variational autoencoders to approximate Gaussian process priors. This method enables efficient Bayesian inference for small-area estimation tasks, reducing computational complexity while maintaining accuracy.</p>
        <p style="margin: 0;"><a href="https://arxiv.org/pdf/2110.10422"><i class="fa-regular fa-file-pdf"></i>https://arxiv.org/pdf/2110.10422</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/GPR.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Geographical Gaussian Process Regression: A Spatial Machine-Learning Model Based on Spatial Similarity</p>
        <p style="margin: 0;">This paper presents a spatial machine-learning model that integrates geographical Gaussian process regression with spatial similarity measures. The approach enhances predictive performance in spatial data analysis by accounting for spatial dependencies and similarities.</p>
        <p style="margin: 0;"><a href="https://onlinelibrary.wiley.com/doi/10.1111/gean.12423"><i class="fa-regular fa-file-pdf"></i>https://onlinelibrary.wiley.com/doi/10.1111/gean.12423</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/airstrike.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Causal Inference with Spatio-Temporal Data: Estimating the Effects of Airstrikes on Insurgent Violence in Iraq</p>
        <p style="margin: 0;">This paper develops a novel framework for estimating causal effects in complex spatio-temporal settings. Focusing on U.S. airstrikes in Iraq between 2007 and 2008, the authors introduce a method combining Bayesian nonparametric modeling with a potential outcomes approach to account for interference and spatial spillover effects. Their analysis reveals that airstrikes significantly reduced insurgent violence locally, but also induced short-term increases in violence in nearby regions, illustrating the nuanced and dynamic impact of military interventions over space and time.</p>
        <p style="margin: 0;"><a href="https://academic.oup.com/jrsssb/article/84/5/1969/7072904?login=false"><i class="fa-regular fa-file-pdf"></i>https://academic.oup.com/jrsssb/article/84/5/1969/7072904?login=false</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/Connection between climatic change and international food prices.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Connection between climatic change and international food prices: evidence from robust long-range cross-correlation and variable-lag transfer entropy with sliding windows approach</p>
        <p style="margin: 0;">This paper investigates how fluctuations in the North Atlantic Oscillation (NAO) index, a key climate indicator, affect global food prices. Utilizing advanced statistical methods, including a robust bivariate Hurst exponent and variable-lag transfer entropy within a sliding windows framework, the study analyzes daily data from January 2020 to May 2022. The findings reveal significant positive correlations and causal relationships between NAO index changes and price fluctuations in major agricultural commodities such as corn, wheat, soybeans, and oats, across both short- and long-term periods. These results suggest that the NAO index can serve as a predictive factor for international food price movements, offering valuable insights for policymakers aiming to enhance food security amidst climate variability.</p>
        <p style="margin: 0;"><a href="https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-024-00482-1"><i class="fa-regular fa-file-pdf"></i>https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-024-00482-1</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/Bayesian neural fields.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Scalable spatiotemporal prediction with Bayesian neural fields</p>
        <p style="margin: 0;">This paper introduces Bayesian Neural Fields (BayesNF), a statistical model designed for analyzing large-scale spatiotemporal datasets. BayesNF combines deep neural networks with hierarchical Bayesian inference to provide accurate predictions and robust uncertainty quantification. The model has demonstrated improved performance over existing methods in tasks such as forecasting and interpolation across various domains, including climate science and public health. An open-source software implementation is available, optimized for GPU and TPU accelerators via the JAX machine learning platform.</p>
        <p style="margin: 0;"><a href="https://www.nature.com/articles/s41467-024-51477-5"><i class="fa-regular fa-file-pdf"></i>https://www.nature.com/articles/s41467-024-51477-5</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/Bayesian COVID19.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">A Bayesian machine learning approach for spatio-temporal prediction of COVID-19 cases</p>
        <p style="margin: 0;">This paper presents a model that integrates neural networks within a Bayesian framework to predict COVID-19 case numbers across different regions and time periods. By incorporating factors such as human mobility, spatial proximity, and temporal correlations, the model effectively captures the complex dynamics of disease spread. Applied to data from 245 health zones in Castilla-Leon, Spain, the approach demonstrates strong predictive performance, highlighting the significant influence of human movement and neighboring infection rates on COVID-19 transmission.</p>
        <p style="margin: 0;"><a href="https://link.springer.com/article/10.1007/s00477-021-02168-w#"><i class="fa-regular fa-file-pdf"></i>https://link.springer.com/article/10.1007/s00477-021-02168-w#</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/DNNST.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Comparison of Deep Neural Networks and Deep Hierarchical Models for Spatio-Temporal Data</p>
        <p style="margin: 0;">This paper examines the strengths and limitations of two modeling approaches for complex spatio-temporal processes. It contrasts hierarchical dynamic spatio-temporal models (H-DSTMs), which offer interpretability and uncertainty quantification but can be computationally intensive, with deep neural networks, known for their flexibility and scalability but often lacking probabilistic frameworks. The study explores hybrid models that integrate elements from both paradigms, aiming to leverage their respective advantages for improved modeling of high-dimensional, nonlinear spatio-temporal data.</p>
        <p style="margin: 0;"><a href="https://link.springer.com/article/10.1007/s13253-019-00361-7"><i class="fa-regular fa-file-pdf"></i>https://link.springer.com/article/10.1007/s13253-019-00361-7</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>
<!-- STOP -->
</div>
