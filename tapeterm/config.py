import os
HOME = os.environ['HOME']
CONFIG_FOLDER = os.path.join(HOME, '.tapeterm')
JSON_EN = os.path.join(CONFIG_FOLDER, 'config_en.json')
JSON_EL = os.path.join(CONFIG_FOLDER, 'config_el.json')

def check_config_files():
    import shutil
    if not os.path.exists(os.path.join(HOME, '.tapeterm')):
        os.makedirs(os.path.join(HOME, '.tapeterm'))
    if not os.path.exists(JSON_EN):
        shutil.copy(
            os.path.join('./tapeterm', os.path.basename(JSON_EN)),
            os.path.join(CONFIG_FOLDER, os.path.basename(JSON_EN))
        )
    if not os.path.exists(JSON_EL):
        shutil.copy(
            os.path.join('./tapeterm', os.path.basename(JSON_EL)),
            os.path.join(CONFIG_FOLDER, os.path.basename(JSON_EL))
        )
