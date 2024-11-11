import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Aayush Jaiswal Portfolio", layout="wide", initial_sidebar_state="expanded")

# Initialize session state for dark mode
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = True

# Function to toggle dark mode
def toggle_dark_mode():
    st.session_state["dark_mode"] = not st.session_state["dark_mode"]

# Dark mode button
if st.session_state["dark_mode"]:
    dark_mode_button = st.sidebar.button("🌞 Light Mode", on_click=toggle_dark_mode)
else:
    dark_mode_button = st.sidebar.button("🌜 Dark Mode", on_click=toggle_dark_mode)

# CSS for light and dark modes
def apply_css(dark_mode):
    if dark_mode:
        st.markdown("""
            <style>
            .main {
                background-color: #121212;
                color: #e0e0e0;
                padding: 20px;
            }
            .sidebar .sidebar-content {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            .sidebar .sidebar-content a {
                color: #BB86FC;
            }
            .sidebar .sidebar-content a:hover {
                color: #3700B3;
            }
            .title {
                text-align: center;
                font-family: 'Helvetica', sans-serif;
                color: #BB86FC;
            }
            .section-title {
                color: #BB86FC;
                font-size: 24px;
                font-weight: bold;
                border-bottom: 2px solid #BB86FC;
                margin-bottom: 10px;
                padding-bottom: 5px;
            }
            .item h4, .item p, .item ul li {
                font-size: 18px;
                color: #e0e0e0;
                margin: 5px 0;
            }
            .item a {
                color: #BB86FC;
                text-decoration: none;
            }
            .item a:hover {
                text-decoration: underline;
            }
            .contact-icons img, .company-logos img {
                height: 30px;
                margin-right: 10px;
            }
            .st-expander {
                font-size: 20px !important;
                line-height: 1.6 !important;
            }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .main {
                background-color: #ffffff;
                color: #000000;
                padding: 20px;
            }
            .sidebar .sidebar-content {
                background-color: #f8f9fa;
                color: #000000;
            }
            .sidebar .sidebar-content a {
                color: #007bff;
            }
            .sidebar .sidebar-content a:hover {
                color: #0056b3;
            }
            .title {
                text-align: center;
                font-family: 'Helvetica', sans-serif;
                color: #007bff;
            }
            .section-title {
                color: #007bff;
                font-size: 24px;
                font-weight: bold;
                border-bottom: 2px solid #007bff;
                margin-bottom: 10px;
                padding-bottom: 5px;
            }
            .item h4, .item p, .item ul li {
                font-size: 18px;
                color: #000000;
                margin: 5px 0;
            }
            .item a {
                color: #007bff;
                text-decoration: none;
            }
            .item a:hover {
                text-decoration: underline;
            }
            .contact-icons img, .company-logos img {
                height: 30px;
                margin-right: 10px;
            }
            .st-expander {
                font-size: 20px !important;
                line-height: 1.6 !important;
            }
            </style>
            """, unsafe_allow_html=True)

apply_css(st.session_state["dark_mode"])

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu", ["Home", "Skills", "Experience", "Projects", "Publications", "Education"],
        icons=["house", "book", "briefcase", "code-slash", "journal", "bank2"],
        menu_icon="cast", default_index=0, orientation="vertical",
    )

# Home Page
if selected == "Home":
    st.title("Aayush Jaiswal")
    st.image("images/profile.jpeg", width=150)
    
    st.subheader("Contact Information")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image("images/email.jpg", width=30)
        st.write("[Email](mailto:aajais@iu.edu)")
    with col2:
        st.image("images/linkedin-icon.png", width=30)
        st.write("[LinkedIn](https://linkedin.com/in/jaiswal-aayush)")
    with col3:
        st.image("images/github-icon.png", width=30)
        st.write("[GitHub](https://github.com/aayush9400)")
    with col4:
        st.image("images/google-scholar-icon.png", width=30)
        st.write("[Google Scholar](https://scholar.google.com/citations?user=ZvTNhlcAAAAJ&hl=en)")
    with col5:
        st.image("images/medium-icon.png", width=30)
        st.write("[Medium](https://medium.com/@jaayush12)")
    
    st.write("I'm looking for full-time roles in AI/ML. Please email me for any opportunities.")
    
    st.subheader("Professional Summary")
    st.write("Innovative AI/ML engineer with a proven track record of developing high-impact AI solutions and optimizing cloud infrastructure. Expertise in deep learning, computer vision, and scalable cloud architectures. Passionate about advancing AI technologies and implementing ethical AI practices to drive business success.")

# Skills Page
elif selected == "Skills":
    st.markdown('<h1 class="section-title">Skills Summary</h1>', unsafe_allow_html=True)
    skills = [
        "Proficient in AI/ML technologies, including deep learning, NLP, and generative AI, with hands-on experience in frameworks such as TensorFlow, PyTorch, and Keras.",
        "Strong coding skills in Python, Java, and C++, with expertise in data manipulation libraries like Pandas and NumPy.",
        "Extensive experience in designing and implementing scalable cloud architectures on AWS, GCP, and Azure, leveraging containerization technologies (Docker, Kubernetes).",
        "Skilled in deploying and optimizing AI models in cloud environments, ensuring high performance and cost efficiency through the use of MLOps tools (W&B, MLFlow).",
        "Proficient in developing real-time data pipelines using DBT, BigQuery, and Spark, enhancing data analytics efficiency.",
        "Demonstrated leadership in cross-functional teams, driving innovation and strategic AI initiatives while adhering to ethical AI practices and regulatory compliance."
    ]
    
    # Visualization of Skills
    import matplotlib.pyplot as plt

    skill_categories = ['AI/ML Technologies', 'Programming Languages', 'Cloud Architectures', 'MLOps Tools', 'Data Pipelines', 'Leadership']
    skill_levels = [90, 85, 80, 75, 80, 70]

    fig, ax = plt.subplots()
    ax.barh(skill_categories, skill_levels, color='#007bff')
    ax.set_xlim(0, 100)
    ax.set_xlabel('Proficiency (%)')
    ax.set_title('Skill Proficiency')

    st.pyplot(fig)

    # Displaying Skills
    for skill in skills:
        st.markdown(f"<div class='item'><li>{skill}</li></div>", unsafe_allow_html=True)

# Experience Page
elif selected == "Experience":
    st.markdown('<h1 class="section-title">Experience</h1>', unsafe_allow_html=True)
    experience = [
        {
            "title": "AI Research Assistant",
            "company": "Indiana University",
            "duration": "Aug 2023 -- May 2024",
            "location": "Bloomington, IN",
            "details": [
                "Enhanced research capabilities by developing AI-powered Generative models for 3D brain image synthesis, collaborating with cross-functional stakeholders (Doctors, Researchers, ML Experts).",
                "Mentored 150+ students in courses on Distributed & Cloud Computing and AWS, focusing on cloud architectures and big data applications."
            ],
            "logo": "images/indiana-university-logo.png"
        },
        {
            "title": "Data Scientist / Machine Learning Engineer - 1",
            "company": "Trell, Sequoia Backed Social Media Platform",
            "duration": "Jan 2021 -- Mar 2022",
            "location": "Remote",
            "details": [
                "Led the deployment of a multilingual short video recommendation system, enhancing user engagement by 20% and retention by 45%, through collaboration with cross-functional teams to improve feed quality and drive satisfaction.",
                "Improved operational efficiency by 30% by architecting and automating AI model training and deployment using AWS, Prometheus, Grafana, and W&B, ensuring high performance and scalability.",
                "Enhanced data retrieval speed by 25% and data quality by 10% by optimizing real-time data pipelines and cloud database efficiency with GCP Big Query and DBT, focusing on performance and scalability.",
                "Defined success metrics and prioritized solutions by creating an MIS dashboard for AI projects based on user metrics."
            ],
            "logo": "images/trell.png"
        },
        {
            "title": "Research Assistant",
            "company": "Manipal University",
            "duration": "Jan 2020 -- Jul 2020",
            "location": "Jaipur, India",
            "details": [
                "Conducted research on computer vision algorithms for COVID-19 detection, resulting in 2 published papers with 700+ citations.",
                "Developed an end-to-end AI application for doctors, ensuring low-latency predictions and seamless integration into medical workflows."
            ],
            "logo": "images/manipal.png"
        },
        {
            "title": "Data Science Intern",
            "company": "Airtel (Leading telecom provider of India)",
            "duration": "Jun 2019 -- Jul 2019",
            "location": "Delhi, India",
            "details": [
                "Improved marketing campaign effectiveness by 10% through the development of user behavior-based clustering algorithms, collaborating closely with the marketing team to deliver AI-driven insights."
            ],
            "logo": "images/airtel.png"
        }
    ]

    for exp in experience:
        st.image(exp["logo"], width=50)
        st.markdown(f"<h2>{exp['title']} at {exp['company']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<div><b>Duration</b>: {exp['duration']} | <b>Location</b>: {exp['location']}</div>", unsafe_allow_html=True)
        st.markdown("<div><b>Responsibilities</b>:</div>", unsafe_allow_html=True)
        for detail in exp["details"]:
            st.markdown(f"<div>- {detail}</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

# Projects Page
elif selected == "Projects":
    st.markdown('<h1 class="section-title">Projects</h1>', unsafe_allow_html=True)
    projects = [
        {
            "name": "3D Conditional Diffusion Model",
            "description": "Developed advanced 3D Generative AI models including 3D VQ-VAE and VQ-GAN, utilizing diffusion techniques for synthetic brain image generation, contributing to significant advancements in medical imaging.",
            "technologies": "Python, PyTorch, TensorFlow, GPU, Slurm, W&B, Generative AI",
            "link": "https://api.wandb.ai/links/dipy_genai/dzrwwnai"
        },
        {
            "name": "Multi-Lingual Short Video Recommendation System",
            "description": "Architected and implemented a custom AI two-tower recommendation system, enhancing retrieval speed by 50% and leveraging AI and ML techniques to adapt to real-time user behavior.",
            "technologies": "TensorFlow, AWS, GCP, SQL, Docker, MLFlow, CI/CD",
            "link": "https://medium.com/@jaayush12/streamlining-recommendation-systems-with-tensorflow-recommenders-tfrs-f77801d3f059"
        },
        {
            "name": "RAG based AI Agent for Code Repositories",
            "description": "Created a code assistant using the DiPY codebase and implemented a LangGraph RAG pipeline using local LLM for prompt engineering.",
            "technologies": "Python, Transformers, Vector Databases, RAG, LangChain, LLM",
            "link": "https://github.com/aayush9400/dipy_code_assistant"
        },
        {
            "name": "Real-time data pipeline using DBT",
            "description": "Enhanced data analytics efficiency and reduced access times by 15% through the development of real-time data pipelines using DBT, showcasing proficiency in SQL and cloud platforms.",
            "technologies": "Python, SQL, GCP, DBT",
            "link": ""
        },
        {
            "name": "Rapid SARS-COV-2 Detection",
            "description": "Achieved 96% accuracy in COVID-19 detection from X-ray and CT scans using AI techniques and published findings in reputable journals.",
            "technologies": "Python, TensorFlow, OpenCV, AWS, Flask API, EC2",
            "link": "https://github.com/aayush9400/Covid-19-CT-SCAN-Classifier"
        },
        {
            "name": "Brain Image Segmentation using Vision Transformers (ViT)",
            "description": "Developed a 3D CNN neural network with an attention mechanism to identify tumor regions in MRI images, achieving 95% accuracy.",
            "technologies": "Python, PyTorch, Hugging Face",
            "link": "https://github.com/the-neural-networker/brain-tumor-segmentation"
        },
        {
            "name": "Monitoring for Cloud-Native Environments",
            "description": "Implemented scalable monitoring on AWS, enhancing system reliability, uptime, and performance insights by over 30%.",
            "technologies": "AWS, Prometheus, Grafana, Kubernetes, PromQL, S3",
            "link": "https://medium.com/@jaayush12/utilizing-prometheus-for-efficient-monitoring-in-cloud-native-environments-2ef370c41971"
        }
    ]

    for project in projects:
        st.markdown(f"<h2>{project['name']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<div><b>Technologies Used</b>: {project['technologies']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div>{project['description']}</div>", unsafe_allow_html=True)
        if project["link"]:
            st.markdown(f"<div><a href='{project['link']}' target='_blank'>Project Link</a></div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

# Publications Page
elif selected == "Publications":
    st.markdown('<h1 class="section-title">Publications</h1>', unsafe_allow_html=True)
    publications = [
        {
            "title": "3D Conditional Diffusion Model for Synthetic Brain Image Generation",
            "journal": "TBD",
            "authors": "Aayush Jaiswal, JongSung Park, Eleftherios Garyfalladis",
            "year": 2024,
            "details": "Developed 3D VQ-VAE and VQ-GAN models using Python and PyTorch, achieving high-quality synthetic brain images with improved latent representation. Contributed to advancements in medical imaging, enhancing diagnostic capabilities and research methodologies."
        },
        {
            "title": "Classification of the COVID-19 Infected Patients Using DenseNet201 Based Deep Transfer Learning",
            "journal": "Taylor & Francis",
            "authors": "Aayush Jaiswal, Neha Gianchandani, Dilbag Singh, Vijay Kumar, Manjit Kaur",
            "year": 2020,
            "details": "Achieved 96.25% accuracy and AUC of 0.97 in classifying COVID-19 from chest CT scans using DenseNet201 and deep transfer learning techniques. Utilized Python and TensorFlow to provide a faster, non-invasive alternative to RT-PCR for COVID-19 diagnosis, significantly reducing false positives and negatives."
        },
        {
            "title": "Rapid COVID-19 Diagnosis Using Ensemble Deep Transfer Learning Models from Chest Radiographic Images",
            "journal": "Springer",
            "authors": "Aayush Jaiswal, Neha Gianchandani, Dilbag Singh, Vijay Kumar, Manjit Kaur",
            "year": 2020,
            "details": "Designed ensemble models using Python and TensorFlow, achieving 98.25% accuracy in differentiating COVID-19, viral, and bacterial pneumonia from chest X-rays. Validated on two datasets, models demonstrated high sensitivity and specificity, enabling effective large-scale COVID-19 screening."
        }
    ]

    for pub in publications:
        st.markdown(f"<h2>{pub['title']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<div><b>Journal</b>: {pub['journal']} | <b>Year</b>: {pub['year']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div><b>Authors</b>: {pub['authors']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div>{pub['details']}</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

# Education Page
elif selected == "Education":
    st.markdown('<h1 class="section-title">Education</h1>', unsafe_allow_html=True)
    education = [
        {
            "degree": "Master of Science in Data Science",
            "institution": "Indiana University Bloomington",
            "duration": "Aug 2022 -- May 2024",
            "gpa": "3.60"
        },
        {
            "degree": "Bachelor of Technology in Computer Science",
            "institution": "Manipal University Jaipur",
            "duration": "Aug 2017 -- May 2021",
            "gpa": "3.70"
        }
    ]

    for edu in education:
        st.markdown(f"<h2>{edu['degree']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<div><b>Institution</b>: {edu['institution']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div><b>Duration</b>: {edu['duration']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div><b>GPA</b>: {edu['gpa']}</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

apply_css(st.session_state["dark_mode"])
