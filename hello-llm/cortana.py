from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name='gpt2'

# 加载预训练模型及其分词器
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)


# print(model.parameters())
def generate_text(prompt_text, max_length=50):
    

    # 编码输入文本，增加必要的格式标记
    encoded_input = tokenizer.encode(prompt_text, return_tensors='pt')
    
    # 生成文本
    output_sequences = model.generate(
        input_ids=encoded_input,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        top_p=0.92,
        temperature=0.85,
    )

    # 解码生成的文本
    return tokenizer.decode(output_sequences[0], skip_special_tokens=True)



print("Model is ready")
while(True):
    print("\n\n\n======")
    prompt = input("Say something to our model>>>")
    reply = generate_text(prompt)
    print("\n\n=======Following is machine's reply=======")
    print(reply)
    print("==========================================")
