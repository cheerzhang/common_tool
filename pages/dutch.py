import streamlit as st
import pandas as pd


def sentence_with_translate(dutch, english, chinese):
    st.write(dutch)
    with st.expander("See translation"):
        st.write(english)
        st.write(chinese)

st.title(f"NOS news")
# ---------------------------------- article ---------------------------------------
article_dutch = [
    "Woningcorporatie Vesteda verbreekt contact met huurders die willen 'omkopen'",
    "Woningcorporatie Vesteda verbreekt het contact met kandidaat-huurders die de organisatie willen omkopen om zo een huurwoning te bemachtigen. De potentiële huurders bieden steeds vaker geld om voorrang te krijgen op een woning.",
    "Vesteda verhuurt appartementen en andere woningen in heel Nederland. De krappe verhuurmarkt leidt volgens Vesteda tot ongewenst gedrag zoals pogingen tot omkoping. Het gaat om bedragen die oplopen tot 5000 euro."
]
article_english = [
    "Housing corporation Vesteda cuts off contact with tenants who want to 'bribe'",
    "In The Hague, dozens of people joined a silent march tonight for 36-year-old Antoneta, who was stabbed to death in a branch of Albert Heijn last week.",
    "The tour started on the Laan van Reagan and Gorbachev and ended at the Albert Heijn where Antoneta was stabbed to death. Participants in the procession wore a white shirt with a picture of the woman and carried candles or white roses. The candles and flowers that were taken were also left at the supermarket, Omroep West writes.",
    "The silent march was organized by a former colleague of Antoneta. 'The need in the team of former colleagues is great for this trip. We feel that we have not been able to say goodbye,' she previously told Omroep West."
]
article_chinese = [
    "住房公司 Vesteda 切断了与想要“贿赂”的租户的联系",
    "在海牙，今晚有数十人为 36 岁的安东内塔举行无声游行，他上周在 Albert Heijn 的一个分店被刺死。",
    "巡演从里根和戈尔巴乔夫大街开始，在安东内塔被刺死的阿尔伯特海金结束。游行的参与者穿着印有该女子照片的白衬衫，并随身携带蜡烛或白玫瑰。奥姆罗普·韦斯特写道，他们随身携带的鲜花也留在了超市。",
    "这次无声巡演是由安东内塔的一位前同事组织的。'这次巡演非常需要前同事团队。 我们有一种无法说再见的感觉，'她之前告诉 Omroep West"
]
for item in range(0, len(article_dutch)):
    sentence_with_translate(article_dutch[item], article_english[item], article_chinese[item])


st.title(f"NOS news")
# ---------------------------------- article ---------------------------------------
article_dutch = [
    "Olympisch ticket is binnen, nu duikt B-Girl India 'echte breakingcultuur' in",
    "In Den Haag hebben tientallen mensen vanavond meegelopen in een stille tocht voor de 36-jarige Antoneta, die vorige week in een filiaal van Albert Heijn werd doodgestoken.",
    "De tocht begon op de Laan van Reagan en Gorbatsjov en eindigde bij de Albert Heijn waar Antoneta werd doodgestoken. Deelnemers aan de stoet droegen een wit shirt met een foto van de vrouw en hadden kaarsen of witte rozen bij zich. De meegenomen kaarsen en bloemen werden ook bij de supermarkt achtergelaten, schrijft Omroep West.",
    "De stille tocht werd georganiseerd door een ex-collega van Antoneta. 'De behoefte in het team van oud-collega's is groot voor deze tocht. We hebben het gevoel dat we geen afscheid hebben kunnen nemen', zei ze eerder tegen Omroep West."
]
article_english = [
    "Olympic ticket is in, now B-Girl India dives into 'real breaking culture'",
    "In The Hague, dozens of people joined a silent march tonight for 36-year-old Antoneta, who was stabbed to death in a branch of Albert Heijn last week.",
    "The tour started on the Laan van Reagan and Gorbachev and ended at the Albert Heijn where Antoneta was stabbed to death. Participants in the procession wore a white shirt with a picture of the woman and carried candles or white roses. The candles and flowers that were taken were also left at the supermarket, Omroep West writes.",
    "The silent march was organized by a former colleague of Antoneta. 'The need in the team of former colleagues is great for this trip. We feel that we have not been able to say goodbye,' she previously told Omroep West."
]
article_chinese = [
    "奥运门票已到，印度 B-Girl 开始涉足'真正的突破文化'",
    "在海牙，今晚有数十人为 36 岁的安东内塔举行无声游行，他上周在 Albert Heijn 的一个分店被刺死。",
    "巡演从里根和戈尔巴乔夫大街开始，在安东内塔被刺死的阿尔伯特海金结束。游行的参与者穿着印有该女子照片的白衬衫，并随身携带蜡烛或白玫瑰。奥姆罗普·韦斯特写道，他们随身携带的鲜花也留在了超市。",
    "这次无声巡演是由安东内塔的一位前同事组织的。'这次巡演非常需要前同事团队。 我们有一种无法说再见的感觉，'她之前告诉 Omroep West"
]
for item in range(0, len(article_dutch)):
    sentence_with_translate(article_dutch[item], article_english[item], article_chinese[item])








