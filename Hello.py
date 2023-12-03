import streamlit as st
import info
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
def linksSection():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedinLink = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedinLink,unsafe_allow_html = True)
    st.sidebar.text("Checkout my work")
    githubLink = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(githubLink,unsafe_allow_html = True)
    st.sidebar.text("Or email me!")
    emailHTML = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(emailHTML,unsafe_allow_html = True)
linksSection()

#Education
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
educationSection(info.education_data,info.course_data)

#Professional Experience
def experienceSection(experienceData):
    st.header("💼 Professional Experience")
    for jobTitle,(jobDescription,image) in experienceData.items():
        expander = st.expander(f"**{jobTitle}**")
        expander.image(image,width = 250)
        for bullet in jobDescription:
            expander.write(bullet)
    st.write("---")
experienceSection(info.experience_data)

#Projects
def projectSection(projectsData):
    st.header("🛠️ Projects")
    for projectName,(projectDescription,image,projectLink) in projectsData.items():
        expander = st.expander(f"**{projectName}**")
        expander.image(image,width = 250)
        expander.write(f"[**{projectName}**]({projectLink})")
        expander.write(projectDescription)
    st.write("---")
projectSection(info.projects_data)

#Skills
def skillsSection(programmingData,spokenData):
    st.header("🧑‍💻 Skills")
    st.subheader("Programming Languages")
    for skill,percentage in programmingData.items():
        st.write(f"{skill} {info.programming_icons.get(skill)}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken,proficiency in spokenData.items():
        st.write(f"{spoken} {info.spoken_icons.get(spoken)}: {proficiency}")
    st.write("---")
skillsSection(info.programming_data,info.spoken_data)

#Activities
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
activitiesSection(info.leadership_data,info.activity_data)
