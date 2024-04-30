# GPT2-PDFs-Summarizers Transformers Project

This project utilizes the GPT2 library for natural language processing tasks.

## Overview

The project includes functions for reading different file types, loading datasets, training language models, and generating text using pre-trained models.

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:dirias/GPT2-PDFs-Summarizers.git
   cd GPT2-PDFs-Summarizers

2. Install requirements
 
   ```bash
   pip install -r requirements.txt

3. Start streamlit app
 
   ```bash
   streamlit run app.py

## Interface

### Training Screen

In this screen, you can upload PDFs to train the model, the PDF will be converted into text and tokenized using GPT2Tokenizer library.

![image](https://drive.google.com/uc?export=view&id=15TxsGZ9ldwFRXgYeIBdU16Z5WSszrTIh)

### Chat Screen

Based on the training data, the GPT will be able to answer questions using the trained dataset.

![image](https://drive.google.com/uc?export=view&id=1p5fSAAB-5DF7vST-ZElVKuj8nLlJ0nsn)

# Usage


#License
This project is licensed under the MIT License - see the LICENSE file for details.