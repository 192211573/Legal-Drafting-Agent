#!/usr/bin/env python3
"""
Test script for the Legal Document Assistant - Drafting Agent
This script tests the new enhanced features we've implemented.
"""

import asyncio
import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from app.services.enhanced_drafting_agent import EnhancedDraftingAgent

async def test_legal_assistant():
    """Test the Legal Document Assistant functionality"""
    
    print("🤖 Testing Legal Document Assistant - Drafting Agent")
    print("=" * 60)
    
    # Initialize the agent
    agent = EnhancedDraftingAgent()
    
    # Test 1: Explain Legal Terms
    print("\n📖 Test 1: Explaining Legal Terms")
    print("-" * 30)
    
    legal_text = """
    The parties hereby agree that notwithstanding any prior agreements, 
    this contract shall indemnify both parties against liability for 
    breach of confidentiality clauses.
    """
    
    result = await agent.explain_legal_terms(legal_text)
    if result['success']:
        print(f"✅ Found {result['terms_found']} legal terms")
        for term, explanation in result['explanations'].items():
            print(f"   • {term}: {explanation}")
        print(f"\n📝 Simplified: {result['simplified_text']}")
    else:
        print(f"❌ Error: {result['error']}")
    
    # Test 2: Suggest Missing Clauses
    print("\n📋 Test 2: Suggesting Missing Clauses")
    print("-" * 30)
    
    incomplete_contract = """
    This is an agreement between John Doe and ABC Company.
    John will provide consulting services for $5000.
    """
    
    result = await agent.suggest_missing_clauses(incomplete_contract, 'service_agreement')
    if result['success']:
        print(f"✅ Completeness Score: {result['completeness_score']:.1f}%")
        print("Missing clauses:")
        for clause in result['missing_clauses']:
            print(f"   • {clause['name']}: {clause['description']}")
    else:
        print(f"❌ Error: {result['error']}")
    
    # Test 3: Check Document Completeness
    print("\n✅ Test 3: Checking Document Completeness")
    print("-" * 30)
    
    result = await agent.check_document_completeness(incomplete_contract, 'service_agreement')
    if result['success']:
        print(f"✅ Completion: {result['completion_percentage']:.1f}%")
        print("Recommendations:")
        for rec in result['recommendations']:
            print(f"   • {rec}")
    else:
        print(f"❌ Error: {result['error']}")
    
    # Test 4: Draft a Complete Document
    print("\n📄 Test 4: Drafting a Complete Document")
    print("-" * 30)
    
    request_data = {
        'document_type': 'service_agreement',
        'parties': {
            'party1': 'TechCorp Inc.',
            'party2': 'Jane Smith Consulting'
        },
        'terms': {
            'service_description': 'Web development and design services',
            'total_fee': '$10,000',
            'payment_schedule': 'Monthly payments of $2,500'
        },
        'jurisdiction': 'California',
        'special_instructions': 'Include intellectual property clause'
    }
    
    result = await agent.draft_legal_document(request_data)
    if result['success']:
        print(f"✅ Document created successfully!")
        print(f"   • Word count: {result['word_count']}")
        print(f"   • Compliance score: {result['compliance_score']:.1f}%")
        print(f"   • Confidence: {result['confidence']:.1f}")
        print(f"   • Suggestions: {len(result['suggestions'])}")
        
        # Show first 200 characters of the document
        preview = result['document_content'][:200] + "..."
        print(f"\n📝 Document Preview:\n{preview}")
    else:
        print(f"❌ Error: {result['error']}")
    
    # Test 5: Available Tasks
    print("\n📋 Test 5: Available Tasks")
    print("-" * 30)
    
    print(f"✅ Total available tasks: {len(agent.available_tasks)}")
    print("Task categories:")
    
    categories = {
        'Document Creation': ['create_contract', 'draft_legal_letter', 'generate_legal_form', 'build_custom_agreement'],
        'Content Enhancement': ['suggest_clauses', 'improve_language', 'fix_formatting', 'add_legal_provisions'],
        'Educational Support': ['explain_terms', 'explain_clauses', 'answer_questions', 'suggest_alternatives'],
        'Document Management': ['convert_format', 'create_versions', 'merge_sections', 'update_documents'],
        'Quality Assurance': ['check_consistency', 'identify_problems', 'verify_completeness', 'suggest_improvements']
    }
    
    for category, tasks in categories.items():
        print(f"   • {category}: {len(tasks)} tasks")
    
    print("\n🎉 All tests completed!")
    print("=" * 60)
    print("Your Legal Document Assistant is ready to help users!")
    print("\nKey Features:")
    print("• Creates legal documents from scratch")
    print("• Explains legal terms in simple English")
    print("• Suggests missing important clauses")
    print("• Improves document clarity and formatting")
    print("• Checks document completeness")
    print("• Uses friendly, non-technical language")
    print("• Focuses on drafting, not legal advice")

if __name__ == "__main__":
    asyncio.run(test_legal_assistant())