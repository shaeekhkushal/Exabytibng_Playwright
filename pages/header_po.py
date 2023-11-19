class Header:
	def __init__(self, page):
		self.logo_click = page.locator(".elementor-widget-wrap")
		self.service = page.get_by_role("link", name="Services ")
		self.our_expertise = page.get_by_role("link", name="Our Expertise")
		self.development_practices = page.get_by_role("link", name="Development Practices")
		self.industries = page.get_by_role("link", name="Industries ")
		self.fin_tech = page.get_by_role("link", name="FinTech")

	def click_on_logo(self):
		self.logo_click.first.click()

	def click_service(self):
		self.service.click()

	def click_our_expertise(self):
		self.our_expertise.first.click()

	def click_development_practices(self):
		self.development_practices.first.click()

	def click_industries(self):
		self.industries.click()

	def click_fin_tech(self):
		self.fin_tech.first.click()
