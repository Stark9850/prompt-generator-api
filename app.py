import streamlit as st
import requests

st.set_page_config(page_title='Aivengers Prompt Generator', layout='centered')
st.title('🚀 Aivengers Prompt Generator')
st.markdown('Create powerful prompts with Groq + Aivengers.')

# Define prompt packs and mapping
packs = {
    "AI Agent Builder": "ai_agent_builder",
    "Cold Outreach": "cold_outreach",
    "Custom Prompt Builder": "custom_prompt_builder",
    "Debug Helper": "debug_helper",
    "Market Research": "market_research",
    "Product Ideation": "product_ideation",
    "Smart Email Assistant": "smart_email_assistant",
    "Video Script Generator": "video_script_generator",
    "Viral LinkedIn Post": "viral_linkedin_post",
}

selected_pack = st.selectbox('🎯 Choose Prompt Pack', list(packs.keys()))
inputs = {}

if selected_pack == 'AI Agent Builder':
    inputs['agent_name_role'] = st.text_input('Agent Name/Role', placeholder='Defines agent identity; useful for instruction and context.')
    inputs['objective_goal'] = st.text_input('Objective/Goal', placeholder='Primary mission of the agent; central to defining purpose and functionality.')
    inputs['domain_context'] = st.text_area('Domain/Context', placeholder='Industry knowledge or environment; improves relevance and accuracy.')
    inputs['tools_abilities'] = st.text_input('Tools/Abilities', placeholder='External tools or APIs; expands agent capabilities and realism.')
    inputs['constraints_rules'] = st.text_input('Constraints/Rules', placeholder='Guardrails or limitations; ensures safety, compliance, and focus.')
    inputs['persona_tone'] = st.text_input('Persona/Tone', placeholder='Agent’s communication style; enhances user experience and consistency.')
    inputs['output_format'] = st.text_input('Output Format', placeholder='How the agent should respond (list, JSON, etc.); aligns with expectations.')

if selected_pack == 'Cold Outreach':
    inputs['recipient_profile'] = st.text_input('Recipient Profile', placeholder='Defines the target; enables personalization and tone adjustment.')
    inputs['context_personalization'] = st.text_area('Context/Personalization', placeholder='Creates relevance and trust through tailored intros.')
    inputs['sender_profile'] = st.text_input('Sender Profile', placeholder='Establishes credibility and context for the pitch.')
    inputs['value_proposition'] = st.text_input('Value Proposition', placeholder='Highlights why the message matters; the benefit to the recipient.')
    inputs['ask_call_to_action'] = st.text_input('Ask/Call-to-Action', placeholder='Prompts the next step; clarifies desired outcome.')
    inputs['tone_style'] = st.text_input('Tone/Style', placeholder='Influences approachability and formality.')
    inputs['subject_line'] = st.text_input('Subject Line', placeholder='First impression (for emails); impacts open rates and interest.')

if selected_pack == 'Custom Prompt Builder':
    inputs['persona_role'] = st.text_input('Persona/Role', placeholder='Defines the AI’s identity and style of response.')
    inputs['task_objective'] = st.text_input('Task/Objective', placeholder='States the job to be done; anchors the prompt.')
    inputs['context_background'] = st.text_area('Context/Background', placeholder='Provides situational data or prior inputs; aids relevance.')
    inputs['format_output_requirements'] = st.text_input('Format/Output Requirements', placeholder='Shapes structure of output (e.g., list, JSON).')
    inputs['tone_style_guidelines'] = st.text_input('Tone/Style Guidelines', placeholder='Refines voice and personality of the response.')
    inputs['constraints_rules'] = st.text_input('Constraints/Rules', placeholder='Adds guardrails to limit or enforce behavior.')
    inputs['examples_few_shot'] = st.text_input('Examples (Few-shot)', placeholder='Demonstrates desired outputs; improves specificity.')
    inputs['additional_instructions'] = st.text_input('Additional Instructions', placeholder='Covers any extra guiding behavior or meta steps.')

if selected_pack == 'Debug Helper':
    inputs['programming_language'] = st.text_input('Programming Language', placeholder='Aligns syntax and best practices with the language used.')
    inputs['code_snippet'] = st.text_input('Code Snippet', placeholder='Provides the logic for diagnosis; central to solving the issue.')
    inputs['error_message_issue'] = st.text_input('Error Message/Issue', placeholder='Pinpoints what went wrong; helps isolate the problem.')
    inputs['expected_behavior'] = st.text_input('Expected Behavior', placeholder='Clarifies intended outcome; distinguishes right from wrong behavior.')
    inputs['steps_taken_attempts'] = st.text_input('Steps Taken/Attempts', placeholder='Avoids redundant suggestions; informs debugging strategy.')
    inputs['environment_details'] = st.text_input('Environment Details', placeholder='Catches context-specific bugs; identifies version-related issues.')
    inputs['output_preference'] = st.text_input('Output Preference', placeholder='Defines if explanation, fix, or both are expected.')

if selected_pack == 'Market Research':
    inputs['market_industry'] = st.text_input('Market/Industry', placeholder='Sets the scope for insights; ensures topic relevance.')
    inputs['geographic_scope'] = st.text_input('Geographic Scope', placeholder='Targets research to specific markets or regions.')
    inputs['key_topics_questions'] = st.text_input('Key Topics/Questions', placeholder='Specifies what insights are needed; drives structured output.')
    inputs['customer_persona'] = st.text_input('Customer Persona', placeholder='Focuses insights on specific user segments.')
    inputs['time_frame'] = st.text_input('Time Frame', placeholder='Sets a window for analysis; current, historical, or forecast.')
    inputs['preferred_format'] = st.text_input('Preferred Format', placeholder='Defines how the results should be presented.')

if selected_pack == 'Product Ideation':
    inputs['industry_domain'] = st.text_input('Industry/Domain', placeholder='Defines the market context; sets background for ideation.')
    inputs['target_customer'] = st.text_input('Target Customer', placeholder='Focuses ideas on solving problems for specific users.')
    inputs['problem_pain_point'] = st.text_input('Problem/Pain Point', placeholder='Defines what needs solving; drives meaningful and relevant ideas.')
    inputs['value_proposition_focus'] = st.text_input('Value Proposition Focus', placeholder='Guides toward a unique competitive edge (e.g., speed, cost).')
    inputs['trends_tech_to_leverage'] = st.text_input('Trends/Tech to Leverage', placeholder='Infuses innovation by leveraging current trends or technologies.')
    inputs['constraints_criteria'] = st.text_input('Constraints/Criteria', placeholder='Ensures ideas are feasible and aligned with real-world limits.')
    inputs['output_detail_level'] = st.text_input('Output Detail Level', placeholder='Controls depth of output; can range from summaries to full plans.')

if selected_pack == 'Smart Email Assistant':
    inputs['email_type_purpose'] = st.text_input('Email Type/Purpose', placeholder='Establishes structure and tone based on intent.')
    inputs['recipient_&_relationship'] = st.text_input('Recipient & Relationship', placeholder='Tailors formality and phrasing to the relationship.')
    inputs['key_points_to_include'] = st.text_input('Key Points to Include', placeholder='Ensures essential information is conveyed.')
    inputs['tone_formality'] = st.text_input('Tone/Formality', placeholder='Sets mood and language style.')
    inputs['email_length'] = st.text_input('Email Length', placeholder='Controls brevity or depth based on situation.')
    inputs['specific_phrases_or_style_guidelines'] = st.text_input('Specific Phrases or Style Guidelines', placeholder='Adds or avoids phrases as needed; customizes style.')

if selected_pack == 'Video Script Generator':
    inputs['topic_title'] = st.text_input('Topic/Title', placeholder='Central theme of the video; guides content and message.')
    inputs['video_format_style'] = st.text_input('Video Format/Style', placeholder='Defines structure and pacing; matches audience expectations.')
    inputs['target_audience'] = st.text_input('Target Audience', placeholder='Shapes tone and complexity; ensures relevance and engagement.')
    inputs['tone_mood'] = st.text_input('Tone/Mood', placeholder='Sets emotional impact and storytelling approach.')
    inputs['duration_length'] = st.text_input('Duration/Length', placeholder='Controls pacing and detail level of the script.')
    inputs['key_points_outline'] = st.text_input('Key Points/Outline', placeholder='Ensures all intended content is included and structured.')
    inputs['visual_or_scene_directions'] = st.text_input('Visual or Scene Directions', placeholder='Guides visual cues for syncing script with visuals.')
    inputs['closing_message_cta'] = st.text_input('Closing Message/CTA', placeholder='Wraps up the message and prompts viewer action.')

if selected_pack == 'Viral LinkedIn Post':
    inputs['topic_theme'] = st.text_input('Topic/Theme', placeholder='Main subject of the post; defines focus and helps generate a strong hook.')
    inputs['target_audience'] = st.text_input('Target Audience', placeholder='Who the post is for; tailoring to the audience improves relevance and tone.')
    inputs['personal_story_or_insight'] = st.text_area('Personal Story or Insight', placeholder='Adds authenticity; makes the post more relatable and unique.')
    inputs['tone_style'] = st.text_input('Tone/Style', placeholder='Sets the emotional voice and engagement style of the post.')
    inputs['call_to_action_cta'] = st.text_input('Call-to-Action (CTA)', placeholder='Encourages interaction (comments, shares); boosts engagement and reach.')
    inputs['hashtags_keywords'] = st.text_input('Hashtags/Keywords', placeholder='Improves discoverability; categorizes the post for reach.')
    inputs['length_format'] = st.text_input('Length/Format', placeholder='Shapes readability and pacing; aligns with platform best practices.')

if st.button('🚀 Generate Prompt'):
    with st.spinner('Calling backend...'):
        try:
            response = requests.post(
                'https://prompt-generator-api.onrender.com/generate',
                json={'pack': packs[selected_pack], 'inputs': inputs}
            )
            data = response.json()
            st.markdown('### ✨ Generated Prompt')
            st.code(data.get('prompt', 'No response received.'))
        except Exception as e:
            st.error(f'Error: {str(e)}')