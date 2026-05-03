#!/usr/bin/env python3
"""
VSL Kishōtenketsu Script Generator
Generates VSL scripts based on Kishōtenketsu structure
"""

import json
from typing import Dict, List, Optional
from datetime import datetime


class VSLGenerator:
    """Generate VSL scripts using Kishōtenketsu structure"""
    
    def __init__(self, language: str = "pt"):
        self.language = language
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def generate_script(self, data: Dict) -> Dict:
        """
        Generate complete VSL script from research data
        
        Args:
            data: Dictionary containing all VSL information
                - product_name: str
                - offer: str
                - brand: str
                - icp: Dict
                - market_research: Dict
                - kishotenketsu_answers: Dict
        
        Returns:
            Dictionary with complete VSL script
        """
        
        script = {
            "metadata": {
                "product": data.get("product_name", ""),
                "offer": data.get("offer", ""),
                "brand": data.get("brand", ""),
                "language": self.language,
                "created_at": self.timestamp,
            },
            "ki": self._generate_ki(data),
            "sho": self._generate_sho(data),
            "ten": self._generate_ten(data),
            "ketsu": self._generate_ketsu(data),
            "timing": self._calculate_timing(),
        }
        
        return script
    
    def _generate_ki(self, data: Dict) -> Dict:
        """Generate Ki (Introduction) phase"""
        
        ki_text_pt = f"""
ABERTURA - KI (Introdução)
[0-15% do vídeo]

Olá, meu nome é [SEU_NOME].

Deixe-me contar uma história...

{data.get("ki_story", "[HISTÓRIA EMOCIONAL E CATIVANTE]")}

Essa história é importante porque...

{data.get("ki_connection", "[CONEXÃO COM A AUDIÊNCIA]")}

Você já se viu nessa situação?
"""
        
        ki_text_en = f"""
OPENING - KI (Introduction)
[0-15% of video]

Hello, my name is [YOUR_NAME].

Let me tell you a story...

{data.get("ki_story", "[EMOTIONAL AND ENGAGING STORY]")}

This story is important because...

{data.get("ki_connection", "[CONNECTION WITH AUDIENCE]")}

Have you found yourself in this situation?
"""
        
        return {
            "phase": "Ki (Introduction)",
            "duration": "0-15%",
            "purpose": "Capture attention with an emotional story",
            "script": ki_text_pt if self.language == "pt" else ki_text_en,
            "key_elements": [
                "Emotional hook",
                "Relatable situation",
                "Subtle hints about the solution (vestiges)",
                "Build empathy",
            ]
        }
    
    def _generate_sho(self, data: Dict) -> Dict:
        """Generate Sho (Development) phase"""
        
        sho_text_pt = f"""
DESENVOLVIMENTO - SHO (Desenvolvimento)
[15-50% do vídeo]

Agora, você pode estar se perguntando...

{data.get("sho_problem", "[PROBLEMA DO CLIENTE]")}

Muitas pessoas enfrentam esse desafio:

{data.get("sho_consequences", "[CONSEQUÊNCIAS DO PROBLEMA]")}

A verdade é que...

{data.get("sho_context", "[CONTEXTO E REALIDADE]")}

Mas aqui está o que a maioria das pessoas não sabe...
"""
        
        sho_text_en = f"""
DEVELOPMENT - SHO (Development)
[15-50% of video]

Now, you might be wondering...

{data.get("sho_problem", "[CUSTOMER PROBLEM]")}

Many people face this challenge:

{data.get("sho_consequences", "[PROBLEM CONSEQUENCES]")}

The truth is...

{data.get("sho_context", "[CONTEXT AND REALITY]")}

But here's what most people don't know...
"""
        
        return {
            "phase": "Sho (Development)",
            "duration": "15-50%",
            "purpose": "Connect story with customer's reality",
            "script": sho_text_pt if self.language == "pt" else sho_text_en,
            "key_elements": [
                "Deepen the problem",
                "Show consequences",
                "Build tension",
                "NO product mention yet",
                "NO sales language",
            ]
        }
    
    def _generate_ten(self, data: Dict) -> Dict:
        """Generate Ten (Plot/Twist) phase"""
        
        ten_text_pt = f"""
REVIRAVOLTA - TEN (Plot Twist)
[50-85% do vídeo]

E aqui está a reviravolta...

{data.get("ten_revelation", "[REVELAÇÃO IMPACTANTE]")}

Isso muda tudo porque...

{data.get("ten_mechanism", "[MECANISMO ÚNICO]")}

Por isso criamos {data.get("product_name", "[PRODUTO]")}:

{data.get("ten_solution", "[APRESENTAÇÃO DA SOLUÇÃO]")}

Veja só o que fica possível:

{data.get("ten_transformation", "[TRANSFORMAÇÃO POSSÍVEL]")}

Sem desconto, sem mimimi.
"""
        
        ten_text_en = f"""
PLOT TWIST - TEN (Twist)
[50-85% of video]

And here's the plot twist...

{data.get("ten_revelation", "[IMPACTFUL REVELATION]")}

This changes everything because...

{data.get("ten_mechanism", "[UNIQUE MECHANISM]")}

That's why we created {data.get("product_name", "[PRODUCT]")}:

{data.get("ten_solution", "[SOLUTION PRESENTATION]")}

See what becomes possible:

{data.get("ten_transformation", "[POSSIBLE TRANSFORMATION]")}

No discount, no nonsense.
"""
        
        return {
            "phase": "Ten (Plot/Twist)",
            "duration": "50-85%",
            "purpose": "Reveal solution and create desire",
            "script": ten_text_pt if self.language == "pt" else ten_text_en,
            "key_elements": [
                "Unexpected revelation",
                "Connect story to solution",
                "Present product confidently",
                "Show transformation",
                "Create desire, not pressure",
            ]
        }
    
    def _generate_ketsu(self, data: Dict) -> Dict:
        """Generate Ketsu (Conclusion) phase"""
        
        ketsu_text_pt = f"""
CONCLUSÃO - KETSU (Reconciliação)
[85-100% do vídeo]

Deixe-me ser claro...

{data.get("ketsu_reaffirmation", "[REAFIRMAÇÃO DA OFERTA]")}

Você terá acesso a:

{data.get("ketsu_benefits", "[BENEFÍCIOS PRINCIPAIS]")}

Garantia: {data.get("ketsu_guarantee", "[GARANTIA/SEGURANÇA]")}

Agora é com você.

Clique no botão abaixo e comece sua transformação.

Obrigado, e até breve.
"""
        
        ketsu_text_en = f"""
CONCLUSION - KETSU (Reconciliation)
[85-100% of video]

Let me be clear...

{data.get("ketsu_reaffirmation", "[REAFFIRMATION OF OFFER]")}

You will have access to:

{data.get("ketsu_benefits", "[MAIN BENEFITS]")}

Guarantee: {data.get("ketsu_guarantee", "[GUARANTEE/SECURITY]")}

Now it's up to you.

Click the button below and start your transformation.

Thank you, and see you soon.
"""
        
        return {
            "phase": "Ketsu (Conclusion)",
            "duration": "85-100%",
            "purpose": "Consolidate decision and drive action",
            "script": ketsu_text_pt if self.language == "pt" else ketsu_text_en,
            "key_elements": [
                "Reaffirm offer from new perspective",
                "List concrete benefits",
                "Mention guarantee (if strong)",
                "Show confidence without begging",
                "Clear call-to-action",
                "Professional goodbye",
            ]
        }
    
    def _calculate_timing(self) -> Dict:
        """Calculate video timing recommendations"""
        
        timing_pt = {
            "ki": "15-30 segundos (15% do vídeo)",
            "sho": "60-120 segundos (35% do vídeo)",
            "ten": "60-90 segundos (35% do vídeo)",
            "ketsu": "30-45 segundos (15% do vídeo)",
            "total": "3-5 minutos (ideal para VSL)",
        }
        
        timing_en = {
            "ki": "15-30 seconds (15% of video)",
            "sho": "60-120 seconds (35% of video)",
            "ten": "60-90 seconds (35% of video)",
            "ketsu": "30-45 seconds (15% of video)",
            "total": "3-5 minutes (ideal for VSL)",
        }
        
        return timing_pt if self.language == "pt" else timing_en


def generate_storyboard(script: Dict, language: str = "pt") -> Dict:
    """
    Generate visual storyboard from script
    
    Args:
        script: VSL script dictionary
        language: "pt" for Portuguese, "en" for English
    
    Returns:
        Dictionary with storyboard scenes
    """
    
    scenes_pt = [
        {
            "scene": 1,
            "phase": "KI",
            "duration": "0-15s",
            "visual": "Apresentador/Avatar em primeiro plano, fundo neutro",
            "action": "Olhar direto para câmera, sorriso genuíno",
            "audio": "Voz clara, tom conversacional",
            "text": "Abertura com história emocional",
        },
        {
            "scene": 2,
            "phase": "KI",
            "duration": "15-30s",
            "visual": "Transição: B-roll da história ou animação",
            "action": "Narração envolvente, gestos naturais",
            "audio": "Música de fundo suave, narração clara",
            "text": "Desenvolvimento da história",
        },
        {
            "scene": 3,
            "phase": "SHO",
            "duration": "30-90s",
            "visual": "Apresentador + gráficos/dados do problema",
            "action": "Demonstrar empatia, reconhecer dor",
            "audio": "Tom empático, música ligeiramente mais dramática",
            "text": "Aprofundar o problema e contexto",
        },
        {
            "scene": 4,
            "phase": "SHO",
            "duration": "90-150s",
            "visual": "Consequências visuais do problema",
            "action": "Mostrar frustração, mas com esperança",
            "audio": "Tensão crescente, pausa estratégica",
            "text": "Consequências e realidade do cliente",
        },
        {
            "scene": 5,
            "phase": "TEN",
            "duration": "150-180s",
            "visual": "Efeito visual de reviravolta (transição dramática)",
            "action": "Mudança de postura, energia renovada",
            "audio": "Efeito sonoro de impacto, música mais positiva",
            "text": "REVELAÇÃO - Mudança de perspectiva",
        },
        {
            "scene": 6,
            "phase": "TEN",
            "duration": "180-240s",
            "visual": "Apresentação do produto/solução",
            "action": "Demonstração confiante, sem hesitação",
            "audio": "Tom autorizado, música inspiradora",
            "text": "Apresentação da solução",
        },
        {
            "scene": 7,
            "phase": "TEN",
            "duration": "240-270s",
            "visual": "Transformação/Resultados visuais",
            "action": "Entusiasmo controlado, evidência de sucesso",
            "audio": "Depoimentos ou resultados, música positiva",
            "text": "Transformação possível",
        },
        {
            "scene": 8,
            "phase": "KETSU",
            "duration": "270-300s",
            "visual": "Apresentador + CTA visual (botão/link)",
            "action": "Olhar direto, confiança, sem desespero",
            "audio": "Tom claro e direto, música de conclusão",
            "text": "Reafirmação e Call-to-Action",
        },
    ]
    
    scenes_en = [
        {
            "scene": 1,
            "phase": "KI",
            "duration": "0-15s",
            "visual": "Presenter/Avatar in foreground, neutral background",
            "action": "Direct eye contact, genuine smile",
            "audio": "Clear voice, conversational tone",
            "text": "Opening with emotional story",
        },
        {
            "scene": 2,
            "phase": "KI",
            "duration": "15-30s",
            "visual": "Transition: B-roll of story or animation",
            "action": "Engaging narration, natural gestures",
            "audio": "Soft background music, clear narration",
            "text": "Story development",
        },
        {
            "scene": 3,
            "phase": "SHO",
            "duration": "30-90s",
            "visual": "Presenter + graphics/data of problem",
            "action": "Show empathy, acknowledge pain",
            "audio": "Empathetic tone, slightly dramatic music",
            "text": "Deepen problem and context",
        },
        {
            "scene": 4,
            "phase": "SHO",
            "duration": "90-150s",
            "visual": "Visual consequences of problem",
            "action": "Show frustration, but with hope",
            "audio": "Growing tension, strategic pause",
            "text": "Consequences and customer reality",
        },
        {
            "scene": 5,
            "phase": "TEN",
            "duration": "150-180s",
            "visual": "Visual effect of plot twist (dramatic transition)",
            "action": "Change of posture, renewed energy",
            "audio": "Impact sound effect, more positive music",
            "text": "REVELATION - Change of perspective",
        },
        {
            "scene": 6,
            "phase": "TEN",
            "duration": "180-240s",
            "visual": "Product/solution presentation",
            "action": "Confident demonstration, no hesitation",
            "audio": "Authoritative tone, inspiring music",
            "text": "Solution presentation",
        },
        {
            "scene": 7,
            "phase": "TEN",
            "duration": "240-270s",
            "visual": "Transformation/visual results",
            "action": "Controlled enthusiasm, evidence of success",
            "audio": "Testimonials or results, positive music",
            "text": "Possible transformation",
        },
        {
            "scene": 8,
            "phase": "KETSU",
            "duration": "270-300s",
            "visual": "Presenter + CTA visual (button/link)",
            "action": "Direct gaze, confidence, no desperation",
            "audio": "Clear and direct tone, conclusion music",
            "text": "Reaffirmation and Call-to-Action",
        },
    ]
    
    return {
        "total_duration": "4-5 minutes",
        "scenes": scenes_pt if language == "pt" else scenes_en,
    }


if __name__ == "__main__":
    # Example usage
    print("VSL Kishōtenketsu Generator")
    print("=" * 50)
    
    example_data = {
        "product_name": "Curso Online",
        "offer": "Acesso vitalício + comunidade",
        "brand": "Marca X",
        "ki_story": "Conheci um empreendedor que...",
        "ki_connection": "Muitos de nós passamos por isso",
        "sho_problem": "O problema é que...",
        "sho_consequences": "Isso resulta em...",
        "sho_context": "A realidade é que...",
        "ten_revelation": "Mas descobrimos que...",
        "ten_mechanism": "O mecanismo é...",
        "ten_solution": "Por isso criamos...",
        "ten_transformation": "Agora você pode...",
        "ketsu_reaffirmation": "O que você está recebendo é...",
        "ketsu_benefits": "1. Benefício 1\n2. Benefício 2\n3. Benefício 3",
        "ketsu_guarantee": "30 dias de garantia",
    }
    
    generator = VSLGenerator(language="pt")
    script = generator.generate_script(example_data)
    storyboard = generate_storyboard(script, language="pt")
    
    print("\nVSL Script Generated:")
    print(json.dumps(script, indent=2, ensure_ascii=False))
    
    print("\n\nStoryboard Generated:")
    print(json.dumps(storyboard, indent=2, ensure_ascii=False))
