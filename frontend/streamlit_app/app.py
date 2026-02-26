import streamlit as st
from streamlit_option_menu import option_menu
import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.api_client import APIClient

# Page configuration
st.set_page_config(
    page_title="🧹 Dataset Cleaning AI Agent",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'api_client' not in st.session_state:
    st.session_state.api_client = APIClient()

if 'project_id' not in st.session_state:
    st.session_state.project_id = None

if 'current_task' not in st.session_state:
    st.session_state.current_task = None

# Custom styling
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #0d1117;
    }
    .main-title {
        font-size: 2.5em;
        font-weight: bold;
        background: linear-gradient(120deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1em;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("🧹 Dataset Cleaner")
    selected = option_menu(
        "Main Menu",
        ["Dashboard", "New Project", "Active Projects", "Reports", "Settings"],
        icons=["house", "plus-circle", "folder", "bar-chart", "gear"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0d1117"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#667eea"},
        }
    )

# Main content based on selection
if selected == "Dashboard":
    st.markdown('<div class="main-title">📊 Cleaning Dashboard</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Projects", "12", "+2")
    with col2:
        st.metric("Files Cleaned", "1,234", "+145")
    with col3:
        st.metric("Active Tasks", "3", "-1")
    with col4:
        st.metric("Success Rate", "98.5%", "+0.5%")
    
    st.subheader("🔄 Active Cleaning Tasks")
    st.info("Loading active tasks...")
    
    st.subheader("📈 Cleaning Metrics")
    st.info("Loading metrics...")

elif selected == "New Project":
    st.markdown('<div class="main-title">📁 Create New Project</div>', unsafe_allow_html=True)
    
    with st.form("project_form"):
        project_name = st.text_input("Project Name", placeholder="My Dataset Cleaning Project")
        description = st.text_area("Description", placeholder="Describe your dataset and cleaning needs")
        
        col1, col2 = st.columns(2)
        with col1:
            data_type = st.multiselect(
                "Data Types",
                ["CSV/Tabular", "Images", "Videos", "JSON", "XML", "Other"]
            )
        with col2:
            cleaning_priority = st.selectbox(
                "Cleaning Priority",
                ["Quick Clean", "Balanced", "Deep Clean"]
            )
        
        uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)
        
        if st.form_submit_button("🚀 Create & Start Project", use_container_width=True):
            st.success("✅ Project created successfully!")

elif selected == "Active Projects":
    st.markdown('<div class="main-title">📁 Your Projects</div>', unsafe_allow_html=True)
    st.info("No projects yet. Create one to get started!")

elif selected == "Reports":
    st.markdown('<div class="main-title">📊 Cleaning Reports</div>', unsafe_allow_html=True)
    st.write("Detailed reports with before/after metrics, cleaning summaries, and recommendations.")

elif selected == "Settings":
    st.markdown('<div class="main-title">⚙️ Settings</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        api_key = st.text_input("API Key", type="password")
    with col2:
        theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
    
    if st.button("💾 Save Settings"):
        st.success("✅ Settings saved!")

st.markdown("---")
st.caption("🧹 Dataset Cleaning AI Agent | v1.0.0 | Built with ❤️")