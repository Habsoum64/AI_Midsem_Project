import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

with open('AI_Midsem_Project/rf_reg.pkl', 'rb') as f:
    rf_reg = pickle.load(f)

with open('AI_Midsem_Project/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


def make_prediction(data):
    prediction = rf_reg.predict(data)
    return prediction[0]


player_data = {
    'value_eur': st.experimental_get_query_params().get("value_eur", [0])[0],
    'release_clause_eur': st.experimental_get_query_params().get("release_clause_eur", [0])[0],
    'potential': st.experimental_get_query_params().get("potential", [50])[0],
    'passing': st.experimental_get_query_params().get("passing", [50])[0],
    'dribbling': st.experimental_get_query_params().get("dribbling", [50])[0],
    'defending': st.experimental_get_query_params().get("defending", [50])[0],
    'physic': st.experimental_get_query_params().get("physic", [50])[0],
    'movement_reactions': st.experimental_get_query_params().get("movement_reactions", [50])[0],
    'power_shot_power': st.experimental_get_query_params().get("power_shot_power", [50])[0],
    'mentality_composure': st.experimental_get_query_params().get("mentality_composure", [50])[0],
}


player_data['value_eur'] = float(player_data['value_eur'])
player_data['release_clause_eur'] = float(player_data['release_clause_eur'])
player_data['potential'] = int(player_data['potential'])
player_data['passing'] = float(player_data['passing'])
player_data['dribbling'] = float(player_data['dribbling'])
player_data['defending'] = int(player_data['defending'])
player_data['physic'] = int(player_data['physic'])
player_data['movement_reactions'] = int(player_data['movement_reactions'])
player_data['power_shot_power'] = int(player_data['power_shot_power'])
player_data['mentality_composure'] = int(player_data['mentality_composure'])


input_df = pd.DataFrame([player_data])
predicted_rating = make_prediction(input_df)

st.title("Player Rating Prediction")
st.success(f"The predicted rating is: {predicted_rating}")