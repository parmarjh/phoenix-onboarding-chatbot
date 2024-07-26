import csv
import random
import faker

# Create a Faker instance
fake = faker.Faker()

# Define HR-specific questions, categories, and responses
questions = [
    "What is the company's leave policy?",
    "How can I request time off?",
    "Who should I contact for IT support?",
    "What is the procedure for performance reviews?",
    "How can I update my personal information?",
    "What benefits does the company offer?",
    "How do I access my pay stubs?",
    "What is the company's policy on remote work?",
    "How do I request a copy of my employment verification?",
    "What is the process for reporting workplace harassment?",
    # Add more HR-related questions as needed
]

categories = [
    "Leave Policy",
    "Leave Request",
    "IT Support",
    "Performance Reviews",
    "Personal Information",
    "Employee Benefits",
    "Pay Stubs",
    "Remote Work",
    "Employment Verification",
    "Workplace Harassment",
    # Add more categories as needed
]

responses = [
    "Our company offers various types of leave including annual leave, sick leave, and parental leave.",
    "To request time off, please submit a leave request form through the employee portal.",
    "For IT support, please contact the IT helpdesk via email at support@company.com.",
    "Performance reviews are conducted annually. Please check with HR for specific dates and procedures.",
    "You can update your personal information by logging into the employee portal and navigating to the profile section.",
    "Our company offers health insurance, retirement plans, and various employee perks.",
    "You can access your pay stubs through the payroll section of the employee portal.",
    "Our company allows remote work for eligible positions. Please consult with your manager to see if you qualify.",
    "To request an employment verification letter, please contact HR with your request.",
    "Report any incidents of workplace harassment to HR immediately. You can do so via email or in person.",
    # Add more responses as needed
]

# Define keywords and examples (can be adjusted for more specificity)
keywords = [
    "Leave policy,Annual leave,Sick leave,Parental leave",
    "Request time off,Leave request form,Employee portal",
    "IT support,Helpdesk,Contact IT",
    "Performance reviews,Annual review,HR procedures",
    "Update personal information,Employee portal,Profile section",
    "Employee benefits,Health insurance,Retirement plans",
    "Pay stubs,Employee portal,Payroll section",
    "Remote work,Eligibility,Manager consultation",
    "Employment verification,HR request,Employment letter",
    "Workplace harassment,HR reporting,Email report",
    # Add more keywords as needed
]

examples = [
    "What is annual leave?",
    "How do I submit a leave request?",
    "How do I get IT help?",
    "When are performance reviews held?",
    "How do I change my address in the system?",
    "What are the employee perks?",
    "Where can I find my pay stubs online?",
    "Can I work from home?",
    "How can I get an employment verification letter?",
    "How do I report harassment?",
    # Add more examples as needed
]
statuses = ["VALIDATE",
          "TEST",
          "TRAIN"]
# Open a CSV file to write
with open('hr_chatbot_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    
    # Write the header
    writer.writerow(["ID", "Question", "Category", "Response", "Keywords", "Examples", "Date", "Status"])
    
    # Generate 1000 rows of HR-related data
    for i in range(1, 1001):
        random.shuffle(statuses)
        status = statuses[0]
        row = [
            str(i),
            f'"{random.choice(questions)}"',
            f'"{random.choice(categories)}"',
            f'"{random.choice(responses)}"',
            f'"{random.choice(keywords)}"',
            f'"{random.choice(examples)}"',
            f'"{fake.date_this_decade().isoformat()}"',
            f'"{status}"'

        ]
        writer.writerow(row)