import streamlit

streamlit.title("My Mom's new healthy diner")

streamlit.header('Breakfast Favorites')
streamlit.text('๐ฅฃ Omega 3 & Blueberry oatmeal')
streamlit.text('๐ฅKale, Spinach & Rocket Smoothie')
streamlit.text('๐ Hard-Boiled Free-Range Eggs')
streamlit.text('๐ฅ๐Avacado Toast')
streamlit.header('๐๐ฅญ Build Your Own Fruit Smoothie ๐ฅ๐')

import pandas
my_fruits_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruits_list=my_fruits_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick Fruits as per you requirment",list(my_fruits_list.index),['Avocado','Apple'])
fruits_to_show=my_fruits_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
