# scripts/seed_data.py
#
# Purpose:
#   Populates MongoDB with sample data for the HR Employee Service Portal:
#   User, Category, Service Request, Comment, Attachment, AuditLog.
#
#   The data contains realistic cross-references:
#   - A service request's category_id points to a real category
#   - A service request's created_by points to a real user
#   - A comment's service_request_id points to a real service request
#   - An attachment's service_request_id points to a real service request
#   - An audit log's service_request_id points to a real service request
#
# Run from the backend project root:
#   python -m scripts.seed_data
#
# WARNING:
#   This clears the 6 collections below before inserting.
#   Use this for a fresh/development database, not production.


import sys
from datetime import datetime, timedelta
from pathlib import Path


# Allows running the script directly:
# python scripts/seed_data.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


from app.database import database


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

NOW = datetime.utcnow()


def days_ago(n: int) -> datetime:
    """Returns a timestamp n days before the current time."""
    return NOW - timedelta(days=n)


# ---------------------------------------------------------------------------
# 1. USERS
# ---------------------------------------------------------------------------
# Roles:
#   Employee
#   HR Executive
#   HR Manager
#   Admin
#
# Role values are kept lowercase to match the style of the original
# seed structure. If your schema uses exact capitalized values, change them
# to "Employee", "HR Executive", etc.
# ---------------------------------------------------------------------------

USERS = [
    {
        "id": "user-employee-1",
        "name": "Priya Sharma",
        "email": "priya.sharma@company.com",
        "password": "password123",
        "role": "employee",
        "created_at": days_ago(60),
    },
    {
        "id": "user-employee-2",
        "name": "Rahul Verma",
        "email": "rahul.verma@company.com",
        "password": "password123",
        "role": "employee",
        "created_at": days_ago(55),
    },
    {
        "id": "user-employee-3",
        "name": "Ananya Gupta",
        "email": "ananya.gupta@company.com",
        "password": "password123",
        "role": "employee",
        "created_at": days_ago(50),
    },
    {
        "id": "user-employee-4",
        "name": "Karan Mehta",
        "email": "karan.mehta@company.com",
        "password": "password123",
        "role": "employee",
        "created_at": days_ago(45),
    },
    {
        "id": "user-hr-exec-1",
        "name": "Neha Singh",
        "email": "neha.singh@company.com",
        "password": "password123",
        "role": "hr_executive",
        "created_at": days_ago(90),
    },
    {
        "id": "user-hr-exec-2",
        "name": "Arjun Nair",
        "email": "arjun.nair@company.com",
        "password": "password123",
        "role": "hr_executive",
        "created_at": days_ago(85),
    },
    {
        "id": "user-hr-manager-1",
        "name": "Divya Iyer",
        "email": "divya.iyer@company.com",
        "password": "password123",
        "role": "hr_manager",
        "created_at": days_ago(120),
    },
    {
        "id": "user-admin-1",
        "name": "Vikram Rao",
        "email": "vikram.rao@company.com",
        "password": "password123",
        "role": "admin",
        "created_at": days_ago(150),
    },
]


# ---------------------------------------------------------------------------
# 2. CATEGORIES
# ---------------------------------------------------------------------------

CATEGORIES = [
    {
        "id": "cat-leave-clarification",
        "name": "LEAVE_CLARIFICATION",
        "description": (
            "Questions and clarifications related to employee leave "
            "balances, leave policies, leave eligibility, leave types, "
            "and the leave application process."
        ),
        "created_at": days_ago(120),
    },
    {
        "id": "cat-payroll-query",
        "name": "PAYROLL_QUERY",
        "description": (
            "Employee queries related to salary, payslips, payroll "
            "deductions, salary components, tax deductions, and other "
            "payroll-related matters."
        ),
        "created_at": days_ago(120),
    },
    {
        "id": "cat-experience-letter",
        "name": "EXPERIENCE_LETTER",
        "description": (
            "Requests for experience letters, employment confirmation, "
            "service certificates, and related employment documentation."
        ),
        "created_at": days_ago(120),
    },
    {
        "id": "cat-asset-request",
        "name": "ASSET_REQUEST",
        "description": (
            "Requests related to company-provided employee assets such as "
            "laptops, ID cards, access cards, office equipment, and other "
            "work-related resources."
        ),
        "created_at": days_ago(120),
    },
    {
        "id": "cat-onboarding-request",
        "name": "ONBOARDING_REQUEST",
        "description": (
            "Requests and assistance related to employee onboarding, "
            "joining formalities, documentation, HR orientation, and "
            "initial employee setup."
        ),
        "created_at": days_ago(120),
    },
]


# ---------------------------------------------------------------------------
# 3. SERVICE REQUESTS
# ---------------------------------------------------------------------------
#
# IMPORTANT:
# Instead of:
#   ticket-1
#
# We now use:
#   service-request-1
#
# These IDs are referenced by Comments, Attachments and Audit Logs.
# ---------------------------------------------------------------------------

SERVICE_REQUESTS = [
    {
        "id": "service-request-1",
        "title": "Clarification about remaining annual leave balance",
        "description": (
            "I would like to know my current annual leave balance and "
            "whether unused leave from the previous period can be carried "
            "forward to the current year."
        ),
        "category_id": "cat-leave-clarification",
        "status": "new",
        "created_by": "user-employee-1",
        "assigned_to": None,
        "created_at": days_ago(8),
        "updated_at": days_ago(8),
    },

    {
        "id": "service-request-2",
        "title": "Question about sick leave eligibility",
        "description": (
            "Please clarify the number of sick leave days available to me "
            "and whether any supporting document is required when applying "
            "for sick leave."
        ),
        "category_id": "cat-leave-clarification",
        "status": "assigned",
        "created_by": "user-employee-2",
        "assigned_to": "user-hr-exec-1",
        "created_at": days_ago(7),
        "updated_at": days_ago(5),
    },

    {
        "id": "service-request-3",
        "title": "Salary credited is different from payslip amount",
        "description": (
            "The salary credited to my bank account appears to be different "
            "from the net salary mentioned in my latest payslip. Please "
            "help me understand the difference."
        ),
        "category_id": "cat-payroll-query",
        "status": "in_progress",
        "created_by": "user-employee-3",
        "assigned_to": "user-hr-exec-2",
        "created_at": days_ago(6),
        "updated_at": days_ago(3),
    },

    {
        "id": "service-request-4",
        "title": "Clarification regarding payroll deduction",
        "description": (
            "I noticed an additional deduction in my latest salary. "
            "Please provide details about the deduction and confirm "
            "whether it is a standard payroll deduction."
        ),
        "category_id": "cat-payroll-query",
        "status": "resolved",
        "created_by": "user-employee-4",
        "assigned_to": "user-hr-exec-1",
        "created_at": days_ago(12),
        "updated_at": days_ago(2),
    },

    {
        "id": "service-request-5",
        "title": "Request for experience letter",
        "description": (
            "I require an experience letter confirming my employment "
            "with the company. Please let me know the process and "
            "expected timeline for receiving the document."
        ),
        "category_id": "cat-experience-letter",
        "status": "assigned",
        "created_by": "user-employee-1",
        "assigned_to": "user-hr-exec-2",
        "created_at": days_ago(5),
        "updated_at": days_ago(4),
    },

    {
        "id": "service-request-6",
        "title": "Experience letter required for employment documentation",
        "description": (
            "I need an official experience letter for employment-related "
            "documentation. Kindly process the request and provide the "
            "letter once it is approved."
        ),
        "category_id": "cat-experience-letter",
        "status": "closed",
        "created_by": "user-employee-2",
        "assigned_to": "user-hr-exec-1",
        "created_at": days_ago(15),
        "updated_at": days_ago(3),
    },

    {
        "id": "service-request-7",
        "title": "Request for company laptop",
        "description": (
            "I have joined a new project that requires a company laptop. "
            "Please arrange the required laptop asset and let me know "
            "when it will be available for collection."
        ),
        "category_id": "cat-asset-request",
        "status": "in_progress",
        "created_by": "user-employee-3",
        "assigned_to": "user-hr-exec-2",
        "created_at": days_ago(4),
        "updated_at": days_ago(2),
    },

    {
        "id": "service-request-8",
        "title": "Request for replacement employee ID card",
        "description": (
            "I have misplaced my employee ID card and need a replacement. "
            "Please guide me through the process and let me know if any "
            "formalities are required."
        ),
        "category_id": "cat-asset-request",
        "status": "new",
        "created_by": "user-employee-4",
        "assigned_to": None,
        "created_at": days_ago(2),
        "updated_at": days_ago(2),
    },

    {
        "id": "service-request-9",
        "title": "New employee onboarding assistance",
        "description": (
            "I am joining the organization and need assistance with "
            "onboarding formalities, required documents, HR orientation, "
            "and other joining procedures."
        ),
        "category_id": "cat-onboarding-request",
        "status": "assigned",
        "created_by": "user-employee-1",
        "assigned_to": "user-hr-exec-1",
        "created_at": days_ago(3),
        "updated_at": days_ago(2),
    },

    {
        "id": "service-request-10",
        "title": "Clarification on onboarding documentation",
        "description": (
            "Please confirm which documents are required to complete my "
            "employee onboarding process and whether the documents can "
            "be submitted digitally."
        ),
        "category_id": "cat-onboarding-request",
        "status": "resolved",
        "created_by": "user-employee-2",
        "assigned_to": "user-hr-exec-2",
        "created_at": days_ago(10),
        "updated_at": days_ago(4),
    },
]


# ---------------------------------------------------------------------------
# 4. COMMENTS
# ---------------------------------------------------------------------------
#
# IMPORTANT:
# ticket_id has been changed to service_request_id.
#
# The IDs below exactly match the Service Request IDs above.
# ---------------------------------------------------------------------------

COMMENTS = [
    {
        "id": "comment-1",
        "service_request_id": "service-request-1",
        "author_id": "user-employee-1",
        "content": (
            "I checked the employee portal, but I am not sure whether "
            "the unused leave has been carried forward."
        ),
        "created_at": days_ago(8),
    },

    {
        "id": "comment-2",
        "service_request_id": "service-request-2",
        "author_id": "user-hr-exec-1",
        "content": (
            "Your leave balance has been checked. We are reviewing the "
            "applicable leave policy before confirming the details."
        ),
        "created_at": days_ago(5),
    },

    {
        "id": "comment-3",
        "service_request_id": "service-request-3",
        "author_id": "user-hr-exec-2",
        "content": (
            "We are checking the payroll records and salary components "
            "for the current month."
        ),
        "created_at": days_ago(3),
    },

    {
        "id": "comment-4",
        "service_request_id": "service-request-4",
        "author_id": "user-hr-exec-1",
        "content": (
            "The deduction has been verified against the payroll records. "
            "The details have been shared with the employee."
        ),
        "created_at": days_ago(2),
    },

    {
        "id": "comment-5",
        "service_request_id": "service-request-5",
        "author_id": "user-employee-1",
        "content": (
            "Please let me know if any additional information is required "
            "to process my experience letter."
        ),
        "created_at": days_ago(4),
    },

    {
        "id": "comment-6",
        "service_request_id": "service-request-6",
        "author_id": "user-hr-exec-1",
        "content": (
            "The experience letter has been prepared and shared with "
            "the employee."
        ),
        "created_at": days_ago(3),
    },

    {
        "id": "comment-7",
        "service_request_id": "service-request-7",
        "author_id": "user-hr-exec-2",
        "content": (
            "The asset request has been forwarded for availability "
            "confirmation. We will update the request once confirmed."
        ),
        "created_at": days_ago(2),
    },

    {
        "id": "comment-8",
        "service_request_id": "service-request-8",
        "author_id": "user-employee-4",
        "content": (
            "Please let me know when I can collect the replacement ID card."
        ),
        "created_at": days_ago(2),
    },

    {
        "id": "comment-9",
        "service_request_id": "service-request-9",
        "author_id": "user-hr-exec-1",
        "content": (
            "Your onboarding request has been assigned. We will assist "
            "you with the required joining formalities."
        ),
        "created_at": days_ago(2),
    },

    {
        "id": "comment-10",
        "service_request_id": "service-request-10",
        "author_id": "user-hr-exec-2",
        "content": (
            "The required onboarding documents have been confirmed. "
            "Digital submission is supported for the listed documents."
        ),
        "created_at": days_ago(4),
    },
]


# ---------------------------------------------------------------------------
# 5. ATTACHMENTS
# ---------------------------------------------------------------------------
#
# IMPORTANT:
# ticket_id has been changed to service_request_id.
#
# These are metadata-only sample attachments, following the same structure
# as the original seed data.
# ---------------------------------------------------------------------------

ATTACHMENTS = [
    {
        "id": "attachment-1",
        "service_request_id": "service-request-1",
        "uploaded_by": "user-employee-1",
        "filename": "leave_balance_screenshot.png",
        "url": "https://files.example.com/leave_balance_screenshot.png",
        "size": 145600,
        "created_at": days_ago(8),
    },

    {
        "id": "attachment-2",
        "service_request_id": "service-request-2",
        "uploaded_by": "user-employee-2",
        "filename": "leave_application.pdf",
        "url": "https://files.example.com/leave_application.pdf",
        "size": 78200,
        "created_at": days_ago(7),
    },

    {
        "id": "attachment-3",
        "service_request_id": "service-request-3",
        "uploaded_by": "user-employee-3",
        "filename": "salary_slip.pdf",
        "url": "https://files.example.com/salary_slip.pdf",
        "size": 126400,
        "created_at": days_ago(6),
    },

    {
        "id": "attachment-4",
        "service_request_id": "service-request-4",
        "uploaded_by": "user-employee-4",
        "filename": "payroll_deduction_screenshot.png",
        "url": "https://files.example.com/payroll_deduction_screenshot.png",
        "size": 98500,
        "created_at": days_ago(12),
    },

    {
        "id": "attachment-5",
        "service_request_id": "service-request-5",
        "uploaded_by": "user-employee-1",
        "filename": "experience_letter_request.pdf",
        "url": "https://files.example.com/experience_letter_request.pdf",
        "size": 84500,
        "created_at": days_ago(5),
    },

    {
        "id": "attachment-6",
        "service_request_id": "service-request-6",
        "uploaded_by": "user-hr-exec-1",
        "filename": "experience_letter.pdf",
        "url": "https://files.example.com/experience_letter.pdf",
        "size": 92300,
        "created_at": days_ago(3),
    },

    {
        "id": "attachment-7",
        "service_request_id": "service-request-7",
        "uploaded_by": "user-employee-3",
        "filename": "asset_request_form.pdf",
        "url": "https://files.example.com/asset_request_form.pdf",
        "size": 112700,
        "created_at": days_ago(4),
    },

    {
        "id": "attachment-8",
        "service_request_id": "service-request-8",
        "uploaded_by": "user-employee-4",
        "filename": "id_card_replacement_request.pdf",
        "url": "https://files.example.com/id_card_replacement_request.pdf",
        "size": 68400,
        "created_at": days_ago(2),
    },

    {
        "id": "attachment-9",
        "service_request_id": "service-request-9",
        "uploaded_by": "user-employee-1",
        "filename": "onboarding_documents.pdf",
        "url": "https://files.example.com/onboarding_documents.pdf",
        "size": 238500,
        "created_at": days_ago(3),
    },

    {
        "id": "attachment-10",
        "service_request_id": "service-request-10",
        "uploaded_by": "user-employee-2",
        "filename": "joining_document_checklist.pdf",
        "url": "https://files.example.com/joining_document_checklist.pdf",
        "size": 75600,
        "created_at": days_ago(10),
    },
]


# ---------------------------------------------------------------------------
# 6. AUDIT LOGS
# ---------------------------------------------------------------------------
#
# IMPORTANT:
# ticket_id has been changed to service_request_id.
#
# All details also refer to "Service Request", not "Ticket".
# ---------------------------------------------------------------------------

AUDIT_LOGS = [
    {
        "id": "audit-1",
        "service_request_id": "service-request-1",
        "action": "created",
        "performed_by": "user-employee-1",
        "details": (
            "Service Request created with status 'new'. "
            "Title: 'Clarification about remaining annual leave balance'."
        ),
        "created_at": days_ago(8),
    },

    {
        "id": "audit-2",
        "service_request_id": "service-request-2",
        "action": "created",
        "performed_by": "user-employee-2",
        "details": (
            "Service Request created with status 'new'. "
            "Title: 'Question about sick leave eligibility'."
        ),
        "created_at": days_ago(7),
    },

    {
        "id": "audit-3",
        "service_request_id": "service-request-2",
        "action": "assigned",
        "performed_by": "user-hr-manager-1",
        "details": (
            "Service Request 'service-request-2' assigned to "
            "'user-hr-exec-1'. Status moved from 'new' to 'assigned'."
        ),
        "created_at": days_ago(5),
    },

    {
        "id": "audit-4",
        "service_request_id": "service-request-3",
        "action": "created",
        "performed_by": "user-employee-3",
        "details": (
            "Service Request created with status 'new'. "
            "Title: 'Salary credited is different from payslip amount'."
        ),
        "created_at": days_ago(6),
    },

    {
        "id": "audit-5",
        "service_request_id": "service-request-3",
        "action": "assigned",
        "performed_by": "user-hr-manager-1",
        "details": (
            "Service Request 'service-request-3' assigned to "
            "'user-hr-exec-2'. Status moved from 'new' to 'assigned'."
        ),
        "created_at": days_ago(5),
    },

    {
        "id": "audit-6",
        "service_request_id": "service-request-3",
        "action": "status_changed",
        "performed_by": "user-hr-exec-2",
        "details": (
            "Service Request 'service-request-3' status changed "
            "from 'assigned' to 'in_progress'. "
            "Title: 'Salary credited is different from payslip amount'."
        ),
        "created_at": days_ago(3),
    },

    {
        "id": "audit-7",
        "service_request_id": "service-request-4",
        "action": "status_changed",
        "performed_by": "user-hr-exec-1",
        "details": (
            "Service Request 'service-request-4' status changed "
            "from 'in_progress' to 'resolved'. "
            "Title: 'Clarification regarding payroll deduction'."
        ),
        "created_at": days_ago(2),
    },

    {
        "id": "audit-8",
        "service_request_id": "service-request-6",
        "action": "status_changed",
        "performed_by": "user-hr-exec-1",
        "details": (
            "Service Request 'service-request-6' status changed "
            "from 'resolved' to 'closed'. "
            "Title: 'Experience letter required for employment documentation'."
        ),
        "created_at": days_ago(3),
    },

    {
        "id": "audit-9",
        "service_request_id": "service-request-7",
        "action": "assigned",
        "performed_by": "user-hr-manager-1",
        "details": (
            "Service Request 'service-request-7' assigned to "
            "'user-hr-exec-2'. "
            "Title: 'Request for company laptop'."
        ),
        "created_at": days_ago(2),
    },

    {
        "id": "audit-10",
        "service_request_id": "service-request-9",
        "action": "assigned",
        "performed_by": "user-hr-manager-1",
        "details": (
            "Service Request 'service-request-9' assigned to "
            "'user-hr-exec-1'. "
            "Title: 'New employee onboarding assistance'."
        ),
        "created_at": days_ago(2),
    },
]


# ---------------------------------------------------------------------------
# 7. SEED DATABASE
# ---------------------------------------------------------------------------

def seed() -> None:
    """
    Clears the six collections and inserts the HR Employee Service Portal
    seed data.
    """

    collections_and_data = [
        ("users", USERS),
        ("categories", CATEGORIES),
        ("service_requests", SERVICE_REQUESTS),
        ("comments", COMMENTS),
        ("attachments", ATTACHMENTS),
        ("audit_logs", AUDIT_LOGS),
    ]

    for collection_name, documents in collections_and_data:
        collection = database[collection_name]

        deleted = collection.delete_many({}).deleted_count

        collection.insert_many(documents)

        print(
            f"{collection_name}: "
            f"cleared {deleted} old record(s), "
            f"inserted {len(documents)} new record(s)"
        )


# ---------------------------------------------------------------------------
# RUN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    seed()
    print("\nHR Employee Service Portal seeding complete.")