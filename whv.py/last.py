import streamlit as st
import folium
from streamlit_folium import st_folium

# Set background image using CSS
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image URL
set_background("https://dam.destination.one/745854/ff4e4c5ba509704cfdb8869ba8598888533379e90763880d7372d61e62ceac07/s-dstrand-wilhelmshaven.jpg")

# Language translation dictionary
translations = {
    "Deutsch": {
        "title": "Erkunde Wilhelmshaven - Dein digitaler Küstenführer",
        "description": "Entdecke die Highlights von Wilhelmshaven! Interaktive Karten, historische Infos, Restaurants und praktische Tipps helfen dir, die Stadt zu erleben.",
        "features": [
            "Interaktive Karte",
            "Sehenswürdigkeiten",
            "Historische Fakten",
            "Hotels",
            "Restaurants",
            "Teile deine Abenteuer",
        ],
    },
    "English": {
        "title": "Explore Wilhelmshaven - Your Digital Coastal Guide",
        "description": "Discover Wilhelmshaven's highlights! Interactive maps, historical info, restaurants, and practical tips to explore the city.",
        "features": [
            "Interactive Map",
            "Attractions",
            "Historical Facts",
            "Hotels",
            "Restaurants",
            "Share Your Adventures",
        ],
    },
}

# Language settings
language = st.sidebar.selectbox("Sprache / Language", ["Deutsch", "English"])
text = translations[language]

# Title and Description
st.title(text["title"])
st.write(text["description"])

# Navigation between different features
feature = st.sidebar.selectbox("Select Feature", text["features"])

# Data for map markers
locations = {
    "Sehenswürdigkeiten": [
        {
            "Name": "Kaiser-Wilhelm-Brücke",
            "Latitude": 53.5086,
            "Longitude": 8.1079,
            "Description": "Die älteste Drehbrücke Deutschlands und ein Wahrzeichen der Stadt." if language == "Deutsch" else "The oldest swing bridge in Germany and a landmark of the city.",
            "Image": "https://brueckenzug.de/wp-content/uploads/Wilhelmshaven_Kaiser-Wilhelm-Bruecke.webp",
            "Link": "https://maps.app.goo.gl/C8P7NPmcbhsTHxHw7",
        },
        {
            "Name": "Deutsches Marinemuseum",
            "Latitude": 53.5137,
            "Longitude": 8.1168,
            "Description": "Tauchen Sie ein in die Geschichte der Deutschen Marine." if language == "Deutsch" else "Dive into the history of the German Navy.",
            "Image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/68/dd/8f/img-20180824-121545-largejpg.jpg?w=1200&h=-1&s=1",
            "Link": "https://maps.app.goo.gl/NLQFquFvKcyrgE3j7",
        },
        {
            "Name": "Südstrand",
            "Latitude": 53.5037,
            "Longitude": 8.1121,
            "Description": "Ein beliebter Ort, um am Wasser zu entspannen." if language == "Deutsch" else "A popular spot to relax and walk along the waterfront.",
            "Image": "https://dam.destination.one/928449/df187e33dc168fdbd2b7532885d2a1f375314eea132708a6bb2eaa88f2d3dba6/b-nke-auf-der-s-dstrandpromenade.jpg",
            "Link": "https://g.co/kgs/s7rrv5J",
        },
        {
            "Name": "Wattenmeer Besucherzentrum",
            "Latitude": 53.5146,
            "Longitude": 8.1034,
            "Description": "Ein Nationalparkzentrum mit interaktiven Ausstellungen über das Wattenmeer." if language == "Deutsch" else "A visitor center with interactive exhibits about the Wadden Sea.",
            "Image": "https://www.wattenmeer-besucherzentrum.de/images/Wattenmeer-Besucherzentrum1.png",
            "Link": "https://maps.app.goo.gl/C8P7NPmcbhsTHxHw7",
        },
    ],
    "Hotels": [
        {
            "Name": "Atlantic Hotel Wilhelmshaven",
            "Latitude": 53.5112,
            "Longitude": 8.1041,
            "Description": "Luxushotel mit Blick auf den Hafen." if language == "Deutsch" else "Luxury hotel overlooking the harbor.",
            "Image": "https://www.atlantic-hotels.de/fileadmin/_processed_/5/b/csm_atlantic-hotel-wilhelmshaven-aussenansicht-mit-logo_c97ce07495.jpg",
            "Link": "https://maps.app.goo.gl/PBZWwtRsj9VENcP57",
            "Stars": 5,
            "Price": "ab 150€ pro Nacht",
            "Rating": "4.6/5",
        },
        {
            "Name": "Tide Hotel",
            "Latitude": 53.5142,
            "Longitude": 8.1001,
            "Description": "Modernes Hotel nahe dem Südstrand." if language == "Deutsch" else "Modern hotel near the southern beach.",
            "Image": "https://www.hotel-am-stadtpark.de/files/stadtpark/images/Tide-Hotel-Aussen/Tide-Hotel-Frontansicht.jpg",
            "Link": "https://maps.app.goo.gl/dvtbmLBsNKTzwXUAA",
            "Stars": 4,
            "Price": "ab 100€ pro Nacht",
            "Rating": "4.4/5",
        },
        {
            "Name": "City Hotel Valois",
            "Latitude": 53.5201,
            "Longitude": 8.1064,
            "Description": "Zentral gelegenes Hotel in der Nähe des Bahnhofs." if language == "Deutsch" else "Centrally located hotel near the train station.",
            "Image": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/12665667.jpg?k=2019e057a2f241cdca711f456a0d963297dbdf192afc9f1d7b9801ec9a6913c2&o=",
            "Link": "https://maps.app.goo.gl/oiUajn2RPh8emp3K7",
            "Stars": 3,
            "Price": "ab 80€ pro Nacht",
            "Rating": "4.2/5",
        },
    ],
    "Restaurants": [
        {
            "Name": "CaOs",
            "Latitude": 53.5158,
            "Longitude": 8.1015,
            "Description": "Einzigartige, kreative Küche mit regionalen Zutaten." if language == "Deutsch" else "Unique, creative cuisine with regional ingredients.",
            "Image": "https://lh3.googleusercontent.com/p/AF1QipM4m5Q-ieQqb-Ckih0InKjBmkH0AXI1qrINL2iv=s1360-w1360-h1020",
            "Link": "https://maps.app.goo.gl/fu9UBw5u9MYk25t4A",
            "Rating": "4.7/5",
            "Price": "25-50€ pro Person",
        },
        {
            "Name": "L' Orient Libanesisches Restaurant",
            "Latitude": 53.5182,
            "Longitude": 8.1101,
            "Description": "Authentische libanesische Gerichte in gemütlicher Atmosphäre." if language == "Deutsch" else "Authentic Lebanese dishes in a cozy atmosphere.",
            "Image": "https://lh5.googleusercontent.com/p/AF1QipPw6KF-92Osg2g5gBbO65fmUN-VEyWMpDRk3BHP=w750-h606-p-k-no",
            "Link": "https://goo.gl/maps/LkP5z7VbMeN2",
            "Rating": "4.5/5",
            "Price": "20-40€ pro Person",
        },
    ],
}

# Historical Facts Data
historical_facts = [
           {
        "Year": 1853,
        "Fact": "Unterzeichnung des ‚Jadevertrages‘. Preußen erwirbt vom Großherzogtum Oldenburg ein Gelände von etwa 313 Hektar zum Bau eines Marinehafens."
        if st.session_state.get("language", "Deutsch") == "Deutsch"
        else "Signing of the 'Jade Treaty'. Prussia acquires an area of about 313 hectares from the Grand Duchy of Oldenburg for the construction of a naval harbor.",
    },
    {
        "Year": 1867,
        "Fact": "Eröffnung der Eisenbahnlinie von Bremen über Oldenburg nach Heppens."
        if st.session_state.get("language", "Deutsch") == "Deutsch"
        else "Opening of the railway line from Bremen via Oldenburg to Heppens.",
    },
    {
        "Year": 1869,
        "Fact": "Die Stadt wird durch den preußischen König Wilhelm I. benannt."
        if st.session_state.get("language", "Deutsch") == "Deutsch"
        else "The city is named by the Prussian King Wilhelm I.",
    },
    {
        "Year": 1870,
        "Fact": "Flutung der ersten Hafenanlage mit Schleuse, Kanal und Bauhafen."
        if st.session_state.get("language", "Deutsch") == "Deutsch"
        else "Flooding of the first harbor facility with a lock, canal, and construction harbor.",
    },
    {
        "Year": 1873,
        "Fact": "Wilhelmshaven wird als Marinestützpunkt gegründet."
        if st.session_state.get("language", "Deutsch") == "Deutsch"
        else "Wilhelmshaven was established as a naval base.",
    },
    {
        "Year": 1945,
        "Fact": "Wilhelmshaven wird im Zweiten Weltkrieg schwer beschädigt."
        if st.session_state.get("language", "Deutsch") == "Deutsch"
        else "Wilhelmshaven was heavily damaged during World War II.",
    },
    {
        "Year": 1972,
        "Fact": "Das Deutsche Marinemuseum wird eröffnet."
        if st.session_state.get("language", "Deutsch") == "Deutsch"
        else "The German Naval Museum was opened.",
    },
    {
        "Year": 2009,
        "Fact": "Eröffnung des JadeWeserPorts, Deutschlands tiefstem Hafen."
        if st.session_state.get("language", "Deutsch") == "Deutsch"
        else "Opening of the JadeWeserPort, Germany's deepest harbor.",
    },
    {
        "Year": 2022,
        "Fact": "Fertigstellung und Eröffnung des ersten LNG-Terminals der Bundesrepublik Deutschland in Wilhelmshaven."
        if st.session_state.get("language", "Deutsch") == "Deutsch"
        else "Completion and opening of Germany's first LNG terminal in Wilhelmshaven.",
    },
]

# Interactive Map Feature
if feature == text["features"][0]:
    st.header(text["features"][0])

    # Create map
    m = folium.Map(location=[53.515, 8.118], zoom_start=13)

    # Add markers for all locations
    for category, places in locations.items():
        for place in places:
            icon_color = "blue" if category == "Sehenswürdigkeiten" else "green" if category == "Hotels" else "red"
            icon = "cutlery" if category == "Restaurants" else "info-sign"
            folium.Marker(
                location=[place["Latitude"], place["Longitude"]],
                popup=f"<b>{place['Name']}</b><br>{place['Description']}<br><a href='{place['Link']}' target='_blank'>Mehr erfahren</a>",
                icon=folium.Icon(color=icon_color, icon=icon),
            ).add_to(m)

    # Display map
    st_folium(m, width=700, height=500)

# Historical Facts Feature
elif feature == text["features"][2]:  # Historische Fakten
    st.header(text["features"][2])
    for fact in historical_facts:
        st.write(f"**{fact['Year']}** - {fact['Fact']}")

# Displaying details for other features
elif feature == text["features"][1]:  # Sehenswürdigkeiten
    st.header(text["features"][1])
    for place in locations["Sehenswürdigkeiten"]:
        st.image(place["Image"], use_container_width=True)
        st.subheader(f"[{place['Name']}]({place['Link']})")
        st.write(place["Description"])
        st.write("---")

elif feature == text["features"][3]:  # Hotels
    st.header(text["features"][3])
    for place in locations["Hotels"]:
        st.image(place["Image"], use_container_width=True)
        st.subheader(f"[{place['Name']}]({place['Link']})")
        st.write(place["Description"])
        st.write(f"⭐ {place['Stars']} | 💶 {place['Price']} | ✨ {place['Rating']}")
        st.write("---")

elif feature == text["features"][4]:  # Restaurants
    st.header(text["features"][4])
    for place in locations["Restaurants"]:
        st.image(place["Image"], use_container_width=True)
        st.subheader(f"[{place['Name']}]({place['Link']})")
        st.write(place["Description"])
        st.write(f"⭐ {place['Rating']} | 💶 {place['Price']}")
        st.write("---")

elif feature == text["features"][5]:  # Fotos und Videos hochladen
    st.header(text["features"][5])
    uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True, type=["png", "jpg", "jpeg", "mp4"])
    if uploaded_files:
        for file in uploaded_files:
            if file.type.startswith("image"):
                st.image(file)
            elif file.type.startswith("video"):
                st.video(file)