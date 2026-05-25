import streamlit as st
import leafmap.foliumap as leafmap
import os

# 1. Page Configuration & Title Styling
st.set_page_config(page_title="Australia Bushfire Analytics", layout="wide")

st.markdown("""
    <div style="background-color:#1e293b; padding:20px; border-radius:10px; margin-bottom:25px;">
        <h1 style="color:#f8fafc; margin:0;">Australia Wildfire Fuel Load & Risk Mapping Platform</h1>
        <p style="color:#94a3b8; font-size:16px; margin:5px 0 0 0;">
            Target Ecosystem Evaluation: Blue Mountains, New South Wales System Domain
        </p>
    </div>
""", unsafe_allowed_html=True)

# 2. Sidebar Analytical Metadata View
st.sidebar.title("Pipeline Architecture")
st.sidebar.info("""
**Data Sources Ingested:**
* **Optical:** Copernicus Sentinel-2 (NDVI, NDMI Indices)
* **Radar (SAR):** Copernicus Sentinel-1 (C-Band Canopy Volume Structure)

**Predictive Engine:**
* Scikit-Learn Random Forest Classifier (Low, Medium, Extreme Risk Calibration profiles)
""")

# 3. Establish Relative Paths to Data Layers
# This automatically handles both local environments and cloud servers
current_dir = os.path.dirname(__file__)
raster_path = os.path.join(current_dir, "assets", "Fuel_Risk_Map.tif")

# 4. Initialize Interactive Leafmap Framework Canvas
if os.path.exists(raster_path):
    st.subheader("Interactive Operational Predictive Matrix Map")
    
    # Center map coordinates on the Blue Mountains domain footprint
    m = leafmap.Map(center=[-33.65, 150.35], zoom=10)
    
    # Inject diverse basemaps for stakeholder evaluation toggles
    m.add_basemap("HYBRID")
    m.add_basemap("ROADMAP")
    
    # Render your generated Machine Learning array map output on top
    m.add_raster(
        raster_path, 
        bands=1, 
        palette=['#22c55e', '#eab308', '#ef4444'], # Clean CSS hex codes for Green (Low), Yellow (Med), Red (High)
        layer_name="Predictive Fuel Load Risk Index Layers"
    )
    
    # Display within streamlit app DOM architecture framework
    m.to_streamlit(height=700)
else:
    st.error(f"Missing Critical Data Layer Node! Expected asset file layout at: {raster_path}")