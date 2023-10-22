import streamlit as st
import pickle
import pandas as pd

with open('AI_Midsem_Project/gb_reg.pkl', 'rb') as f:
    gb_reg = pickle.load(f)


def load_categories(filename):
  categories = []
  with open(filename, 'r') as f:
    for line in f:
      categories.append(line.strip())
  return categories


def make_prediction(data):
    prediction = gb_reg.predict(player_data)
    return prediction[0]


def load_categories(filename):
  categories = []
  with open(filename, 'r') as f:
    for line in f:
      categories.append(line.strip())  
  return categories


def factorize_input(string_value, categories):
  factorized_value = pd.factorize([string_value], categories=categories)[0][0]
  return factorized_value


short_names = load_categories('short_name.txt')
long_names = load_categories('long_name.txt')
dobs = load_categories('dob.txt')
club_names = load_categories('club_name.txt')

player_data = {
    'short_name': st.experimental_get_query_params().get("short_name", [''])[0],
    'long_name': st.experimental_get_query_params().get("long_name", [''])[0],
    'dob': st.experimental_get_query_params().get("dob", [''])[0],
    'club_name': st.experimental_get_query_params().get("club_name", [''])[0],
    'potential': st.experimental_get_query_params().get("potential", [50])[0],
    'value_eur': st.experimental_get_query_params().get("value_eur", [0])[0],
    'wage_eur': st.experimental_get_query_params().get("wage_eur", [0])[0],
    'release_clause_eur': st.experimental_get_query_params().get("release_clause_eur", [0])[0],
    'passing': st.experimental_get_query_params().get("passing", [50])[0],
    'dribbling': st.experimental_get_query_params().get("dribbling", [50])[0],
    'attacking_short_passing': st.experimental_get_query_params().get("attacking_short_passing", [50])[0],
    'movement_reactions': st.experimental_get_query_params().get("movement_reactions", [50])[0],
    'power_shot_power': st.experimental_get_query_params().get("power_shot_power", [50])[0],
    'mentality_vision': st.experimental_get_query_params().get("mentality_vision", [50])[0],
    'mentality_composure': st.experimental_get_query_params().get("mentality_composure", [50])[0],
}

input_data['short_name'] = factorize_input(input_data['short_name'], short_names)
input_data['long_name'] = factorize_input(input_data['long_name'], long_names)
input_data['dob'] = factorize_input(input_data['dob'], dobs)
input_data['club_name'] = factorize_input(input_data['club_name'], club_names)
input_data['potential'] = int(input_data['potential'])
input_data['value_eur'] = float(input_data['value_eur'])
input_data['wage_eur'] = float(input_data['wage_eur'])
input_data['release_clause_eur'] = float(input_data['release_clause_eur'])
input_data['passing'] = float(input_data['passing'])
input_data['dribbling'] = float(input_data['dribbling'])
input_data['attacking_short_passing'] = int(input_data['attacking_short_passing'])
input_data['movement_reactions'] = int(input_data['movement_reactions'])
input_data['power_shot_power'] = int(input_data['power_shot_power'])
input_data['mentality_vision'] = int(input_data['mentality_vision'])
input_data['mentality_composure'] = int(input_data['mentality_composure'])



input_df = pd.DataFrame([input_data])

predicted_rating = predict_rating(input_df)

st.title("Player Rating Prediction")
st.success(f"The predicted rating is: {predicted_rating}")
