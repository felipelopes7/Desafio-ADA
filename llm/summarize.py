import torch

def generate_summary(model, tokenizer, text, device):
    """
    Gera um resumo do texto fornecido usando o LLM carregado.
    Lida com o truncamento de texto se a entrada for muito longa para a janela de contexto.
    """
    
    if not model or not tokenizer:
        return "Modelo não carregado corretamente."

    print("Gerando resumo...")

    # Define um prompt de sistema simplificado para o modelo
    system_prompt = "Você é um assistente útil que resume textos em português. Seja direto e conciso."
    
    # Truncamento simples para caber na janela de contexto (evita erros de OutOfMemory em PDFs grandes)
    # Uma abordagem mais segura para este desafio é pegar os primeiros ~4000 caracteres 
    # ou implementar um loop de fragmentação (chunking/map-reduce) para textos muito grandes.
    # Aqui truncamos para garantir estabilidade e velocidade.
    max_chars = 6000 
    input_text = text[:max_chars]
    
    if len(text) > max_chars:
        print(f"Aviso: Texto muito longo. Resumindo apenas os primeiros {max_chars} caracteres.")
        input_text += "\n[...texto truncado...]"

    # Constrói o formato de mensagem esperado pelos modelos Instruct
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Resuma o seguinte texto destacando os pontos principais:\n\n{input_text}"}
    ]

    # Prepara as entradas
    text_input = tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=True
    )
    
    model_inputs = tokenizer([text_input], return_tensors="pt").to(device)

    # Gera a resposta
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512,  # Limita o tamanho do resumo
        do_sample=False,     # Determinístico (temperature=0) geralmente é melhor para sumarização
        temperature=0.7,     # Ignorado se do_sample=False, mas é boa prática definir
        top_p=0.9
    )

    # Decodifica a resposta
    # Removemos os tokens de entrada para manter apenas o novo texto gerado
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    
    summary = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    return summary