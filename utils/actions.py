import inspect


class Action:
	def __init__(self, page):
		self.context = None
		self.page = page

	def verify_current_url(self):
		try:
			self.page.wait_for_timeout(50000)

		except TimeoutError:
			print("URL did not match within the timeout period")

	def verify_open_in_new_tab(self, url) -> None:
		initial_page_count = len(self.context.pages)

		updated_page_count = len(self.context.pages)

		is_new_tab_opened = updated_page_count > initial_page_count

		if is_new_tab_opened:
			new_tab_url = self.context.pages[-1].url()
		else:
			print("Link did not open in a new tab")
			new_tab_url = None
		assert url == new_tab_url

	@classmethod
	def get_current_test_name(cls):
		frame = inspect.currentframe().f_back
		method_name = frame.f_code.co_name
		return method_name

	def verify_current_url_to_contain(self, expected_partial_url):
		try:
			self.page.wait_for_timeout(50000)
			current_url = self.page.url
			assert expected_partial_url in current_url, f"Expected '{expected_partial_url}' to be present in URL, but "f"it is not. Current URL: {current_url}"
			print(f"URL verified to contain : '{expected_partial_url}'")
		except TimeoutError:
			print(f"URL did not contain '{expected_partial_url}'")
