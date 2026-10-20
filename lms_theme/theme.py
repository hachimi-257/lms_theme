import os

CSS_FILE = os.path.join(os.path.dirname(__file__), "public", "css", "lms_theme.css")


def inject_stylesheet(response, request):
	"""Append the theme stylesheet to the LMS single-page app's HTML."""
	if response.status_code != 200 or not response.mimetype == "text/html":
		return
	if response.direct_passthrough:
		return

	from lms.lms.utils import get_lms_path

	if not request.path.strip("/").startswith(get_lms_path()):
		return

	html = response.get_data(as_text=True)
	if "</head>" not in html:
		return

	# mtime busts the browser cache whenever the CSS is edited
	version = int(os.path.getmtime(CSS_FILE))
	link = f'<link rel="stylesheet" href="/assets/lms_theme/css/lms_theme.css?v={version}">'
	response.set_data(html.replace("</head>", f"{link}</head>", 1))
