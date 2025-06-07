# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# load_dotenv()

# genai.configure(api_key="AIzaSyDzhNYAdbkqaIM9Kfpr3zKUWKNXhTgm5G8")




# def get_gemini_response(prompt):
#     model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
#     response = model.generate_content(prompt)
#     return response.text


# st.title("The Professor's Academy Assistant")
# st.header("Ask me anything I Will help you with your studies!")

# userprompt = st.text_area("Enter your question here:", key="prompt")
# submitbtn = st.button("Get Answer")

# if submitbtn and userprompt.strip():
#     response = get_gemini_response(userprompt)
#     st.subheader("Your Answer:")
#     st.write(response)



import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="The Professor's Academy - AI Learning Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
    }
    
    .feature-icon {
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        text-align: center;
        opacity: 0.9;
    }
    
    .stats-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 2rem 0;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
    }
    
    .stat-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    .cta-button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    
    .cta-button:hover {
        transform: translateY(-2px);
    }
    
    .testimonial-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .academy-info {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="main-header">🎓 The Professor\'s Academy</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Learning Hub for Academic Excellence</p>', unsafe_allow_html=True)

# Hero Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="academy-info">
        <h2 style="text-align: center; margin-bottom: 1rem;">🤖 Welcome to Our AI Learning Platform</h2>
        <p style="text-align: center; font-size: 1.1rem; line-height: 1.6;">
            Harness the power of Artificial Intelligence to revolutionize your learning experience. 
            Our cutting-edge AI tools are designed to help students excel in their studies through 
            personalized assistance, intelligent tutoring, and innovative learning solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Features Section
st.markdown("## 🚀 Our AI-Powered Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">Smart Tutoring</div>
        <div class="feature-desc">
            Get personalized explanations and step-by-step solutions 
            tailored to your learning style and pace.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📝</div>
        <div class="feature-title">Assignment Helper</div>
        <div class="feature-desc">
            Receive intelligent assistance with homework, projects, 
            and assignments across all subjects.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Exam Preparation</div>
        <div class="feature-desc">
            Practice with AI-generated questions and get targeted 
            preparation for your upcoming exams.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Second row of features
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🖼️</div>
        <div class="feature-title">Visual Learning</div>
        <div class="feature-desc">
            Generate images, diagrams, and visual aids to enhance 
            your understanding of complex concepts.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💬</div>
        <div class="feature-title">24/7 AI Assistant</div>
        <div class="feature-desc">
            Get instant answers to your questions anytime, anywhere 
            with our intelligent chatbot.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Progress Tracking</div>
        <div class="feature-desc">
            Monitor your learning progress with AI-powered analytics 
            and personalized recommendations.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Statistics Section
st.markdown("## 📈 Our Impact")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stats-container">
        <div class="stat-number">10K+</div>
        <div class="stat-label">Students Helped</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-container">
        <div class="stat-number">95%</div>
        <div class="stat-label">Success Rate</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-container">
        <div class="stat-number">24/7</div>
        <div class="stat-label">AI Support</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stats-container">
        <div class="stat-number">50+</div>
        <div class="stat-label">Subjects Covered</div>
    </div>
    """, unsafe_allow_html=True)

# How It Works Section
st.markdown("## 🔄 How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 1️⃣ Ask Your Question
    Simply type your question or upload your assignment. Our AI understands natural language and can help with any subject.
    """)

with col2:
    st.markdown("""
    ### 2️⃣ AI Processing
    Our advanced AI analyzes your query and generates personalized, accurate responses tailored to your academic level.
    """)

with col3:
    st.markdown("""
    ### 3️⃣ Learn & Improve
    Receive detailed explanations, visual aids, and follow-up questions to deepen your understanding.
    """)

# Testimonials Section
st.markdown("## 💬 What Students Say")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="testimonial-card">
        <p><strong>"The Professor's Academy AI has transformed my study routine. The explanations are clear and the 24/7 support is incredible!"</strong></p>
        <p style="text-align: right; color: #667eea; font-weight: bold;">- Sarah M., Computer Science Student</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="testimonial-card">
        <p><strong>"I improved my grades significantly thanks to the personalized tutoring. It's like having a professor available anytime!"</strong></p>
        <p style="text-align: right; color: #667eea; font-weight: bold;">- Alex R., Engineering Student</p>
    </div>
    """, unsafe_allow_html=True)

# Call to Action Section
st.markdown("## 🎯 Ready to Excel in Your Studies?")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h3>Start your AI-powered learning journey today!</h3>
        <p style="font-size: 1.1rem; color: #666; margin-bottom: 2rem;">
            Join thousands of students who are already improving their academic performance with our AI tools.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        if st.button("🤖 AI Chat Assistant", use_container_width=True):
            st.switch_page("pages/01_ChatBot.py")
    
    with col_b:
        if st.button("🖼️ Image Generator", use_container_width=True):
            st.switch_page("pages/02_GenerateImage.py")
    
    with col_c:
        if st.button("📚 Study Helper", use_container_width=True):
            st.switch_page("pages/03_StudyHelper.py")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <h4>🎓 The Professor's Academy</h4>
    <p>Empowering students through AI-driven education technology</p>
    <p>© 2025 The Professor's Academy. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🎓 Quick Navigation")
    st.markdown("---")
    
    st.markdown("### 🚀 AI Tools")
    if st.button("💬 Chat with AI", use_container_width=True):
        st.switch_page("pages/01_GenerateText.py")
    
    if st.button("🖼️ Generate Images", use_container_width=True):
        st.switch_page("pages/02_GenerateImage.py")
    
    if st.button("📝 Study Assistant", use_container_width=True):
        st.switch_page("pages/03_StudyHelper.py")
    
    st.markdown("---")
    st.markdown("### 📞 Support")
    st.info("Need help? Our AI is available 24/7 to assist you with your studies!")
    
    st.markdown("### 🎯 Today's Tip")
    st.success("💡 Try asking specific questions for better AI responses. The more detailed your question, the more helpful the answer!")
