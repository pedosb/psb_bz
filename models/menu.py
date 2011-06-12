_c = request.controller

response.menu = [
		(T('Home'), _c=='default', URL('default', 'index'), ()),
		(T('Publications'), _c=='publications', URL('publications', 'index'), ()),
		]

response.left_bar = False
