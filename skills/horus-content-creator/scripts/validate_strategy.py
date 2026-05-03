#!/usr/bin/env python3
"""
Validate Horus Strategy - Quality Assurance Checklist

This script validates that each phase of the strategy meets quality standards
and compliance requirements.

Usage:
    python validate_strategy.py --phase "1" --client "Nome do Cliente"
"""

import argparse
import json
from datetime import datetime
from typing import Dict, List, Tuple


class StrategyValidator:
    """Validates each phase of the Horus strategy"""
    
    def __init__(self, client_name: str):
        self.client_name = client_name
        self.validation_results = {
            "client": client_name,
            "validated_at": datetime.now().isoformat(),
            "phases": {}
        }
    
    def validate_phase_1(self, data: Dict) -> Tuple[bool, List[str]]:
        """Validate Phase 1: Diagnóstico e Pilar Estratégico"""
        issues = []
        
        # Check required fields
        required_fields = [
            "target_audience_persona",
            "pain_points",
            "desires",
            "competitor_analysis",
            "strategic_pillar",
            "unique_differentiators"
        ]
        
        for field in required_fields:
            if field not in data or not data[field]:
                issues.append(f"❌ Missing or empty: {field}")
        
        # Validate strategic pillar length
        if "strategic_pillar" in data:
            pillar = data["strategic_pillar"]
            if len(pillar) < 50:
                issues.append("⚠️  Strategic pillar too short (minimum 50 characters)")
            if len(pillar) > 500:
                issues.append("⚠️  Strategic pillar too long (maximum 500 characters)")
        
        # Validate persona specificity
        if "target_audience_persona" in data:
            persona = data["target_audience_persona"]
            if "age" not in persona and "demographics" not in persona:
                issues.append("⚠️  Persona lacks demographic information")
        
        return len(issues) == 0, issues
    
    def validate_phase_2(self, data: Dict) -> Tuple[bool, List[str]]:
        """Validate Phase 2: Meta Ads Strategy"""
        issues = []
        
        # Check required fields
        if "angles" not in data or len(data.get("angles", [])) != 5:
            issues.append("❌ Must have exactly 5 angles for Meta Ads")
        
        if "ab_variations" not in data or len(data.get("ab_variations", [])) != 10:
            issues.append("❌ Must have exactly 10 A/B variations (2 per angle)")
        
        # Validate brand compliance
        if "brand_compliance" not in data or not data["brand_compliance"]:
            issues.append("⚠️  Brand compliance not documented")
        else:
            compliance = data["brand_compliance"]
            required_brand_elements = ["colors", "typography", "tone"]
            for element in required_brand_elements:
                if element not in compliance:
                    issues.append(f"⚠️  Missing brand element: {element}")
        
        # Validate each angle has copy and CTA
        if "angles" in data:
            for i, angle in enumerate(data["angles"], 1):
                if "headline" not in angle:
                    issues.append(f"❌ Angle {i} missing headline")
                if "cta" not in angle:
                    issues.append(f"❌ Angle {i} missing CTA")
        
        return len(issues) == 0, issues
    
    def validate_phase_3(self, data: Dict) -> Tuple[bool, List[str]]:
        """Validate Phase 3: Google Ads Strategy"""
        issues = []
        
        # Check required fields
        if "keywords" not in data or len(data.get("keywords", [])) < 20:
            issues.append("❌ Must have at least 20 keywords")
        
        if "ads" not in data or len(data.get("ads", [])) < 5:
            issues.append("❌ Must have at least 5 ad variations")
        
        # Validate keyword structure
        if "keywords" in data:
            for keyword in data["keywords"]:
                if "term" not in keyword:
                    issues.append("⚠️  Keyword missing term")
                if "intent" not in keyword:
                    issues.append("⚠️  Keyword missing intent classification")
                if "cpc_estimate" not in keyword:
                    issues.append("⚠️  Keyword missing CPC estimate")
        
        # Validate ads structure
        if "ads" in data:
            for i, ad in enumerate(data["ads"], 1):
                if "headline_1" not in ad or "headline_2" not in ad:
                    issues.append(f"❌ Ad {i} missing headlines")
                if "description" not in ad:
                    issues.append(f"❌ Ad {i} missing description")
        
        # Validate compliance
        if "oab_compliance" not in data or not data["oab_compliance"]:
            issues.append("❌ OAB compliance not documented (CRITICAL)")
        
        return len(issues) == 0, issues
    
    def validate_phase_4(self, data: Dict) -> Tuple[bool, List[str]]:
        """Validate Phase 4: Landing Page Structure"""
        issues = []
        
        # Check required sections
        required_sections = [
            "hero_section",
            "problem_section",
            "solution_section",
            "social_proof_section",
            "testimonials_section",
            "faq_section",
            "final_cta_section"
        ]
        
        for section in required_sections:
            if section not in data or not data[section]:
                issues.append(f"❌ Missing section: {section}")
        
        # Validate hero section
        if "hero_section" in data:
            hero = data["hero_section"]
            if "headline" not in hero or len(hero.get("headline", "")) < 20:
                issues.append("⚠️  Hero headline too short or missing")
            if "cta_button_text" not in hero:
                issues.append("⚠️  Hero CTA button text missing")
        
        # Validate social proof
        if "social_proof_section" in data:
            proof = data["social_proof_section"]
            if "case_count" not in proof or proof["case_count"] == 0:
                issues.append("⚠️  Social proof missing case count")
        
        # Validate design compliance
        if "design_compliance" not in data or not data["design_compliance"]:
            issues.append("⚠️  Design compliance not documented")
        else:
            design = data["design_compliance"]
            if "brand_colors" not in design:
                issues.append("⚠️  Brand colors not specified")
            if "typography" not in design:
                issues.append("⚠️  Typography not specified")
        
        return len(issues) == 0, issues
    
    def generate_report(self, phase: str, data: Dict) -> Dict:
        """Generate validation report for a phase"""
        validators = {
            "1": self.validate_phase_1,
            "2": self.validate_phase_2,
            "3": self.validate_phase_3,
            "4": self.validate_phase_4
        }
        
        if phase not in validators:
            return {"error": f"Unknown phase: {phase}"}
        
        is_valid, issues = validators[phase](data)
        
        report = {
            "phase": phase,
            "client": self.client_name,
            "is_valid": is_valid,
            "issue_count": len(issues),
            "issues": issues,
            "status": "✅ APPROVED" if is_valid else "❌ NEEDS REVISION",
            "validated_at": datetime.now().isoformat()
        }
        
        return report
    
    def print_report(self, report: Dict) -> None:
        """Print validation report in human-readable format"""
        print("\n" + "="*70)
        print(f"VALIDATION REPORT - PHASE {report['phase']}")
        print(f"Client: {report['client']}")
        print("="*70)
        
        print(f"\nStatus: {report['status']}")
        print(f"Issues found: {report['issue_count']}")
        
        if report['issues']:
            print("\nDetails:")
            for issue in report['issues']:
                print(f"  {issue}")
        else:
            print("\n✅ All checks passed! This phase is ready for approval.")
        
        print(f"\nValidated at: {report['validated_at']}")
        print("="*70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Validate Horus strategy phases for quality and compliance',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python validate_strategy.py --phase "1" --client "Silva & Associados"
  python validate_strategy.py --phase "2" --client "Haroldo Lobo" --data strategy.json
        '''
    )
    
    parser.add_argument('--phase', required=True, choices=['1', '2', '3', '4'],
                       help='Phase to validate (1-4)')
    parser.add_argument('--client', required=True, help='Client name')
    parser.add_argument('--data', help='JSON file with strategy data', default=None)
    
    args = parser.parse_args()
    
    # Initialize validator
    validator = StrategyValidator(args.client)
    
    # Load data if provided
    data = {}
    if args.data:
        try:
            with open(args.data, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"❌ File not found: {args.data}")
            return
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON in: {args.data}")
            return
    
    # Generate and print report
    report = validator.generate_report(args.phase, data)
    
    if "error" in report:
        print(f"❌ Error: {report['error']}")
        return
    
    validator.print_report(report)
    
    # Save report to JSON
    report_file = f"validation_phase_{args.phase}_{args.client.replace(' ', '_').lower()}.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"📄 Report saved to: {report_file}")


if __name__ == '__main__':
    main()
