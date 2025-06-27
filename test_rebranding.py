#!/usr/bin/env python3
"""
Test script to verify Heeddata AI Agent rebranding
"""

import os
import re

def test_file_content(file_path, expected_patterns, description):
    """Test if a file contains expected rebranding patterns."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"\n🔍 Testing {description}...")
        print(f"   File: {file_path}")
        
        all_found = True
        for pattern, expected in expected_patterns.items():
            if expected in content:
                print(f"   ✅ Found: {expected}")
            else:
                print(f"   ❌ Missing: {expected}")
                all_found = False
        
        return all_found
    except Exception as e:
        print(f"   ❌ Error reading file: {e}")
        return False

def main():
    """Main test function."""
    print("🧪 Testing Heeddata AI Agent Rebranding")
    print("=" * 50)
    
    # Test frontend configuration
    frontend_tests = [
        {
            'file': 'frontend/src/lib/site.ts',
            'patterns': {
                'company_name': 'Heeddata AI Agent',
                'domain': 'heeddata.com',
                'linkedin': 'in.linkedin.com/company/heeddata'
            },
            'description': 'Frontend Site Configuration'
        },
        {
            'file': 'frontend/package.json',
            'patterns': {
                'package_name': 'ai-agent'
            },
            'description': 'Frontend Package Configuration'
        }
    ]
    
    # Test backend configuration
    backend_tests = [
        {
            'file': 'backend/pyproject.toml',
            'patterns': {
                'project_name': 'ai-agent',
                'homepage': 'heeddata.com'
            },
            'description': 'Backend Project Configuration'
        }
    ]
    
    # Test documentation
    doc_tests = [
        {
            'file': 'README.md',
            'patterns': {
                'title': 'AI Agent - Open Source Generalist AI Agent',
                'company': 'Heeddata',
                'domain': 'heeddata.com'
            },
            'description': 'README Documentation'
        }
    ]
    
    all_tests = frontend_tests + backend_tests + doc_tests
    
    passed = 0
    total = len(all_tests)
    
    for test in all_tests:
        if test_file_content(test['file'], test['patterns'], test['description']):
            passed += 1
    
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS")
    print("=" * 50)
    print(f"✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ Heeddata AI Agent rebranding is complete and verified!")
    else:
        print(f"\n⚠️  {total - passed} tests failed. Please check the files above.")
    
    print("\n🔄 Next Steps:")
    print("1. Install Node.js to test the frontend")
    print("2. Replace logo files with actual Heeddata logos")
    print("3. Test the full application")
    print("4. Deploy to production")

if __name__ == "__main__":
    main() 