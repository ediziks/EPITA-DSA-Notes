# from random import random
# import streamlit as st 
# import numpy as np 

# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn.model_selection import train_test_split

# from sklearn.decomposition import PCA
# from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier

# from sklearn.metrics import accuracy_score


# st.title('DSP ML APP')

# st.write("""
# # Select options on the left and then press 'Predict' to train the model
# """)

# dataset_name = st.sidebar.selectbox(
#     'Select Dataset',
#     ('Iris', 'Breast Cancer', 'Wine')
# )

# classifier_name = st.sidebar.selectbox(
#     'Select classifier',
#     ('KNN', 'SVM', 'Random Forest', 'DecisionTree')
# )

# def get_dataset(name):
#     data = None
#     if name == 'Iris':
#         data = datasets.load_iris()
#     elif name == 'Wine':
#         data = datasets.load_wine()
#     else:
#         data = datasets.load_breast_cancer()
#     X = data.data
#     y = data.target
#     return X, y

# X, y = get_dataset(dataset_name)

# def add_parameter_ui(clf_name):
#     params = dict()
#     if clf_name == 'SVM':
#         C = st.sidebar.slider('C', 0.01, 10.0)
#         params['C'] = C
#     elif clf_name == 'KNN':
#         K = st.sidebar.slider('K', 1, 15)
#         params['K'] = K
#     elif clf_name == 'DecisionTree':
#         max_depth_dt = st.sidebar.slider('max_depth', 2, 15)
#         params['max_depth_dt'] = max_depth_dt
#     else:
#         max_depth = st.sidebar.slider('max_depth', 2, 15)
#         params['max_depth'] = max_depth
#         n_estimators = st.sidebar.slider('n_estimators', 1, 100)
#         params['n_estimators'] = n_estimators
#     return params

# params = add_parameter_ui(classifier_name)

# def get_classifier(clf_name, params):
#     clf = None
#     if clf_name == 'SVM':
#         clf = SVC(C=params['C'])
#     elif clf_name == 'KNN':
#         clf = KNeighborsClassifier(n_neighbors=params['K'])
#     elif clf_name == 'DecisionTree':
#         clf = DecisionTreeClassifier(criterion='entropy', random_state=1234, max_depth=params['max_depth_dt'])
#     else:
#         clf = clf = RandomForestClassifier(n_estimators=params['n_estimators'], 
#             max_depth=params['max_depth'], random_state=1234)
#     return clf

# clf = get_classifier(classifier_name, params)

# def predict_config():
#     st.write(f"## {dataset_name} Dataset")
#     st.write('Shape of dataset:', X.shape)
#     st.write('Sum of null values in datset: ', np.sum(np.isnan(X)))
#     st.write('number of classes:', len(np.unique(y)))

#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)

#     acc = accuracy_score(y_test, y_pred)

#     st.write(f'Classifier = {classifier_name}')
#     st.write(f'Accuracy =', acc)

#     #### PLOT DATASET ####
#     pca = PCA(2)
#     X_projected = pca.fit_transform(X)

#     x1 = X_projected[:, 0]
#     x2 = X_projected[:, 1]

#     fig = plt.figure()
#     plt.scatter(x1, x2,
#             c=y, alpha=0.8,
#             cmap='viridis')

#     plt.xlabel('Principal Component 1')
#     plt.ylabel('Principal Component 2')
#     plt.colorbar()

#     # show the plot
#     st.pyplot(fig)

# if st.sidebar.button('Predict'):
#     predict_config()


import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import random



# import data file csv
# df = pd.read_csv('merc.csv')
file = st.file_uploader(label='', accept_multiple_files=False, type='csv')
if file is not None:
    st.write(f'{file} is uploaded')
    # df = pd.read_csv(file.read())
    df = pd.read_csv(file)
    st.write(f'{df.info()}')
# set page title
# st.set_page_config('Mercedes Price Prediction App')


st.title('Mobile Phone Prediction with ML')
# social_acc = ['About', 'Kaggle', 'Medium', 'LinkedIn']
# social_acc_nav = st.sidebar.selectbox('About', social_acc)
# if social_acc_nav == 'About':
#     st.sidebar.markdown("<h2 style='text-align: center;'> Sarvesh Kishor Talele</h2> ", unsafe_allow_html=True)
#     st.sidebar.markdown('''---''')
#     st.sidebar.markdown('''
#     • Data Analytics (Python/SQL/Tableau) \n 
#     • Industrial Robotics (KUKA Robots) \n 
#     • Interned as a Data Engineer''')
#     st.sidebar.markdown("[ Visit Google Scholar Account](https://scholar.google.com/citations?user=-4Vyig8AAAAJ&hl=en)")

# elif social_acc_nav == 'Kaggle':
#     st.sidebar.image('kaggle.jpg')
#     st.sidebar.markdown("[Kaggle](https://www.kaggle.com/sarveshtalele)")

# elif social_acc_nav == 'Medium':
#     st.sidebar.image('medium.jpg')
#     st.sidebar.markdown("[Click to read my blogs](https://wyverical.medium.com/)")

# elif social_acc_nav == 'LinkedIn':
#     st.sidebar.image('linkedin.jpg')
#     st.sidebar.markdown("[Visit LinkedIn account](https://www.linkedin.com/in/sarvesh-talele-320356196/)")

menu_list = ['Exploratory Data Analysis', "Predict Price"]
menu = st.radio("Menu", menu_list)

# if menu == 'Exploratory Data Analysis':
#     st.title('Exploratory Data Analysis of Mercedes Benz Car Models ')

#     if st.checkbox("View data"):
#         st.write(df)

#     st.video("https://youtu.be/YlBAKiUnp_Q")
#     st.markdown('---')
#     st.markdown("<h2 style='text-align: center;'> The Deduction Show!</h2>", unsafe_allow_html=True)
#     st.markdown('---')
#     st.markdown("<h3 style='text-align: left;'> Visualisation and Analysis</h3>", unsafe_allow_html=True)
#     st.markdown("<h4 style='text-align: left;'> A) Model v/s Miles per gallon</h4>", unsafe_allow_html=True)
#     st.image('model_mpg.jpg')
#     st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
#     st.markdown('''
#     The objective for using the mean of all data is to show overall performance of automobile models in terms of
#      miles per gallon. We may derive the following assertions from the data provided:\n
#     1. There are about **15** automobile models that get a higher miles per gallon than the average.\n
#     2. In terms of miles per gallon, the E class vehicle outperforms the G class model by more than **5.4 percent**.\n
#     3. When the miles/gallon mean value is greater, the automobile can drive **further** than when the mean value
#      is lower.\n
#     4. It may also be deduced that the mercedes automobile models which are above average value **emits less** carbon 
#     dioxide when compared to other models''')

#     st.markdown("<h4 style='text-align: left;'> B) Model v/s Mileage </h4>", unsafe_allow_html=True)
#     st.image('model_mileage.jpg')
#     st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
#     st.markdown('''
#     1.   According to the median of the statistics, more than 11 Mercedes model automobiles had better mileage
#      performance.
#     2.   However, when compared to the median value of our data, the Mercedes 
#     CLK model has approximately **12.51%** higher miles, and altogether, the CLK model delivers
#      **15.67%** mileage to the dataset.
#     3.  Subsequently, an overall fuel consumption of CLK model is 3265.30 gallons at 33.6 miles per gallon. 
#     4.  Hence, we can deduce that car models with higher mpg value has following applications 
#     - Fuel consumption is reduced.
#     -  Lower Maintenance Costs
#     ''')

#     st.markdown("<h4 style='text-align: left;'> C)  Model v/s Price </h4>", unsafe_allow_html=True)
#     st.image('model_price.jpg')

#     st.markdown("<h4 style='text-align: left;'>D)  Year v/s Price  </h4>", unsafe_allow_html=True)
#     st.image('year_price.jpg')

#     st.markdown("<h4 style='text-align: left;'> E) Mileage v/s Transmission </h4>", unsafe_allow_html=True)
#     st.image('mileage_transmission.jpg')
#     st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
#     st.markdown('''
#     1.  Manual Transmission has the most mileage of the three most recent transmission systems when compared 
#     to the other transmission systems.
#     - Manual transmissions include more gears and a simpler design, resulting in a lighter transmission system.
#     - A simpler design decreases the car's annual fuel consumption and, as a result, the cost of maintenance.
#     2.   The other category may include the following transmission systems (these are some of the examples 
#     of transmission system)
#     - **Tiptronic Transmission :**
#     A tiptronic is a type of automatic transmission that allows for fully automatic gear shifting or manual
#     gear shifting by the driver. Tiptronics use a torque converter rather than a clutch.
#     - **Dual Clutch Transmission (DCT) :**
#     A dual clutch transmission has two gear shafts with a clutch for each. The dual system allows for 
#     faster and smoother gear changes.
#     ''')

#     st.markdown("<h4 style='text-align: left;'> F) Model v/s Tax </h4>", unsafe_allow_html=True)
#     st.image('model_tax.jpg')
#     st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
#     st.markdown(''' **Road Tax Description**: \n
#     1. It is a tax that must be paid by anybody who purchases a car. The Road Tax is a 
#     state-level tax, meaning that it is imposed at the state level by the governments of several states.
#     2. For charging the road tax, each state has its own set of rules and regulations. 
#     The amount of tax varies due to the varied percentages charged by different states. 
#     According to the Central Motor Vehicles Act, if a vehicle is operated for more than a year, 
#     the entire amount of road tax must be paid at once. 
#     3. Individuals purchasing a vehicle pay the road tax which is based on the ex-showroom price of the vehicle. 
#     The calculation of road tax depends on these following things:\n
#     a. Seating capacity of the vehicle \n
#     b. Engine capacity of the vehicle \n
#     c. Age of the vehicle \n
#     d. Weight of the Vehicle \n
#     *Note: This is according to Indian Rules and Regulations* \n
#     **Analysis** \n
#     1. Although the Mercedes C class has more advanced built-in technology, making 
#     the C class interface more user-friendly, it has a far higher road tax than the Mercedes A class, by 9.29 percent.\n
#     2. When it comes to miles per gallon and price, an A class vehicle would be a better choice than a C class model.\n
# ''')

#     st.markdown("<h4 style='text-align: left;'> G) Fueltype v/s Mileage </h4>", unsafe_allow_html=True)
#     st.image('mileage_fuel.jpg')
#     st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
#     st.markdown('''
#     1. For long distance travel, diesel engines are recommended. For those who are Hodophile, 
#     Mercedes automobile models with Diesel engines have a 79 percent probability of being their first preference. 
#     2.  Diesel engines are limited for vehicles that have a high frequency of travel, such as trucks, buses, 
#     and off-road vehicles, despite having higher efficiency and lower costs than petroleum. 
#     Because of the increased green house gases, 
#     diesel engines are limited for vehicles that have a high frequency of travel, such as trucks, buses, and 
#     off-road vehicles.
#     ''')

#     st.markdown("<h2 style='text-align: left;'> Conclusion </h2>", unsafe_allow_html=True)
#     st.markdown('''
#     The deduction and statistical analysis determined with the full consideration of metrics of Mercedes 
#     Model cars using the dataset. 
#     The notebook have explored Transmission, Miles/gallon, Mileage and road tax metrics for better 
#     comprehension of our dataset.  \n
#     1. For those who want to buy a car for travel or daily use, the miles per gallon number should 
#     be greater than 30 mpg.\n
#     2. Mileage is another element that influences a vehicle's fuel usage. The cost of maintaining a car 
#     is determined by its mileage.\n
#     3. Manual transmissions have more gears and a simpler design, making them lighter.\n
#     4. Diesel engines are restricted for vehicles that travel often, such as
#  t  rucks, buses, and off-road vehicles, due to higher greenhouse gas emissions.''')

# elif menu == 'Predict Price':

# model_dic = {'a class': 0, 'b class': 1, 'c class': 2, 'cl class': 3, 'cla class': 4, 'clc class': 5, 'clk': 6,
#                 'cls class': 7, 'e class': 8, 'g class': 9, 'gl class': 10, 'gla class': 11, 'glb class': 12,
#                 'glc class': 13, 'gle class': 14, 'gls class': 15, 'm class': 16, 'r class': 17, 's class': 18,
#                 'sl class': 19, 'slk': 20, 'v class': 21, 'x-class': 22}
# transmission_dic = {'automatic': 0, 'manual': 1, 'other': 2, 'semi-auto': 3}
# fuel_dic = {'diesel': 0, 'hybrid': 1, 'other': 2, 'petrol': 3}

# model_list = [
#     "a class", "b class", "c class", "cl class", "cla class", "clc class", "clk", "cls class", "e class", "g class",
#     "gl class", "gla class", "glb class", "glc class", "gle class", "gls class", "m class", "r class", "s class",
#     "sl class", "slk", "v class", "x-class"]
# transmission_list = ['automatic', 'manual', 'other', 'semi-auto']
# fuel_list = ['diesel', 'hybrid', 'other', 'petrol']

# year = st.slider("Enter the year", 1970, 2021)

# engine_size = st.number_input('Enter Engine Size  (range = 0 - 7)')

# model_choice = st.selectbox(label='Select your favourite Car Model', options=model_list)
# models = model_dic[model_choice]

# transmission_choice = st.selectbox(label=' Select the Transmission type', options=transmission_list)
# transmissions = transmission_dic[transmission_choice]

# fuel_choice = st.selectbox(label='Select the Fuel type', options=fuel_list)
# fuels = fuel_dic[fuel_choice]

battery_power = st.slider('Battery Power', 501.0, 1998.0)
blue = st.checkbox('Bluetooth')
clock_speed = st.slider('Clock Speed', 0.5, 3.0)
dual_sim = st.checkbox('Dual SIM')
fc = st.slider('Front Camera Resolution (MP)', 0.0, 19.0)
four_g = st.checkbox('4G')
int_memory = st.slider('Internal Memory (GB)', 2.0, 64.0)
m_dep = st.slider('Mobile Depth (cm)', 0.1, 1.0)
mobile_wt = st.slider('Mobile Weight (gr)', 80.0, 200.0)
n_cores = st.slider('Number of Cores', 1.0, 8.0)
pc = st.slider('Primary Camera Resolution (MP)', 0.0, 20.0)
px_height = st.slider('Pixel Height (px)', 0.0, 1960.0)
px_width = st.slider('Pixel Width (px)', 500.0, 1998.0)
ram = st.slider('RAM (MB)', 256.0, 3998.0)
sc_h = st.slider('Screen Height (cm)', 5.0, 19.0)
sc_w = st.slider('Screen Width (cm)', 0.0, 18.0)
talk_time = st.slider('Talk Time (min)', 2.0, 20.0)
three_g = st.checkbox('3G')
touch_screen = st.checkbox('Touch Screen')
wifi = st.checkbox('WiFi')

# data = pd.read_csv('') # pass file here
# data['models'] = data['model'].str.strip()
# df = data.drop('model', axis='columns')

# OH_encoder = OneHotEncoder(sparse=False)
# encode_data = pd.DataFrame(OH_encoder.fit_transform(df[['transmission', 'fuelType']]))

# encode_data.columns = ['Automatic', 'Manual', 'Other', 'Semi-Auto', 'Diesel', 'Hybrid', 'Other', 'Petrol']

# merc_data = pd.concat([df, encode_data], axis=1)
# df1 = merc_data.drop(['transmission', 'fuelType', 'models'], axis='columns')
# df2 = pd.get_dummies(df.models)
# df3 = pd.concat([df1, df2], axis=1)
# X = df3.drop(['price', 'tax', 'mpg', 'mileage'], axis='columns')
# y = df3.price

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# decision_tree = DecisionTreeRegressor()
# linear_reg = LinearRegression()

# decision_tree.fit(X_train.values, y_train.values)
# linear_reg.fit(X_train.values, y_train.values)

# decision_score = decision_tree.score(X_test.values, y_test.values)
# linear_score = linear_reg.score(X_test.values, y_test.values)
# column_data = X.columns.values


# def predict_price_decision(model, _year, engineSize, transmission, fuel):
#     try:
#         model_index = model_list.index(model)[0][0]
#         transmission_index = transmission_list.index(transmission)[0][0]
#         fuel_index = fuel_list.index(fuel)[0][0]
#     except ValueError:
#         model_index = -1
#         fuel_index = -1
#         transmission_index = -1

#     x = np.zeros(len(column_data))
#     x[0] = _year
#     x[1] = engineSize
#     if transmission_index >= 0:
#         x[transmission_index] = 1
#     elif fuel_index >= 0:
#         x[fuel_index] = 5
#     elif model_index >= 0:
#         x[model_index] = 9

#     return decision_tree.predict([x])[0]

# def predict_price_linear(model, _year, engineSize, transmission, fuel):
#     try:
#         model_index = model_list.index(model)[0][0]
#         transmission_index = transmission_list.index(transmission)[0][0]
#         fuel_index = fuel_list.index(fuel)[0][0]
#     except ValueError:
#         model_index = -1
#         fuel_index = -1
#         transmission_index = -1

#     x = np.zeros(len(column_data))
#     x[0] = _year
#     x[1] = engineSize
#     if transmission_index >= 0:
#         x[transmission_index] = 1
#     elif fuel_index >= 0:
#         x[fuel_index] = 5
#     elif model_index >= 0:
#         x[model_index] = 9

#     return linear_reg.predict([x])[0]


# alg = ['Decision Tree Regression', 'Linear Regression']
# select_alg = st.selectbox('Choose Algorithm for Efficient Predict', alg)
# if st.button('Predict'):
#     if select_alg == 'Decision Tree Regression':
#         st.write('Accuracy Score', decision_score)
#         st.subheader(predict_price_decision(models, year, engine_size, transmissions, fuels))
#         st.markdown("<h5 style='text-align: left;'> Euros </h5>", unsafe_allow_html=True)

#     elif select_alg == 'Linear Regression':
#         st.write('Accuracy Score', linear_score)
#         predicted_price = st.subheader(predict_price_linear(models, year, engine_size, transmissions, fuels))
#         st.markdown("<h5 style='text-align: left;'> Euros </h5>", unsafe_allow_html=True)
#         if predict_price_linear(models, year, engine_size, transmissions, fuels) <= 0:
#             st.write('Curious about why Linear Regression received Negative value as a Prediction. Here are '
#                         'some resources which would make you understand mathematics behind Linear Regression better. ')
#             st.markdown("[Stack Overflow answer](https://stackoverflow.com/questions/63757258/negative-accuracy-in-linear-regression)")
#             st.markdown("[Quora](https://www.quora.com/What-is-a-negative-regression)")
#             st.markdown("[Edureka Video on Linear regression ](https://www.youtube.com/watch?v=E5RjzSK0fvY)")
#             st.write('Hope this helps you!')

#             st.markdown('---')

if st.button('Predict'):
    # prediction part will be here
    pass