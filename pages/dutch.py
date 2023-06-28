import streamlit as st
import pandas as pd


def sentence_with_translate(dutch, english, chinese):
    st.write(dutch)
    with st.expander("See translation"):
        st.write(english)
        st.write(chinese)


# ---------------------------------- article ---------------------------------------
article_dutch = [
    "Tientallen mensen bij stille tocht doodgestoken Antoneta (36) in Den Haag",
    "In Den Haag hebben tientallen mensen vanavond meegelopen in een stille tocht voor de 36-jarige Antoneta, die vorige week in een filiaal van Albert Heijn werd doodgestoken.",
    "De tocht begon op de Laan van Reagan en Gorbatsjov en eindigde bij de Albert Heijn waar Antoneta werd doodgestoken. Deelnemers aan de stoet droegen een wit shirt met een foto van de vrouw en hadden kaarsen of witte rozen bij zich. De meegenomen kaarsen en bloemen werden ook bij de supermarkt achtergelaten, schrijft Omroep West.",
    "De stille tocht werd georganiseerd door een ex-collega van Antoneta. "De behoefte in het team van oud-collega's is groot voor deze tocht. We hebben het gevoel dat we geen afscheid hebben kunnen nemen", zei ze eerder tegen Omroep West."
]
article_english = [
    "Dozens of people stabbed to death in a silent march Antoneta (36) in The Hague",
    "In The Hague, dozens of people joined a silent march tonight for 36-year-old Antoneta, who was stabbed to death in a branch of Albert Heijn last week.",
    "The tour started on the Laan van Reagan and Gorbachev and ended at the Albert Heijn where Antoneta was stabbed to death. Participants in the procession wore a white shirt with a picture of the woman and carried candles or white roses. The candles and flowers that were taken were also left at the supermarket, Omroep West writes.",
    "The silent march was organized by a former colleague of Antoneta. "The need in the team of former colleagues is great for this trip. We feel that we have not been able to say goodbye," she previously told Omroep West."
]
article_chinese = [
    "在海牙的安东内塔（Antoneta，36岁）静默游行中，数十人被刺死",
    "在海牙，今晚有数十人为 36 岁的安东内塔举行无声游行，他上周在 Albert Heijn 的一个分店被刺死。",
    "巡演从里根和戈尔巴乔夫大街开始，在安东内塔被刺死的阿尔伯特海金结束。游行的参与者穿着印有该女子照片的白衬衫，并随身携带蜡烛或白玫瑰。奥姆罗普·韦斯特写道，他们随身携带的鲜花也留在了超市。",
    "这次无声巡演是由安东内塔的一位前同事组织的。“这次巡演非常需要前同事团队。 我们有一种无法说再见的感觉，”她之前告诉 Omroep West"
]
for item in range(0, len(article_dutch)):
    sentence_with_translate(article_dutch[item], article_english[item], article_chinese[item])








