"""
HRMS Demo Application - Showcase Version

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

📧 Contact: YOUR-EMAIL@example.com
💰 Pricing: Starting at $299
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

print("🚀 HRMS Demo Version Starting...")
print("⚠️  This is a DEMONSTRATION version")
print("💰 Production version: YOUR-EMAIL@example.com")
print("🌐 Demo running at: http://localhost:8000")

app = FastAPI(
    title="HRMS Demo - Human Resource Management System",
    description="Professional HRMS Demo - Production version available",
    version="1.0.0-demo"
)

# Demo data
DEMO_EMPLOYEES = [
    {"id": 1, "name": "Shaheer Ahmad", "email": "shaheer@demo.com", "role": "Manager"},
    {"id": 2, "name": "Jane Smith", "email": "jane@demo.com", "role": "Developer"},
    {"id": 3, "name": "Mike Johnson", "email": "mike@demo.com", "role": "Designer"},
]

@app.get("/")
async def demo_home():
    return {
        "message": "🏢 HRMS Demo Version",
        "warning": "This is a demo with limited functionality",
        "features": [
            "Employee Management (View Only)",
            "Attendance Overview (Sample Data)",
            "Dashboard Statistics (Demo)",
            "Responsive Design (Working)"
        ],
        "production_contact": "shaheerahmad9023@gmail.com",
        "pricing": "Starting at $999"
    }

@app.get("/employees")
async def demo_employees():
    return {
        "message": "DEMO: Employee Management",
        "employees": DEMO_EMPLOYEES,
        "note": "Sample data only. Production includes full CRUD operations.",
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
            "Role-based access"
        ],
        "pricing": {
            "Complete": "$999 For Complete Production Code with minor in demand Customization in Zip-file",
        },
        "contact": "shaheerahmad9023@gmail.com"
    }

if __name__ == "__main__":
    uvicorn.run(app,port=8000)
