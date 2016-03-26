import sublime, sublime_plugin, urllib.request, re

# Extends TextCommand so that run() receives a View to modify.
class WordpressSaltsDotEnvCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for cursor in self.view.sel():
            #Linux broken SSL http://sublimetext.userecho.com/topic/50801-bundle-python-ssl-module/
            req = urllib.request.Request('http://api.wordpress.org/secret-key/1.1/salt')
            response = urllib.request.urlopen(req)
            salts = response.read()
            salts = salts.decode("utf-8")
            salts = re.sub(r"\w+\('", '', salts)
            salts = re.sub(r"',\s+'", '=', salts)
            salts = re.sub(r"'\);", '', salts)
            self.view.insert(edit, cursor.begin(), salts )
