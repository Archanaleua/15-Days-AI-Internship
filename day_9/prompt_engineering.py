# Day 9 - Prompt Engineering
# Zero-shot, Few-shot, Chain of Thought (CoT)

# ============================================
# 1. ZERO-SHOT PROMPTING
# ============================================
# Zero-shot = No examples given, just ask directly

zero_shot_prompt = """
You are a helpful assistant.
Classify the sentiment of this sentence:
'I love this product, it is amazing!'
Answer: Positive or Negative only.
"""

print("=" * 50)
print("1. ZERO-SHOT PROMPT EXAMPLE")
print("=" * 50)
print(zero_shot_prompt)


# ============================================
# 2. FEW-SHOT PROMPTING
# ============================================
# Few-shot = Give examples first, then ask

few_shot_prompt = """
Classify the sentiment:

Example 1:
Text: 'This food is terrible'
Sentiment: Negative

Example 2:
Text: 'I had a great day today'
Sentiment: Positive

Example 3:
Text: 'This movie is boring'
Sentiment: Negative

Now classify this:
Text: 'I love my new phone!'
Sentiment: ?
"""

print("=" * 50)
print("2. FEW-SHOT PROMPT EXAMPLE")
print("=" * 50)
print(few_shot_prompt)


# ============================================
# 3. CHAIN OF THOUGHT (CoT) PROMPTING
# ============================================
# CoT = Ask AI to think step by step

cot_prompt = """
Q: A shop has 50 apples. They sold 20 in the morning
and 15 in the afternoon. How many are left?

Let's think step by step:
Step 1: Start with 50 apples
Step 2: Sold 20 in morning → 50 - 20 = 30
Step 3: Sold 15 in afternoon → 30 - 15 = 15
Answer: 15 apples are left
"""

print("=" * 50)
print("3. CHAIN OF THOUGHT PROMPT EXAMPLE")
print("=" * 50)
print(cot_prompt)


# ============================================
# 4. MARKETING PROMPT EXAMPLE
# ============================================

marketing_prompt = """
You are a professional marketing copywriter.
Write a short Instagram caption for a new
smartphone launch with these features:
- 200MP camera
- 5000mAh battery
- Slim design

Tone: Exciting and modern
Length: 2-3 sentences
Include: 3 relevant hashtags
"""

print("=" * 50)
print("4. MARKETING PROMPT EXAMPLE")
print("=" * 50)
print(marketing_prompt)

print("=" * 50)
print("Day 9 - Prompt Engineering Complete!")
print("=" * 50)