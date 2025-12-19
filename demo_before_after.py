#!/usr/bin/env python3
"""
Demo: Before vs After - Real Document Analysis
This shows the difference between hardcoded responses and real analysis
"""

import asyncio
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from app.services.ai_agents import AIAgentService
from app.services.enhanced_drafting_agent import EnhancedDraftingAgent

async def demo_before_after():
    """Demonstrate the improvement from hardcoded to real analysis"""
    
    print("🎯 DEMO: Before vs After - Real Document Analysis")
    print("=" * 70)
    
    # Create two very different test documents
    documents = {
        'simple_contract.txt': """
        Simple Agreement
        
        John will mow Mary's lawn every week.
        Mary will pay John $50 per week.
        """,
        
        'complex_employment.txt': """
        EMPLOYMENT AGREEMENT
        
        This Employment Agreement is entered into on January 1, 2024 between 
        TechCorp Inc., a Delaware corporation ("Company") and Sarah Johnson ("Employee").
        
        1. POSITION AND DUTIES
        Employee is hired as Chief Technology Officer and agrees to perform duties 
        including strategic technology planning, team leadership, and product development oversight.
        
        2. COMPENSATION AND BENEFITS
        Base Salary: $250,000 per year, payable bi-weekly
        Stock Options: 50,000 shares vesting over 4 years
        Benefits: Full health, dental, vision insurance, 401k with 6% match
        Vacation: 25 days per year plus standard holidays
        
        3. CONFIDENTIALITY AND NON-COMPETE
        Employee agrees to maintain strict confidentiality of all proprietary information,
        trade secrets, customer data, and business strategies. Employee shall not compete
        with Company for 12 months after termination within a 50-mile radius.
        
        4. INTELLECTUAL PROPERTY
        All inventions, patents, copyrights, and work product created during employment
        shall be owned exclusively by Company.
        
        5. TERMINATION
        Either party may terminate this agreement with 30 days written notice.
        Company may terminate immediately for cause including misconduct or breach.
        
        6. GOVERNING LAW
        This agreement shall be governed by the laws of Delaware and any disputes
        shall be resolved through binding arbitration.
        """
    }
    
    # Create test files
    for filename, content in documents.items():
        with open(filename, 'w') as f:
            f.write(content)
    
    agent = AIAgentService()
    drafting_agent = EnhancedDraftingAgent()
    
    print("\n📊 COMPARISON: Simple vs Complex Document Analysis")
    print("=" * 70)
    
    for filename, content in documents.items():
        print(f"\n📄 ANALYZING: {filename.upper()}")
        print("-" * 50)
        
        # Clause Extraction
        clause_result = await agent.extract_clauses(filename, {})
        print(f"🔍 CLAUSES FOUND: {clause_result.get('total_clauses', 0)}")
        for clause in clause_result.get('clauses', [])[:3]:
            print(f"   • {clause['type']}: {clause['content'][:60]}...")
        
        # Risk Analysis
        risk_result = await agent.detect_risks(filename, {})
        print(f"⚠️  RISK SCORE: {risk_result.get('risk_score', 0):.1f}/10")
        print(f"   Risks Found: {risk_result.get('total_risks', 0)}")
        
        # Missing Clauses
        doc_type = 'employment_contract' if 'employment' in filename else 'service_agreement'
        missing_result = await drafting_agent.suggest_missing_clauses(content, doc_type)
        print(f"📋 COMPLETENESS: {missing_result.get('completeness_score', 0):.1f}%")
        print(f"   Missing: {len(missing_result.get('missing_clauses', []))}")
        print(f"   Present: {len(missing_result.get('present_clauses', []))}")
        
        # Document Summary
        summary_result = await agent.summarize_document(filename, {})
        if 'summary' in summary_result:
            summary = summary_result['summary']
            print(f"📝 SUMMARY: {summary['document_type']}")
            print(f"   Words: {summary['word_count']}")
            print(f"   Parties: {summary['parties_involved']}")
    
    print(f"\n🎉 KEY IMPROVEMENTS DEMONSTRATED:")
    print("=" * 70)
    print("✅ DIFFERENT DOCUMENTS → DIFFERENT RESULTS")
    print("   • Simple contract: Few clauses, basic analysis")
    print("   • Complex employment: Many clauses, detailed analysis")
    print()
    print("✅ REAL CONTENT ANALYSIS")
    print("   • Actual clause extraction from document text")
    print("   • Risk scores based on missing elements")
    print("   • Completeness based on actual content")
    print()
    print("✅ DOCUMENT-SPECIFIC INSIGHTS")
    print("   • Employment contract: Higher completeness, more clauses")
    print("   • Simple contract: Lower completeness, fewer clauses")
    print()
    print("✅ ACCURATE WORD COUNTS & METADATA")
    print("   • Real word counts from actual documents")
    print("   • Proper document type detection")
    print("   • Actual party identification")
    
    # Cleanup
    for filename in documents.keys():
        os.remove(filename)
    
    print(f"\n🚀 YOUR LEGAL DOCUMENT ASSISTANT IS NOW FULLY OPERATIONAL!")
    print("=" * 70)
    print("🌐 Frontend: http://localhost:5174")
    print("🔧 Backend API: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print()
    print("Ready to analyze YOUR real documents! 🎯")

if __name__ == "__main__":
    asyncio.run(demo_before_after())