from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def get_input(prompt):
    return input(prompt).strip()

print("=" * 50)
print("     AI RESUME BUILDER - DAY 16")
print("=" * 50)
print("Enter your details below:\n")

# Get user input
name = get_input("Your Full Name: ")
email = get_input("Email: ")
phone = get_input("Phone Number: ")
location = get_input("City, State: ")
linkedin = get_input("LinkedIn (or press Enter to skip): ")
objective = get_input("Career Objective (1-2 lines): ")

print("\n--- EDUCATION ---")
degree = get_input("Degree (e.g. B.Tech Computer Science): ")
university = get_input("University/College Name: ")
year = get_input("Year of Passing: ")
percentage = get_input("Percentage/CGPA: ")

print("\n--- SKILLS ---")
skills = get_input("Your Skills (comma separated): ")

print("\n--- PROJECTS ---")
project1 = get_input("Project 1 Name: ")
project1_desc = get_input("Project 1 Description: ")
project2 = get_input("Project 2 Name: ")
project2_desc = get_input("Project 2 Description: ")

print("\n--- EXPERIENCE ---")
exp = get_input("Internship/Experience (or press Enter if none): ")

print("\nGenerating your resume...")

# Create PDF
filename = f"day_16/{name.replace(' ', '_')}_Resume.pdf"
doc = SimpleDocTemplate(filename, pagesize=A4,
                        rightMargin=0.75*inch, leftMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

styles = getSampleStyleSheet()

# Custom styles
name_style = ParagraphStyle('name', fontSize=24, fontName='Helvetica-Bold',
                             alignment=TA_CENTER, textColor=colors.HexColor('#2C3E50'))
contact_style = ParagraphStyle('contact', fontSize=10, fontName='Helvetica',
                                alignment=TA_CENTER, textColor=colors.HexColor('#555555'))
section_style = ParagraphStyle('section', fontSize=13, fontName='Helvetica-Bold',
                                textColor=colors.HexColor('#2980B9'), spaceBefore=10)
normal_style = ParagraphStyle('normal_custom', fontSize=10, fontName='Helvetica',
                               textColor=colors.HexColor('#333333'), leading=16)
bold_style = ParagraphStyle('bold_custom', fontSize=10, fontName='Helvetica-Bold',
                             textColor=colors.HexColor('#2C3E50'))

content = []

# Name
content.append(Paragraph(name, name_style))
content.append(Spacer(1, 6))

# Contact
contact_info = f"{email} | {phone} | {location}"
if linkedin:
    contact_info += f" | {linkedin}"
content.append(Paragraph(contact_info, contact_style))
content.append(Spacer(1, 10))
content.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#2980B9')))

# Objective
content.append(Spacer(1, 8))
content.append(Paragraph("CAREER OBJECTIVE", section_style))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#BDC3C7')))
content.append(Spacer(1, 6))
content.append(Paragraph(objective, normal_style))

# Education
content.append(Spacer(1, 8))
content.append(Paragraph("EDUCATION", section_style))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#BDC3C7')))
content.append(Spacer(1, 6))
content.append(Paragraph(degree, bold_style))
content.append(Paragraph(f"{university} | {year} | {percentage}", normal_style))

# Skills
content.append(Spacer(1, 8))
content.append(Paragraph("SKILLS", section_style))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#BDC3C7')))
content.append(Spacer(1, 6))
skill_list = skills.split(',')
skill_text = " • ".join([s.strip() for s in skill_list])
content.append(Paragraph(skill_text, normal_style))

# Projects
content.append(Spacer(1, 8))
content.append(Paragraph("PROJECTS", section_style))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#BDC3C7')))
content.append(Spacer(1, 6))
content.append(Paragraph(project1, bold_style))
content.append(Paragraph(project1_desc, normal_style))
content.append(Spacer(1, 6))
content.append(Paragraph(project2, bold_style))
content.append(Paragraph(project2_desc, normal_style))

# Experience
if exp:
    content.append(Spacer(1, 8))
    content.append(Paragraph("EXPERIENCE", section_style))
    content.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#BDC3C7')))
    content.append(Spacer(1, 6))
    content.append(Paragraph(exp, normal_style))

# Internship
content.append(Spacer(1, 8))
content.append(Paragraph("INTERNSHIP", section_style))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#BDC3C7')))
content.append(Spacer(1, 6))
content.append(Paragraph("21 Days AI Internship - M&T TechnoGuide Infosoft Pvt. Ltd.", bold_style))
content.append(Paragraph("Built 10+ AI projects including Image Generation, Face Detection, NLP, Voice Assistant, Chatbot Website and more using Python, OpenCV, NLTK, Flask.", normal_style))

# Build PDF
doc.build(content)

print(f"\nResume generated successfully!")
print(f"File saved: {filename}")
print("Open the PDF to see your professional resume!")