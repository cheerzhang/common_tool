import streamlit as st

# Sample article
article = """
De milieucommissie van het Europees Parlement is het niet gelukt om een compromis te bereiken over de natuurherstelwet van Eurocommissaris Frans Timmermans. Dit betekent dat in het Europees Parlement alles weer open ligt. Over twee weken stemt het voltallig parlement over de wet.

Twee weken geleden werd er in de milieucommissie ook al gestemd over de natuurherstelwet. Toen bleek er geen meerderheid te zijn om de wet te verwerpen. Daarna werd geprobeerd een compromis te bereiken over aanpassing van de wet. Daarvoor werden 2500 amendementen ingediend. De stemming daarover duurde zolang dat die vandaag werden afgemaakt. Maar nog altijd blijven de Europarlementariërs compleet verdeeld.

De natuurherstelwet is de afgelopen weken een politiek hangijzer geworden. Volgens de Europese christendemocraten is de wet onwerkbaar. Ze waarschuwen voor grote gevolgen voor de boeren. Volgens de linkse partijen is dit onzin en zou de EVP enkel tegen zijn als campagnestrategie voor de Europese verkiezingen van volgend jaar.

Meer biodiversiteit
Het doel van de wet is om de biodiversiteit in de EU flink te verbeteren. Volgens de Europese Commissie verkeert 81 procent van de Europese natuur in slechte staat.

De EU-landen wisten vorige week al wel een akkoord te sluiten over de natuurherstelwet. Dat werd een afgezwakte versie van het oorspronkelijke voorstel. Daarin stond dat de landen zouden moeten 'verzekeren' dat delen van natuur niet verder achteruit mogen gaan, een resultaatverplichting. Maar in het compromis van de EU-landen is van een resultaatverplichting geen sprake meer. Alleen nog van een inspanningsverplichting: je best doen dus.

Felle politieke discussie
Mohammed Chahim, Europarlementariër voor de PvdA, denkt dat er een goed kans is dat er in juli wel een meerderheid in het parlement is voor de wet. "Tijdens de plenaire stemming in juli kunnen de EVP'ers hun progressieve leden niet meer vervangen door de conservatieve, zoals ze vandaag deden uit electorale wanhoop klimaatontkenners blind achterna te hollen."

Bas Eickhout van Groenlinks heeft ook goede hoop op een meerderheid in het Europees Parlement in juli. Hij wijst op een "ongekend agressieve campagne" van de christendemocraten. CDA-Europarlementariër Esther de Lange is tegen de natuurherstelwet en schat de kansen voor een meerderheid in juli anders in. "Dat ook Italië, Polen, Finland, Zweden, België en Oostenrijk in de raad niet met het voorstel konden instemmen, laat zien dat er nog veel zorgen leven. Het voorstel zit verkeerd in elkaar en dus moet de Europese Commissie wat ons betreft terug naar de tekentafel om deze zorgen weg te nemen."

De discussie over de natuurherstelwet gaat in alle hevigheid door. In de week van 10 juli volgt de laatste stemming in het Europees Parlement, daarna moeten de 27 landen en het EP samen onderhandelen over een eindvoorstel voor de wet. Die ligt er dan op zijn vroegst volgend voorjaar, vlak voor de Europese verkiezingen.
"""

# Convert the article into a list of words
words = article.split()

# Display the article
st.write(article)

# Function to save the selected word
def save_word(word):
    selected_words = st.session_state.get('selected_words', [])
    if word not in selected_words:
        selected_words.append(word)
        st.session_state.selected_words = selected_words

# Loop through the words and add hover functionality
for word in words:
    hover_text = f'<span style="background-color: yellow;">{word}</span>'
