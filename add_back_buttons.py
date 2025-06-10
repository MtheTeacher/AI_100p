import os
import re

main_slides = [
    'course_introduction.html',
    'ai_definitions.html',
    'mathematical_foundations.html',
    'data_importance.html',
    'ai_techniques.html',
    'practical_applications.html',
    'human_vs_ai.html',
    'ethics_society.html',
    'interactive_exercises.html',
    'summary_next_steps.html'
]

static_dir = '/home/ubuntu/ai_presentation_website_v3/src/static'

back_button_css = '''
      .back-button {
        position: fixed;
        top: 20px;
        left: 20px;
        background: rgba(255,255,255,0.2);
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 50px;
        padding: 10px 20px;
        color: white;
        text-decoration: none;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        z-index: 100;
      }
      
      .back-button:hover {
        background: rgba(255,255,255,0.3);
        transform: translateX(-5px);
      }
'''

back_button_html = '''
    <a href="index.html" class="back-button">
        <i class="fas fa-arrow-left mr-2"></i>Tillbaka
    </a>
'''

for slide_file in main_slides:
    file_path = os.path.join(static_dir, slide_file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Insert CSS
        style_end_tag = '</style>'
        if back_button_css not in content:
            content = content.replace(style_end_tag, back_button_css + style_end_tag)
        
        # Insert HTML
        body_start_tag = '<body>'
        if back_button_html not in content:
            content = content.replace(body_start_tag, body_start_tag + back_button_html)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Added back button to {slide_file}')
    else:
        print(f'File not found: {slide_file}')

print('Finished adding back buttons to main slides.')

