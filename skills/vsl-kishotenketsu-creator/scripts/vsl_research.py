#!/usr/bin/env python3
"""
VSL Kishōtenketsu Research Module
Conducts market research and competitor analysis for VSL creation
"""

import json
from typing import Dict, List, Optional

def generate_research_questions(product_name: str, market: str, language: str = "pt") -> Dict:
    """
    Generate research questions based on product and market
    
    Args:
        product_name: Name of the product/offer
        market: Target market/niche
        language: "pt" for Portuguese, "en" for English
    
    Returns:
        Dictionary with research questions and areas
    """
    
    questions_pt = {
        "mercado": [
            f"Qual é o tamanho do mercado de {market}?",
            f"Quais são as tendências atuais em {market}?",
            f"Qual é o crescimento esperado para {market} nos próximos 2 anos?",
        ],
        "concorrentes": [
            f"Quem são os principais concorrentes de {product_name}?",
            "Qual é o posicionamento deles?",
            "Qual é a estratégia de preço dos concorrentes?",
        ],
        "cliente": [
            f"Quem é o cliente ideal para {product_name}?",
            "Quais são suas principais dores?",
            "Qual é seu poder de compra?",
        ],
        "diferencial": [
            f"Qual é o diferencial único de {product_name}?",
            "Qual é a vantagem competitiva?",
            "Por que o cliente deveria escolher isso em vez de alternativas?",
        ]
    }
    
    questions_en = {
        "market": [
            f"What is the size of the {market} market?",
            f"What are the current trends in {market}?",
            f"What is the expected growth for {market} in the next 2 years?",
        ],
        "competitors": [
            f"Who are the main competitors of {product_name}?",
            "What is their positioning?",
            "What is the competitors' pricing strategy?",
        ],
        "customer": [
            f"Who is the ideal customer for {product_name}?",
            "What are their main pain points?",
            "What is their purchasing power?",
        ],
        "differentiator": [
            f"What is the unique differentiator of {product_name}?",
            "What is the competitive advantage?",
            "Why should the customer choose this over alternatives?",
        ]
    }
    
    return questions_pt if language == "pt" else questions_en


def generate_icp_questions(language: str = "pt") -> List[str]:
    """
    Generate Ideal Customer Profile (ICP) discovery questions
    
    Args:
        language: "pt" for Portuguese, "en" for English
    
    Returns:
        List of ICP questions
    """
    
    questions_pt = [
        "Qual é a idade/faixa etária do cliente ideal?",
        "Qual é sua profissão ou setor?",
        "Qual é sua renda aproximada?",
        "Qual é seu maior desafio/dor?",
        "Qual é seu objetivo principal?",
        "Como ele atualmente resolve esse problema?",
        "Quanto ele está disposto a gastar?",
        "Onde ele busca informações/soluções?",
        "Qual é seu nível de consciência sobre a solução?",
        "Qual é seu processo de decisão de compra?",
    ]
    
    questions_en = [
        "What is the age range of the ideal customer?",
        "What is their profession or industry?",
        "What is their approximate income?",
        "What is their biggest challenge/pain point?",
        "What is their main objective?",
        "How do they currently solve this problem?",
        "How much are they willing to spend?",
        "Where do they seek information/solutions?",
        "What is their awareness level about the solution?",
        "What is their buying decision process?",
    ]
    
    return questions_pt if language == "pt" else questions_en


def generate_kishotenketsu_questions(language: str = "pt") -> Dict:
    """
    Generate specific questions for each Kishōtenketsu phase
    
    Args:
        language: "pt" for Portuguese, "en" for English
    
    Returns:
        Dictionary with questions for each phase
    """
    
    questions_pt = {
        "ki": [
            "Qual é uma história emocional relevante para o seu público?",
            "Qual é um problema comum que afeta muitas pessoas?",
            "Qual é uma verdade universal que seu público reconhece?",
            "Qual é um momento de transformação que seu público vivenciou?",
            "Qual é uma situação relatable que cria empatia imediata?",
        ],
        "sho": [
            "Como essa história inicial se conecta com o problema do seu cliente?",
            "Qual é o contexto que torna o problema ainda mais relevante?",
            "Quais são os sintomas/consequências desse problema?",
            "Como a vida do cliente é afetada por esse problema?",
            "Qual é a jornada que o cliente faz tentando resolver isso?",
        ],
        "ten": [
            "Qual é a revelação/insight que muda tudo?",
            "Qual é o mecanismo único que resolve o problema?",
            "Como seu produto/oferta é a solução óbvia após essa revelação?",
            "Qual é o 'uau' moment que o cliente experimenta?",
            "Qual é a transformação que se torna possível?",
        ],
        "ketsu": [
            "Qual é a nova realidade após usar seu produto?",
            "Qual é a vida/situação melhorada do cliente?",
            "Como você reafirma a confiança na oferta?",
            "Qual é a garantia ou segurança que você oferece?",
            "Qual é o próximo passo claro para o cliente?",
        ]
    }
    
    questions_en = {
        "ki": [
            "What is an emotional story relevant to your audience?",
            "What is a common problem that affects many people?",
            "What is a universal truth that your audience recognizes?",
            "What is a transformation moment that your audience experienced?",
            "What is a relatable situation that creates immediate empathy?",
        ],
        "sho": [
            "How does this initial story connect with your customer's problem?",
            "What is the context that makes the problem even more relevant?",
            "What are the symptoms/consequences of this problem?",
            "How is your customer's life affected by this problem?",
            "What is the journey your customer takes trying to solve this?",
        ],
        "ten": [
            "What is the revelation/insight that changes everything?",
            "What is the unique mechanism that solves the problem?",
            "How is your product/offer the obvious solution after this revelation?",
            "What is the 'wow' moment that the customer experiences?",
            "What is the transformation that becomes possible?",
        ],
        "ketsu": [
            "What is the new reality after using your product?",
            "What is the improved life/situation of the customer?",
            "How do you reaffirm confidence in the offer?",
            "What is the guarantee or security you offer?",
            "What is the clear next step for the customer?",
        ]
    }
    
    return questions_pt if language == "pt" else questions_en


if __name__ == "__main__":
    # Example usage
    print("VSL Kishōtenketsu Research Module")
    print("=" * 50)
    
    # Generate research questions
    research = generate_research_questions("Curso Online", "Marketing Digital", "pt")
    print("\nPesquisa de Mercado:")
    print(json.dumps(research, indent=2, ensure_ascii=False))
    
    # Generate ICP questions
    icp = generate_icp_questions("pt")
    print("\nPerguntas de ICP:")
    for i, q in enumerate(icp, 1):
        print(f"{i}. {q}")
    
    # Generate Kishōtenketsu questions
    kisho = generate_kishotenketsu_questions("pt")
    print("\nPerguntas Kishōtenketsu:")
    for phase, questions in kisho.items():
        print(f"\n{phase.upper()}:")
        for q in questions:
            print(f"  - {q}")
