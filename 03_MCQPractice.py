import streamlit as st

def create_subject_selection_page():
    # Custom CSS for styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .subject-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .subject-card:hover {
        transform: translateY(-5px);
    }
    
    .physics-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .chemistry-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .maths-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    .biology-card {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    }
    
    .card-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .card-description {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    .stats-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown('<h1 class="main-header">🎓 Science MCQ Exam Portal</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Choose your subject and test your knowledge!</p>', unsafe_allow_html=True)

    # Subject Cards Layout
    col1, col2 = st.columns(2)
    
    with col1:
        # Physics Card
        if st.button("📐", key="physics", help="Physics", use_container_width=True):
            st.session_state.selected_subject = "Physics"
            st.switch_page("Home.py")  # Redirect to physics page
        
        st.markdown("""
        <div class="subject-card physics-card">
            <div class="card-icon">⚛️</div>
            <div class="card-title">PHYSICS</div>
            <div class="card-description">Explore the laws of nature, motion, energy, and matter</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Chemistry Card
        if st.button("🧪", key="chemistry", help="Chemistry", use_container_width=True):
            st.session_state.selected_subject = "Chemistry"
            st.switch_page("pages/chemistry.py")  # Redirect to chemistry page
            
        st.markdown("""
        <div class="subject-card chemistry-card">
            <div class="card-icon">🧪</div>
            <div class="card-title">CHEMISTRY</div>
            <div class="card-description">Discover reactions, elements, and molecular structures</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Mathematics Card
        if st.button("📊", key="mathematics", help="Mathematics", use_container_width=True):
            st.session_state.selected_subject = "Mathematics"
            st.switch_page("pages/mathematics.py")  # Redirect to mathematics page
            
        st.markdown("""
        <div class="subject-card maths-card">
            <div class="card-icon">📐</div>
            <div class="card-title">MATHEMATICS</div>
            <div class="card-description">Master numbers, equations, and logical reasoning</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Biology Card
        if st.button("🌱", key="biology", help="Biology", use_container_width=True):
            st.session_state.selected_subject = "Biology"
            st.switch_page("pages/biology.py")  # Redirect to biology page
            
        st.markdown("""
        <div class="subject-card biology-card">
            <div class="card-icon">🧬</div>
            <div class="card-title">BIOLOGY</div>
            <div class="card-description">Study life, organisms, and natural processes</div>
        </div>
        """, unsafe_allow_html=True)

    # Statistics Section
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Questions", "200+", "15 new")
    with col2:
        st.metric("Active Students", "1,250", "50 today")
    with col3:
        st.metric("Subjects Available", "4", "All sciences")
    with col4:
        st.metric("Average Score", "78%", "2% ↗")

    # Features Section
    st.markdown("---")
    st.markdown("### ✨ Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🎯 Instant Feedback**
        - Get immediate results
        - Detailed explanations
        - Progress tracking
        """)
    
    with col2:
        st.markdown("""
        **📚 Comprehensive Coverage**
        - All major topics
        - Difficulty levels
        - Regular updates
        """)
    
    with col3:
        st.markdown("""
        **🏆 Performance Analytics**
        - Score history
        - Weak area identification
        - Improvement suggestions
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🚀 Ready to challenge yourself? Select a subject above to begin!</p>
        <p><small>Made with ❤️ using Streamlit</small></p>
    </div>
    """, unsafe_allow_html=True)

# Alternative Layout with Cards in Grid
def create_alternative_layout():
    st.markdown("""
    <style>
    .subject-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .subject-item {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .subject-item:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    }
    
    .physics-border:hover { border-color: #667eea; }
    .chemistry-border:hover { border-color: #f5576c; }
    .maths-border:hover { border-color: #00f2fe; }
    .biology-border:hover { border-color: #43e97b; }
    </style>
    """, unsafe_allow_html=True)

    st.title("🎓 Science MCQ Portal")
    st.markdown("### Select your subject to start the exam")

    # Create 2x2 grid for subjects
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    subjects = [
        {"name": "Physics", "icon": "⚛️", "color": "#667eea", "col": row1_col1},
        {"name": "Chemistry", "icon": "🧪", "color": "#f5576c", "col": row1_col2},
        {"name": "Mathematics", "icon": "📐", "color": "#00f2fe", "col": row2_col1},
        {"name": "Biology", "icon": "🧬", "color": "#43e97b", "col": row2_col2}
    ]

    for subject in subjects:
        with subject["col"]:
            if st.button(
                f"{subject['icon']} {subject['name']}", 
                key=subject['name'].lower(),
                use_container_width=True,
                type="primary"
            ):
                st.session_state.selected_subject = subject['name']
                # Redirect logic here
                st.success(f"Redirecting to {subject['name']} exam...")
                st.balloons()

# Main function to display the page
def main():
    st.set_page_config(
        page_title="Science MCQ Portal",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Choose which layout to use
    create_subject_selection_page()
    # create_alternative_layout()  # Uncomment to use alternative layout

if __name__ == "__main__":
    main()
