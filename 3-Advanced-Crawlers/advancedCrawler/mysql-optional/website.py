class Website:
	'Common base class for all articles/pages'


	def __init__(self, id, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, pageTitle, pageBody):
		self.id = id
		self.name = name
		self.url = url
		self.searchUrl = searchUrl
		self.resultListing = resultListing
		self.resultUrl = resultUrl
		self.absoluteUrl=absoluteUrl
		self.pageTitle = pageTitle
		self.pageBody = pageBody