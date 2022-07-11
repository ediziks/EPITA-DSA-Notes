import streamlit as st
import tensorflow_text as text
import tensorflow_hub as hub
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image
import shutil
import pickle
import datetime
import os.path


# Descriptions
st.title("Spam Message Detector")
image = Image.open('inspectorGadget.jpeg')
st.image(image)
st.subheader("An NLP model on top of BERT to detect spam messages")
st.subheader('Spam Samples: ')
st.write('1. URGENT! Your Mobile number has been awarded with a £5000 prize GUARANTEED. Call 080738278496 from land line. Claim 3030. Valid 12hrs only 150ppm')
st.write('2. Please call our customer service representative on 0923 876 0789 between 9am-10pm as you have WON a guaranteed £1000 cash or £5000 prize!')
st.write('3. You are awarded a Canon Digital Camera! call 09061221061 from landline. Delivery within 28days. T Cs Box177. M221BP. 2yr warranty. p£5.99')

# text input
plain_text = st.text_input('Enter your message and press Enter to predict')

# load data
df_first = pd.read_csv('./spam_data.csv')
# rearrange the columns
df_first.drop(columns=df_first.columns[0], axis=1, inplace=True)
# rename columns
df_first = df_first.rename({'target': 'Category', 'text': 'Message'}, axis=1)
# creating 2 new dataframe as df_hm , df_spm
df_spm = df_first[df_first['Category']=='spam']
df_hm = df_first[df_first['Category']=='ham']
# dataframe downsampling to process easily
df_hm_downsampled = df_hm.sample(df_spm.shape[0])
# join two datasets
df_simplified = pd.concat([df_spm , df_hm_downsampled])
# encoding the Category column to num values
df_simplified['spam'] = df_simplified['Category'].apply(lambda x:1 if x=='spam' else 0)
# test/train split
X_train, X_test , y_train, y_test = train_test_split(df_simplified['Message'], df_simplified['spam'], stratify = df_simplified['spam'])

if plain_text:
    if not os.path.isfile('./model.h5'):
        with st.spinner('New model is training, it could take up to 10mins... See the details in the command line.'):
            print('MODEL IS TRAINING')
            # get the BERT model
            bert_pre_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3'
            bert_enc_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4'
            bert_preprocessor = hub.KerasLayer(bert_pre_url)
            bert_encoder = hub.KerasLayer(bert_enc_url)
            text_inp = tf.keras.layers.Input(shape = (), dtype = tf.string, name = 'Inputs')
            text_preprocessed = bert_preprocessor(text_inp)
            embedded = bert_encoder(text_preprocessed)
            dropout = tf.keras.layers.Dropout(0.1, name='Dropout')(embedded['pooled_output'])
            outputs = [tf.keras.layers.Dense(1, activation='sigmoid', name='Dense')(dropout)]
            inputs = [text_inp]
            # prepare the latest model
            model = tf.keras.Model(inputs=inputs, outputs=outputs)
            model.compile(optimizer='adam',
                        loss='binary_crossentropy',
                        metrics=[tf.keras.metrics.BinaryAccuracy(name = 'accuracy'),
                                tf.keras.metrics.Precision(name = 'precision'),
                                tf.keras.metrics.Recall(name = 'recall')
                                ])

            # delete if logs folder exist
            if os.path.isdir('./logs'):
                shutil.rmtree('./logs/')
            # create logs to improve further epochs
            log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            tensor_call_back=[tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)]
            with tf.device('/cpu:0'):
                # model fitting
                keras_history = model.fit(X_train, y_train, epochs=3, callbacks=tensor_call_back)
            with tf.device('/cpu:0'):
                # performance evaluation
                model.evaluate(X_test,y_test)
            # save the model into the directory
            pickle.dump(model, open('model.h5', 'wb'))
            model.save('./model.h5')
    else:
        print('MODEL IS LOADING...')
        # read the model if saved
        with st.spinner('Model is loading. Please Wait...'):
            model = tf.keras.models.load_model('./model.h5', custom_objects={'KerasLayer': hub.KerasLayer})

    # get the text and show the result
    text_to_be_predicted = [plain_text]
    with tf.device('/cpu:0'):
        predict_result = model.predict(text_to_be_predicted)
    output = np.where(predict_result>0.5,'spam', 'ham')
    output = 'Spam' if predict_result>0.5 else 'Ham'
    st.warning(f'This message is likely to be a {output}')
    st.warning(f'Spam percentage is {predict_result[0][0]}')

    if st.button('Get model accuracy'):
        with st.spinner('Getting model accuracy...'):
            st.write('Accuracy might differ slightly due to random train test split on each run')
            with tf.device('/cpu:0'):
                st.write(f'Model accuracy is: ', model.evaluate(X_test, y_test)[1])
