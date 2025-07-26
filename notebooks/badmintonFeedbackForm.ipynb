# Install required libraries
!pip install google-auth google-auth-oauthlib google-auth-httplib2 googleapiclient gspread

# Import necessary libraries
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread

# Path to your service account JSON file (Upload it to Colab first)
SERVICE_ACCOUNT_FILE = '/content/drive/MyDrive/GoogleApiKeys/XXXX.json'

SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets"
]

# Authenticate with Google APIs
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
forms_service = build("forms", "v1", credentials=credentials)
sheets_service = build("sheets", "v4", credentials=credentials)
gc = gspread.authorize(credentials)

# Step 1: Create a Google Form (Only Title Allowed Initially)
form_body = {
    "info": {
        "title": "Badminton Practice & Tournament Feedback",
        "documentTitle" : "Badminton Practice & Tournament Feedback"
    }
}

form = forms_service.forms().create(body=form_body).execute()
form_id = form["formId"]

# ✅ Fix: Add Sections - Define questions with section breaks
# Build questions list with correct indexing
questions = []

# --- TRAINING SECTION ---
training_questions = [
    {"title": "Date of Practice Session", "question": {"required": True, "textQuestion": {}}},
    {"title": "Session Duration (in minutes)", "question": {"required": True, "textQuestion": {}}},
    {"title": "Overall Performance Rating (1-10)", "question": {"required": True, "scaleQuestion": {"low": 1, "high": 10}}},
    {"title": "How effective was your Warm-up Routine?", "question": {"choiceQuestion": {"type": "RADIO", "options": [
        {"value": "Excellent"}, {"value": "Good"}, {"value": "Average"}, {"value": "Needs Improvement"}]}}},
    {"title": "Footwork Speed & Agility", "question": {"choiceQuestion": {"type": "RADIO", "options": [
        {"value": "Fast & Sharp"}, {"value": "Good"}, {"value": "Average"}, {"value": "Needs Work"}]}}},
    {"title": "Strongest Shots Today?", "question": {"choiceQuestion": {"type": "CHECKBOX", "options": [
        {"value": "Clears"}, {"value": "Smashes"}, {"value": "Drop Shots"}, {"value": "Net Play"}, {"value": "Backhand"}, {"value": "Other"}]}}},
    {"title": "Challenging Shots?", "question": {"textQuestion": {}}},
    {"title": "Shot Selection Effectiveness?", "question": {"choiceQuestion": {"type": "RADIO", "options": [
        {"value": "Smart & Varied"}, {"value": "Predictable"}, {"value": "Needs More Strategy"}]}}},
    {"title": "Court Coverage", "question": {"choiceQuestion": {"type": "RADIO", "options": [
        {"value": "Excellent"}, {"value": "Good"}, {"value": "Average"}, {"value": "Needs Work"}]}}},
    {"title": "Stamina & Endurance", "question": {"choiceQuestion": {"type": "RADIO", "options": [
        {"value": "Strong"}, {"value": "Good"}, {"value": "Average"}, {"value": "Weak"}]}}},
    {"title": "Mental Focus & Confidence", "question": {"choiceQuestion": {"type": "RADIO", "options": [
        {"value": "Focused"}, {"value": "Confident"}, {"value": "Distracted"}, {"value": "Nervous"}]}}},
    {"title": "Overall Summary of Today’s Practice", "question": {"textQuestion": {}}},
    {"title": "Focus Areas for the Next Session", "question": {"textQuestion": {}}}
]

# --- SECTION BREAK ---
section_break = {
    "createItem": {
        "item": {
            "title": "Tournament Feedback",
            "description": "This section is for tournament-related reflections.",
            "pageBreakItem": {}
        },
        "location": {"index": len(training_questions)}  # Placed after training questions
    }
}

# --- TOURNAMENT SECTION ---
tournament_questions = [
    {"title": "Did you play in a tournament recently?", "question": {"choiceQuestion": {"type": "RADIO", "options": [
        {"value": "Yes"}, {"value": "No"}]}}},
    {"title": "Tournament Name & Date (if applicable)", "question": {"textQuestion": {}}},
    {"title": "Tournament Performance Rating (1-10)", "question": {"scaleQuestion": {"low": 1, "high": 10}}},
    {"title": "What went well in the tournament?", "question": {"textQuestion": {}}},
    {"title": "Biggest challenges faced in the tournament?", "question": {"textQuestion": {}}},
    {"title": "Key learnings from this tournament?", "question": {"textQuestion": {}}},
    {"title": "What will you improve before the next tournament?", "question": {"textQuestion": {}}}
]

# --- Build full requests list ---
index = 0

# Add training questions
for q in training_questions:
    questions.append({
        "createItem": {
            "item": {
                "title": q["title"],
                "questionItem": {"question": q["question"]}
            },
            "location": {"index": index}
        }
    })
    index += 1

# Add section break
questions.append(section_break)
index += 1

# Add tournament questions
for q in tournament_questions:
    questions.append({
        "createItem": {
            "item": {
                "title": q["title"],
                "questionItem": {"question": q["question"]}
            },
            "location": {"index": index}
        }
    })
    index += 1




# Step 3: Add Questions to Form
forms_service.forms().batchUpdate(formId=form_id, body={"requests": questions}).execute()

# Step 4: Get Form URL
form_url = f"https://docs.google.com/forms/d/{form_id}/edit"
print("✅ Google Form Created Successfully!")
print(f"🔗 Form URL: {form_url}")

# Step 5: Create a Google Sheet
spreadsheet = sheets_service.spreadsheets().create(
    body={"properties": {"title": "Badminton Practice & Tournament Responses"}, "sheets": [{"properties": {"title": "Responses"}}]}
).execute()

sheet_id = spreadsheet["spreadsheetId"]
sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"
print("📊 Google Sheet Created for Responses!")
print(f"🔗 Sheet URL: {sheet_url}")

