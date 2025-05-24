def build_user_prompt(pack, inputs):
    if pack == "viral_linkedin":
        return f"""Use Case: Viral LinkedIn Post
Topic: {inputs.get('topic')}
Goal: {inputs.get('goal')}
Format: {inputs.get('format')}
Tone: {inputs.get('tone')}

Generate a detailed prompt for ChatGPT to write a LinkedIn post based on this setup."""

    elif pack == "ai_agent_builder":
        return f"""Use Case: AI Agent Builder
Goal: {inputs.get('goal')}
Agent Role: {inputs.get('agent_role')}
Input Type: {inputs.get('input_type')}
Output Type: {inputs.get('output_type')}
Tools: {inputs.get('tools', 'None')}

Generate a prompt for ChatGPT that would power such an agent."""

    elif pack == "product_ideation":
        return f"""Use Case: Product Ideation
Problem: {inputs.get('problem')}
Target User: {inputs.get('target_user')}
Industry: {inputs.get('industry')}
Outcome: {inputs.get('outcome')}

Generate a prompt to brainstorm product ideas or validate them."""

    elif pack == "landing_page_copy":
        return f"""Use Case: Landing Page Copy
Product Type: {inputs.get('product_type')}
Audience: {inputs.get('audience')}
Value Proposition: {inputs.get('value')}
Call to Action: {inputs.get('cta')}

Create a ChatGPT prompt to write a persuasive landing page copy."""

    elif pack == "video_script":
        return f"""Use Case: Video Script Generator
Topic: {inputs.get('topic')}
Platform: {inputs.get('platform')}
Emotion: {inputs.get('emotion')}
Goal: {inputs.get('goal')}

Generate a script-writing prompt for ChatGPT tailored to this scenario."""

    elif pack == "cold_outreach":
        return f"""Use Case: Cold Outreach
Industry: {inputs.get('industry')}
Target Role: {inputs.get('role')}
Offer Type: {inputs.get('offer')}
Tone: {inputs.get('tone')}

Write a prompt that helps ChatGPT create a personalized cold email."""

    elif pack == "competitor_teardown":
        return f"""Use Case: Competitor Teardown
Competitor: {inputs.get('competitor')}
Objective: {inputs.get('objective')}
Format: {inputs.get('format')}

Create a prompt to analyze this competitor's product, strategy, or positioning."""

    elif pack == "market_research":
        return f"""Use Case: Market Research
Industry: {inputs.get('industry')}
Persona Type: {inputs.get('persona')}
Research Goal: {inputs.get('goal')}

Generate a prompt to get user insights or trends in this market."""

    elif pack == "course_creator":
        return f"""Use Case: Course or Ebook Creation
Topic: {inputs.get('topic')}
Audience: {inputs.get('audience')}
Format: {inputs.get('format')}
Depth: {inputs.get('depth')}

Create a prompt to generate a full course or ebook outline."""

    elif pack == "debug_helper":
        return f"""Use Case: Debugging / Code Fix
Code Language: {inputs.get('language')}
Problem Description: {inputs.get('problem')}
Error Output: {inputs.get('error')}
Context: {inputs.get('context', 'None')}

Write a prompt for ChatGPT to help fix this code issue."""

    elif pack == "smart_email":
        return f"""Use Case: Smart Email Draft
Purpose: {inputs.get('purpose')}
Tone: {inputs.get('tone')}
Audience: {inputs.get('audience')}
Key Points: {inputs.get('points')}

Write a prompt to help ChatGPT draft a high-quality email for this purpose."""

    return "Unsupported prompt pack."
