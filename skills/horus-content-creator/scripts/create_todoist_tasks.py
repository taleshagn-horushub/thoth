#!/usr/bin/env python3
"""
Create Todoist Tasks from Horus Strategy

This script generates structured tasks in Todoist based on the 4-phase
strategy workflow for legal marketing campaigns.

Usage:
    python create_todoist_tasks.py --client "Nome do Cliente" --phase "1" [--project-id PROJECT_ID]
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path


def generate_phase_1_tasks(client_name: str) -> list:
    """Generate tasks for Phase 1: Diagnóstico e Pilar Estratégico"""
    return [
        {
            "title": f"[{client_name}] FASE 1: Análise de Público-alvo",
            "description": "Definir persona, dores, desejos e comportamentos do público-alvo",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=1)).isoformat()
        },
        {
            "title": f"[{client_name}] FASE 1: Análise Competitiva",
            "description": "Pesquisar concorrentes, estratégias e diferenciadores",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=1)).isoformat()
        },
        {
            "title": f"[{client_name}] FASE 1: Definir Pilar Estratégico",
            "description": "Consolidar insights e criar pilar estratégico único",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=2)).isoformat()
        },
        {
            "title": f"[{client_name}] VALIDAÇÃO: Pilar Estratégico",
            "description": "Aguardar validação do cliente sobre o pilar estratégico",
            "priority": 3,
            "due_date": (datetime.now() + timedelta(days=3)).isoformat()
        }
    ]


def generate_phase_2_tasks(client_name: str) -> list:
    """Generate tasks for Phase 2: Estratégia Meta Ads"""
    return [
        {
            "title": f"[{client_name}] FASE 2: Criar 5 Ângulos Meta Ads",
            "description": "Desenvolver 5 ângulos diferentes focados em conversão",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=4)).isoformat()
        },
        {
            "title": f"[{client_name}] FASE 2: Criar Variações A/B",
            "description": "Criar 2 variações A/B para cada ângulo (10 anúncios totais)",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=5)).isoformat()
        },
        {
            "title": f"[{client_name}] FASE 2: Aplicar Brand Horus",
            "description": "Garantir compliance com cores, tipografia e tom Sábio-Mago",
            "priority": 3,
            "due_date": (datetime.now() + timedelta(days=5)).isoformat()
        },
        {
            "title": f"[{client_name}] VALIDAÇÃO: Meta Ads Strategy",
            "description": "Aguardar validação da estratégia Meta Ads",
            "priority": 3,
            "due_date": (datetime.now() + timedelta(days=6)).isoformat()
        }
    ]


def generate_phase_3_tasks(client_name: str) -> list:
    """Generate tasks for Phase 3: Estratégia Google Ads"""
    return [
        {
            "title": f"[{client_name}] FASE 3: Pesquisa de Palavras-chave",
            "description": "Identificar palavras-chave de alto potencial com volume e CPC",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=7)).isoformat()
        },
        {
            "title": f"[{client_name}] FASE 3: Criar Anúncios Google",
            "description": "Desenvolver headlines, descriptions e landing page URLs",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=8)).isoformat()
        },
        {
            "title": f"[{client_name}] FASE 3: Compliance Jurídico OAB",
            "description": "Validar conformidade com regulamentações OAB",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=8)).isoformat()
        },
        {
            "title": f"[{client_name}] VALIDAÇÃO: Google Ads Strategy",
            "description": "Aguardar validação da estratégia Google Ads",
            "priority": 3,
            "due_date": (datetime.now() + timedelta(days=9)).isoformat()
        }
    ]


def generate_phase_4_tasks(client_name: str) -> list:
    """Generate tasks for Phase 4: Landing Page Structure"""
    return [
        {
            "title": f"[{client_name}] FASE 4: Estrutura LP - Hero Section",
            "description": "Headline, subheadline e CTA principal baseados no pilar estratégico",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=10)).isoformat()
        },
        {
            "title": f"[{client_name}] FASE 4: Estrutura LP - Seções Intermediárias",
            "description": "Problema, solução, prova social, depoimentos, FAQ",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=11)).isoformat()
        },
        {
            "title": f"[{client_name}] FASE 4: Estrutura LP - Seção Final",
            "description": "CTA final, garantias, urgência e objeções",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=11)).isoformat()
        },
        {
            "title": f"[{client_name}] FASE 4: Aplicar Design Horus",
            "description": "Implementar brand colors, typography e visual identity",
            "priority": 3,
            "due_date": (datetime.now() + timedelta(days=12)).isoformat()
        },
        {
            "title": f"[{client_name}] VALIDAÇÃO: Landing Page Structure",
            "description": "Aguardar validação da estrutura da landing page",
            "priority": 3,
            "due_date": (datetime.now() + timedelta(days=13)).isoformat()
        }
    ]


def generate_deliverable_tasks(client_name: str) -> list:
    """Generate tasks for final deliverables"""
    return [
        {
            "title": f"[{client_name}] ENTREGÁVEL 1: Documento Interno",
            "description": "Gerar documento Markdown com toda a estratégia e Brand Horus",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=14)).isoformat()
        },
        {
            "title": f"[{client_name}] ENTREGÁVEL 2: Tarefas Todoist",
            "description": "Verificar se todas as tarefas foram criadas e organizadas",
            "priority": 3,
            "due_date": (datetime.now() + timedelta(days=14)).isoformat()
        },
        {
            "title": f"[{client_name}] ENTREGÁVEL 3: Apresentação Cliente",
            "description": "Gerar slides profissionais para apresentação ao cliente",
            "priority": 4,
            "due_date": (datetime.now() + timedelta(days=14)).isoformat()
        },
        {
            "title": f"[{client_name}] EXECUÇÃO: Implementar Estratégia",
            "description": "Iniciar implementação das campanhas Meta Ads e Google Ads",
            "priority": 2,
            "due_date": (datetime.now() + timedelta(days=15)).isoformat()
        }
    ]


def generate_all_tasks(client_name: str) -> dict:
    """Generate all tasks for the complete workflow"""
    return {
        "client": client_name,
        "generated_at": datetime.now().isoformat(),
        "phases": {
            "1_diagnostico": generate_phase_1_tasks(client_name),
            "2_meta_ads": generate_phase_2_tasks(client_name),
            "3_google_ads": generate_phase_3_tasks(client_name),
            "4_landing_page": generate_phase_4_tasks(client_name),
            "deliverables": generate_deliverable_tasks(client_name)
        }
    }


def save_tasks_json(tasks: dict, output_path: str = None) -> str:
    """Save tasks to JSON file for later import"""
    if output_path is None:
        output_path = f"horus_tasks_{tasks['client'].replace(' ', '_').lower()}.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
    
    return output_path


def print_tasks_summary(tasks: dict) -> None:
    """Print a summary of generated tasks"""
    print("\n" + "="*70)
    print(f"📋 TAREFAS GERADAS PARA: {tasks['client']}")
    print("="*70)
    
    total_tasks = 0
    for phase_name, phase_tasks in tasks['phases'].items():
        print(f"\n{phase_name.upper().replace('_', ' ')}:")
        print(f"  {len(phase_tasks)} tarefas")
        total_tasks += len(phase_tasks)
        
        for task in phase_tasks:
            priority_icon = "🔴" if task['priority'] == 4 else "🟡" if task['priority'] == 3 else "🟢"
            print(f"  {priority_icon} {task['title']}")
    
    print(f"\n{'='*70}")
    print(f"✅ TOTAL: {total_tasks} tarefas criadas")
    print(f"📅 Data de geração: {tasks['generated_at']}")
    print("="*70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Generate Todoist tasks for Horus Content Creator strategy',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python create_todoist_tasks.py --client "Silva & Associados"
  python create_todoist_tasks.py --client "Haroldo Lobo Advogados" --output tasks.json
        '''
    )
    
    parser.add_argument('--client', required=True, help='Client name')
    parser.add_argument('--output', help='Output JSON file path', default=None)
    parser.add_argument('--phase', help='Generate tasks for specific phase (1-4)', default=None)
    
    args = parser.parse_args()
    
    # Generate tasks
    if args.phase:
        print(f"⚠️  Phase-specific generation not yet implemented. Generating all phases.")
    
    tasks = generate_all_tasks(args.client)
    
    # Save to JSON
    output_file = save_tasks_json(tasks, args.output)
    
    # Print summary
    print_tasks_summary(tasks)
    
    print(f"💾 Tasks saved to: {output_file}")
    print("\n📌 Next step: Import this JSON into Todoist or use the MCP integration")


if __name__ == '__main__':
    main()
