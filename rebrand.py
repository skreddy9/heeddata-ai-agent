#!/usr/bin/env python3
"""
Rebranding Script for Heeddata AI Agent
This script rebrands from Kortix Suna to Heeddata AI Agent.
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List

class HeeddataRebrander:
    def __init__(self):
        """Initialize the Heeddata rebrander."""
        
        # Define the replacements
        self.replacements = {
            'Kortix': 'Heeddata',
            'Suna': 'AI Agent',
            'kortix.ai': 'heeddata.com',
            'suna.so': 'heeddata.com',
            'support@kortix.ai': 'info@heeddata.com',
            '@kortixai': '@heeddata',
            'kortix-ai': 'heeddata',
            'kortix/suna': 'heeddata/ai-agent',
            'Kortix Suna': 'Heeddata AI Agent',
            'Suna by Kortix': 'AI Agent by Heeddata',
            'Kortix Team': 'Heeddata Team',
            'Kortix AI Corp': 'Heeddata Inc',
            'Kortix AI': 'Heeddata AI',
            'https://github.com/kortix-ai/suna': 'https://heeddata.com',
            'https://github.com/Kortix-ai/Suna': 'https://heeddata.com',
            'https://x.com/kortixai': 'https://in.linkedin.com/company/heeddata',
            'https://discord.gg/kortixai': 'https://in.linkedin.com/company/heeddata',
            'https://instagram.com/kortixai': 'https://in.linkedin.com/company/heeddata',
            'https://www.linkedin.com/company/kortix/': 'https://in.linkedin.com/company/heeddata',
            'https://kortix.ai': 'https://heeddata.com',
            'https://kortix.ai/careers': 'https://heeddata.com',
            'hey@kortix.ai': 'info@heeddata.com',
            'dom@kortix.ai': 'info@heeddata.com',
            'legal@kortixai.com': 'info@heeddata.com',
            'team/kortix/enterprise-demo': 'team/heeddata/enterprise-demo',
            'kortix.cloud': 'heeddata.cloud',
        }
        
        # Files to exclude from text replacement
        self.exclude_patterns = [
            r'\.git/',
            r'node_modules/',
            r'__pycache__/',
            r'\.pyc$',
            r'\.DS_Store$',
            r'\.env',
            r'\.env\.local',
            r'\.env\.example',
            r'rebrand\.py',
            r'REBRANDING_GUIDE\.md',
        ]
        
        # File extensions to process
        self.text_extensions = {
            '.py', '.js', '.jsx', '.ts', '.tsx', '.json', '.md', '.txt', 
            '.html', '.css', '.scss', '.toml', '.yml', '.yaml', '.sql'
        }

    def should_process_file(self, file_path: str) -> bool:
        """Check if a file should be processed."""
        # Check exclude patterns
        for pattern in self.exclude_patterns:
            if re.search(pattern, file_path):
                return False
        
        # Check if it's a text file
        ext = Path(file_path).suffix.lower()
        return ext in self.text_extensions

    def replace_in_file(self, file_path: str) -> List[str]:
        """Replace branding in a single file."""
        changes = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Perform replacements
            for old, new in self.replacements.items():
                if old in content:
                    content = content.replace(old, new)
                    changes.append(f"  - Replaced '{old}' with '{new}'")
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return changes
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
        
        return changes

    def rename_files(self) -> List[str]:
        """Rename files that contain the old branding."""
        changes = []
        
        # Files to rename
        rename_patterns = [
            ('kortix-logo.svg', 'heeddata-logo.svg'),
            ('kortix-logo-white.svg', 'heeddata-logo-white.svg'),
            ('kortix-symbol.svg', 'heeddata-symbol.svg'),
        ]
        
        for old_name, new_name in rename_patterns:
            old_path = Path('frontend/public') / old_name
            new_path = Path('frontend/public') / new_name
            
            if old_path.exists():
                try:
                    shutil.move(str(old_path), str(new_path))
                    changes.append(f"Renamed {old_path} to {new_path}")
                except Exception as e:
                    print(f"Error renaming {old_path}: {e}")
        
        return changes

    def update_component_references(self) -> List[str]:
        """Update component references in code."""
        changes = []
        
        # Component files to rename
        component_renames = [
            ('kortix-logo.tsx', 'heeddata-logo.tsx'),
            ('kortix-enterprise-modal.tsx', 'heeddata-enterprise-modal.tsx'),
        ]
        
        for old_name, new_name in component_renames:
            old_path = Path('frontend/src/components/sidebar') / old_name
            new_path = Path('frontend/src/components/sidebar') / new_name
            
            if old_path.exists():
                try:
                    # Rename the file
                    shutil.move(str(old_path), str(new_path))
                    changes.append(f"Renamed component {old_path} to {new_path}")
                    
                    # Update the component name inside the file
                    with open(new_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Update component name
                    content = re.sub(
                        r'export function KortixLogo',
                        'export function HeeddataLogo',
                        content
                    )
                    content = re.sub(
                        r'export function KortixProcessModal',
                        'export function HeeddataProcessModal',
                        content
                    )
                    content = re.sub(
                        r'interface KortixLogoProps',
                        'interface HeeddataLogoProps',
                        content
                    )
                    content = re.sub(
                        r'KortixLogoProps',
                        'HeeddataLogoProps',
                        content
                    )
                    
                    with open(new_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    changes.append(f"Updated component names in {new_path}")
                    
                except Exception as e:
                    print(f"Error updating component {old_path}: {e}")
        
        return changes

    def process_directory(self, directory: str = '.') -> Dict[str, List[str]]:
        """Process all files in a directory recursively."""
        results = {
            'files_processed': [],
            'files_changed': [],
            'errors': []
        }
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                
                if self.should_process_file(file_path):
                    results['files_processed'].append(file_path)
                    
                    try:
                        changes = self.replace_in_file(file_path)
                        if changes:
                            results['files_changed'].append({
                                'file': file_path,
                                'changes': changes
                            })
                    except Exception as e:
                        results['errors'].append(f"Error processing {file_path}: {e}")
        
        return results

    def run(self) -> Dict[str, any]:
        """Run the complete rebranding process."""
        print("🚀 Starting Heeddata rebranding process...")
        print("Company: Heeddata")
        print("Product: AI Agent")
        print("Domain: heeddata.com")
        print()
        
        # Process text files
        print("📝 Processing text files...")
        text_results = self.process_directory()
        
        # Rename files
        print("📁 Renaming files...")
        file_renames = self.rename_files()
        
        # Update component references
        print("🔧 Updating component references...")
        component_updates = self.update_component_references()
        
        # Summary
        print("\n" + "="*50)
        print("✅ HEEDDATA REBRANDING COMPLETE!")
        print("="*50)
        
        print(f"\n📊 Summary:")
        print(f"  Files processed: {len(text_results['files_processed'])}")
        print(f"  Files changed: {len(text_results['files_changed'])}")
        print(f"  Files renamed: {len(file_renames)}")
        print(f"  Components updated: {len(component_updates)}")
        
        if text_results['errors']:
            print(f"  Errors: {len(text_results['errors'])}")
            for error in text_results['errors']:
                print(f"    - {error}")
        
        print(f"\n🔄 Next steps:")
        print(f"  1. Replace logo files in frontend/public/ with Heeddata logos")
        print(f"  2. Update banner.png with Heeddata branding")
        print(f"  3. Update favicon.png with Heeddata logo")
        print(f"  4. Test the application")
        print(f"  5. Update any environment variables")
        print(f"  6. Update deployment configurations")
        
        return {
            'text_results': text_results,
            'file_renames': file_renames,
            'component_updates': component_updates,
        }

def main():
    """Main function to run the rebranding script."""
    print("🎨 Heeddata AI Agent Rebranding Tool")
    print("=" * 50)
    print()
    
    # Run the rebranding
    rebrander = HeeddataRebrander()
    results = rebrander.run()
    
    print(f"\n💾 Rebranding completed successfully!")

if __name__ == "__main__":
    main() 