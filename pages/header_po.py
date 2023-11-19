class Header:
	def __init__(self, page):
		self.logo_click = page.locator(".elementor-widget-wrap")
		self.service = page.get_by_role("link", name="Services ")
		self.our_expertise = page.get_by_role("link", name="Our Expertise")
		self.development_practices = page.get_by_role("link", name="Development Practices")
		self.industries = page.get_by_role("link", name="Industries ")
		self.fin_tech = page.get_by_role("link", name="FinTech")
		self.health_tech = page.get_by_role("link", name="HealthTech")
		self.ad_tech = page.get_by_role("link", name="AdTech")
		self.process_automation = page.get_by_role("link", name="Process Automation")
		self.join_us = page.get_by_role("link", name="Join Us")
		self.about_us = page.get_by_role("link", name="About Us")
		self.contact_us = page.get_by_role("link", name="Contact US", exact=True)

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

	def click_health_tech(self):
		self.health_tech.first.click()

	def click_ad_tech(self):
		self.ad_tech.first.click()

	def click_process_automation(self):
		self.process_automation.first.click()

	def click_join_us(self):
		self.join_us.first.click()

	def click_about_us(self):
		self.about_us.first.click()

	def click_contact_us(self):
		self.contact_us.first.click()
