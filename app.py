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
    inputs['agent_name_role'] = st.text_input('Agent Name/Role')
    inputs['objective_goal'] = st.text_input('Objective/Goal')
    inputs['domain_context'] = st.text_area('Domain/Context')
    inputs['tools_abilities'] = st.text_input('Tools/Abilities')
    inputs['constraints_rules'] = st.text_input('Constraints/Rules')
    inputs['persona_tone'] = st.text_input('Persona/Tone')
    inputs['output_format'] = st.text_input('Output Format')

if selected_pack == 'Cold Outreach':
    inputs['recipient_profile'] = st.text_input('Recipient Profile')
    inputs['context_personalization'] = st.text_area('Context/Personalization')
    inputs['sender_profile'] = st.text_input('Sender Profile')
    inputs['value_proposition'] = st.text_input('Value Proposition')
    inputs['ask_call_to_action'] = st.text_input('Ask/Call-to-Action')
    inputs['tone_style'] = st.text_input('Tone/Style')
    inputs['subject_line'] = st.text_input('Subject Line')

if selected_pack == 'Custom Prompt Builder':
    inputs['persona_role'] = st.text_input('Persona/Role')
    inputs['task_objective'] = st.text_input('Task/Objective')
    inputs['context_background'] = st.text_area('Context/Background')
    inputs['format_output_requirements'] = st.text_input('Format/Output Requirements')
    inputs['tone_style_guidelines'] = st.text_input('Tone/Style Guidelines')
    inputs['constraints_rules'] = st.text_input('Constraints/Rules')
    inputs['examples_few_shot'] = st.text_input('Examples (Few-shot)')
    inputs['additional_instructions'] = st.text_input('Additional Instructions')

if selected_pack == 'Debug Helper':
    inputs['programming_language'] = st.text_input('Programming Language')
    inputs['code_snippet'] = st.text_input('Code Snippet')
    inputs['error_message_issue'] = st.text_input('Error Message/Issue')
    inputs['expected_behavior'] = st.text_input('Expected Behavior')
    inputs['steps_taken_attempts'] = st.text_input('Steps Taken/Attempts')
    inputs['environment_details'] = st.text_input('Environment Details')
    inputs['output_preference'] = st.text_input('Output Preference')

if selected_pack == 'Market Research':
    inputs['market_industry'] = st.text_input('Market/Industry')
    inputs['geographic_scope'] = st.text_input('Geographic Scope')
    inputs['key_topics_questions'] = st.text_input('Key Topics/Questions')
    inputs['customer_persona'] = st.text_input('Customer Persona')
    inputs['time_frame'] = st.text_input('Time Frame')
    inputs['preferred_format'] = st.text_input('Preferred Format')

if selected_pack == 'Product Ideation':
    inputs['industry_domain'] = st.text_input('Industry/Domain')
    inputs['target_customer'] = st.text_input('Target Customer')
    inputs['problem_pain_point'] = st.text_input('Problem/Pain Point')
    inputs['value_proposition_focus'] = st.text_input('Value Proposition Focus')
    inputs['trends_tech_to_leverage'] = st.text_input('Trends/Tech to Leverage')
    inputs['constraints_criteria'] = st.text_input('Constraints/Criteria')
    inputs['output_detail_level'] = st.text_input('Output Detail Level')

if selected_pack == 'Smart Email Assistant':
    inputs['email_type_purpose'] = st.text_input('Email Type/Purpose')
    inputs['recipient_&_relationship'] = st.text_input('Recipient & Relationship')
    inputs['key_points_to_include'] = st.text_input('Key Points to Include')
    inputs['tone_formality'] = st.text_input('Tone/Formality')
    inputs['email_length'] = st.text_input('Email Length')
    inputs['specific_phrases_or_style_guidelines'] = st.text_input('Specific Phrases or Style Guidelines')

if selected_pack == 'Video Script Generator':
    inputs['topic_title'] = st.text_input('Topic/Title')
    inputs['video_format_style'] = st.text_input('Video Format/Style')
    inputs['target_audience'] = st.text_input('Target Audience')
    inputs['tone_mood'] = st.text_input('Tone/Mood')
    inputs['duration_length'] = st.text_input('Duration/Length')
    inputs['key_points_outline'] = st.text_input('Key Points/Outline')
    inputs['visual_or_scene_directions'] = st.text_input('Visual or Scene Directions')
    inputs['closing_message_cta'] = st.text_input('Closing Message/CTA')

if selected_pack == 'Viral LinkedIn Post':
    inputs['topic_theme'] = st.text_input('Topic/Theme')
    inputs['target_audience'] = st.text_input('Target Audience')
    inputs['personal_story_or_insight'] = st.text_area('Personal Story or Insight')
    inputs['tone_style'] = st.text_input('Tone/Style')
    inputs['call_to_action_cta'] = st.text_input('Call-to-Action (CTA)')
    inputs['hashtags_keywords'] = st.text_input('Hashtags/Keywords')
    inputs['length_format'] = st.text_input('Length/Format')

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