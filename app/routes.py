from fastapi import APIRouter
from pydantic import BaseModel

from app.search_service import search_businesses
from app.scrape_service import scrape_website
from app.llm_service import analyze_business
from app.scoring_service import score_lead
from app.outreach_service import generate_outreach
from app.storage_service import save_results
from app.email_service import extract_emails
from app.export_service import export_to_csv


router = APIRouter()


class LeadRequest(BaseModel):
    niche: str
    location: str
    num_leads: int


@router.get("/")
def home():
    return {
        "message": "Lead Generation Agent API is running"
    }


@router.post("/generate-leads")
def generate_leads(request: LeadRequest):
    search_results = search_businesses(
        niche=request.niche,
        location=request.location,
        num_leads=request.num_leads
    )

    final_results = []

    for item in search_results:
        website = item.get("link", "")
        snippet = item.get("snippet", "")
        company_name = item.get("title", "")

        website_text = scrape_website(website)

        emails = extract_emails(website_text)

        analysis = analyze_business(website_text)

        score = score_lead(analysis)

        outreach = generate_outreach(analysis)

        final_results.append({
            "company_name": company_name,
            "website": website,
            "emails": emails,
            "snippet": snippet,
            "analysis": analysis,
            "score": score,
            "outreach": outreach
        })

    save_results(final_results)

    export_to_csv(final_results)

    return {
        "results": final_results
    }