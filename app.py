"""
╔══════════════════════════════════════════════════════════════════╗
║   DASHBOARD ANALISIS KEPENDUDUKAN JAWA BARAT 2023–2025          ║
║   Dasar Perencanaan Fasilitas Kesehatan Berbasis Data            ║
╠══════════════════════════════════════════════════════════════════╣
║  CARA MENJALANKAN:                                               ║
║  1. pip install streamlit pandas numpy plotly scikit-learn       ║
║  2. streamlit run app.py                                         ║
╚══════════════════════════════════════════════════════════════════╝
"""
import streamlit as st

# 🔥 Paksa tidak ikut dark mode
st.markdown("""
    <meta name="color-scheme" content="light">
    <style>
        html, body, [class*="css"] {
            background-color: #ffffff !important;
            color: #000000 !important;
        }
    </style>
""", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

# ───────────────────────────────────────────────────────────────────
#  KONFIGURASI HALAMAN
# ───────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="POPINE | Faskes Jawa Barat",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ───────────────────────────────────────────────────────────────────
#  GAYA VISUAL (CSS) - LIGHT BLUE FUTURISTIC (HOLOGRAPHIC TECH)
# ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Font bergaya Tech / HUD Masa Depan yang Bersih */
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;600&display=swap');

    /* Override Background Utama Aplikasi - Biru Muda Hologram */
    .stApp {
        background-color: #f0f9ff;
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(56, 189, 248, 0.08), transparent 25%),
            radial-gradient(circle at 85% 30%, rgba(2, 132, 199, 0.05), transparent 25%),
            linear-gradient(rgba(2, 132, 199, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(2, 132, 199, 0.05) 1px, transparent 1px);
        background-size: 100% 100%, 100% 100%, 25px 25px, 25px 25px;
        color: #0f172a;
        font-family: 'Rajdhani', sans-serif;
    }

    html, body, [class*="css"], p, span, div {
        font-family: 'Rajdhani', sans-serif !important;
        color: #0f172a;
    }

    /* Avatar AI Animation - Light Theme */
    .avatar-wrapper {
        display: flex; justify-content: center; align-items: center; margin-bottom: 10px;
    }
    .avatar-container {
        width: 120px; height: 120px;
        border-radius: 12px;
        padding: 3px;
        background: linear-gradient(45deg, #38bdf8, #0ea5e9, #0284c7, #38bdf8);
        background-size: 300% 300%;
        animation: rotate-glow-light 4s linear infinite;
        position: relative;
        transform: rotate(45deg);
    }
    .avatar-img {
        width: 100%; height: 100%; border-radius: 9px;
        background-color: #e0f2fe; border: 2px solid #e0f2fe;
        object-fit: cover;
        transform: rotate(-45deg);
    }
    @keyframes rotate-glow-light {
        0% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.5); background-position: 0% 50%; }
        50% { box-shadow: 0 0 25px rgba(2, 132, 199, 0.6); background-position: 100% 50%; }
        100% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.5); background-position: 0% 50%; }
    }

    /* Header Dashboard Futuristic Light */
    .header-box {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(14, 165, 233, 0.3);
        border-left: 6px solid #0ea5e9;
        padding: 35px 45px;
        border-radius: 4px;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px rgba(2, 132, 199, 0.08);
        position: relative;
        overflow: hidden;
    }
    .header-box::after {
        content: ''; position: absolute; top: 0; right: 0; width: 150px; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.1));
        transform: skewX(-45deg) translateX(200px);
        animation: tech-shine 4s infinite;
    }
    @keyframes tech-shine { 0% { transform: skewX(-45deg) translateX(-600px); } 100% { transform: skewX(-45deg) translateX(800px); } }
    
    .header-box h1 { margin: 0 0 8px 0; font-size: 2.5rem; font-weight: 700; color: #0369a1; text-transform: uppercase; letter-spacing: 1.5px; font-family: 'Chakra Petch', sans-serif; }
    .header-box p  { margin: 0; color: #334155; font-size: 1.1rem; font-weight: 600; letter-spacing: 0.5px; }
    .header-status { font-family: 'Chakra Petch', sans-serif; font-size:0.9rem; color:#0284c7; letter-spacing:3px; margin-bottom:5px; font-weight:600; }

    /* Kartu KPI bergaya Light HUD */
    .kartu {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(2, 132, 199, 0.15);
        border-radius: 4px;
        padding: 24px 20px;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.05);
        margin-bottom: 16px;
        transition: all 0.3s ease;
        position: relative;
    }
    .kartu:hover {
        border-color: var(--cyan-color, #0ea5e9);
        box-shadow: 0 0 20px var(--cyan-color, rgba(14, 165, 233, 0.3));
        transform: translateY(-4px);
    }
    .kartu .label { font-size: 0.85rem; color: #475569; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; font-family: 'Chakra Petch', sans-serif; }
    .kartu .angka { font-size: 2.3rem; font-weight: 700; margin: 4px 0; color: #0f172a; }
    .kartu .KATEGORI { font-size: 0.85rem; font-weight: 700; padding-top: 6px; }

    /* Informasi Kotak General - Light Cyber Style */
    .kotak-general {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(2, 132, 199, 0.1);
        border-radius: 4px;
        padding: 20px 24px;
        margin: 12px 0;
        box-shadow: inset 0 0 10px rgba(255,255,255,0.5);
        color: #1e293b;
        font-size: 1.05rem;
        font-weight: 500;
    }
    .kotak-biru   { border-left: 4px solid #0ea5e9; border-right: 1px solid rgba(14, 165, 233, 0.3); }
    .kotak-ungu   { border-left: 4px solid #8b5cf6; border-right: 1px solid rgba(139, 92, 246, 0.3); }
    .kotak-hijau  { border-left: 4px solid #10b981; border-right: 1px solid rgba(16, 185, 129, 0.3); }
    .kotak-kuning { border-left: 4px solid #f59e0b; border-right: 1px solid rgba(245, 158, 11, 0.3); }
    .kotak-merah  { border-left: 4px solid #ef4444; border-right: 1px solid rgba(239, 68, 68, 0.3); }

    h2 { color: #0369a1 !important; font-weight: 700; letter-spacing: 1px; margin-top: 1.5rem; margin-bottom: 1rem; text-transform: uppercase; border-bottom: 1px solid rgba(2, 132, 199, 0.2); padding-bottom: 10px; font-family: 'Chakra Petch', sans-serif;}
    h3 { color: #0284c7 !important; font-weight: 700; font-size: 1.3rem; margin-top: 1rem; text-transform: uppercase; letter-spacing: 0.5px; font-family: 'Chakra Petch', sans-serif;}
    
    .stTabs [data-baseweb="tab"] { font-size: 1.1rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 1px; font-family: 'Chakra Petch', sans-serif;}
    .stTabs [aria-selected="true"] { color: #0284c7 !important; border-bottom-color: #0284c7 !important; text-shadow: 0 0 8px rgba(2, 132, 199, 0.3); }
    
    /* Text utilities */
    .text-merah { color: #e11d48; font-weight: 700; }
    .text-kuning { color: #d97706; font-weight: 700; }
    .text-hijau { color: #059669; font-weight: 700; }

    /* Custom CSS Tabel Matrix Light */
    .custom-table-container { overflow-x: auto; margin-top: 15px; background: rgba(255, 255, 255, 0.8); border: 1px solid rgba(14, 165, 233, 0.3); border-radius: 4px; box-shadow: 0 4px 10px rgba(2,132,199,0.05); }
    .custom-table { width: 100%; border-collapse: collapse; font-size: 1rem; text-align: left; color: #0f172a; font-weight: 500;}
    .custom-table th { background-color: rgba(14, 165, 233, 0.1); color: #0369a1; padding: 14px 16px; font-weight: 700; border-bottom: 2px solid rgba(14, 165, 233, 0.3); text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; font-family: 'Chakra Petch', sans-serif;}
    .custom-table td { padding: 14px 16px; border-bottom: 1px solid rgba(2, 132, 199, 0.1); vertical-align: middle; }
    .custom-table tr:hover { background-color: rgba(56, 189, 248, 0.08); }

    /* Styling Kategori Tabel */
    .kategori-tinggi { border: 1px solid #ef4444; color: #b91c1c; padding: 4px 10px; border-radius: 2px; font-weight: 700; display: inline-block; font-size: 0.85rem; background: rgba(239, 68, 68, 0.1); }
    .kategori-sedang { border: 1px solid #f59e0b; color: #b45309; padding: 4px 10px; border-radius: 2px; font-weight: 700; display: inline-block; font-size: 0.85rem; background: rgba(245, 158, 11, 0.1); }
    .kategori-rendah { border: 1px solid #10b981; color: #047857; padding: 4px 10px; border-radius: 2px; font-weight: 700; display: inline-block; font-size: 0.85rem; background: rgba(16, 185, 129, 0.1); }
    
    /* Garis pemisah Tech */
    .tech-line { border: none; border-top: 1px dashed rgba(2, 132, 199, 0.3); margin: 25px 0; }
    
    /* Memaksa text input/select di sidebar berwarna gelap agar terbaca */
    .stSelectbox label, .stMultiSelect label, .stRadio label { color: #0f172a !important; font-weight: 700 !important; font-family: 'Chakra Petch', sans-serif !important;}
    .stMarkdown p { color: #1e293b; }
</style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────────────────────────
#  DATA KEPENDUDUKAN & FASILITAS KESEHATAN 2022-2025
# ───────────────────────────────────────────────────────────────────
WILAYAH = [
    "Bogor","Sukabumi","Cianjur","Bandung","Garut","Tasikmalaya","Ciamis",
    "Kuningan","Cirebon","Majalengka","Sumedang","Indramayu","Subang",
    "Purwakarta","Karawang","Bekasi","Bandung Barat","Pangandaran",
    "Kota Bogor","Kota Sukabumi","Kota Bandung","Kota Cirebon",
    "Kota Bekasi","Kota Depok","Kota Cimahi","Kota Tasikmalaya","Kota Banjar"
]
JENIS = ["Kabupaten"] * 18 + ["Kota"] * 9

PENDUDUK_2022 = [5567, 2807, 2543, 3719, 2627, 1906, 1248, 1196, 2315, 1335, 1167, 1872, 1624, 1029, 2505, 3215, 1847, 432, 1064, 356, 2462, 341, 2590, 2123, 575, 733, 206]
LAJU_2022 = [1.46, 1.69, 1.50, 1.49, 0.92, 1.25, 0.87, 1.38, 1.12, 1.31, 0.72, 1.16, 1.04, 1.75, 1.54, 1.86, 1.86, 1.17, 1.12, 1.65, 0.41, 1.35, 1.04, 1.85, 0.69, 1.37, 1.55]
KEPADATAN_2022 = [1861, 674, 700, 2136, 847, 705, 782, 1003, 2150, 1004, 745, 902, 750, 1036, 1309, 2570, 1439, 383, 9550, 7377, 14776, 8646, 12159, 10622, 13557, 3988, 1576]
RSU_2022 = [26, 9, 5, 11, 7, 1, 5, 11, 10, 3, 3, 11, 9, 9, 23, 49, 6, 1, 17, 6, 23, 9, 43, 22, 7, 8, 4]
RSK_2022 = [3, 0, 0, 0, 0, 1, 1, 1, 2, 2, 0, 1, 1, 2, 2, 4, 3, 0, 5, 0, 15, 1, 3, 4, 1, 5, 0]
PKM_RI_2022 = [30, 10, 39, 5, 33, 19, 23, 6, 11, 9, 17, 10, 25, 7, 31, 11, 6, 11, 0, 0, 7, 0, 0, 0, 0, 9, 2]
PKM_NRI_2022 = [71, 48, 8, 57, 34, 21, 14, 31, 49, 23, 18, 39, 15, 13, 19, 35, 26, 4, 25, 15, 73, 22, 48, 38, 13, 13, 8]
KLINIK_2022 = [188, 96, 66, 177, 139, 66, 60, 23, 75, 62, 82, 61, 113, 88, 222, 318, 77, 25, 125, 34, 187, 76, 363, 193, 45, 49, 19]
POSYANDU_2022 = [5141, 3680, 2945, 4350, 4334, 2392, 1612, 1436, 2706, 1503, 1713, 2363, 1925, 1050, 2375, 2883, 2340, 532, 982, 461, 1999, 345, 1615, 1063, 411, 909, 200]

PENDUDUK = {
    2023: [5627,2802.4,2558.1,3721.1,2683.7,1907.1,1251.5,1201.8,2360.4,1340.6,1178.2,1894.3,1649.8,1037.1,2526,3237.4,1859.6,431.5,1070.7,360.6,2506.6,342,2627.2,2145.4,590.8,741.8,207.5],
    2024: [5682.3,2828,2585,3753.1,2717,1920.9,1259.2,1213.9,2388,1352.5,1187.1,1914,1663.2,1050.3,2554.4,3273.9,1884.2,434.1,1078.4,365.7,2528.2,344.9,2644.1,2163.6,598.7,750.7,209.8],
    2025: [5721.6,2852.1,2610.3,3783.2,2748.7,1933.8,1266.3,1225.5,2413.8,1363.8,1195.5,1932.5,1675.5,1063,2581.3,3303,1907.8,436.5,1083.8,370.7,2548.8,347.5,2648.3,2168,606.4,759.4,212]
}
LAJU = {
    2023: [1.32,1.02,1.17,0.97,1.36,0.81,0.66,1.05,1.42,0.97,0.81,1.18,1.23,1.41,1.28,1.44,1.43,0.67,0.96,1.48,0.92,0.94,1.18,1.55,1.41,1.29,1.17],
    2024: [1.23,0.99,1.14,0.94,1.33,0.79,0.65,1.04,1.35,0.95,0.79,1.14,1.12,1.38,1.24,1.35,1.40,0.65,0.89,1.46,0.91,0.91,1.04,1.37,1.39,1.27,1.15],
    2025: [1.12,0.96,1.10,0.91,1.30,0.76,0.63,1.02,1.30,0.92,0.77,1.10,1.04,1.34,1.20,1.26,1.37,0.63,0.81,1.44,0.89,0.88,0.85,1.12,1.37,1.24,1.13]
}
KEPADATAN = {
    2023: [1881,673,704,2138,865,705,784,1007,2202,1008,752,912,762,1044,1320,2588,1449,382,9614,7465,15047,8671,12332,10732,13924,4033,1584],
    2024: [1899,679,712,2156,876,710,789,1018,2228,1017,758,922,768,1058,1335,2617,1468,385,9683,7571,15176,8744,12411,10823,14110,4081,1601],
    2025: [1912,685,719,2173,886,715,793,1027,2252,1025,763,931,774,1070,1349,2640,1486,387,9731,7673,15300,8812,12431,10845,14291,4128,1618]
}
RSU = {
    2023: [27,9,5,15,8,1,5,11,10,5,3,11,10,9,24,50,6,1,17,6,26,9,45,24,7,8,4],
    2024: [28,9,7,17,9,2,5,12,11,5,5,11,10,9,25,51,6,1,18,6,27,9,46,24,7,9,4],
    2025: [31,9,8,17,9,2,5,11,12,6,5,11,11,10,27,51,6,1,18,6,27,9,47,24,7,9,4]
}
RSK = {
    2023: [4,0,0,0,0,1,1,1,2,1,0,1,1,2,2,4,5,0,5,0,15,1,3,4,1,6,0],
    2024: [3,0,0,0,0,1,1,1,2,1,0,1,1,2,1,4,6,0,4,0,15,1,2,4,1,6,0],
    2025: [1,0,0,0,0,1,1,1,2,0,0,1,1,1,2,4,6,0,4,0,15,1,2,4,1,6,0]
}
PKM_RI = {
    2023: [30,10,8,5,33,19,23,6,11,9,17,10,25,7,35,4,6,11,0,0,0,0,0,0,0,9,2],
    2024: [31,10,8,4,33,21,23,6,11,9,17,10,25,9,35,4,6,11,0,0,0,0,0,0,0,9,2],
    2025: [30,10,8,4,33,21,24,6,11,9,17,10,25,9,40,4,7,11,0,0,0,0,0,0,0,9,2]
}
PKM_NRI = {
    2023: [71,48,39,57,34,21,14,31,49,23,18,39,15,13,15,47,26,4,25,15,80,22,48,38,13,13,8],
    2024: [70,48,39,58,34,19,14,31,49,23,18,39,15,11,15,47,26,4,25,15,80,22,48,38,13,13,8],
    2025: [71,48,39,58,34,19,13,31,49,23,18,39,15,11,10,51,25,4,25,15,80,22,53,38,13,13,8]
}
KLINIK = {
    2023: [188,96,66,177,139,66,60,23,75,62,82,61,113,88,222,318,77,25,125,34,187,76,363,193,45,49,19],
    2024: [267,105,71,199,112,69,69,32,98,70,88,67,108,103,293,417,88,28,160,39,257,70,304,279,54,62,19],
    2025: [286,105,71,221,130,74,77,31,104,64,90,60,111,105,333,524,90,29,156,37,289,69,404,275,54,62,19]
}
POSYANDU = {
    2023: [5141,3680,2945,4350,4334,2392,1612,1436,2706,1503,1713,2363,1925,1050,2375,2883,2340,532,982,461,1999,345,1615,1063,411,909,200],
    2024: [5152,3568,2950,4355,4379,2429,1618,1439,2712,1506,1718,2365,1928,1062,2388,2951,2343,531,983,461,2000,345,1617,1071,413,913,206],
    2025: [5169,3583,2950,4364,4403,2433,1620,1443,2716,1509,1721,2369,1931,1070,2395,2967,2347,531,1000,462,2003,350,1622,1081,418,918,208]
}

# ───────────────────────────────────────────────────────────────────
#  FUNGSI BANTU: BUAT DATAFRAME
# ───────────────────────────────────────────────────────────────────
@st.cache_data
def buat_df():
    rows = []
    for tahun in [2023, 2024, 2025]:
        for i, wil in enumerate(WILAYAH):
            pkm_total = PKM_RI[tahun][i] + PKM_NRI[tahun][i]
            fsk_total = RSU[tahun][i] + RSK[tahun][i] + pkm_total + KLINIK[tahun][i]
            pop = PENDUDUK[tahun][i]
            rasio_rsu = (RSU[tahun][i] / pop) * 100 if pop > 0 else 0
            rasio_pkm = (pkm_total / pop) * 100 if pop > 0 else 0
            rows.append({
                "Wilayah": wil,
                "Jenis": JENIS[i],
                "Tahun": tahun,
                "Penduduk_Ribu": pop,
                "Penduduk_Jiwa": round(pop * 1000),
                "Laju_Pertumbuhan": LAJU[tahun][i],
                "Kepadatan": KEPADATAN[tahun][i],
                "RSU": RSU[tahun][i],
                "RSK": RSK[tahun][i],
                "Puskesmas_RI": PKM_RI[tahun][i],
                "Puskesmas_NRI": PKM_NRI[tahun][i],
                "Puskesmas_Total": pkm_total,
                "Klinik_Pratama": KLINIK[tahun][i],
                "Posyandu": POSYANDU[tahun][i],
                "Total_Faskes": fsk_total,
                "Rasio_RSU_100rb": round(rasio_rsu, 3),
                "Rasio_PKM_100rb": round(rasio_pkm, 3),
            })
    return pd.DataFrame(rows)

df_all = buat_df()


# ───────────────────────────────────────────────────────────────────
#  SIDEBAR / KONTROL HUD
# ───────────────────────────────────────────────────────────────────
with st.sidebar:
    # --- AI AVATAR FUTURISTIC LIGHT ---
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <div class="avatar-wrapper">
            <div class="avatar-container">
                <img src="https://api.dicebear.com/7.x/bottts/svg?seed=AeroBlue&backgroundColor=e0f2fe&baseColor=0ea5e9" alt="AI Avatar" class="avatar-img">
            </div>
        </div>
        <h2 style="color: #0284c7 !important; margin-top: 15px; font-size: 1.8rem; margin-bottom: 2px; border:none; padding:0; text-shadow: 0 0 10px rgba(2,132,199,0.2);">POPINE SYSTEM</h2>
        <p style="color: #0ea5e9; font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; font-weight:700;">Population Insight for Health Care</p>
    </div>
    <hr class="tech-line">
    """, unsafe_allow_html=True)
    
    # KETERANGAN FITUR TAHUN
    st.markdown("""
    <div style="background: rgba(255,255,255,0.8); border: 1px solid rgba(14, 165, 233, 0.3); border-radius: 4px; padding: 12px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(2,132,199,0.05); border-left: 4px solid #0ea5e9;">
        <small style="color: #334155; font-size: 0.85rem; line-height: 1.4; font-weight:600;">[SYS.INFO] <b>Filter Siklus:</b><br>Gunakan dropdown di bawah untuk memilih tahun data yang akan dirender di semua visualisasi.</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 1rem; color: #0f172a !important; margin-bottom:-10px;'>🗓️ TAHUN SIKLUS</h3>", unsafe_allow_html=True)
    tahun_filter = st.multiselect(
        "Pilih Tahun",
        options=[2023, 2024, 2025],
        default=[2023, 2024, 2025],
        label_visibility="collapsed"
    )
    
    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)
    
    # KETERANGAN FITUR WILAYAH
    st.markdown("""
    <div style="background: rgba(255,255,255,0.8); border: 1px solid rgba(14, 165, 233, 0.3); border-radius: 4px; padding: 12px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(2,132,199,0.05); border-left: 4px solid #8b5cf6;">
        <small style="color: #334155; font-size: 0.85rem; line-height: 1.4; font-weight:600;">[SYS.INFO] <b>Sektor Wilayah:</b><br>Pilih spesifik kabupaten atau kota untuk memfokuskan analisis pemetaan infrastruktur.</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='font-size: 1rem; color: #0f172a !important; margin-bottom:-10px;'>🗺️ SEKTOR WILAYAH</h3>", unsafe_allow_html=True)
    jenis_filter = st.radio(
        "Pilih Zona",
        ["Semua", "Kabupaten saja", "Kota saja"],
        index=0,
        label_visibility="collapsed"
    )
    if jenis_filter == "Kabupaten saja":
        wil_tersedia = [w for w, j in zip(WILAYAH, JENIS) if j == "Kabupaten"]
    elif jenis_filter == "Kota saja":
        wil_tersedia = [w for w, j in zip(WILAYAH, JENIS) if j == "Kota"]
    else:
        wil_tersedia = WILAYAH.copy()

    wilayah_pilih = st.multiselect(
        "Pilih Sektor",
        options=wil_tersedia,
        default=wil_tersedia[:10],
        label_visibility="collapsed"
    )
    
    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)
    
    # KETERANGAN FITUR VARIABEL
    st.markdown("""
    <div style="background: rgba(255,255,255,0.8); border: 1px solid rgba(14, 165, 233, 0.3); border-radius: 4px; padding: 12px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(2,132,199,0.05); border-left: 4px solid #10b981;">
        <small style="color: #334155; font-size: 0.85rem; line-height: 1.4; font-weight:600;">[SYS.INFO] <b>Parameter Metrik:</b><br>Pilih indikator (contoh: Populasi, RSU, Klinik) yang ingin ditampilkan pada grafik bar utama.</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='font-size: 1rem; color: #0f172a !important; margin-bottom:-10px;'>📊 PARAMETER METRIK</h3>", unsafe_allow_html=True)
    var_map = {
        "Jumlah Penduduk (ribu jiwa)"  : "Penduduk_Ribu",
        "Kepadatan Penduduk (jiwa/km²)": "Kepadatan",
        "Laju Pertumbuhan Penduduk (%)" : "Laju_Pertumbuhan",
        "Rumah Sakit Umum"             : "RSU",
        "Rumah Sakit Khusus"           : "RSK",
        "Puskesmas (Total)"            : "Puskesmas_Total",
        "Klinik Pratama"               : "Klinik_Pratama",
        "Posyandu"                     : "Posyandu",
        "Total Fasilitas Kesehatan"    : "Total_Faskes",
        "Rasio RSU per 100rb Penduduk" : "Rasio_RSU_100rb",
    }
    var_label = st.selectbox(
        "Pilih Indikator", 
        list(var_map.keys()), 
        index=0,
        label_visibility="collapsed"
    )
    var_col   = var_map[var_label]

    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)
    st.markdown("""
    <div style="color: #334155; font-size: 0.85rem; line-height: 1.8; background: rgba(255,255,255,0.6); padding: 10px; border-radius: 4px; border: 1px solid rgba(2,132,199,0.1);">
        <b>💡 INDEKS STATUS HUB:</b><br>
        <span class="text-merah">🔴 KRITIS</span> : Eksekusi Segera<br>
        <span class="text-kuning">🟡 WARNING</span> : Monitor Ketat<br>
        <span class="text-hijau">🟢 STABIL</span> : Parameter Aman
    </div>
    """, unsafe_allow_html=True)

# Terapkan filter
if not tahun_filter:
    tahun_filter = [2025]
if not wilayah_pilih:
    wilayah_pilih = wil_tersedia[:10]

df = df_all[
    (df_all["Tahun"].isin(tahun_filter)) &
    (df_all["Wilayah"].isin(wilayah_pilih))
].copy()

d25_all = df_all[df_all["Tahun"] == 2025]
d23_all = df_all[df_all["Tahun"] == 2023]


# ───────────────────────────────────────────────────────────────────
#  HEADER UTAMA (LIGHT HUD STYLE)
# ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* 🔥 paksa semua elemen dalam header putih (anti override global) */
div.header-box, 
div.header-box * {
    color: #ffffff !important;
}

/* container */
div.header-box {
    text-align: center;
    padding: 25px;
    border-radius: 14px;
    background: linear-gradient(135deg, #1d4ed8, #38bdf8);
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

/* status */
div.header-box .header-status {
    font-size: 0.9rem;
    opacity: 0.9;
    margin-bottom: 8px;
    color: #e0f2fe !important;
}

/* title */
div.header-box .header-title {
    font-weight: 700;
    letter-spacing: 1px;
    margin: 12px 0;
    font-size: 28px;
}

/* subtitle */
div.header-box p {
    margin: 0;
    font-size: 14px;
    opacity: 0.9;
}
</style>

<div class="header-box">
  <div class="header-status">
    [ KONEKSI STABIL : SINKRONISASI DATA AKTIF ]
  </div>
  
  <h1 class="header-title">
    MONITORING KEPENDUDUKAN & FASKES JABAR
  </h1>
  
  <p>
    Sistem Pemetaan Fasilitas Kesehatan Cerdas Berbasis Matriks Demografi &nbsp;|&nbsp; 
    <span style="opacity:0.85;">
      SUMBER LOG: BPS 2023–2025
    </span>
  </p>
</div>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────────────────────────
#  KARTU RINGKASAN (KPI)
# ───────────────────────────────────────────────────────────────────
total_pop25   = d25_all["Penduduk_Jiwa"].sum()
total_rsu25   = d25_all["RSU"].sum()
total_pkm25   = d25_all["Puskesmas_Total"].sum()
total_klinik25= d25_all["Klinik_Pratama"].sum()
total_posyd25 = d25_all["Posyandu"].sum()
KATEGORI_pop     = ((total_pop25 - d23_all["Penduduk_Jiwa"].sum()) / d23_all["Penduduk_Jiwa"].sum()) * 100
KATEGORI_rsu     = total_rsu25 - d23_all["RSU"].sum()
KATEGORI_klinik  = total_klinik25 - d23_all["Klinik_Pratama"].sum()

c1, c2, c3, c4, c5 = st.columns(5)
for col, judul, angka, ket, warna in [
    (c1, "POPULASI GLOBAL '25", f"{total_pop25/1_000_000:.2f} JT", f"↑ +{KATEGORI_pop:.1f}% DARI 2023", "#0284c7"), 
    (c2, "RS UMUM AKTIF",       str(total_rsu25),                  f"↑ +{KATEGORI_rsu} UNIT BARU",    "#0ea5e9"), 
    (c3, "JARINGAN PUSKESMAS",  str(total_pkm25),                  "STATUS: TERDISTRIBUSI",        "#059669"), 
    (c4, "KLINIK PRATAMA",      str(total_klinik25),               f"↑ +{KATEGORI_klinik} DARI 2023", "#d97706"), 
    (c5, "NODE POSYANDU",       str(total_posyd25),                "JARINGAN MIKRO AKTIF",         "#e11d48"), 
]:
    with col:
        st.markdown(f"""
        <div class="kartu" style="border-top: 4px solid {warna}; --cyan-color: {warna};">
          <div class="label" style="color: {warna};">{judul}</div>
          <div class="angka">{angka}</div>
          <div class="KATEGORI" style="color:#64748b;">{ket}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  TAB NAVIGASI
# ═══════════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 TREN MATRIKS",
    "📊 KOMPARASI SEKTOR",
    "🎯 KLASTER AI",
    "🏥 DETEKSI KECUKUPAN",
    "💡 TRANSMISI INSIGHT",
])

# Template standar untuk chart Plotly agar selaras dengan tema Light Hologram
plot_layout_light = dict(
    plot_bgcolor="rgba(255,255,255,0.4)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#0f172a", family="Rajdhani", size=13, weight="bold"),
    xaxis=dict(gridcolor="rgba(2, 132, 199, 0.1)", zerolinecolor="rgba(2, 132, 199, 0.2)"),
    yaxis=dict(gridcolor="rgba(2, 132, 199, 0.1)", zerolinecolor="rgba(2, 132, 199, 0.2)"),
)


# ═══════════════════════════════════════════════════════════════════
#  TAB 1 – TREN & PERTUMBUHAN
# ═══════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("## TREN DEMOGRAFI & INFTRASTRUKTUR")
    
    st.markdown("""
    <div class="kotak-general kotak-biru">
    [POPINE LOG] Visualisasi lintasan waktu dari pertumbuhan populasi berbanding lurus dengan kapasitas fisik infrastruktur kesehatan.
    </div>
    """, unsafe_allow_html=True)

    k1, k2 = st.columns(2)

    with k1:
        st.markdown("### LINTASAN POPULASI GLOBAL (JABAR)")
        tot_year = df_all.groupby("Tahun")["Penduduk_Ribu"].sum().reset_index()
        tot_year["Juta"] = tot_year["Penduduk_Ribu"] / 1000
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=tot_year["Tahun"], y=tot_year["Juta"],
            mode="lines+markers+text",
            text=[f"{v:.2f} JT" for v in tot_year["Juta"]],
            textposition="top center",
            line=dict(color="#0284c7", width=3.5, shape='spline'),
            marker=dict(size=12, color="#0ea5e9", line=dict(width=2, color="#ffffff")),
            fill="tozeroy", fillcolor="rgba(14, 165, 233, 0.15)",
            textfont=dict(color="#0369a1", family="Rajdhani", size=14)
        ))
        fig.update_layout(**plot_layout_light)
        fig.update_layout(height=380, xaxis_title="TAHUN SIKLUS", yaxis_title="POPULASI (JUTA)", margin=dict(t=30, l=0, r=0, b=0))
        fig.update_xaxes(tickvals=[2023,2024,2025])
        st.plotly_chart(fig, use_container_width=True)

    with k2:
        st.markdown("### PERTUMBUHAN INFRASTRUKTUR")
        agg = df_all.groupby("Tahun")[["RSU","Puskesmas_Total","Klinik_Pratama"]].sum().reset_index()
        fig2 = go.Figure()
        for col_name, warna, lab in [
            ("RSU","#e11d48","RS UMUM"),
            ("Puskesmas_Total","#059669","PUSKESMAS"),
            ("Klinik_Pratama","#d97706","KLINIK PRATAMA"),
        ]:
            fig2.add_trace(go.Scatter(
                x=agg["Tahun"], y=agg[col_name],
                mode="lines+markers", name=lab,
                line=dict(color=warna, width=3, shape='spline'), 
                marker=dict(size=10, line=dict(width=2, color="#ffffff")),
            ))
        fig2.update_layout(**plot_layout_light)
        fig2.update_layout(height=380, legend=dict(orientation="h", yanchor="bottom", y=1.02), margin=dict(t=30, l=0, r=0, b=0))
        fig2.update_xaxes(tickvals=[2023,2024,2025])
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)

    st.markdown(f"### DINAMIKA {var_label.upper()} PER SEKTOR")
    if len(wilayah_pilih) > 15:
        st.info("ℹ️ Terdapat terlalu banyak noise visual. Batasi pemilihan maksimal 15 sektor di panel kiri.")
    else:
        df_tren = df_all[df_all["Wilayah"].isin(wilayah_pilih)].copy()
        fig3 = px.line(
            df_tren, x="Tahun", y=var_col, color="Wilayah", markers=True,
            color_discrete_sequence=["#0284c7", "#e11d48", "#059669", "#d97706", "#7c3aed", "#0891b2"]
        )
        fig3.update_layout(**plot_layout_light)
        fig3.update_layout(height=450, legend=dict(orientation="h", yanchor="bottom", y=-0.3), margin=dict(t=30, l=0, r=0, b=0))
        fig3.update_xaxes(tickvals=[2023,2024,2025])
        fig3.update_traces(line=dict(width=3), marker=dict(size=8, opacity=0.9, line=dict(width=1, color="white")))
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)

    st.markdown("### MATRIKS PERTUMBUHAN PENDUDUK SEKTORAL")
    
    def get_population(wil, tahun):
        if tahun == 2022:
            idx = WILAYAH.index(wil) if wil in WILAYAH else -1
            return PENDUDUK_2022[idx] if idx >= 0 else None
        else:
            data = df_all[(df_all["Wilayah"]==wil) & (df_all["Tahun"]==tahun)]["Penduduk_Ribu"]
            return data.values[0] if len(data) > 0 else None
    
    def get_kategori_html(pct):
        if pct > 2.5: return f'<span class="kategori-tinggi">CRITICAL ({pct:.2f}%)</span>'
        elif pct > 1.5: return f'<span class="kategori-sedang">WARNING ({pct:.2f}%)</span>'
        else: return f'<span class="kategori-rendah">STABLE ({pct:.2f}%)</span>'
    
    tbl = []
    tahun_list = sorted([t for t in tahun_filter if t in [2023,2024,2025]])
    for wil in wilayah_pilih:
        row_data = {"SEKTOR": wil}
        pop_2022 = get_population(wil, 2022)
        for tahun in tahun_list:
            pop = get_population(wil, tahun)
            if pop is not None:
                row_data[f"POPULASI {tahun}"] = f"{pop:,.1f}K"
                if tahun == 2023 and pop_2022 is not None:
                    pct = ((pop - pop_2022) / pop_2022) * 100 if pop_2022 > 0 else 0
                    row_data[f"KATEGORI {tahun}"] = get_kategori_html(pct)
                elif tahun > 2023:
                    prev_pop = get_population(wil, tahun-1)
                    if prev_pop is not None:
                        pct = ((pop - prev_pop) / prev_pop) * 100 if prev_pop > 0 else 0
                        row_data[f"KATEGORI {tahun}"] = get_kategori_html(pct)
                    else:
                        row_data[f"KATEGORI {tahun}"] = "-"
                else:
                    row_data[f"KATEGORI {tahun}"] = "-"
            else:
                row_data[f"POPULASI {tahun}"] = "-"
                row_data[f"KATEGORI {tahun}"] = "-"
        if len(row_data) > 1: tbl.append(row_data)
    
    if tbl:
        df_tabel = pd.DataFrame(tbl)
        html_table = '<div class="custom-table-container"><table class="custom-table"><tr>'
        for col in df_tabel.columns: html_table += f'<th>{col}</th>'
        html_table += '</tr>'
        for _, row in df_tabel.iterrows():
            html_table += '<tr>'
            for col in df_tabel.columns: html_table += f'<td>{row[col]}</td>'
            html_table += '</tr>'
        html_table += '</table></div>'
        st.markdown(html_table, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  TAB 2 – PERBANDINGAN ANTAR WILAYAH
# ═══════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("## KOMPARASI SEKTOR REGIONAL")
    st.markdown("""<div class="kotak-general kotak-ungu">[POPINE LOG] Pemindaian silang antar sektor aktif. Melacak anomali sebaran distribusi kapasitas penampungan.</div>""", unsafe_allow_html=True)

    tahun_banding = st.select_slider("Sinkronisasi Siklus Waktu:", options=[2023,2024,2025], value=2025)
    df_b = df_all[(df_all["Tahun"]==tahun_banding) & (df_all["Wilayah"].isin(wilayah_pilih))].copy()

    # --- GRAFIK 1: BAR CHART ---
    df_sort = df_b.sort_values(var_col, ascending=True)
    fig_bar = px.bar(
        df_sort, x=var_col, y="Wilayah", orientation="h",
        text=var_col, color_discrete_sequence=["#0ea5e9"]
    )
    fig_bar.update_traces(texttemplate="%{text:,.0f}", textposition="outside", textfont=dict(color="#0f172a"), marker=dict(line=dict(color="#0284c7", width=1)))
    
    fig_bar.update_layout(**plot_layout_light)
    fig_bar.update_layout(
        title=dict(text=f"DISTRIBUSI {var_label.upper()} [{tahun_banding}]", font=dict(size=18, color="#0369a1")),
        height=max(500, len(wilayah_pilih)*32),
        margin=dict(l=0, r=40, t=50, b=0)
    )
    fig_bar.update_xaxes(showgrid=True, gridcolor="rgba(2, 132, 199, 0.1)")
    fig_bar.update_yaxes(gridcolor="rgba(0,0,0,0)") 
    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)

    # --- GRAFIK 2: KOMPOSISI ---
    st.markdown(f"### KOMPOSISI INFRASTRUKTUR PER SEKTOR [{tahun_banding}]")
    df_melt = df_b[["Wilayah","RSU","RSK","Puskesmas_Total","Klinik_Pratama"]].melt(id_vars="Wilayah", var_name="Jenis", value_name="Jumlah")
    fig_stk = px.bar(
        df_melt.merge(df_b[["Wilayah","Total_Faskes"]]).sort_values("Total_Faskes", ascending=False),
        x="Wilayah", y="Jumlah", color="Jenis",
        color_discrete_sequence=["#0284c7", "#8b5cf6", "#10b981", "#f59e0b"],
    )
    
    fig_stk.update_layout(**plot_layout_light)
    fig_stk.update_layout(
        height=500, xaxis_tickangle=-45,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, title=""),
        margin=dict(t=20)
    )
    fig_stk.update_xaxes(gridcolor="rgba(0,0,0,0)") 
    st.plotly_chart(fig_stk, use_container_width=True)

    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)

    # --- GRAFIK 3: SCATTER PLOT ---
    st.markdown(f"### PEMETAAN KOORDINAT: POPULASI VS KAPASITAS [{tahun_banding}]")
    st.markdown("""<div class="kotak-general kotak-kuning" style="font-size: 0.95rem;"><b>RADAR SCAN:</b> Kuadran kanan-bawah mendeteksi rasio kritis (populasi tinggi, infrastruktur minim). Radius memproyeksikan densitas node Posyandu.</div>""", unsafe_allow_html=True)
    
    fig_sc = px.scatter(
        df_b, x="Penduduk_Ribu", y="Total_Faskes",
        size="Posyandu", color="Jenis", text="Wilayah",
        color_discrete_map={"Kabupaten":"#0284c7","Kota":"#e11d48"},
        labels={"Penduduk_Ribu":"POPULASI (RIBU)","Total_Faskes":"TOTAL KAPASITAS FISIK","Jenis":"TIPE ZONA"},
    )
    fig_sc.update_traces(
        textposition="top center", textfont_size=12, 
        textfont_color="#0f172a", marker=dict(line=dict(width=1.5, color="#ffffff"), opacity=0.85)
    )
    
    fig_sc.update_layout(**plot_layout_light)
    fig_sc.update_layout(height=550, margin=dict(t=20))
    st.plotly_chart(fig_sc, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════
#  TAB 3 – ANALISIS KLASTER
# ═══════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("## PENGELOMPOKAN WILAYAH ")
    st.markdown("""<div class="kotak-general kotak-hijau">[POPINE AI ENGINE] Memproses segmentasi wilayah berdasarkan multidimensi data kepadatan dan ketersediaan layanan untuk menemukan pola defisit tak kasat mata.</div>""", unsafe_allow_html=True)

    tahun_kl = st.select_slider("Sinkronisasi Siklus Pembelajaran:", options=[2023,2024,2025], value=2025, key="kl")
    df_kl = df_all[df_all["Tahun"]==tahun_kl].copy()

    X = df_kl[["Penduduk_Ribu","Kepadatan","RSU","Puskesmas_Total","Klinik_Pratama","Rasio_RSU_100rb","Rasio_PKM_100rb"]].fillna(0)
    X_scaled = StandardScaler().fit_transform(X)
    km = KMeans(n_clusters=3, random_state=42, n_init=10)
    df_kl["Klaster_Raw"] = km.fit_predict(X_scaled)

    rata = df_kl.groupby("Klaster_Raw")["Rasio_RSU_100rb"].mean().sort_values()
    urutan = rata.index.tolist()
    lbl = {
        urutan[0]: "PRIORITAS TINGGI [DEFISIT]",
        urutan[1]: "PRIORITAS SEDANG [MONITOR]",
        urutan[2]: "PRIORITAS RENDAH [STABIL]",
    }
    df_kl["Klaster"] = df_kl["Klaster_Raw"].map(lbl)
    warna_kl = {
        "PRIORITAS TINGGI [DEFISIT]": "#ef4444",
        "PRIORITAS SEDANG [MONITOR]": "#f59e0b",
        "PRIORITAS RENDAH [STABIL]" : "#10b981",
    }

    fig_kl = px.scatter(
        df_kl, x="Penduduk_Ribu", y="Rasio_RSU_100rb",
        color="Klaster", size="Total_Faskes", text="Wilayah",
        color_discrete_map=warna_kl,
        labels={"Penduduk_Ribu":"POPULASI (RIBU)","Rasio_RSU_100rb":"RASIO RS UMUM/100K","Klaster":"KELAS SEGMEN"}
    )
    fig_kl.update_traces(
        textposition="top center", textfont_size=11, textfont_color="#0f172a",
        marker=dict(line=dict(width=1, color="#ffffff"), opacity=0.85)
    )
    
    fig_kl.update_layout(**plot_layout_light)
    fig_kl.update_layout(height=550, legend=dict(orientation="h", yanchor="bottom", y=-0.25, title=""), margin=dict(t=20))
    st.plotly_chart(fig_kl, use_container_width=True)

    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)

    st.markdown("### PEMETAAN ZONA HASIL PENGELOMPOKAN WILAYAH")
    for label, bg, bc in [
        ("PRIORITAS TINGGI [DEFISIT]", "rgba(239,68,68,0.1)", "#ef4444"),
        ("PRIORITAS SEDANG [MONITOR]", "rgba(245,158,11,0.1)", "#f59e0b"),
        ("PRIORITAS RENDAH [STABIL]",  "rgba(16,185,129,0.1)", "#10b981"),
    ]:
        angg = df_kl[df_kl["Klaster"]==label]["Wilayah"].tolist()
        if angg:
            badges = " ".join(
                f'<span style="background:white; border:1px solid {bc}; color:{bc}; '
                f'padding:6px 14px; border-radius:4px; font-size:0.9rem; font-weight:700; '
                f'margin:4px 4px 4px 0; display:inline-block; box-shadow:0 2px 5px {bg};">{w}</span>'
                for w in angg
            )
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.7); border-radius:4px; padding:20px 24px;
                        border: 1px solid rgba(2, 132, 199, 0.1); border-left:5px solid {bc}; margin:16px 0;
                        box-shadow: 0 4px 10px rgba(0,0,0,0.03);">
              <b style="color:{bc}; font-size:1.1rem; display:block; margin-bottom:12px; letter-spacing:1px; font-family: 'Chakra Petch', sans-serif;">{label}</b>
              <div>{badges}</div>
            </div>
            """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  TAB 4 – KECUKUPAN FASILITAS KESEHATAN
# ═══════════════════════════════════════════════════════════════════
with tab4:
    st.markdown("## DETEKSI STANDAR KELAYAKAN GLOBAL")
    st.markdown("""
    <div class="kotak-general kotak-biru">
    <b>REFERENSI PROTOKOL (WHO & KEMENKES RI):</b><br>
    > <b>RS UMUM:</b> Threshold minimal <b>0.42</b> per 100K populasi.<br>
    > <b>PUSKESMAS:</b> Threshold minimal <b>3.33</b> per 100K populasi.
    </div>
    """, unsafe_allow_html=True)

    tahun_cek = st.select_slider("Target Resolusi Tahun:", options=[2023,2024,2025], value=2025, key="cek")
    df_cek = df_all[(df_all["Tahun"]==tahun_cek) & (df_all["Wilayah"].isin(wilayah_pilih))].copy()

    STD_RSU = 0.42
    STD_PKM = 3.33
    df_cek["Status_RSU"] = df_cek["Rasio_RSU_100rb"].apply(lambda x: "DEFISIT" if x < STD_RSU else "AMAN")
    df_cek["Status_PKM"] = df_cek["Rasio_PKM_100rb"].apply(lambda x: "DEFISIT" if x < STD_PKM else "AMAN")

    k1, k2 = st.columns(2)
    with k1:
        n = (df_cek["Status_RSU"]=="DEFISIT").sum()
        st.markdown(f"""
        <div class="kotak-general kotak-merah" style="text-align: center; padding: 30px 20px;">
        <div style="font-size: 1.1rem; color:#1e293b; font-weight:700; letter-spacing:2px; font-family: 'Chakra Petch', sans-serif;">ANOMALI RS UMUM [{tahun_cek}]</div>
        <div style="font-size: 4rem; font-weight: 700; color: #ef4444; line-height:1.2; margin: 10px 0;">{n} <span style="font-size: 1.5rem; color: #94a3b8;">/ {len(df_cek)}</span></div>
        <div style="font-size: 0.95rem; color:#475569; font-weight:600;">Sektor Berstatus Kritis (Di Bawah Threshold)</div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        n2 = (df_cek["Status_PKM"]=="DEFISIT").sum()
        st.markdown(f"""
        <div class="kotak-general kotak-kuning" style="text-align: center; padding: 30px 20px;">
        <div style="font-size: 1.1rem; color:#1e293b; font-weight:700; letter-spacing:2px; font-family: 'Chakra Petch', sans-serif;">ANOMALI PUSKESMAS [{tahun_cek}]</div>
        <div style="font-size: 4rem; font-weight: 700; color: #f59e0b; line-height:1.2; margin: 10px 0;">{n2} <span style="font-size: 1.5rem; color: #94a3b8;">/ {len(df_cek)}</span></div>
        <div style="font-size: 0.95rem; color:#475569; font-weight:600;">Membutuhkan Penetrasi Jaringan Layanan Primer</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"### PEMINDAIAN KESENJANGAN RS UMUM [{tahun_cek}]")
    df_cs = df_cek.sort_values("Rasio_RSU_100rb")
    fig_h = go.Figure(go.Bar(
        x=df_cs["Rasio_RSU_100rb"], y=df_cs["Wilayah"], orientation="h",
        marker_color=["#ef4444" if v < STD_RSU else "#10b981" for v in df_cs["Rasio_RSU_100rb"]],
        text=[f"{v:.3f}" for v in df_cs["Rasio_RSU_100rb"]], textposition="outside",
        textfont=dict(color="#0f172a", family="Rajdhani", size=13),
        marker_line_width=0
    ))
    fig_h.add_vline(x=STD_RSU, line_dash="dash", line_color="#f59e0b", line_width=3,
                    annotation_text=f"THRESHOLD MINIMAL ({STD_RSU})", annotation_position="top right", annotation_font_color="#b45309")
    
    fig_h.update_layout(**plot_layout_light)
    fig_h.update_layout(height=max(500, len(wilayah_pilih)*32), margin=dict(l=0, r=40, t=20, b=0))
    st.plotly_chart(fig_h, use_container_width=True)

    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)

    st.markdown("### DATA LOG INFRASTRUKTUR")
    tbl_c = df_cek[["Wilayah","Penduduk_Ribu","RSU","Puskesmas_Total","Rasio_RSU_100rb","Rasio_PKM_100rb","Status_RSU","Status_PKM"]].sort_values("Rasio_RSU_100rb")
    html_c = '<div class="custom-table-container"><table class="custom-table"><tr><th>SEKTOR</th><th>POPULASI (K)</th><th>RSU</th><th>PKM</th><th>RASIO RSU</th><th>RASIO PKM</th><th>STATUS RSU</th><th>STATUS PKM</th></tr>'
    
    for _, row in tbl_c.iterrows():
        html_c += '<tr>'
        html_c += f'<td style="color:#0369a1; font-weight:700;">{row["Wilayah"]}</td>'
        html_c += f'<td>{row["Penduduk_Ribu"]:.1f}</td><td>{row["RSU"]}</td><td>{row["Puskesmas_Total"]}</td>'
        html_c += f'<td>{row["Rasio_RSU_100rb"]:.3f}</td><td>{row["Rasio_PKM_100rb"]:.3f}</td>'
        
        # Status RSU
        bg_rs, col_rs = ("rgba(239, 68, 68, 0.15)", "#b91c1c") if row["Status_RSU"] == "DEFISIT" else ("rgba(16, 185, 129, 0.15)", "#047857")
        html_c += f'<td><span style="background:{bg_rs}; color:{col_rs}; border:1px solid rgba({239 if row["Status_RSU"]=="DEFISIT" else 16}, {68 if row["Status_RSU"]=="DEFISIT" else 185}, {68 if row["Status_RSU"]=="DEFISIT" else 129}, 0.5); padding:4px 10px; border-radius:2px; font-size:0.85rem; font-weight:700;">{row["Status_RSU"]}</span></td>'
        
        # Status PKM
        bg_pkm, col_pkm = ("rgba(239, 68, 68, 0.15)", "#b91c1c") if row["Status_PKM"] == "DEFISIT" else ("rgba(16, 185, 129, 0.15)", "#047857")
        html_c += f'<td><span style="background:{bg_pkm}; color:{col_pkm}; border:1px solid rgba({239 if row["Status_PKM"]=="DEFISIT" else 16}, {68 if row["Status_PKM"]=="DEFISIT" else 185}, {68 if row["Status_PKM"]=="DEFISIT" else 129}, 0.5); padding:4px 10px; border-radius:2px; font-size:0.85rem; font-weight:700;">{row["Status_PKM"]}</span></td>'
        html_c += '</tr>'
    html_c += '</table></div>'
    st.markdown(html_c, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  TAB 5 – INSIGHT & REKOMENDASI
# ═══════════════════════════════════════════════════════════════════
with tab5:
    st.markdown("## POPINE INSIGHT & REKOMENDASI EKSEKUTIF")
    
    wil_pop_max   = d25_all.loc[d25_all["Penduduk_Ribu"].idxmax(), "Wilayah"]
    pop_max       = d25_all["Penduduk_Ribu"].max()
    wil_rsu_min   = d25_all.loc[d25_all["Rasio_RSU_100rb"].idxmin(), "Wilayah"]
    rsu_min_val   = d25_all["Rasio_RSU_100rb"].min()
    wil_rsu_max   = d25_all.loc[d25_all["Rasio_RSU_100rb"].idxmax(), "Wilayah"]
    rsu_max_val   = d25_all["Rasio_RSU_100rb"].max()
    wil_padat     = d25_all.loc[d25_all["Kepadatan"].idxmax(), "Wilayah"]
    kepadatan_max = d25_all["Kepadatan"].max()
    n_kurang_rsu  = (d25_all["Rasio_RSU_100rb"] < 0.42).sum()
    klinik_naik   = d25_all["Klinik_Pratama"].sum() - d23_all["Klinik_Pratama"].sum()

    st.markdown("### [DATA CUBE] HASIL PEMINDAIAN PROVINSI (2023-2025)")

    k1, k2 = st.columns(2)
    
    findings = [
        ("kotak-merah",  
         f"[!] KONDISI KRITIS: {wil_rsu_min.upper()}",
         f"Rasio terendah tercatat (<b>{rsu_min_val:.3f}</b>/100K). Zona ini mengalami kegagalan sistemik dalam memenuhi kapasitas minimum rujukan sekunder. Intervensi struktural darurat diperlukan."),
        ("kotak-kuning", 
         f"[-] DEFISIT SKALA BESAR ({n_kurang_rsu} SEKTOR)",
         f"<b>{(n_kurang_rsu/27)*100:.0f}%</b> grid wilayah berada di bawah rasio aman WHO. Anomali ini menunjukkan ketidakmampuan tata ruang mengimbangi laju reproduksi demografi."),
        ("kotak-biru",   
         f"[+] BEBAN MAKSIMUM: {wil_pop_max.upper()}",
         f"Puncak populasi di angka <b>{pop_max/1000:.1f} JT Jiwa</b>. Sistem kesehatan di kuadran ini menahan tekanan terberat dan rawan mengalami 'bottle-neck' layanan fisik."),
        ("kotak-hijau",  
         f"[✓] PERTUMBUHAN JARINGAN MIKRO (+{klinik_naik})",
         f"Kenaikan eksponensial pada node Klinik Pratama membuktikan pergeseran beban faskes primer ke entitas swasta untuk kompensasi kapasitas Puskesmas yang over-limit."),
        ("kotak-biru",   
         f"[+] HIPER-DENSITAS: {wil_padat.upper()}",
         f"Kepadatan spasial menembus <b>{kepadatan_max:,} jiwa/km²</b>. Skema konvensional tidak akan cukup; memerlukan aktivasi protokol Telemedisin dan integrasi digital."),
        ("kotak-hijau",  
         f"[✓] BLUEPRINT REFERENSI: {wil_rsu_max.upper()}",
         f"Mencapai skor optimum <b>{rsu_max_val:.3f}</b>. Matriks tata kota dan alokasi lahan kesehatan dari sektor ini direkomendasikan untuk di-kloning ke sektor defisit."),
    ]

    for idx, (gaya, judul, isi) in enumerate(findings):
        col = k1 if idx % 2 == 0 else k2
        with col:
            st.markdown(f"""
            <div class="kotak-general {gaya}" style="min-height: 160px; border-radius: 4px;">
              <b style="font-size: 1.1rem; letter-spacing: 1px; font-family: 'Chakra Petch', sans-serif;">{judul}</b><br><br>
              <div style="font-size: 0.95rem; color: #475569;">{isi}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<hr class='tech-line'>", unsafe_allow_html=True)
    st.markdown("### [COMMAND] PROTOKOL TINDAK LANJUT")
    
    rekomendasi = [
        ("01", "#0284c7",
         "AKSELERASI INFRASTRUKTUR ZONA KRITIS",
         f"Alihkan anggaran belanja modal difokuskan penuh pada kuadran defisit tinggi seperti {wil_rsu_min}. Target: mencapai ekuilibrium 1 RS per 240K warga dalam siklus 5 tahun."),
        ("02", "#059669",
         "UPGRADE KELAS NODE PUSKESMAS",
         "Aktifkan mode konversi massal Puskesmas Non-Rawat Inap menjadi Rawat Inap pada koordinat wilayah dengan bentang geografis luas guna menekan angka rasio rujukan RS."),
        ("03", "#d97706",
         "DEREGULASI JARINGAN SWASTA",
         f"Buka blokir birokrasi dan berikan stimulus pada pembangunan Klinik Pratama baru di episentrum padat ({wil_padat}) untuk memecah konsentrasi antrean pasien."),
        ("04", "#e11d48",
         "SINKRONISASI DATA REAL-TIME",
         "Hubungkan modul sistem ini secara live dengan database BPJS dan satelit Kemenkes. Hindari lag keputusan yang disebabkan oleh sistem pendataan tahunan."),
    ]

    c1, c2 = st.columns(2)
    for idx, (no, warna, judul, isi) in enumerate(rekomendasi):
        col = c1 if idx % 2 == 0 else c2
        with col:
            st.markdown(f"""
            <div style="background:rgba(255, 255, 255, 0.9); border-radius:4px; padding:24px;
                        border: 1px solid rgba(2, 132, 199, 0.15); border-top: 4px solid {warna};
                        box-shadow: 0 4px 15px rgba(2,132,199,0.05);
                        margin-bottom:20px; min-height: 190px; position:relative; overflow:hidden; transition: all 0.3s ease;"
                 onmouseover="this.style.boxShadow='0 8px 25px rgba(2,132,199,0.15)'; this.style.transform='translateY(-3px)';" 
                 onmouseout="this.style.boxShadow='0 4px 15px rgba(2,132,199,0.05)'; this.style.transform='translateY(0)';">
              <div style="position:absolute; right:-5px; top:-5px; font-size:4rem; font-weight:700; font-family: 'Chakra Petch', sans-serif; color:rgba(2,132,199,0.05); line-height:1;">{no}</div>
              <div style="display: flex; align-items: center; margin-bottom: 15px;">
                  <span style="color: {warna}; font-weight: 700; font-family: 'Chakra Petch', sans-serif; font-size: 1.2rem; margin-right: 12px;">[{no}]</span>
                  <div style="font-size: 1.1rem; font-weight: 700; font-family: 'Chakra Petch', sans-serif; color: #0f172a; letter-spacing: 1px;">{judul}</div>
              </div>
              <div style="font-size: 0.95rem; color: #475569; line-height: 1.6; font-weight: 500;">{isi}</div>
            </div>
            """, unsafe_allow_html=True)


# ───────────────────────────────────────────────────────────────────
#  FOOTER (HUD Terminal Light Style)
# ───────────────────────────────────────────────────────────────────
st.markdown("""
<hr class="tech-line" style="margin-top: 40px;">
<div style="text-align: center; font-size: 0.85rem; color: #64748b; font-weight: 600; padding-bottom: 30px; font-family: 'Courier New', Courier, monospace;">
  >_ TERMINAL: POPINE_DASHBOARD_JABAR_2023_2025 // KONEKSI AMAN<br>
  >_ SUMBER INTELIJEN: BPS JAWA BARAT // MODEL MESIN: K-MEANS CLUSTERING<br>
  <span style="color: #0284c7; font-weight: 700;">>_ RENDERED BY STREAMLIT & PLOTLY ENGINE</span>
</div>
""", unsafe_allow_html=True)