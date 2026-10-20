app_name = "lms_theme"
app_title = "LMS Theme"
app_publisher = "vidiSI"
app_description = "Thème vidiSI pour Frappe LMS"
app_email = ""
app_license = "mit"

required_apps = ["lms"]

after_request = ["lms_theme.theme.inject_stylesheet"]
after_install = "lms_theme.setup.apply_branding"
