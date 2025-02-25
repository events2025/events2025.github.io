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
      <img src="/assets/images/thumb/neural_spatiotemporal_point_processes_trends_and_challenges.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Neural Spatiotemporal Point Processes: Trends and Challenges</p>
        <p style="margin: 0;">This paper, published in Febraury 2025 discusses STPPs, probabilistic models for events occurring in continuous space and time; they categorize existing approaches, unify key design choices, explain the challenges of working with this data modality, identify open challenges, and gaps in the litreature. They describe the applications possible in various datasets, such as natural disasters, crimes, and traffic.</p>
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
        <p style="margin: 0;">This paper, published in August 2021 discusses Neural TPPs, for merging for combining deep learning with Temporal Point Process models. They focus on design choices for this topic, applications and datasets such as earthquake occurrences; they discuss the open challenges such as the lack of standardized experimental setups and high-quality benchmark datasets whcih makes a problematic challenege for the comparison of different neural TPP architectures</p>
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
        <p style="margin: 0;">This paper, published in December 2024 discusses Neural TPPs, this paper mainly focuses on the temporal point process using deep learning</p>
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
        <p style="margin: 0;">This paper, published in November 2016 provides a review describing statistical models and methods for spatio-temporal data. They define characteristics and statistics to uniquely characterise certain spatio-temporal point processes</p>
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
        <p style="margin: 0;">This paper, published in August 2018 the basic theory, survey related estimation and inference techniques, highlights several key applications, and suggests directions for future research. and highlights self-exciting models when spatio-temporal point process can be divided into clusters of events triggered by common causes </p>
        <p style="margin: 0;"><a href="https://surl.li/oekoqa"><i class="fa-regular fa-file-pdf"></i>https://surl.li/oekoqa</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>

<div style="display: flex; justify-content: space-between; align-items: stretch; margin-bottom: 20px;">
    <div style="display: flex; align-items: stretch;">
      <img src="/assets/images/thumb/statistical_deep_learning_for_spatial_and_spatiotemporal_data.jpg" alt="Logo" style="width: 100px; height: 100px; margin-right: 20px;">
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <p style="margin: 0; color: purple; font-size: 1.3em; font-weight: bold;">Statistical deep learning for spatial and spatiotemporal data</p>
        <p style="margin: 0;">This paper, published 2023 provides a review on traditional and machine learning spatial and spatial-temporal data with focus on variety of hybrid models that integrate statistical models with deep learning models and give an overview of computational technologies that proven useful</p>
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
        <p style="margin: 0;">This paper, published september 2024 provides background on major aspects of Hawkes processes with focus on simulations methods and estimation techniques among overview of stochastic processes and the challenges of Hawkes processes.</p>
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
        <p style="margin: 0;">This paper, published December 2024, explains that during disruptions like pandemics, business closures affect not just the businesses themselves but also people's movements, which then impacts other businesses. The study uses data from five US cities to measure how businesses depend on each other. It finds that behavior-based relationships improve predictions of business resilience by about 40% compared to distance-based models. Ignoring these relationships can lead to underestimating the spread of disruptions. The research highlights the need to understand human mobility patterns to boost urban economic resilience.</p>
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
        <p style="margin: 0;">This paper, published July 2024, highlights the impact of conflict events on the incidence of child marriage. They used georeferenced data on armed conflict and population-level microdata for marriages of more than 2 million women across 56 countries to estimate the impact of the occurrence and severity of conflict events in or before the year of marriage on the incidence of child marriage. </p>
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
        <p style="margin: 0;">This paper, published Jan 2022, discusses how armed conflict influence tropical forest loss. In this study they propose a class of causal models for spatio-temporal stochastic processes which allows to formally define and quantify the causal effects. </p>
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
        <p style="margin: 0;">This paper, published May 2024, proposes a novel MoST learning framework via Self-Supervised Learning, namely MoSSL, which aims to uncover latent patterns from temporal, spatial, and modality perspectives while quantifying dynamic heterogeneity. Experiment results on two real-world MoST datasets verify the superiority of this approach compared with the state-of-the-art baselines.</p>
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
        <p style="margin: 0;">This paper, published Jun 2024, highlights the limitation of graph neural netowkr and made a first effort to to combine two different spatio-temooral prespective.</p>
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
        <p style="margin: 0;">This paper, published February 2025, highlights if environmental factors alter rates of online social activity, the study was performed on the U.S.A using Facebook and X (twitter) data with over 3.5 billion posts. They found that extreme temperatures and added precipitation each independently amplified social-media activity, effects that persisted within individuals. Compounded weather extremes produced markedly larger increases in social-media activity. </p>
        <p style="margin: 0;"><a href="https://journals.sagepub.com/doi/10.1177/09567976241306099"><i class="fa-regular fa-file-pdf"></i>https://journals.sagepub.com/doi/10.1177/09567976241306099</a> </p>
      </div>
    </div>
    <!-- <div style="color: lightgray; align-self: flex-start; margin-left: 10px; white-space: nowrap; font-size: 200%;">2022</div>  -->
  </div>
<!-- STOP -->
</div>
