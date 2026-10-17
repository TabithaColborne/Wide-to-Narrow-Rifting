# Numerical Experiment Scripts
Used in my Honours thesis: Thermomechanical Controls on the Transition from Wide to Narrow Continental Rifting 

## Overview 
This repository contains the python scripts used to run geodynamic experiments testing the transition from wide to narrow continental rifting using the Underworld 2 framework (https://doi.org/10.5281/zenodo.10976370).

These experiments explore the effect of varying the temperature of the geotherm, material strength/rheology, and extension velocity/strain rate. All experiments are based on the Reference Experiment, where a brief summary of each experiment is provided below:

| Experiment  | Key Model Constraints |
| ------------- | ------------- |
| Reference Experiment  | 780° C Moho, 2cm/yr extension, wet flow law assigned to all layers  |
| T700  | Low temperature geotherm endmember (700° C at Moho) |
| T900 | High temperature geotherm endmember (900° C at Moho) |
| EX1 | Low strain rate end member (1cm/yr extension) |
| EX4 | High strain rate end member (4cm/yr extension) |
| SLCSM | Strong lower crust, strong mantle |
| SCSM | Strong crust, strong mantle |
| SCWM | Strong crust, weak mantle |

## Visualisation
Post-processing and visualisation of model outputs was accomplished using open-source software ParaView.
