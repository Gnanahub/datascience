#requirements 
from ast import main
#from logging.config import _LoggerConfiguration
import streamlit as st 
import pandas as pd 
import numpy as np 
#from streamlit_option_menu import option_menu



open_pubs = pd.read_csv("C:\MY_FOLDER\DATA SCIENCE INTERN (notes, assignment)\pub_task\pages\data\open_pubs.csv")
open_pubs.columns=['unique.Id','Name','Address','PostCode','Easting','Northing','Latitude','Longitude','District_Authority']
#replacing the null values
open_pubs = open_pubs.replace('\\N', np.NaN)
open_pubs = open_pubs.dropna()
data_selection = open_pubs.District_Authority.unique()
pub = "Total number of Pubs: "+str(open_pubs.shape[0])
auth = "Total number of Pubs in District: "+str(data_selection.shape[0])

#streamlit
def main():
  st.title(" Pub Lockh ")

  st.subheader(pub)
  st.subheader(auth)
  
############################################################################################

page_bg_img = '''
<style>
.stApp {
background-image: url("https://cdn.eyeem.com/thumb/76fe6281351829df3b851c9687fa359926b29a40-1506017077476/640/480");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

#with st.sidebar:
#    choose = option_menu("Dashboard", ["About", "Pub Location", "Nearest Pub", ],
 #                        icons=['house', 'location', 'Pub', 'book',],
 #                        menu_icon="app-indicator", default_index=0,
  #                       styles={
   
#     "container": {"padding": "5!important", "background-color": "#92a8d1"},
 #       "icon": {"color": "black", "font-size": "25px"}, 
  #      "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
   #     "nav-link-selected": {"background-color": "#02ab21"},
    #}
    #)






if __name__ == "__main__":
  main() 
