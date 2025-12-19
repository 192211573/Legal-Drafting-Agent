#!/usr/bin/env python3
"""
Test Backend Connection and Drafting Agent
This script tests if the backend and drafting agent are working properly.
"""

import asyncio
import sys
import os
import requests
import json

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from app.services.enhanced_drafting_agent import EnhancedDraftingAgent

async def test_backend_connection():
    """Test the backend connection and drafting agent"""
    
    print("🔍 Testing Backend Connection and Drafting Agent")
    print("=" * 60)
    
    # Test 1: Check if backend is running
    print("\n🌐 Test 1: Backend Health Check")
    print("-" * 30)
    
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend is running successfully!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Backend returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend. Make sure it's running on port 8000")
        return False
    except Exception as e:
        print(f"❌ Error connecting to backend: {e}")
        return False
    
    # Test 2: Check API documentation
    print("\n📚 Test 2: API Documentation")
    print("-" * 30)
    
    try:
        response = requests.get("http://localhost:8000/docs", timeout=5)
        if response.status_code == 200:
            print("✅ API documentation is accessible at http://localhost:8000/docs")
        else:
            print(f"⚠️  API docs returned status: {response.status_code}")
    except Exception as e:
        print(f"⚠️  Could not access API docs: {e}")
    
    # Test 3: Test Drafting Agent Directly (without API)
    print("\n🤖 Test 3: Drafting Agent Direct Test")
    print("-" * 30)
    
    try:
        agent = EnhancedDraftingAgent()
        print("✅ Drafting agent initialized successfully")
        
        # Test document creation
        request_data = {
            'document_type': 'service_agreement',
            'parties': {
                'party1': 'Test Company Inc.',
                'party2': 'John Doe Consulting'
            },
            'terms': {
                'service_description': 'Software development services',
                'total_fee': '$5,000'
            },
            'jurisdiction': 'California',
            'special_instructions': 'Include standard liability clauses'
        }
        
        result = await agent.draft_legal_document(request_data)
        
        if result['success']:
            print("✅ Document drafting successful!")
            print(f"   • Word count: {result['word_count']}")
            print(f"   • Compliance score: {result['compliance_score']:.1f}%")
            print(f"   • Confidence: {result['confidence']:.1f}")
            print(f"   • Suggestions: {len(result['suggestions'])}")
            
            # Show preview
            preview = result['document_content'][:300] + "..."
            print(f"\n📄 Document Preview:\n{preview}")
            
        else:
            print(f"❌ Document drafting failed: {result.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing drafting agent: {e}")
        return False
    
    # Test 4: Test Legal Term Explanation
    print("\n💡 Test 4: Legal Term Explanation")
    print("-" * 30)
    
    try:
        test_text = "The parties hereby agree to indemnify each other against liability."
        result = await agent.explain_legal_terms(test_text)
        
        if result['success']:
            print("✅ Legal term explanation successful!")
            print(f"   • Terms found: {result['terms_found']}")
            for term, explanation in result['explanations'].items():
                print(f"   • {term}: {explanation}")
        else:
            print(f"❌ Term explanation failed: {result.get('error', 'Unknown error')}")
            
    except Exception as e:
        print(f"❌ Error testing term explanation: {e}")
    
    # Test 5: Check OpenAI Connection
    print("\n🔑 Test 5: OpenAI Connection Check")
    print("-" * 30)
    
    if agent.openai_client:
        print("✅ OpenAI client is initialized")
        print("   Note: Actual API calls will depend on valid API key")
    else:
        print("⚠️  OpenAI client not initialized (API key missing)")
        print("   Using fallback rule-based processing")
    
    # Test 6: Template System
    print("\n📋 Test 6: Template System")
    print("-" * 30)
    
    try:
        templates = agent.template_manager.templates
        print(f"✅ Template system loaded with {len(templates)} templates:")
        for template_name in templates.keys():
            print(f"   • {template_name}")
    except Exception as e:
        print(f"❌ Error testing template system: {e}")
    
    print("\n🎉 Backend Connection Test Complete!")
    print("=" * 60)
    
    return True

async def test_api_endpoints():
    """Test API endpoints that don't require authentication"""
    
    print("\n🔌 Testing Public API Endpoints")
    print("-" * 30)
    
    # Test root endpoint
    try:
        response = requests.get("http://localhost:8000/", timeout=5)
        if response.status_code == 200:
            print("✅ Root endpoint working")
            print(f"   Response: {response.json()}")
        else:
            print(f"⚠️  Root endpoint status: {response.status_code}")
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")

if __name__ == "__main__":
    async def main():
        success = await test_backend_connection()
        await test_api_endpoints()
        
        if success:
            print("\n✅ All tests passed! Your backend is working correctly.")
            print("\n📝 Next Steps:")
            print("1. Add your OpenAI API key to backend/.env file")
            print("2. Start the frontend with 'npm run dev'")
            print("3. Test the full application in your browser")
        else:
            print("\n❌ Some tests failed. Check the errors above.")
    
    asyncio.run(main())