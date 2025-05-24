def build_user_prompt(pack, inputs):

    if pack == "ai_agent_builder":
        return f"""Use Case: AI Agent Builder
Agent Name/Role: {{inputs.get('agent_name_role', '')}}
Objective/Goal: {{inputs.get('objective_goal', '')}}
Domain/Context: {{inputs.get('domain_context', '')}}
Tools/Abilities: {{inputs.get('tools_abilities', '')}}
Constraints/Rules: {{inputs.get('constraints_rules', '')}}
Persona/Tone: {{inputs.get('persona_tone', '')}}
Output Format: {{inputs.get('output_format', '')}}
Generate a detailed prompt for ChatGPT based on the above context."""

    if pack == "cold_outreach":
        return f"""Use Case: Cold Outreach
Recipient Profile: {{inputs.get('recipient_profile', '')}}
Context/Personalization: {{inputs.get('context_personalization', '')}}
Sender Profile: {{inputs.get('sender_profile', '')}}
Value Proposition: {{inputs.get('value_proposition', '')}}
Ask/Call-to-Action: {{inputs.get('ask_call_to_action', '')}}
Tone/Style: {{inputs.get('tone_style', '')}}
Subject Line: {{inputs.get('subject_line', '')}}
Generate a detailed prompt for ChatGPT based on the above context."""

    if pack == "custom_prompt_builder":
        return f"""Use Case: Custom Prompt Builder
Persona/Role: {{inputs.get('persona_role', '')}}
Task/Objective: {{inputs.get('task_objective', '')}}
Context/Background: {{inputs.get('context_background', '')}}
Format/Output Requirements: {{inputs.get('format_output_requirements', '')}}
Tone/Style Guidelines: {{inputs.get('tone_style_guidelines', '')}}
Constraints/Rules: {{inputs.get('constraints_rules', '')}}
Examples (Few-shot): {{inputs.get('examples_few_shot', '')}}
Additional Instructions: {{inputs.get('additional_instructions', '')}}
Generate a detailed prompt for ChatGPT based on the above context."""

    if pack == "debug_helper":
        return f"""Use Case: Debug Helper
Programming Language: {{inputs.get('programming_language', '')}}
Code Snippet: {{inputs.get('code_snippet', '')}}
Error Message/Issue: {{inputs.get('error_message_issue', '')}}
Expected Behavior: {{inputs.get('expected_behavior', '')}}
Steps Taken/Attempts: {{inputs.get('steps_taken_attempts', '')}}
Environment Details: {{inputs.get('environment_details', '')}}
Output Preference: {{inputs.get('output_preference', '')}}
Generate a detailed prompt for ChatGPT based on the above context."""

    if pack == "market_research":
        return f"""Use Case: Market Research
Market/Industry: {{inputs.get('market_industry', '')}}
Geographic Scope: {{inputs.get('geographic_scope', '')}}
Key Topics/Questions: {{inputs.get('key_topics_questions', '')}}
Customer Persona: {{inputs.get('customer_persona', '')}}
Time Frame: {{inputs.get('time_frame', '')}}
Preferred Format: {{inputs.get('preferred_format', '')}}
Generate a detailed prompt for ChatGPT based on the above context."""

    if pack == "product_ideation":
        return f"""Use Case: Product Ideation
Industry/Domain: {{inputs.get('industry_domain', '')}}
Target Customer: {{inputs.get('target_customer', '')}}
Problem/Pain Point: {{inputs.get('problem_pain_point', '')}}
Value Proposition Focus: {{inputs.get('value_proposition_focus', '')}}
Trends/Tech to Leverage: {{inputs.get('trends_tech_to_leverage', '')}}
Constraints/Criteria: {{inputs.get('constraints_criteria', '')}}
Output Detail Level: {{inputs.get('output_detail_level', '')}}
Generate a detailed prompt for ChatGPT based on the above context."""

    if pack == "smart_email_assistant":
        return f"""Use Case: Smart Email Assistant
Email Type/Purpose: {{inputs.get('email_type_purpose', '')}}
Recipient & Relationship: {{inputs.get('recipient_&_relationship', '')}}
Key Points to Include: {{inputs.get('key_points_to_include', '')}}
Tone/Formality: {{inputs.get('tone_formality', '')}}
Email Length: {{inputs.get('email_length', '')}}
Specific Phrases or Style Guidelines: {{inputs.get('specific_phrases_or_style_guidelines', '')}}
Generate a detailed prompt for ChatGPT based on the above context."""

    if pack == "video_script_generator":
        return f"""Use Case: Video Script Generator
Topic/Title: {{inputs.get('topic_title', '')}}
Video Format/Style: {{inputs.get('video_format_style', '')}}
Target Audience: {{inputs.get('target_audience', '')}}
Tone/Mood: {{inputs.get('tone_mood', '')}}
Duration/Length: {{inputs.get('duration_length', '')}}
Key Points/Outline: {{inputs.get('key_points_outline', '')}}
Visual or Scene Directions: {{inputs.get('visual_or_scene_directions', '')}}
Closing Message/CTA: {{inputs.get('closing_message_cta', '')}}
Generate a detailed prompt for ChatGPT based on the above context."""

    if pack == "viral_linkedin_post":
        return f"""Use Case: Viral LinkedIn Post
Topic/Theme: {{inputs.get('topic_theme', '')}}
Target Audience: {{inputs.get('target_audience', '')}}
Personal Story or Insight: {{inputs.get('personal_story_or_insight', '')}}
Tone/Style: {{inputs.get('tone_style', '')}}
Call-to-Action (CTA): {{inputs.get('call_to_action_cta', '')}}
Hashtags/Keywords: {{inputs.get('hashtags_keywords', '')}}
Length/Format: {{inputs.get('length_format', '')}}
Generate a detailed prompt for ChatGPT based on the above context."""

    return 'Unsupported prompt pack.'