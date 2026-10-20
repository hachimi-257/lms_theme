import os

import frappe

APP_NAME = "vidiSI"
IMAGES = os.path.join(os.path.dirname(__file__), "public", "images")

# Website Settings field -> image in public/images (LMS reads these for branding)
BRANDING = {
	"banner_image": "logo-square.png",  # sidebar, shown in a small square
	"app_logo": "logo-square.png",
	"favicon": "favicon.png",
	"footer_logo": "logo.png",
}


def apply_branding():
	"""Set app name, logos and favicon in Website Settings."""
	settings = frappe.get_single("Website Settings")
	settings.app_name = APP_NAME
	for field, image in BRANDING.items():
		settings.set(field, _get_or_create_file(image))
	settings.save(ignore_permissions=True)
	frappe.db.commit()


def _get_or_create_file(image):
	file_name = f"vidisi-{image}"
	existing = frappe.db.get_value("File", {"file_name": file_name, "is_private": 0}, "file_url")
	if existing:
		return existing

	with open(os.path.join(IMAGES, image), "rb") as f:
		file = frappe.get_doc(
			{"doctype": "File", "file_name": file_name, "is_private": 0, "content": f.read()}
		).insert(ignore_permissions=True)
	return file.file_url
