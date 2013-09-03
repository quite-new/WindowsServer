import web
import urlparse, subprocess, os, webbrowser


urls = (
    '/','index',
    '/start','start',
    '/stop','stop',
    '/cleanup','cleanup',
    )

class index:
    def GET(self):
        return "Server running!"


class start:
    def GET(self):
        request = web.input(browser = 'no browser')
        browser_name = web.websafe(request.browser)
        request = web.input(url = 'http://google.com')  
        url = web.websafe(request.url)

        if browser_name == "ie":
            ie = webbrowser.get('c:\\program files (x86)\\internet explorer\\iexplore.exe')
            ie.open('http://google.com')
        elif browser_name == "chrome":
            chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            os.system("start \"\" \""+chrome_path+"\" "+url)
        elif browser_name == "firefox":
            firefox_path = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
            os.system("start \"\" \""+firefox_path+"\" "+url)
        elif browser_name == "safari":
            safari_path = 'C:\\Program Files (x86)\\Safari\\safari.exe'
            os.system("start \"\" \""+safari_path+"\" "+url)
        return "Start request for "+browser_name+"!!"

class stop:
    def GET(self):
        request = web.input(browser = 'no browser')
        browser_name = web.websafe(request.browser)
        print "["+browser_name+"]"
        if browser_name == "ie":
            browser_name = "iexplore"
        os.system("taskkill /F /IM "+browser_name+".exe")
        return "Stop request for "+browser_name+"!"

class cleanup:
    def GET(self):
        os.system("C:\\server\\cleanup.bat")
        return "Cleanup Request!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()