"""
HRMS Demo Application - Complete Showcase Version

⚠️ DEMO LIMITATIONS:
- Sample data only
- No data persistence
- Limited functionality 
- View-only mode

💰 Production Version Available:
- Complete functionality
- Real database integration  
- Advanced features
- Production-ready code

📧 Contact: shaheerahmad9023@gmail.com
💰 Pricing: Starting at $299
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

print("🚀 HRMS Demo Version Starting...")
print("⚠️  This is a DEMONSTRATION version")
print("💰 Production version: shaheerahmad9023@gmail.com")
print("🌐 Demo running at: http://localhost:8000")

app = FastAPI(
    title="HRMS Demo - Human Resource Management System", 
    description="Professional HRMS Demo - Production version available",
    version="1.0.0-demo"
)

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Demo data
DEMO_EMPLOYEES = [
    {"id": 1, "name": "John Doe", "email": "john.doe@demo.com", "role": "Manager", "phone": "+1 (555) 123-4567", "joined": "Jan 2023"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@demo.com", "role": "Developer", "phone": "+1 (555) 234-5678", "joined": "Mar 2023"},
    {"id": 3, "name": "Mike Johnson", "email": "mike.johnson@demo.com", "role": "Designer", "phone": "+1 (555) 345-6789", "joined": "Feb 2023"},
    {"id": 4, "name": "Sarah Wilson", "email": "sarah.wilson@demo.com", "role": "HR Specialist", "phone": "+1 (555) 456-7890", "joined": "Apr 2023"},
    {"id": 5, "name": "David Brown", "email": "david.brown@demo.com", "role": "Analyst", "phone": "+1 (555) 567-8901", "joined": "May 2023"},
]

DEMO_ATTENDANCE = [
    {"employee": "John Doe", "date": "2024-01-15", "check_in": "09:00 AM", "check_out": "06:00 PM", "status": "Present", "hours": "8.0"},
    {"employee": "Jane Smith", "date": "2024-01-15", "check_in": "09:15 AM", "check_out": "05:45 PM", "status": "Late", "hours": "7.5"},
    {"employee": "Mike Johnson", "date": "2024-01-15", "check_in": "08:45 AM", "check_out": "06:15 PM", "status": "Present", "hours": "8.5"},
    {"employee": "Sarah Wilson", "date": "2024-01-15", "check_in": "09:30 AM", "check_out": "05:30 PM", "status": "Late", "hours": "7.0"},
    {"employee": "David Brown", "date": "2024-01-15", "check_in": "08:50 AM", "check_out": "06:00 PM", "status": "Present", "hours": "8.2"},
]

# HTML Routes
@app.get("/", response_class=HTMLResponse)
async def demo_home(request: Request):
    return templates.TemplateResponse("demo_dashboard.html", {
        "request": request,
        "demo_mode": True,
        "employee_count": len(DEMO_EMPLOYEES),
        "contact_email": "shaheerahmad9023@gmail.com"
    })

@app.get("/login", response_class=HTMLResponse)
async def demo_login(request: Request):
    return templates.TemplateResponse("demo_login.html", {
        "request": request,
        "demo_mode": True
    })

@app.get("/employees", response_class=HTMLResponse)
async def demo_employees_page(request: Request):
    return templates.TemplateResponse("demo_employees.html", {
        "request": request,
        "employees": DEMO_EMPLOYEES,
        "demo_mode": True
    })

@app.get("/attendance", response_class=HTMLResponse)
async def demo_attendance_page(request: Request):
    return templates.TemplateResponse("demo_attendance.html", {
        "request": request,
        "attendance": DEMO_ATTENDANCE,
        "employees": DEMO_EMPLOYEES,
        "demo_mode": True,
        "present_count": 3,
        "late_count": 2,
        "absent_count": 0,
        "attendance_rate": "85%"
    })

# API Routes
@app.get("/api/employees")
async def demo_employees():
    return {
        "message": "DEMO: Employee Management",
        "employees": DEMO_EMPLOYEES,
        "note": "Sample data only. Production includes full CRUD operations.",
        "contact": "shaheerahmad9023@gmail.com"
    }

@app.get("/api/attendance")
async def demo_attendance():
    return {
        "message": "DEMO: Attendance Tracking",
        "attendance": DEMO_ATTENDANCE,
        "note": "Demo data only. Production includes real-time tracking.",
        "contact": "shaheerahmad9023@gmail.com"
    }

@app.get("/api/dashboard")
async def demo_dashboard():
    return {
        "message": "DEMO: Dashboard Statistics",
        "stats": {
            "total_employees": len(DEMO_EMPLOYEES),
            "present_today": 3,
            "late_today": 2,
            "attendance_rate": "85%",
            "system_status": "Demo Active"
        },
        "note": "Sample statistics only.",
        "contact": "shaheerahmad9023@gmail.com"
    }

@app.get("/demo-info")
async def demo_info():
    return {
        "demo_version": "1.0.0",
        "limitations": [
            "Sample data only",
            "No data persistence", 
            "Limited functionality",
            "View-only mode"
        ],
        "production_features": [
            "Complete CRUD operations",
            "Real database integration",
            "Advanced reporting",
            "User authentication",
            "Role-based access",
            "Export functionality",
            "Email notifications",
            "Advanced search & filters"
        ],
        "pricing": {
            "starter": "$299 - Core features",
            "professional": "$499 - Advanced features", 
            "enterprise": "$799 - Full features + customization"
        },
        "contact": "shaheerahmad9023@gmail.com",
        "demo_links": {
            "dashboard": "/",
            "login_demo": "/login",
            "employees_demo": "/employees",
            "attendance_demo": "/attendance",
            "api_employees": "/api/employees",
            "api_attendance": "/api/attendance"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, port=8000)