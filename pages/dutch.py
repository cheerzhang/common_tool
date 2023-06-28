import streamlit as st
import pandas as pd

# ---------------------------------- article ---------------------------------------
article_1 = """
Tientallen mensen bij stille tocht doodgestoken Antoneta (36) in Den Haag
"""
article_2 = """
Dozens of people stabbed to death in a silent march Antoneta (36) in The Hague
"""
article_3 = """
海牙安东内塔的静默游行中数十人被刺死(36)
"""
st.write(article_1)
# --------------------------------- translate ---------------------------------------
with st.expander("See translation"):
    st.write(article_2)
    st.write(article_3)




# ---------------------------------- article ---------------------------------------
article_1 = """
In Den Haag hebben tientallen mensen vanavond meegelopen in een stille tocht voor de 36-jarige Antoneta, die vorige week in een filiaal van Albert Heijn werd doodgestoken.
"""
article_2 = """
In The Hague, dozens of people joined a silent march tonight for 36-year-old Antoneta, who was stabbed to death in a branch of Albert Heijn last week.
"""
article_3 = """
在海牙，今晚有数十人参加了为 36 岁的安东内塔举行的无声游行，他上周在阿尔伯特·海因 (Albert Heijn) 的一家分店被刺死。
"""
st.write(article_1)
# --------------------------------- translate ---------------------------------------
with st.expander("See translation"):
    st.write(article_2)
    st.write(article_3)


