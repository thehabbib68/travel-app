import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page setup
st.set_page_config(page_title="GlobeTrek Travels", layout="wide")

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load airplane animation
lottie_airplane = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_qp1q7mct.json")

# Custom header styles
st.markdown("""
    <style>
    .main-header {
        background-color: #005f73;
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .header-title {
        font-size: 3em;
        font-weight: bold;
    }
    .subheader-title {
        font-size: 1.3em;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><div class="header-title">🌍 GlobeTrek Travels</div><div class="subheader-title">Crafting Journeys, Creating Memories</div></div>', unsafe_allow_html=True)
st.write("")

# Sidebar navigation
menu = st.sidebar.radio("Go to", ["Home", "Destinations", "Packages", "About", "Contact"])

# Home Page
if menu == "Home":
    st.markdown("## ✈️ Welcome to GlobeTrek Travels")

    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_airplane, speed=1, reverse=False, loop=True, quality="high", height=250)

    with col2:
        st.write("""
        At **GlobeTrek**, we design unforgettable travel experiences to destinations all over the world. 
        Whether you're looking for a romantic escape, a family vacation, or a solo adventure, 
        we help you explore more with less hassle.
        """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🌐 Countries Covered", "50+")
    with col2:
        st.metric("😊 Happy Travelers", "10,000+")
    with col3:
        st.metric("📅 Years of Service", "10")

    st.markdown("---")
    st.markdown("## 📸 Our Featured Destination")
    st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", use_container_width=True)

# Destinations Page
elif menu == "Destinations":
    st.markdown("## 🗺 Top Destinations")
    cols = st.columns(3)

    destinations = [
        ("Bali, Indonesia", "Relaxing beaches and culture", "🏝"),
        ("Paris, France", "Romantic city of lights", "🗼"),
        ("Banff, Canada", "Snowy peaks and adventure", "🏔"),
        ("Cape Town, SA", "Safari and natural beauty", "🌄"),
        ("Tokyo, Japan", "Tech meets tradition", "🎎"),
        ("Dubai, UAE", "Luxury and innovation", "🌆"),
    ]

    for i, (place, desc, emoji) in enumerate(destinations):
        with cols[i % 3]:
            st.markdown(f"### {emoji} {place}")
            st.write(desc)

# Packages Page
elif menu == "Packages":
    st.markdown("## 📦 Travel Packages")

    st.info("Here are some of our best-selling all-inclusive packages:")
    packages = [
        {
            "title": "Romantic Paris",
            "duration": "5 Nights / 6 Days",
            "price": "$1200",
            "desc": "Includes flights, hotels, Eiffel Tower dinner cruise."
        },
        {
            "title": "Adventure in Banff",
            "duration": "7 Nights / 8 Days",
            "price": "$1500",
            "desc": "Mountain trekking, skiing, and cozy cabins."
        },
        {
            "title": "Beach Vibes in Bali",
            "duration": "6 Nights / 7 Days",
            "price": "$1100",
            "desc": "Beachside resort, temple tours, snorkeling."
        }
    ]

    for pkg in packages:
        with st.container():
            st.markdown(f"### 🧳 {pkg['title']}")
            st.write(f"**Duration:** {pkg['duration']}  \n**Price:** {pkg['price']}  \n{pkg['desc']}")
            st.markdown("---")

# About Page
elif menu == "About":
    st.markdown("## 👥 About GlobeTrek")
    st.write("""
    GlobeTrek Travels was founded in 2015 by passionate travelers with one mission: 
    to make world travel easier, safer, and more fulfilling for everyone.

    We are proud to be a customer-first company, offering:
    - ✅ Personalized travel planning
    - ✅ Competitive pricing
    - ✅ 24/7 customer support
    - ✅ Sustainable tourism partnerships
    """)

# Contact Page
elif menu == "Contact":
    st.markdown("## 📞 Contact Us")

    st.write("We’d love to hear from you! Fill out the form below:")

    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        msg = st.text_area("Your Message")
        send = st.form_submit_button("Submit")

        if send:
            st.success(f"Thanks {name}, we've received your message and will reply shortly!")

    st.markdown("""
    ---
    📧 **Email:** contact@globetrek.com  
    📞 **Phone:** +123-456-7890  
    📍 **Office:** 101 Wanderlust Lane, Adventure City, Earth
    """)
