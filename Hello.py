import streamlit as st
import pandas as pd

#About Me
profile_picture = "cover.png"
about_me = "I'm Ansh Misra. I am a first-year Neuroscience student at the Georgia Institute of Technology with an interest in cancer biology, psychology, and computer science. I am seeking opportunites in the medical industry, hoping to make a positive impact on society and all people I meet. I strive to be an active member in all aspects of the college community including academics, arts, and athletics."
def aboutMeSection():
    st.header("🚀 About Me")
    st.image(profile_picture,width = 250)
    st.write(about_me)
    st.write("---")
aboutMeSection()

#Sidebar Links
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"
my_linkedin_url = "https://linkedin.com/in/ansh-misra-683065255"
my_github_url = "https://github.com/anshmisra"
my_email_address = "anshmisra2004@gmail.com"
def linksSection():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedinLink = f'<a href="{my_linkedin_url}"><img src="{linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedinLink,unsafe_allow_html = True)
    st.sidebar.text("Checkout my work")
    githubLink = f'<a href="{my_github_url}"><img src="{github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(githubLink,unsafe_allow_html = True)
    st.sidebar.text("Or email me!")
    emailHTML = f'<a href="mailto:{my_email_address}"><img src="{email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(emailHTML,unsafe_allow_html = True)
linksSection()

#Education
education_data ={
    'Degree': 'Bachelor of Science in Neuroscience',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': 'Spring 2027',
    'GPA': '4.0'
}
course_data = {
    "code":["BIOS 1107", "MATH 1551", "MATH 1552", "MATH 1554", "MATH 2551", "CHEM 1211K", "CS 1301", "PSYC 1101"], 
    "names":["Biological Principles", "Differential Calculus", "Integral Calculus", "Linear Algebra", "Multivariable Calculus", "Chemical Principles I", "Intro to CS", "General Psychology"], 
    "semester_taken":["Advanced Placement Credit", "Advanced Placement Credit", "Advanced Placement Credit", "Dual Enrollment", "Dual Enrollment", "1st", "1st", "1st"],
    "skills":["Basic cellular function, Genetics, Ecology", "Differentiation of equations, Application of Derivatives", "Integration of equations, Application of Integrals", "Solving system of equations, Applications to linear systems", "Linear approximation, Taylor's theorems, Multiple integration, Vector analysis", "Atomic structure, Properties of matter, Thermodynamics, Laboratory skills", "Coding in Python, Web Design, Basic software development", "Psychological approaches and theories, Research methods"],
    }
def educationSection(educationData,courseData):
    st.header("📚 Education")
    st.subheader(f"**{educationData['Institution']}**")
    st.write(f"**Degree:** {educationData['Degree']}")
    st.write(f"**Graduation Date:** {educationData['Graduation Date']}")
    st.write(f"**GPA:** {educationData['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(courseData)
    st.dataframe(coursework,column_config={
        "code": "Course Code",
        "names": "Course Name",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index = True
        )
    st.write("---")
educationSection(education_data,course_data)

#Professional Experience
experience_data = {
    "Pharmacy Technician at CVS Pharmacy": (["- Dispense and distribute medication to customers", "- Answering and fulfilling prescription orders online and through the phone"],"cvs.png"),
    "Volunteer at Emory Midtown Winship Cancer Institute":(["- Offering support to patients and their families to improve their care experience", "- Signing in and escorting patients to their rooms"],"emory.jpeg"),
    "Researcher in Prulitsky Biomechanics and Motor Control Lab":(["- Analyzing animal motorcontrol and gait data", "- Creating digital model for animal motor systems"],"research.jpg")
}
def experienceSection(experienceData):
    st.header("💼 Professional Experience")
    for jobTitle,(jobDescription,image) in experienceData.items():
        expander = st.expander(f"**{jobTitle}**")
        expander.image(image,width = 250)
        for bullet in jobDescription:
            expander.write(bullet)
    st.write("---")
experienceSection(experience_data)

#Projects
projects_data = {
    "Yellow Jacket Lifts": ("Application that provides full workouts targetting specific muscle groups for college students to accomplish their fitness goals. Most college students are busy and short on time, so the application designs a workout with exercises that fits the student's schedule.", "yellowjacket.png", "https://yellowjacketlifts.streamlit.app")
}
def projectSection(projectsData):
    st.header("🛠️ Projects")
    for projectName,(projectDescription,image,projectLink) in projectsData.items():
        expander = st.expander(f"**{projectName}**")
        expander.image(image,width = 250)
        expander.write(f"[**{projectName}**]({projectLink})")
        expander.write(projectDescription)
    st.write("---")
projectSection(projects_data)

#Skills
programming_data = {
    "Python": 90,
    "Java": 10,
    "HTTP": 30,
    "CSS": 25,
}
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "HTTP": "➡️",
    "CSS": "🔍",
}
spoken_icons = {
    "English": "🇬🇧",
    "Hindi": "🇮🇳",
    "Odia": "🇮🇳",
    "Spanish":"🇪🇸"
}
spoken_data = {
    "English": "Fluent",
    "Hindi": "Fluent",
    "Odia": "Fluent",
    "Spanish": "Conversant",
}
def skillsSection(programmingData,spokenData):
    st.header("🧑‍💻 Skills")
    st.subheader("Programming Languages")
    for skill,percentage in programmingData.items():
        st.write(f"{skill} {programming_icons.get(skill)}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken,proficiency in spokenData.items():
        st.write(f"{spoken} {spoken_icons.get(spoken)}: {proficiency}")
    st.write("---")
skillsSection(programming_data,spoken_data)

#Activities
leadership_data = {
    "Finance Officer for GT MEDLIFE": (["- Aiding fundraising director in collecting funds for the club", "- Planning fundraising events for the club and the GT community", "- Tracking internal finances"],"medlife.png"),

}
activity_data={
    "Georgia Tech MEDLIFE": (["- Raising money for healthcare, education, and medical supplies for developing countries", "- Creating awareness for improved healthcare for people in developing countries", "- Sorting medical supplies at MEDSHARE distribution centers"], "medlife.png"),
    "Student Neuroscience Association": (["- Providing opportunities for undergraduate Neuroscience students", "- Sharing information on current news in Neuroscience", "- Raising awareness for students' concerns of current course curriculum and student experience"], "gtsna.jpeg"),
    "Georgia Tech Qurbani": (["- Spreading the love for Indian culture and music through dance", "- Traveling throughout the country taking part in various dance competitions"], "qurbani.png")
}
def activitiesSection(leadershipData,activityData):
    st.header("🧗 Activities")
    tab1,tab2 = st.tabs(["Leadership","Community Involvement"])
    with tab1:
        st.subheader("🎖️️ Leadership")
        for title,(details,image) in leadershipData.items():
            expander = st.expander(f"**{title}**")
            expander.image(image,width = 250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("🤝 Community Involvement")
        for title,(details,image) in activityData.items():
            expander = st.expander(f"**{title}**")
            expander.image(image,width = 250)
            for bullet in details:
                expander.write(bullet)
    st.write("---")
activitiesSection(leadership_data,activity_data)