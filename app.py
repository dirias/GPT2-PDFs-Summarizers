import streamlit as st
import re
import model
import os

# Streamlit UI
st.title("PDF to AI Bot")

# Create a sidebar with train and ask options
selected_tab = st.sidebar.radio("Select Operation", ["Train", "Ask"])

if selected_tab == "Train":
    st.header("Training the QA Model")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        train_file_path = "PDFs"
        os.makedirs(train_file_path, exist_ok=True)
        pdf_file_path = os.path.join(train_file_path, "uploaded_file.pdf")
        # Save uploaded file
        with open(pdf_file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success("File uploaded successfully!")

        # Tokenization and Fine-Tuning
        text_data = model.read_documents_from_directory(train_file_path)
        text_data = re.sub(r'\n+', '\n', text_data).strip()
        with open("train.txt", "w") as f:
            f.write(text_data)

        model_name = 'gpt2'
        output_dir = './custom_q_and_a'
        overwrite_output_dir = False
        per_device_train_batch_size = 8
        num_train_epochs = 10
        save_steps = 50000

        # Train
        model.train(
            train_file_path='train.txt',
            model_name=model_name,
            output_dir=output_dir,
            overwrite_output_dir=overwrite_output_dir,
            per_device_train_batch_size=per_device_train_batch_size,
            num_train_epochs=num_train_epochs,
            save_steps=save_steps
        )

        st.success("Fine-tuning completed!")

elif selected_tab == "Ask":
    st.header("Ask a Question")

    question = st.text_input("Enter your question:")

    if st.button("Get Answer"):

        # Extract and display the answer
        model1_path = "."
        amax_len = 150
        answer = model.generate_text('./custom_q_and_a', question, amax_len)

        st.subheader("Answer:")
        print('Answer:\n', answer)
        st.text_area(" ", value='\n'.join(answer.split('\n')[1:]), height=250, disabled=False)
