class Footer:
	def __init__(self, page):
		self.fin_tech = page.get_by_role("link", name="FinTech")
		self.health_tech = page.get_by_role("link", name="HealthTech")
		self.ad_tech = page.get_by_role("link", name="AdTech")
		self.process_automation = page.get_by_role("link", name="Process Automation")
		self.about_us = page.get_by_role("contentinfo").get_by_role("link", name="About Us")
		self.join_us = page.get_by_role("contentinfo").get_by_role("link", name="Join Us")
		self.contact_us = page.get_by_role("link", name="Contact US", exact=True)

	def click_fin_tech(self):
		self.fin_tech.click()

	def click_health_tech(self):
		self.health_tech.click()

	def click_ad_tech(self):
		self.ad_tech.click()

	def click_process_automation(self):
		self.process_automation.click()

	def click_about_us(self):
		self.about_us.click()

	def click_join_us(self):
		self.join_us.click()

	def click_contact_us(self):
		self.contact_us.click()
