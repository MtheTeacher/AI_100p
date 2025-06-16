
import os
import re

base_dir = '/home/ubuntu/course_website/Artificiell_Intelligens_Nivå1_kurs'

pages_and_parents = {
    # Level 1 pages (parent is index.html)
    'introduction/course_introduction.html': '../index.html',
    'definitions/ai_definitions.html': '../index.html',
    'foundations/mathematical_foundations.html': '../index.html',
    'data/data_importance.html': '../index.html',
    'techniques/ai_techniques.html': '../index.html',
    'applications/practical_applications.html': '../index.html',
    'human/human_vs_ai.html': '../index.html',
    'ethics/ethics_society.html': '../index.html',
    'interactive/interactive_exercises.html': '../index.html',

    # Level 2 pages
    'introduction/three_projects.html': 'course_introduction.html',

    'definitions/turing_test.html': 'ai_definitions.html',
    'definitions/ai_coined.html': 'ai_definitions.html',
    'definitions/expert_systems.html': 'ai_definitions.html',
    'definitions/deep_blue_kasparov.html': 'ai_definitions.html',
    'definitions/deep_learning_breakthrough.html': 'ai_definitions.html',

    'applications/ai_in_netflix.html': 'practical_applications.html',
    'applications/ai_in_google_maps.html': 'practical_applications.html',
    'applications/ai_in_spotify.html': 'practical_applications.html',
    'applications/ai_in_instagram.html': 'practical_applications.html',
    'applications/ai_in_siri_alexa.html': 'practical_applications.html',
    'applications/ai_in_tesla.html': 'practical_applications.html',
    'applications/ai_in_ecommerce.html': 'practical_applications.html',
    'applications/ai_in_healthcare.html': 'practical_applications.html',
    'applications/ai_in_security.html': 'practical_applications.html',
    'applications/ai_in_transportation.html': 'practical_applications.html',

    # These might not exist yet, will be skipped if so
    'techniques/ai_prediction.html': 'ai_techniques.html',
    'techniques/ai_robotics.html': 'ai_techniques.html',
}

back_button_css_marker = '/* --- Back Button CSS --- */'
back_button_css = f'''{back_button_css_marker}
      .back-button {{
        position: fixed;
        top: 20px;
        left: 20px;
        background: rgba(0,0,0,0.3); /* Darker for better visibility on various backgrounds */
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 50px;
        padding: 10px 15px; /* Slightly smaller padding */
        font-size: 0.9rem; /* Slightly smaller font */
        color: white;
        text-decoration: none;
        backdrop-filter: blur(8px); /* Slightly less blur */
        transition: all 0.3s ease;
        z-index: 1000; /* Ensure it's on top */
        display: flex; /* For icon alignment */
        align-items: center; /* For icon alignment */
      }}
      
      .back-button:hover {{
        background: rgba(0,0,0,0.5); /* Darker hover */
        transform: translateX(-3px); /* Slightly less transform */
      }}
      .back-button i {{
        margin-right: 8px; /* Space between icon and text */
      }}
'''

font_awesome_link = '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">'

for page_file, parent_file in pages_and_parents.items():
    file_path = os.path.join(base_dir, page_file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content # For checking if changes were made

        # Ensure Font Awesome is linked
        if font_awesome_link not in content and '</head>' in content:
            content = content.replace('</head>', f'    {font_awesome_link}\n</head>', 1)

        # CSS part
        style_end_tag = '</style>'
        if back_button_css_marker not in content:
            if style_end_tag in content:
                content = content.replace(style_end_tag, back_button_css + style_end_tag, 1)
            elif '</head>' in content: # Fallback if no style tag
                content = content.replace('</head>', f'<style>\n{back_button_css}\n</style>\n</head>', 1)
        
        # HTML part
        # Remove existing back button(s) to avoid duplicates and ensure correct href
        content_before_removal = content
        content = re.sub(r'<a[^>]*class=("|\')back-button("|\')[^>]*>.*?</a>', '', content, flags=re.IGNORECASE | re.DOTALL)
        # if content_before_removal != content:
            # print(f'Removed existing back button from {page_file}')

        if '.old.html' not in page_file and page_file != 'index.html':
            current_back_button_html = f'''
    <a href="{parent_file}" class="back-button">
        <i class="fas fa-arrow-left"></i>Tillbaka
    </a>'''
            body_start_tag_match = re.search(r'<body[^>]*>', content, flags=re.IGNORECASE)
            if body_start_tag_match:
                body_start_tag = body_start_tag_match.group(0)
                # Ensure not to insert inside an existing script or style tag if body tag is minimal
                if body_start_tag.endswith(">"):
                    content = content.replace(body_start_tag, body_start_tag + current_back_button_html, 1)
                else: # Less ideal, but a fallback
                    content = current_back_button_html + content
            else: 
                content = current_back_button_html + content
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated back button for {page_file} (links to {parent_file})')
        else:
            print(f'No changes needed for {page_file}')
            
    else:
        print(f'File not found, skipping: {page_file}')

print('Finished processing back buttons.')


